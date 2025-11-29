# Exercise 1: Count Image Batches
# In this exercise, you'll simulate processing batches of images in a machine learning model.
# You'll start from a given number of images and process them in batches until all images are processed.
# Use processed_images as the variable that you'll change each time through the loop.

# Example Input:

# total_images = 100
# batch_size = 20
# Example Output:

# processed_images = 100

total_images = 100
batch_size = 20

processed_images = 0
# TODO

while processed_images < total_images:
    processed_images += batch_size


### Notebook grading
def get_solution(total_images, batch_size):
    processed_images = 0
    while processed_images < total_images:
        processed_images += batch_size
    return processed_images


correct = get_solution(total_images, batch_size)

if processed_images == correct:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")


# Exercise 2: Validate Batch Processing
# In this exercise, you'll validate that your batch processing function works correctly
# and handle the case where the number of images to process is less than the batch size.

# Example Input:

# total_images = 100
# batch_size = 20
# Example Output:

# result = 100
# Example Input with total_images < batch_size:

# total_images = 10
# batch_size = 20
# Example Output:

# result = 10

total_images = 100
batch_size = 20
result = 0

if total_images < batch_size:
    result = total_images
else:
    processed_images = 0
    while processed_images < total_images:
        processed_images += batch_size
        if processed_images > total_images:
            processed_images = total_images
    result = processed_images


### Notebook grading
def get_solution(total_images, batch_size):
    if total_images < batch_size:
        return total_images
    else:
        processed_images = 0
        while processed_images < total_images:
            processed_images += batch_size
        return processed_images


correct_ans = get_solution(total_images, batch_size)

if result == correct_ans:
    print("Good job!")
else:
    print("Oops! It doesn't look like the expected answer.")

# Exercise 3: Find Nearest Batch Size
# In this exercise, you'll write a while loop that finds the largest batch size
# (a perfect square less than an integer limit) and stores it in a variable nearest_batch.
# A batch size is the product of an integer multiplied by itself, for example 36 is a perfect
# batch size because it equals 6*6.

# Example Input:

# limit = 50
# Example Output:

# nearest_batch = 36

limit = 50
nearest_batch = 0
current_value = 0

while pow(current_value + 1, 2) < limit:
    current_value += 1
    nearest_batch = pow(current_value, 2)


### Notebook grading
def get_solution(limit):
    current_value = 0
    while (current_value + 1) ** 2 < limit:
        current_value += 1
        nearest_batch = current_value**2
    return nearest_batch


correct_ans = get_solution(limit)

if nearest_batch == correct_ans:
    print("Good job!")
else:
    print("Not quite. Did you assign your result to `nearest_batch`?")

# Other exercise question:

num_list = [
    422,
    136,
    524,
    85,
    96,
    719,
    85,
    92,
    10,
    17,
    312,
    542,
    87,
    23,
    86,
    191,
    116,
    35,
    173,
    45,
    149,
    59,
    84,
    69,
    113,
    166,
]

max_odd_numbers = 5
sum_odd_numbers = 0
num_odd_numbers = 0

for num in num_list:
    if num % 2 == 1:
        sum_odd_numbers += num
        num_odd_numbers += 1
        if num_odd_numbers >= max_odd_numbers:
            break

print(f"Sum odd numbers is {sum_odd_numbers}")
