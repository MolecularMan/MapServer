#!/usr/bin/python3

import glob
import os
import sqlite3

directory="/opt/maps"


dirs = os.listdir(directory)
zdirs=[]
##if dir start with 'z', add it to z-started dirs list
for dir in dirs:
    if dir.startswith('z'):
        zdirs.append(dir)

##make dir with result if not exist

if not os.path.exists(directory+'/converted'):
    os.makedirs(directory+'/converted')

for zdir in zdirs:
    print("Working with directory "+zdir)
    dblist = glob.glob(directory+'/'+zdir+'/**/**/*.sqlitedb', recursive=True)
    dblist = list(set(dblist)) # deduplicate list with db files
    conn = sqlite3.connect(directory+'/converted/'+zdir+'.sqlitedb')
    c = conn.cursor()
    c.execute("CREATE TABLE tiles (x INTEGER NOT NULL,y INTEGER NOT NULL,z INTEGER DEFAULT "+zdir.replace('z','')+" NOT NULL,b BLOB,constraint PK_TB primary key (x,y))")
    c.execute("CREATE INDEX tiles_x_idx on tiles (x);")
    conn.commit()
    for db in dblist:
        #print("Trying work with database "+db)
        c.execute('ATTACH DATABASE "'+db+'" AS sasdb')
        c.execute('INSERT INTO tiles (x, y, b) SELECT x, y, b FROM sasdb.t')
        conn.commit() #fixing 'database is locked'
        c.execute('DETACH DATABASE sasdb')
        conn.commit()
        print("SAS.Planet DB "+db+" inserted to "+directory+'/converted/'+zdir+'.sqlitedb')

    c.close()
    print("Done with "+zdir)
    print("==============================")
