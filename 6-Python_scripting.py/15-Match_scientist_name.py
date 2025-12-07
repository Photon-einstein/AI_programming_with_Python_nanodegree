# Write your code here

# HINT: create a dictionary from scientists.txt

# Create the Dictionary:
# Write a function named create_scientist_dict() that:
# Reads the scientists.txt file.
# Creates a dictionary where each key is a letter and each value is an AI scientist's name.
# Handles the case where the file might not be found and prints an appropriate error message.

def create_scientist_dict():
    file = 'scientists.txt'
    scientist_dict = dict()
    with open(file,'r') as entries:
        if not entries:
            print("File {} not found ".format(file))
        for entry in entries:
            data = entry.split()
            data[0] = data[0].split(":")[0]
            if data[0] not in scientist_dict:
                scientist_dict[data[0]] = data[1]
    return scientist_dict


        

# HINT: create a function to ask for user's first and last name

# Get Scientist Name Based on User Input:
# Write a function named get_scientist_name() that:
# Prompts the user for their first and last name.
# Extracts the first letter of the first name and converts it to uppercase.
# Looks up the corresponding AI scientist's name in the dictionary.
# Prints the AI scientist's name or an error message if no match is found.
# Ensures the function handles cases where the user input is empty or invalid.

def get_scientist_name():
    try:
        first_name = input("First name? ")
        if len(first_name) == 0:
            raise ValueError("First name cannot be empty.")
        last_name = input("Last name? ")
        if len(last_name) == 0:
            raise ValueError("Last name cannot be empty.")
        first_letter = first_name[0].upper()
        if first_letter in scientist_dict:
            print("{}: {}".format(first_letter, scientist_dict[first_letter]))
        else:
            raise ValueError("No match found for the first letter '{}' in the dictionary.".format(first_letter))
    except Exception as error:
        print("Error caught: {}".format(error))




# print the desired output

# Combine Functions in a Main Block:
# Write the main block of the program that:
# Calls create_scientist_dict() to create the dictionary from the file.
# If the dictionary is successfully created, calls get_scientist_name() 
# to prompt the user for their name and print the matching AI scientist's name.

if __name__ == "__main__":
    scientist_dict = create_scientist_dict()
    if len(scientist_dict) > 0:
        get_scientist_name()