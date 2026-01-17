# Example 1 - Step 1. Make the necessary import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Read the data from a CSV file
pokemon = pd.read_csv('pokemon.csv')
print(pokemon.shape)
pokemon.head(10)
