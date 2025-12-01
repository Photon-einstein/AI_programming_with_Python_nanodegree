# Exercise 1: Zip Model Metrics
# Use zip to write a for loop that creates a string specifying the model name and its
# corresponding metrics (accuracy, precision, recall) and appends it to the list model_metrics.

# Each string should be formatted as model: accuracy, precision, recall.
# For example, the string for the first model should be Model1: 0.95, 0.94, 0.93.

model_names = ["Model1", "Model2", "Model3", "Model4", "Model5"]
accuracy = [0.95, 0.89, 0.92, 0.87, 0.93]
precision = [0.94, 0.88, 0.91, 0.86, 0.92]
recall = [0.93, 0.87, 0.91, 0.85, 0.91]
model_metrics = []

# write your for loop here
for model, accuracy, precision, recall in zip(model_names, accuracy, precision, recall):
    model_metrics.append("{}: {}, {}, {}".format(model, accuracy, precision, recall))


### Notebook grading
correct_answer = [
    "Model1: 0.95, 0.94, 0.93",
    "Model2: 0.89, 0.88, 0.87",
    "Model3: 0.92, 0.91, 0.91",
    "Model4: 0.87, 0.86, 0.85",
    "Model5: 0.93, 0.92, 0.91",
]
if model_metrics == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")


# Exercise 2: Zip Metrics to Dictionary
# Use zip to create a dictionary model_performance that uses model_names as keys and accuracies as values.

model_names = ["Model1", "Model2", "Model3", "Model4", "Model5"]
accuracies = [0.95, 0.89, 0.92, 0.87, 0.93]

model_performance = dict(zip(model_names, accuracies))

### Notebook grading
correct_answer = {
    "Model1": 0.95,
    "Model2": 0.89,
    "Model3": 0.92,
    "Model4": 0.87,
    "Model5": 0.93,
}
if model_performance == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

# Exercise 3: Unzip Model Metrics
# Unzip the model_performance tuple into two model_names and accuracies tuples.

model_performance = (
    ("Model1", 0.95),
    ("Model2", 0.89),
    ("Model3", 0.92),
    ("Model4", 0.87),
    ("Model5", 0.93),
)

# define model_names and accuracies here
model_names, accuracies = zip(*model_performance)

### Notebook grading
correct_answer_names = ("Model1", "Model2", "Model3", "Model4", "Model5")
correct_answer_accuracies = (0.95, 0.89, 0.92, 0.87, 0.93)
if model_names == correct_answer_names and accuracies == correct_answer_accuracies:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

# Exercise 4: Transpose Metrics Matrix
# Use zip to transpose metrics_data from a 4-by-3 matrix to a 3-by-4 matrix.

metrics_data = (
    (0.95, 0.94, 0.93),
    (0.89, 0.88, 0.87),
    (0.92, 0.91, 0.90),
    (0.87, 0.86, 0.85),
)

# Transpose the matrix
metrics_data_transpose = [tuple(col) for col in zip(*metrics_data)]

### Notebook grading
correct_answer = [
    (0.95, 0.89, 0.92, 0.87),
    (0.94, 0.88, 0.91, 0.86),
    (0.93, 0.87, 0.90, 0.85),
]
if metrics_data_transpose == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

# Exercise 5: Enumerate Model Performances
# Use enumerate to modify the model_descriptions list so that each element contains the model name
# followed by its corresponding accuracy.
# For example, the first element of model_descriptions should change from "Model1 Description" to
# "Model1 Description 0.95".

model_descriptions = [
    "Model1 Description",
    "Model2 Description",
    "Model3 Description",
    "Model4 Description",
    "Model5 Description",
]
accuracies = [0.95, 0.89, 0.92, 0.87, 0.93]

# write your for loop here
for i, mode in enumerate(model_descriptions):
    model_descriptions[i] = "{} {}".format(model_descriptions[i], accuracies[i])

### Notebook grading
correct_answer = [
    "Model1 Description 0.95",
    "Model2 Description 0.89",
    "Model3 Description 0.92",
    "Model4 Description 0.87",
    "Model5 Description 0.93",
]
if model_descriptions == correct_answer:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")
