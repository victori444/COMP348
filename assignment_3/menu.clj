(ns menu
  (:require [clojure.string :as str]
            [db]))

(defn show-menu []
  (println "\n\n*** City Information Menu ***")
  (println "-----------------------------\n")
  (println "1. List Cities")
  (println "2. Display City Information")
  (println "3. List Provinces")
  (println "4. Display Province Information")
  (println "5. Exit")
  (print "\nEnter an option? ")
  (flush)
  (read-line))

(defn list-cities []
  (println "1.1 List all cities, ordered by city name (ascending)")
  (println "1.2 List all cities for a given province, ordered by size (descending) and name (ascending)")
  (println "1.3 List all cities for a given province, ordered by population density (ascending)")
  (print "\nEnter an option? ")
  (flush)
  (read-line))

(defn list-all-cities [cities]
  (->> cities
       (sort-by :city)
       (map :city)
       (println)))

(defn cities-by-province [cities province]
  (->> cities
       (filter #(= (:province %) province))
       (sort-by (juxt #(case (:size %)
                         "Large urban" 1
                         "Medium" 2
                         "Small" 3)
                      :city))
       (map (juxt :city :size :population))
       (println)))

(defn cities-by-density [cities province]
  (->> cities
       (filter #(= (:province %) province))
       (sort-by #(/ (:population %) (:area %)))
       (map (juxt :city :size :population))
       (println)))

(defn display-city-info [cities city]
  (let [city-info (first (filter #(= (:city %) city) cities))]
    (if city-info
      (println city-info)
      (println "City not found."))))

(defn list-provinces [cities]
  (let [province-count (frequencies (map :province cities))
        sorted-provinces (sort-by (comp - val) province-count)]
    (doseq [[province count] sorted-provinces]
      (println [province count]))
    (println "Total:" (count province-count) "provinces," (count cities) "cities on file.")))

(defn display-province-population [cities]
  (let [province-populations (reduce (fn [acc city]
                                       (update acc (:province city) (fnil + 0) (:population city)))
                                     {}
                                     cities)]
    (doseq [[province population] (sort-by key province-populations)]
      (println [province population]))))

(defn process-option [cities option]
  (case option
    "1" (let [sub-option (list-cities)]
          (case sub-option
            "1.1" (list-all-cities cities)
            "1.2" (do (print "Enter province name: ") (flush) (let [province (read-line)] (cities-by-province cities province)))
            "1.3" (do (print "Enter province name: ") (flush) (let [province (read-line)] (cities-by-density cities province)))
            (println "Invalid option")))
    "2" (do (print "Enter city name: ") (flush) (let [city (read-line)] (display-city-info cities city)))
    "3" (list-provinces cities)
    "4" (display-province-population cities)
    "5" (println "Good Bye")
    (println "Invalid option")))

(defn menu []
  (loop []
    (let [option (show-menu)]
      (if (= option "5")
        (println "\nGood Bye\n")
        (do
          (process-option db/citiesDB option)
          (recur))))))
