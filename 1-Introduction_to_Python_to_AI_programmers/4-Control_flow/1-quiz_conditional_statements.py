# Performance Categories:

# 0.0 - 0.5: Poor performance
# 0.51 - 0.75: Average performance
# 0.76 - 0.90: Good performance
# 0.91 - 1.0: Excellent performance

accuracy = 0.85  # use this input to make your submission


if accuracy <= 0.5:
    result = "Model performance: Poor."
elif accuracy <= 0.75:
    result = "Model performance: Average."
elif accuracy <= 0.90:
    result = "Model performance: Good."
else:
    result = "Model performance: Excellent."

# Notebook grading
if result == "Model performance: Good.":
    print("Nice work!")
else:
    print("Not quite! Are your result strings formatted correctly?")
