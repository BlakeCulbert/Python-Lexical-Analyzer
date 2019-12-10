# Lexical Analyzer (Dates)


I created a lexical analyzer in Python which takes a lexeme from a test file or user input and using a finite state automata, will output whether the input is a vaild date or not (Ex: November 13, 1995). To output back the user given input, I created a Mealy machine which given the state of the FSA, as well as the character symbol, will add the symbol to our day, month or year variable. These wil then be outputted, as well as if it was a valid date or not.
