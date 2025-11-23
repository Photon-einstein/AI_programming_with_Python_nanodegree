# Quiz: Define and Manipulate a Dictionary for Model Accuracies

# Part 1: Define the Dictionary
# Define a dictionary named model_accuracies that contains this data:

# Keys	Values
# ResNet	0.91
# AlexNet	0.85
# VGG	0.88
# Inception	0.92

# Part 2: Calculate the Average Accuracy
# Write code to calculate the average accuracy of the models in the model_accuracies dictionary and store
# it in the variable average_accuracy.

# Part 3: Find the Best Model
# Write code to find the model with the highest accuracy and store its name in the variable best_model.

# Part 4: Add a New Model
# Add a new model named MobileNet with an accuracy of 0.89 to the model_accuracies dictionary.

# Instructions:
# Define a dictionary model_accuracies where the key is the name of an image classification model (a string)
# and the associated value is its accuracy (a float).
# Calculate the average accuracy of the models.
# Find the model with the highest accuracy.
# Add a new model to the dictionary.

# Part 1: Define the dictionary
# TODO: replace None with appropriate code
# Define a dictionary, `model_accuracies`, that provides information
# on the accuracies of different image classification models.
# The key is the name of a model (a string), and the associated value
# is its accuracy (a float).
#   Key      |   Value
# ResNet     |   0.91
# AlexNet    |   0.85
# VGG        |   0.88
# Inception  |   0.92
model_accuracies = {"ResNet": 0.91, "AlexNet": 0.85, "VGG": 0.88, "Inception": 0.92}

# Part 2: Calculate the average accuracy
# TODO: replace None with appropriate code
sumAccuracies = 0
for value in model_accuracies.values():
    sumAccuracies += value

average_accuracy = sumAccuracies / len(model_accuracies)

# Part 3: Find the best model
# TODO: replace None with appropriate code
bestModel = ""
maxAccuracy = 0
for key in model_accuracies.keys():
    if model_accuracies[key] > maxAccuracy:
        bestModel = key
        maxAccuracy = model_accuracies[key]

best_model = bestModel

# Part 4: Add a new model
# TODO: replace None with appropriate code
# Add the model MobileNet with an accuracy of 0.89
new_model = "MobileNet"
new_accuracy = 0.89

# Add the new model to the dictionary
model_accuracies[new_model] = new_accuracy

### Notebook grading
model_accuracies_solution = {
    "ResNet": 0.91,
    "AlexNet": 0.85,
    "VGG": 0.88,
    "Inception": 0.92,
    "MobileNet": 0.89,
}

if model_accuracies == model_accuracies_solution:
    print("Nice work defining the dictionary!\n")

average_accuracy_solution = 0.89
if average_accuracy == average_accuracy_solution:
    print("Nice work calculating the average accuracy!\n")
else:
    print(
        f"Double check your average accuracy calculation. It should be {average_accuracy_solution}."
    )

best_model_solution = "Inception"
if best_model == best_model_solution:
    print("Nice work finding the best model!\n")
else:
    print(
        f"Double check your best model calculation. It should be {best_model_solution}."
    )
