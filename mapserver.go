package main

import (
	"flag"
	"strconv"
	"log"
	"net/http"
	"github.com/gorilla/mux"
	"database/sql"
	 _ "github.com/mattn/go-sqlite3"
	)

var cache string

func TilesHandler(w http.ResponseWriter, r *http.Request) {


  vars := mux.Vars(r)
  zstr := vars["z"]
  x := vars["x"]
  y := vars["y"]
  zint, _ := strconv.Atoi(zstr)
  zint = zint + 1
  z := strconv.Itoa(zint)

  db, _ := sql.Open("sqlite3", cache+"/z"+z+".sqlitedb")
  defer db.Close()


  rows, _ := db.Query("SELECT b from tiles WHERE x = "+x+" AND y = "+y)
  defer rows.Close()

  var tileData []byte
  for rows.Next() {
    rows.Scan(&tileData)
  }

  w.Write(tileData)

}

func main() {

var port string

flag.StringVar(&port, "port", "8085", "listen port (8085 by default)")
flag.StringVar(&cache, "cache", "", "Set SAS.Planet SQLite3 CONVERTED cache folder")

flag.Parse()

r := mux.NewRouter()

r.HandleFunc("/maps/{z}/{x}/{y}", TilesHandler).Methods("GET")

log.Fatal(http.ListenAndServe(":" + port, r))
}
