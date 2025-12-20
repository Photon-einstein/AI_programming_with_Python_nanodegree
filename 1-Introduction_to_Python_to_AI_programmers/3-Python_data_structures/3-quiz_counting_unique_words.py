# Quiz: Count Unique Words in AI Model Descriptions
# Your task for this quiz is to find the number of unique words in the text of AI model descriptions.
# In the code editor below, complete these three steps to get your answer.

# Split model_descriptions into a list of words. Hint: You can use a string method you learned in the previous lesson.
# Convert the list into a data structure that would keep only the unique elements from the list.
# Print the length of the container.

model_descriptions = "ResNet is a convolutional neural network that is 50 layers deep. MobileNet is a lightweight convolutional neural network designed for mobile and embedded vision applications. VGG is a convolutional neural network model proposed by Visual Geometry Group of Oxford University. Inception is a deep convolutional neural network architecture that has achieved state-of-the-art results."

print(model_descriptions, "\n")

# TODO: replace None with appropriate code
# split model_descriptions into list of words
model_list = model_descriptions.split()
print(model_list, "\n")

# TODO: replace None with appropriate code
# convert list to a data structure that stores unique elements
model_set = set(model_list)
print(model_set, "\n")

# TODO: replace None with appropriate code
# find the number of unique words
num_unique = len(model_set)
print(num_unique, "\n")

### Notebook grading
correct_answer = 36  # Adjust this according to the actual count
if type(model_list) != list:
    print("`model_list` should be a list of all words in `model_descriptions`.")
elif type(model_set) != set:
    print("`model_set` should be a set of all unique words in `model_list`.")
elif type(num_unique) != int:
    print("Make sure you define `num_unique` with the number of unique words!")
elif num_unique != correct_answer:
    print("Not quite! Are you finding the length of the set correctly?")
else:
    print("Nice job! You can see my solution in the next page.")


# Quiz: Model Accuracy Dictionary
# In the code cell below, you'll find a dictionary containing the names of different AI
# models as keys and their corresponding accuracy values stored as values.
# Use this dictionary to answer the following questions. Submit these answers in the quiz below this Jupyter Notebook.

# Try to answer these using code, rather than inspecting the dictionary manually!

# How many unique models are in model_accuracy_dict?
# Is the key "SqueezeNet" in model_accuracy_dict?
# What is the first element in the list created when model_accuracy_dict is sorted by keys?
# Which key (model) has the highest value in model_accuracy_dict?

model_accuracy_dict = {
    "ResNet": 0.91,
    "MobileNet": 0.89,
    "VGG": 0.88,
    "Inception": 0.92,
    "AlexNet": 0.85,
    "EfficientNet": 0.93,
    "SqueezeNet": 0.87,
}

print(model_accuracy_dict, "\n")

# find number of unique keys in the dictionary
num_models = len(model_accuracy_dict.keys())
print(num_models)

# find whether 'SqueezeNet' is a key in the dictionary
contains_squeezenet = model_accuracy_dict.get("SqueezeNet") != None
print(contains_squeezenet)

# create and sort a list of the dictionary's keys
sorted_keys = list(model_accuracy_dict.keys())
sorted_keys.sort()
print(sorted_keys)

# get the first element in the sorted list of keys
first_key = sorted_keys[0]
print(first_key)

# find the element with the highest value in the dictionary
highest_accuracy_model = max(model_accuracy_dict, key=model_accuracy_dict.get)
print(highest_accuracy_model)

correct_num_models = 7
correct_contains_squeezenet = True
correct_first_key = "AlexNet"
correct_highest_accuracy_model = "EfficientNet"

if num_models != correct_num_models:
    print(f"Not quite! The number of unique models should be {correct_num_models}.")
elif contains_squeezenet != correct_contains_squeezenet:
    print(f"Not quite! Check if 'SqueezeNet' is a key in the dictionary.")
elif first_key != correct_first_key:
    print(f"Not quite! The first key when sorted should be {correct_first_key}.")
elif highest_accuracy_model != correct_highest_accuracy_model:
    print(
        f"Not quite! The model with the highest accuracy should be {correct_highest_accuracy_model}."
    )
else:
    print("Nice job! You can see my solution in the next page.")
