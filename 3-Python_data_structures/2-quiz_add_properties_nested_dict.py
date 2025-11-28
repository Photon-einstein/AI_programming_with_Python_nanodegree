# Quiz: Adding Properties to Nested Dictionaries for Image Classification Models
# In this exercise, you will work with nested dictionaries. Add another entry, is_lightweight,
# to each dictionary in the models dictionary. After inserting the new entries, you should be able to perform these lookups:

# >>> print(models['ResNet']['is_lightweight'])
# False
# >>> print(models['MobileNet']['is_lightweight'])
# True
# Here is the initial models dictionary:

models = {
    "ResNet": {"layers": 50, "accuracy": 0.91, "type": "CNN"},
    "MobileNet": {"layers": 28, "accuracy": 0.89, "type": "CNN"},
}

# TODO: Add an 'is_lightweight' entry to the ResNet and MobileNet dictionaries
# hint: MobileNet is a lightweight model, ResNet isn't

models["ResNet"]["is_lightweight"] = False
models["MobileNet"]["is_lightweight"] = True


### Notebook grading
explanation_str = """Your code produced the wrong result. Looks like you did not add the 'is_lightweight' property properly for {}."""
if (
    not ("is_lightweight" in models["ResNet"].keys())
    or models["ResNet"]["is_lightweight"] != False
):
    print(explanation_str.format("'ResNet'"))
elif (
    not ("is_lightweight" in models["MobileNet"].keys())
    or models["MobileNet"]["is_lightweight"] != True
):
    print(explanation_str.format("'MobileNet'"))
else:
    print("""Your code passes all of our tests, nice work!""")
