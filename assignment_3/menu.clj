(ns menu
  (:require [clojure.string :as str])
  (:require [clojure.java.io :as io]))
  ; this is where you would also include/require the compress module

; Display the menu and ask the user for the option
(defn showMenu
  []
  (println "\n\n*** City Information Menu ***")
  (println "-----------------------------\n")
  (println "1. List cities")
  (println "2. Display City Information")
  (println "3. List Provinces")
  (println "4. Display Province Information")
  (println "5. Exit")
  (do 
    (print "\nEnter an option? ") 
    (flush) 
    (read-line)))


; Replace the println expression your own code (i.e. calling another function(s))
(defn option1
  [] ;parm(s) can be provided here, if needed
  (println "this is a place holder for option 1, you may use a sub-menu for options 1.1, 1.2, or 1.3"))
; 1.1 List all cities in the file, ordered by name
; 1.2. List all cities of a given province order by size and name
; 1.3.  all cities of a given province ordered by population desity in ascending order
    
    
; Replace the println expression your own code
(defn option2
  [] ;parm(s) can be provided here, if needed
  (print "\nPlease enter the city name => ") 
  (flush)
  (let [city_name (read-line)]
     (println "Display size, population, land area, population density for" city_name)))


(defn option 3
; Replace the println expression your own code
  [] ;parm(s) can be provided here, if needed
  (println "List all provinces with total number of cities"))


(defn option4
  [] ;parm(s) can be provided here, if needed
  (println "List all provinces with total population"))


; If the menu selection is valid, call the relevant function to 
; process the selection
(defn processOption
  [option] ; other parm(s) can be provided here, if needed
  (if( = option "1")
     (option1)
     (if( = option "2")
        (option2)
        (if( = option "3")
           (option3)  ; other args(s) can be passed here, if needed
           (if( = option "4")
              (option4)   ; other args(s) can be passed here, if needed
              (println "Invalid Option, please try again"))))))


; Display the menu and get a menu item selection. Process the
; selection and then loop again to get the next menu selection
(defn menu
  [] ; parm(s) can be provided here, if needed
  (let [option (str/trim (showMenu))]
    (if (= option "5")
      (println "\nGood Bye\n")
      (do 
         (processOption option)
         (recur )))))   ; other args(s) can be passed here, if needed


; ------------------------------
; Run the program. You might want to prepare the data required for the mapping operations
; before you display the menu. You don't have to do this but it might make some things easier

; A cities.txt file will be provided in the *current directory*, during grading
; In general you need to read, process, and display the file content (cities.txt) 
; You may use Java's File class to check for existence. 

(menu) ; other args(s) can be passed here, if needed
