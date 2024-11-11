import logging

# Setup logging to file
logging.basicConfig(filename="error_log.txt", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def error_handling_example():
    try:
        # Example 1: FileNotFoundError
        with open("non_existent_file.txt", "r") as file:
            data = file.read()
        
        # Example 2: ValueError
        number = int("not_a_number")
        
    except FileNotFoundError as fnf_error:
        logging.error(f"FileNotFoundError: {fnf_error}")
        print("File not found. Check the file name and try again.")
    except ValueError as ve_error:
        logging.error(f"ValueError: {ve_error}")
        print("Value error occurred. Ensure correct data types.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

# Usage example
error_handling_example()
