#  Python Basics & First Projects

This repository contains my Python practices and fundamental projects.

## What's inside?

### 1. Rock, Paper, Scissors Game:
A simple game where you compete against the computer by choosing one of three options and deciding how many rounds there will be. The computer makes random choices, 
and the winner is decided by comparing the score tables.

* **Key Features:**
  * Using `while True` and `try-except` to prevent invalid input.
  * Managing parameters and `return` values.
  * Dynamic game loop that rotates the number of turns specified by the user.


 ### 2. Number Guessing Game:
 Another simple game where the user tries to guess the random number the computer chose, after determining the range and the number of trials to have.


 ### 3. Password Generator:
 Generates secure passwords depending on the user's choices (length of the password, whether there should be special characters or numbers).

* **Key Features:**
  * Cryptographically Secure: Uses the `secrets` module for randomness.
  * Interactive CLI: Prompts users for length (8-64 characters), numbers, and special characters.
  * Validation: Guarantees that the generated password strictly contains at least one character from each requested pool (numbers/symbols).
  * Input Handling: Safe from crashes due to invalid character inputs or sudden user interruptions (`Ctrl+C`).
    

