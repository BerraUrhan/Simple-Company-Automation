# Corporation Automation

This Python script provides a simple way to automate corporate management tasks. The `corporation` class provides methods to add/remove staff, calculate salaries, manage budgets, and end the process. Data is stored and retrieved from files to allow for persistence of information across sessions.

## Usage

1. Clone the repository
2. Run the script `corporation_automation.py`
3. Follow the menu prompts to execute various tasks

## Available Methods

- `msg_box`: Displays a welcome message to the user
- `program`: Main function that prompts the user to select an operation
- `menuOption`: Allows the user to choose an operation
- `addStaff`: Adds a new staff member to the corporation
- `delStaff`: Removes a staff member from the corporation
- `salary`: Calculates the total salary to be paid to staff members
- `budget`: Manages the corporation's budget
- `income`: Not implemented
- `outlay`: Not implemented
- `theend`: Ends the process

## Future Improvements

The `income` and `outlay` methods have not been implemented in this version. These methods could be added to allow the user to track the corporation's income and expenses. 

Overall, this script provides a useful starting point for building more sophisticated corporate management systems. With additional development, this script could be expanded to handle more complex situations and help automate routine tasks.
