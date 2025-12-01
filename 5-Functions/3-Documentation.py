# Exercise: Readable Time for Data Processing
# Scenario:
# You are optimizing a machine learning pipeline, and you need to report the processing time
# of a dataset in a human-readable format.
# The time is provided in days, and you need to convert it to weeks and days to better
# communicate the processing schedule to the stakeholders.

# Task:
# Write a function named readable_processing_time. The function should take one argument,
# an integer days, and return a string that says how many weeks and days that is.


def readable_processing_time(days):
    """
    Convert a number of days into a readable string format of weeks and days.

    This function takes an integer number of days and converts it into a
    human-readable string format that shows how many full weeks and remaining
    days are contained within that number of days. This is particularly useful
    for reporting processing times in machine learning projects, making the
    duration easier to understand for stakeholders.

    Parameters:
    days (int): The total number of days to be converted.

    Returns:
    str: A string representing the number of weeks and days.

    Example:
    >>> readable_processing_time(10)
    '1 week(s) and 3 day(s)'
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


### Notebook grading
import inspect

if "readable_processing_time" not in locals():
    print("Your code doesn't define the `readable_processing_time` function.")
elif inspect.getdoc(readable_processing_time) is None:
    print(
        "Your function doesn't have a docstring! Add one that explains the function's purpose."
    )
else:
    print("Nicely done! You can view my solution on the next page.")
