# Exercise 1: Model Accuracy Guess¶
# In this exercise, you'll compare a predicted accuracy to an actual accuracy and provide feedback 
# on whether the predicted accuracy is too low, too high, or matches the actual accuracy.

# Problem Statement
# You have an actual model accuracy stored in a variable called actual_accuracy. 
# Another user provides a predicted accuracy called predicted_accuracy.
# By comparing predicted_accuracy to actual_accuracy, inform the user if their prediction
# is too high, too low, or correct.

# Example Input:

# actual_accuracy = 0.85  # replace with actual accuracy
# predicted_accuracy = 0.80  # replace with predicted accuracy
# Instructions:

# Compare predicted_accuracy to actual_accuracy.
# Inform the user if their prediction is too high, too low, or correct.

### Notebook grading
def get_solution(actual_accuracy, predicted_accuracy):
    if predicted_accuracy < actual_accuracy:
        return "Oops! Your prediction was too low."
    elif predicted_accuracy > actual_accuracy:
        return "Oops! Your prediction was too high."
    else:
        return "Nice! Your prediction matched the actual accuracy!"

# Actual and predicted accuracies
actual_accuracy = 0.85  # replace with actual accuracy
predicted_accuracy = 0.80  # replace with predicted accuracy

# Compare predicted accuracy to actual accuracy
result  = get_solution(actual_accuracy, predicted_accuracy)

if result == get_solution(actual_accuracy, predicted_accuracy):
    print("Good job!")
else:
    print("Try again. That doesn't look like the expected answer.")


# Exercise: Compute Resource Cost Calculation¶
# In this exercise, you'll calculate the total cost of running a machine learning model training session
# based on the cloud provider used. Different providers have different cost rates.

# Problem Statement
# Depending on the cloud provider, you need to apply the appropriate cost rate to the computation cost. 
# The providers and their rates are as follows: AWS (7.5%), Azure (9.5%), and GCP (8.9%). 
# Use this information to calculate the total cost of running the training session based on the provider and the initial computation cost.

# Example Input:

# provider = "AWS"  # Either "AWS", "Azure", or "GCP"
# computation_cost = 1000  # amount of computation cost
# Instructions:

# Use the provider to determine the cost rate.
# Calculate the total cost based on the computation cost and the cost rate.
# Inform the user of the total cost based on their provider.

# Provider and computation cost
provider = "AWS"  # Either "AWS", "Azure", or "GCP"
computation_cost = 1000  # amount of computation cost

# Determine the cost rate based on the provider and calculate the total cost
if provider == "AWS":
    cost_rate = .075
    total_cost = computation_cost*(1+cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
elif provider == "Azure":
    cost_rate = .095
    total_cost = computation_cost*(1+cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
elif provider == "GCP":
    cost_rate = 0.089
    total_cost = computation_cost*(1+cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
else:
    result = "Provider not recognized"

### Notebook grading
def get_solution(provider, computation_cost):
    if provider == 'AWS':
        cost_rate = .075
        total_cost = computation_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    elif provider == 'Azure':
        cost_rate = .095
        total_cost = computation_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    elif provider == 'GCP':
        cost_rate = .089
        total_cost = computation_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    else:
        result = "Provider not recognized."
    return result

if result == get_solution(provider, computation_cost):
    print("Good job!")
else:
    print("Oops! That doesn't look like the expected answer.")