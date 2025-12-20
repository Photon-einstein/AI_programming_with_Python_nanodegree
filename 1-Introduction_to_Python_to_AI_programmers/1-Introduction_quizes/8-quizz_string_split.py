# Quiz: Analyzing AI Model Output Text

# Scenario:
# You are analyzing the output of an AI model from a recent project.
# You need to answer specific questions about the text using string methods.

# Task:
# Answer the following questions about the string variable model_output:

# What is the length of the string variable model_output?
# What is the index of the first occurrence of the word 'accuracy' in model_output?
# What is the index of the last occurrence of the word 'model' in model_output?
# What is the count of occurrences of the word 'model' in model_output?
# Tokenize the model_output into individual words.
# Perform a basic sentiment analysis by counting the number of positive and negative words in the model_output.

model_output = (
    "The AI model achieved an accuracy of 92.5% in the initial tests."
    "\nThe model's performance was consistent across different datasets.\nFurther tuning of "
    "the model hyperparameters improved the accuracy to 94%."
    "\nThis model is now ready for deployment in the production environment.\nModel performance will "
    "be monitored continuously to ensure it meets the expected standards."
)

print(model_output)

# Answer the questions
length_of_model_output = len(model_output)
index_first_accuracy = model_output.find("accuracy")
index_last_model = model_output.rfind("model")
count_model = model_output.lower().count("model")

# Tokenize the model_output into individual words
tokens = model_output.split()
normalized_tokens = [token.strip(".,'\"!?").lower() for token in tokens]

# Perform a basic sentiment analysis
positive_words = ["achieved", "consistent", "improved", "ready", "meets"]
negative_words = ["monitored"]

count_positive = sum(1 for token in normalized_tokens if token in positive_words)
count_negative = sum(1 for token in normalized_tokens if token in negative_words)
print("-" * 50)
# Output your answers in descriptive messages
print(
    "The length of the model output string is {} characters.".format(
        length_of_model_output
    )
)
print(
    "The first occurrence of the word 'accuracy' is at index {}.".format(
        index_first_accuracy
    )
)
print(
    "The last occurrence of the word 'model' is at index {}.".format(index_last_model)
)
print("The word 'model' occurs {} times in the model output.".format(count_model))
print("\nThe tokenized model output is: {}".format(tokens))
print("\nThe number of positive words is: {}".format(count_positive))
print("\nThe number of negative words is: {}".format(count_negative))
