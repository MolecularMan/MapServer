# MapServer

This is simple Golang Tile map server, worked with [SAS.Planet](http://www.sasgis.org/sasplaneta/) SQLite3 cache after conversion by ```converter.py```

  - By defailt, start on port 8085 (can be changed with parameter -port, e.g. ```-port 8090```)
  - For converter, need set directory with z-starting folders (z1, z2, z3,..., zN) inside SAS.Planet sqlite-cache folder
  - Can work with [Leaflet](https://leafletjs.com/) (an open-source JavaScript library for mobile-friendly interactive maps)
  - After running converter, will be created ```/converted``` folder with files for mapserver

# Dependencies

  - Go 1.16+
  - Python 3
  - Go packages:
  -  ``` "github.com/gorilla/mux" ```
  - ``` "github.com/mattn/go-sqlite3"```
# Installing
  - ``` go get "github.com/gorilla/mux" ```
  - ``` go get "github.com/mattn/go-sqlite3"```
  - ``` go build mapserver.go ```

# Usage
```
./mapserver -cache /path/to/converter/result/folder/with/files/zN.sqlitedb [-port 8085]
```
After running, tiles be in url ```/maps/z/x/y```, e.g. http://localhost:8085/maps/4/9/5 where 4-Zoom, 9-X and 5-Y