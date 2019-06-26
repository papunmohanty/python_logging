import logging


#To print the messaages, WARNING and above.
#as WARNING is set by default.
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")


# Setting logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)  # if defined/initialized, second config setting up wont work, as it can only initial once and next initialization won't be considered.
logging.debug("This will get logged")


# Logging to a file, insted to console,
# and formatting the message as name - levelname - message
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

# Changing formatting option in message.
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

# Formatting option with adding ASCII time to the log message.
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

# Formatting datetime with the help of datefmt argument.
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

# Passing argumant to the message dynamically.
name = 'John Doe'
# logging.error('%s raised an error', name)
logging.error(f'{name} raised an error')

# Capturing Stack Traces
# by passing exc_info=Trye in the error method.
a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occured", exc_info=True)

# Using loging.exception() instead of logging.error(exc_info=True).
# It will give the same output with stack trace.
# But we need to be very cautious while using ths,
# this only be used insde of the exception block, as it always dumps
# exception information
a = 1
b = 0
try:
    c = a / b
except Exception as e:
    logging.exception("Exception occurred")

# Logger class, for custom logger, instead of default logger "root".
logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
# unlike the root logger, a custom logger can’t be configured using basicConfig().
# You have to configure it using Handlers and Formatters.

# To log from the same module
logger = logging.getLogger(__name__)
logger.warning('This is a warning')

# Using Handlers
'''
Like loggers, you can also set the severity level in handlers.
This is useful if you want to set multiple handlers for the same logger
but want different severity levels for each of them. For example,
you may want logs with level WARNING and above to be logged to the console,
but everything with level ERROR and above should also be saved to a file.
Here’s a program that does that:
'''
# Create custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
