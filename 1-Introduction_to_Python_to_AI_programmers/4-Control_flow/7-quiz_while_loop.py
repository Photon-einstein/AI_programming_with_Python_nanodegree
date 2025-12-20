# Exercise 1: Learning Rate Schedule using While Loops
# Problem Statement
# Given an initial learning rate and a decay factor, use a while loop to apply the decay
# to the learning rate at each epoch until a specified number of epochs is reached.

# Example Input:

# initial_lr = 0.1
# decay_factor = 0.9
# epochs = 5
# Instructions:

# Initialize the learning rate to initial_lr.
# Use a while loop to apply the decay factor to the learning rate for each epoch.
# Print the learning rate for each epoch.

# Initial learning rate
initial_lr = 0.1
# Decay factor
decay_factor = 0.9
# Number of epochs
epochs = 5

# Initialize current learning rate
current_lr = initial_lr
# Initialize current epoch
current_epoch = 0

# While loop to apply learning rate decay
while current_epoch < epochs:
    current_lr *= decay_factor
    current_epoch += 1

# Notebook grading
if abs(current_lr - 0.059049) < 1e-6:
    print("Nice work!")
else:
    print("Not quite. Check your learning rate calculations.")

# Exercise 2: Iterating Through Model Parameters using For Loops
# Problem Statement
# Given a list of model parameters and their corresponding gradients,
# use a for loop to update each parameter.

# Example Input:

# parameters = [0.5, 1.5, -0.5]
# gradients = [0.1, -0.2, 0.05]
# learning_rate = 0.01
# Instructions:

# Use a for loop to iterate through the parameters and gradients.
# Apply a gradient update to each parameter using the learning rate.

# Model parameters
parameters = [0.5, 1.5, -0.5]
# Corresponding gradients
gradients = [0.1, -0.2, 0.05]
# Learning rate
learning_rate = 0.01

# For loop to update each parameter
i = 0
while i < len(parameters):
    parameters[i] -= gradients[i] * learning_rate
    i += 1

# Notebook grading
if parameters == [0.499, 1.502, -0.5005]:
    print("Nice work!")
else:
    print("Not quite. Check your parameter updates.")
