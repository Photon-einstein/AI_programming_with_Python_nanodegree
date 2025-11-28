# Exercise: Performance Level Based on Model Accuracy¶
# The code below is the solution to the Evaluating Model Performance quiz you've seen previously.
# You're going to rewrite this based on what you've learned about truth values.

# In this exercise, you'll assign performance levels to models based on their accuracy and use the
# truth value of the performance level to determine the evaluation message.

# Problem Statement
# Given an accuracy value, assign a performance level based on the following criteria:

# 0% - 50%: Poor performance
# 51% - 75%: Average performance
# 76% - 90%: Good performance
# 91% - 100%: Excellent performance
# Assign the corresponding result message based on the performance level.

# Example Input:

# accuracy = 0.88  # use this as input for your submission
# Instructions:

# Establish the default performance level to None.
# Use the accuracy value to assign performance levels to the correct performance names.
# Use the truth value of performance level to assign result to the correct message.

accuracy = 0.88  # use this as input for your submission

# Establish the default performance level to None
performance = None

# Use the accuracy value to assign performance levels to the correct performance names
if accuracy <= 0.5:
    performance = "Poor performance"
elif accuracy <= 0.75:
    performance = "Average performance"
elif accuracy <= 0.90:
    performance = "Good performance"
else:
    performance = "Excellent performance"


# Use the truth value of performance to assign result to the correct phrase
if performance:
    result = "The model has achieved {}.".format(performance)
else:
    result = "Performance level not defined."

### Notebook grading
if result == "The model has achieved Good performance.":
    print("Good work!")
else:
    print("Not quite! Are your result string formatted correctly?")