# Exercise: Displaying and Returning Dataset Sizes
# Scenario:
# You are developing a utility to handle large datasets for a machine learning project.
# You need functions to both display and return the size of a dataset after adding a specified increment.
# This is useful for logging and processing purposes.

# Task:
# Transform the following code to create functions that display and return the dataset size after adding an increment.
# Use these functions to handle dataset sizes and log the outputs.

# This exercise will help you understand the difference between functions that print results directly and those that
# return values for further processing.


# This function prints the dataset size after adding the increment, but does not return anything
def display_new_size(dataset_size, increment):
    new_size = dataset_size + increment
    print(f"New dataset size after adding {increment} GB: {new_size} GB")


# This function returns the dataset size after adding the increment
def get_new_size(dataset_size, increment):
    return dataset_size + increment


# Example usage:
dataset_size = 50  # in GB
increment = 10  # in GB

print("Calling display_new_size...")
return_value_1 = display_new_size(dataset_size, increment)
print("Done calling")
print("This function returned: {}".format(return_value_1))

print("\nCalling get_new_size...")
return_value_2 = get_new_size(dataset_size, increment)
print("Done calling")
print("This function returned: {} GB".format(return_value_2))
