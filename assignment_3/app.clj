(ns app
  (:require [menu]))

; Define entry point of the application
(defn -main []
  (menu/menu))
; Call main function
(-main)
