# MapServer

This is simple Golang Tile map server, worked with [SAS.Planet](http://www.sasgis.org/sasplaneta/) SQLite3 cache

  - By defailt, start on port 8085 (can be changed with parameter -port, e.g. ```-port 8090```)
  - Need set directory with z-starting folders (z1, z2, z3,..., zN) inside SAS.Planet sqlite-cache folder with ```-cache``` parameter
  - Can work with [Leaflet](https://leafletjs.com/) (an open-source JavaScript library for mobile-friendly interactive maps)


# Dependencies

  - Go 1.15.6+
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
./mapserver -cache /path/to/SAS.Planet/cache/with/zN folders/ [-port 8085]
```
After running, tiles be in url ```/maps/z/x/y```, e.g. http://localhost:8085/maps/4/9/5 where 4-Zoom, 9-X and 5-Y