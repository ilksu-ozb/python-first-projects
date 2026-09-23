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

 ### 3. Alarm Clock:
 A terminal-based alarm clock application. It leverages Python's built-in `datetime` and `time` modules to provide real-time tracking with minimal system resource usage.

* **Key Features:**
  * Input Validation: Safely parses user input in `hh:mm` format, validating integer conversion and checking standard time boundaries (`0-23` hours, `0-59` minutes).
  * Resource Efficient: Utilizes `time.sleep` interval polling to prevent unnecessary CPU usage while waiting for the alarm trigger.
  * Audible & Visual Alerts: Triggers a terminal audio prompt and visual notice once the target time is reached.
  * Modular Architecture: Structured around clean functional programming principles with dedicated functions for user input processing (`set_timer()`), time monitoring, and main execution flow (`main()`).
 
 ### 4. To-Do-List:
 A modular Python To-Do List application built with a Command Line Interface (CLI) and data persistence using JSON.

 * **Key Features:**
   * Task Management: Add, view, update, and delete tasks.
   * Data Persistence: Tasks are automatically saved to `tasks.json` and reloaded upon app startup.
   * Error Handling: Input validation using `try-except` blocks.
   * Modular Architecture: Separate modules for logic (`main.py`) and data persistence (`storage.py`).
   
   
  



