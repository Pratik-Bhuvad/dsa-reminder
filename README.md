## DSA REMINDER v0.0.0

A lightweight Python-based daily DSA problem reminder system designed to help maintain consistent problem-solving practice.

## PURPOSE

Maintaining consistency in DSA practice is often harder than solving the problems themselves. This project aims to remove the decision-making overhead by automatically selecting a problem from a predefined pool and presenting it to the user.

Version 0 focuses on the core workflow:

- Load problems from a local JSON file
- Track previously shown problems
- Prevent repetition until the entire problem pool has been exhausted
- Reset the cycle once all problems have been shown
- Display the selected problem in the terminal

## FEATURES

- **Daily Problem Selection**: Automatically selects a problem from the pool each day.

- **Non-Repetitive**: Ensures that problems are not repeated until all have been shown.

- **Local Storage**: Uses a local JSON file to store problems and track shown problems.

- **RESET Functionality**: Once all problems have been shown, the system resets to allow for a new cycle.


## ARCHITECTURE

This system follows a simple pipeline architecture:

PROBLEM SOURCE (JSON) --> DAILY PROBLEM SERVICE --> STORAGE (SQLite) --> DELIVERY (Terminal)

## SETUP

1. **Clone the Repository**: Clone this repository to your local machine.
```
git clone <repository-url>
```

2. **Install Dependencies**: Ensure you have Python installed. Install any required packages using pip.
```
pip install -r requirements.txt
```

3. **Prepare the Problem Pool**: Ensure you have a `problems.json` file in the `data` directory with your DSA problems.

4. **Run the Application**: Execute the main script to see your daily problem.
```
python main.py
```

## EXAMPLE USAGE

When you run the application, it will display a problem in the terminal. If all problems have been shown, it will reset and start over.

```
Problem of the Day:
====================
Today's Problem: Valid Parentheses
Topics: Stack, String
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/
====================
```

## CURRENT STATUS

DSA Reminder v0 is the foundation release.

Implemented:

- JSON-based problem source
- Sequential problem selection
- SQLite persistence
- History reset mechanism
- Terminal delivery

Planned for future versions:

- Automated daily execution
- Email delivery
- Alternative selection strategies
- Dynamic problem sources
- Topic rotation
- Difficulty progression
- Adaptive learning recommendations