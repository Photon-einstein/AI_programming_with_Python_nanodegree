# Exercise 1: Tokenizing a Sentence
# Problem Statement: Given a sentence, tokenize it into individual words and print each word on a new line.
# This is a common step in NLP to prepare text data for further analysis.

# Instructions:

# Create a list of words from a sentence.
# Use a for loop to print each word on a new line.
# Example Input:

# sentence = "the quick brown fox jumped over the lazy dog"

# Define the sentence
sentence = "the quick brown fox jumped over the lazy dog"

# Tokenize the sentence into words
words = sentence.split()

# Print each word on a new line
for word in words:
    print(word)

# Exercise 2: Batching Data for Model Training
# In this exercise, you will simulate the process of batching data for model training, where data is processed
# in fixed-size batches.

# Problem Statement: Given a dataset, divide it into batches of a specified size and print each batch.
# This simulates the process of batching data during model training.

# Instructions:

# Create a list of numbers from 1 to 30.
# Use a for loop to divide the list into batches of 5 items each and print each batch.

# Define the dataset
data = list(range(1, 31))

# Define the batch size
batch_size = 5

batch_number = 1
batch_total_count = len(data) // batch_size

print("\n\n")
# Process the data in batches
for i in range(batch_total_count):
    batch = data[i * batch_size : (i + 1) * batch_size]
    print(f"Batch {i+1}: {batch}")
