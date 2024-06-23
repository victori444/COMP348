(ns db
  (:require [clojure.string :as str]))

; Parses each line of the input file and
; creates a map with the fields city, province, size, population, and area
(defn parse-line [line]
  (let [[city province size population area] (str/split line #"\|")]
    {:city city
     :province province
     :size size
     :population (Integer/parseInt population)
     :area (Double/parseDouble area)}))

; Load data from input file and parse it
(defn load-data [filename]
  (let [lines (str/split-lines (slurp filename))] ; Split file by lines
    (map parse-line lines))) ; create list of maps of cities

; Load city data from input file into the variable citiesDB
(def citiesDB (load-data "cities.txt"))