# Create a function to handle errors that occur during code execution
# This will display a message to the user adn may log the error for the support team to
# help with debugging
# 
# Parameters:
#   error_code: Unique error code assigned to each type of error: e.g. 45 is datatype conversion error
#   error_severity: 0 - fatal error should never occur
#                   1 - severe error code cannot continue
#                   2 - warning code can continue but may be missing information in records
#   log_to_db: Should this error be logged to the database 
#   error_message: Error message to display to user and write to database
#   source_module: Name of the python module that generated ther error

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    # Imagine code here that logs our error to a database or file

first_number = 10
second_number = 5
    # This function call by itself is confusing, I have to look at the
    # definition of the error_logger function to understand it
if first_number > second_number:
    error_logger(45,1,True,'Second number greater than first','adding_method')


if first_number > second_number:
    # This function call by itself is easier to understand because I can 
    # see how the values I pass in map to the function parameters
    error_logger(error_code=45, 
                 error_severity=1,
                 log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='adding_method')
