(let
    ((input (uiop:read-file-string #p"01-input.txt")))
  (uiop:split-string input :separator "\n\n"))
