# Logging is a means of tracking events that happen when some software runs. Logging in Python lets you record important information about your program’s execution. You use the built-in logging module to capture logs, which provide insights into application flow, errors, and usage patterns. With logging, can create and configure loggers, set log levels, and format log messages without installing additional packages. You can also generate log files to store records for later analysis

# The main component of the logging module is something called the logger. You can think of the logger as a reporter in your code that decides what to record, at what level of detail, and where to store or send these records

# root logger 

# import logging 
# logging.warning("Save your Code”) 
                
# o/p WARNING:root:Save your Code 
# This output shows the default format that can be configured to include things like a timestamp or other details. 


#  five log levels 

# DEBUG - logging.debug() - Provides detailed information that’s valuable to you as a developer. 
# INFO -  logging.info() -  Provides general information about what’s going on with your program.
# WARNING -  logging.warning() -  Indicates that there’s something you should look into. 
# ERROR -  logging.error() - Alerts you to an unexpected problem that’s occured in your program. 
# CRITICAL -  logging.critical() - Tells you that a serious error has occurred and may have crashed your app.

# ADJUSTING/SETTING LOG LEVELS

# import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Program started successfully!")

# Output:

# INFO:root:Program started successfully!


# import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("Debugging info")
# logging.info("General info")
# logging.warning("This is a warning")
# logging.error("Something went wrong!")
# logging.critical("Critical error!")

# Formattinng the output

# Use format in basicConfig() to change how logs look.

# import logging

# logging.basicConfig(
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     level=logging.DEBUG
# )

# logging.info("This is a formatted log.")

# Output:

# 2025-05-14 18:00:00 - INFO - This is a formatted log.

# Logging to a File

# Instead of printing logs to the console, we can save them in a file

# logging.basicConfig(
#     filename='app.log',
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# logging.warning("This will be written to a file.") #app.log file


# Using Handlers

# Handlers decide where the log messages go
# StreamHandler: Console
# FileHandler: File


# import logging

# # Create logger
# logger = logging.getLogger("myApp")
# logger.setLevel(logging.DEBUG)

# # Console Handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)

# # File Handler
# file_handler = logging.FileHandler("logfile.log")
# file_handler.setLevel(logging.DEBUG)

# # Formatter
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# # Add handlers
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# # Logging
# logger.debug("This is a DEBUG message (goes to file)")
# logger.info("This is an INFO message (goes to file and console)")
# logger.error("This is an ERROR message")


# Adjusting Log Levels Dynamically

# console_handler.setLevel(logging.WARNING)
# file_handler.setLevel(logging.DEBUG)

# Logging Exceptions 

# import logging

# logging.basicConfig(level=logging.ERROR)

# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     logging.exception("Division by zero occurred!")

# Output:

# ERROR:root:Division by zero occurred!
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero

# Disabling Logging

# logging.disable(logging.CRITICAL)
