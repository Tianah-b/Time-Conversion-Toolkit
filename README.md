Description:
This repository contains a Python-based toolkit for converting time units, specifically days into hours or minutes. The toolkit comprises three main components:

time_conversion_gui.py: This file implements a graphical user interface (GUI) using tkinter, allowing users to input a number of days and select the desired conversion unit (hours or minutes). The result of the conversion is then displayed within the GUI.

helper.py: This file contains the core functionality of the toolkit. It includes the days_to_units function, which performs the actual conversion from days to the selected time unit, and the validate_and_execute function, which validates the user input and executes the conversion process.

main.py: This script provides a command-line interface (CLI) for the toolkit. It prompts users to enter the number of days and the desired conversion unit, and then utilizes the functions defined in helper.py to perform the conversion and display the result.

This toolkit is ideal for educational purposes or for anyone needing a simple tool to convert time units from days to hours or minutes. The GUI and CLI interfaces make it accessible for both programming beginners and those preferring a more traditional command-line approach.

Usage:

Run main.py for a command-line interface.
Run time_conversion_gui.py for a graphical user interface.
