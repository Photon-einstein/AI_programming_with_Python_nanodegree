# Modify the resource_allocator Function:

# Write a function named resource_allocator(resources, tasks) that:

# Takes the number of resources and tasks as inputs.
# Uses a try-except block to handle division by zero errors.
# If the number of tasks is zero, raises a ZeroDivisionError with a custom error message.
# If no error occurs, calculates how many resources each task gets and the number of leftover resources.
# Returns the number of resources per task and the number of leftovers, or None values if an error occurs.

def resource_allocator(resources, tasks):
    """Allocates resources to tasks and handles division by zero errors."""
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        if tasks == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        resources_per_task = resources // tasks
        leftovers = resources % tasks
        return resources_per_task, leftovers
    except ZeroDivisionError as error:
        print("ZeroDivisionError occurred: {}".format(error))
        return None, None
    
    
# Validate Input in the Main Loop:

# Write a main() function that:

# Initializes a loop that continues as long as the user wants to optimize resource allocation.
# Prompts the user to input the number of resources (cookies) and the number of tasks (people).
# Uses a try-except block to handle invalid inputs (e.g., non-integer values) and prints an appropriate error message.
# Checks if the input values are positive. If not, prints an error message and prompts the user to enter valid positive numbers.
# Calls the resource_allocator function with the user inputs and captures the returned values.
# If the resource allocation is successful (i.e., the function does not return None values), prints the allocation results in a formatted message.
# Asks the user if they want to continue optimizing, and exits the loop if the answer is 'n' (no).

# The main code block is below
def main():
    lets_optimize = 'y'
    while lets_optimize == 'y':
        try:
            resources = int(input("How many computational resources (computers) are available? "))
            if resources < 0:
                print("Number of resources cannot be negative. Please enter a positive number.")
                continue

            tasks = int(input("How many tasks (people) need resources? "))
            if tasks < 0:
                print("Number of tasks cannot be negative. Please enter a positive number.")
                continue

            resources_each, leftovers = resource_allocator(resources, tasks)

            if resources_each is not None:
                message = "\nResource Allocation: We'll have {} tasks, each will get {} resources, and we'll have {} resources left over."
                print(message.format(tasks, resources_each, leftovers))

            lets_optimize = input("\nWould you like to optimize more? (y or n) ").lower()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
