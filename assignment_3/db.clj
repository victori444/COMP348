(ns db
  (:require [clojure.string :as str]))

(defn parse-line [line]
  (let [[city province size population area] (str/split line #"\|")]
    {:city city
     :province province
     :size size
     :population (Integer/parseInt population)
     :area (Double/parseDouble area)}))

(defn load-data [filename]
  (let [lines (str/split-lines (slurp filename))]
    (map parse-line lines)))

(def citiesDB (load-data "cities.txt"))