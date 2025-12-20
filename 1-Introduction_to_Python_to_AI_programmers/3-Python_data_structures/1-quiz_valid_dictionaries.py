# In this exercise, you will correct an invalid dictionary that maps AI model researchers to their research topics.
# In Python, dictionary keys must be immutable types, such as strings or tuples. Lists, being mutable,
# cannot be used as dictionary keys.

# corrected dictionary using tuples as keys
research_topics = {
    ("AlexNet", "Convolutional Neural Network"): "Image Classification",
    ("VGG", "Visual Geometry Group"): "Deep Learning",
    ("ResNet", "Residual Networks"): "Network Architecture",
}

# Verify the corrected dictionary
print(research_topics)
