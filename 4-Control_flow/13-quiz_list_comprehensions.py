# Exercise 1: Extract Model Acronyms
# In this exercise, you'll use a list comprehension to create a new list containing just
# the acronyms of model names. Each acronym is made by taking the first letter of each word
# in the model name, converting it to uppercase, and joining the letters together.

# Example Input:

# models = ["Logistic Regression", "Decision Tree", "Random Forest", "Support Vector Machine", "Naive Bayes"]
# Example Output:

# model_acronyms = ['LR', 'DT', 'RF', 'SVM', 'NB']

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "Support Vector Machine",
    "Naive Bayes",
]
model_acronyms = [
    "".join(word[0].upper() for word in model.split()) for model in models
]

print(model_acronyms)
### Notebook grading
correct_answer = ["LR", "DT", "RF", "SVM", "NB"]
if model_acronyms == correct_answer:
    print("Good job!")
else:
    print("Not quite! Did you create the acronyms correctly?")

# Exercise 2: Learning Rate Decay
# In this exercise, you'll use a list comprehension to create a list containing the learning
# rates (LR) a model will see during training, with an initial learning rate of 0.1 and a
# decay factor of 0.1. The decay is applied multiplicatively for each subsequent step.
# Generate the learning rates for the first 5 steps.

# Example Output:

# learning_rates = [0.1, 0.01, 0.001, 0.0001, 0.00001]

num_steps = 5 + 1
initial_lr = 0.1
decay_factor = 0.1
learning_rates = [initial_lr * decay_factor**step for step in range(num_steps)]
learning_rates = [format(lr, ".6f") for lr in learning_rates]
print(learning_rates)

### Notebook grading
correct_answer = [
    "0.100000",
    "0.010000",
    "0.001000",
    "0.000100",
    "0.000010",
    "0.000001",
]
if learning_rates == correct_answer:
    print("Good job!")
else:
    print(
        "Not quite! Are you sure the decay factor is applied correctly for each step?"
    )

# Exercise 3: Filter Models by Performance
# In this exercise, you'll use a list comprehension to create a list of model names that
# achieved at least 85% performance.

# Example Input:

# model_performances = {
#    "Logistic Regression": 90,
#    "Decision Tree": 75,
#    "Random Forest": 92,
#    "Support Vector Machine": 80,
#    "Naive Bayes": 88
# }
# Example Output:

# passed_models = ['Logistic Regression', 'Random Forest', 'Naive Bayes']

model_performances = {
    "Logistic Regression": 90,
    "Decision Tree": 75,
    "Random Forest": 92,
    "Support Vector Machine": 80,
    "Naive Bayes": 88,
}

min_performance = 85

passed_models = [
    model
    for model, performance in model_performances.items()
    if performance >= min_performance
]

### Notebook grading
correct_answer = ["Logistic Regression", "Random Forest", "Naive Bayes"]
if passed_models == correct_answer:
    print("Good job!")
else:
    print("Not quite! Did you use the corresponding performance to filter each model?")
