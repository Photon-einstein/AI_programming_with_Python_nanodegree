# Task:
# Write code that handles a ZeroDivisionError during data processing. If an exception occurs,
# it should print a friendly error message instead of crashing.


# Function to process data
def process_data(value):
    try:
        # Perform a division operation
        result = 100 / value
        print(f"Result: {result}")
    except ZeroDivisionError:
        # Handle the division by zero exception
        print("Error, caught division by zero exception.")


# Test the function with an invalid value (0) to trigger the exception
process_data(0)
