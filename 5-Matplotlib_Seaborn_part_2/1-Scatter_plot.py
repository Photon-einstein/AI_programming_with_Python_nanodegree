import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Example 1 a. Scatter plot showing negative correlation between two variables
# TO DO: Necessary import
# Read the CSV file
fuel_econ = pd.read_csv("fuel_econ.csv")
print("Table 'fuel_econ.csv, first entries:\n", fuel_econ.head(10))
# Scatter plot
plt.scatter(data=fuel_econ, x="displ", y="comb")
plt.xlabel("Displacement (L)")
plt.ylabel("Combined Fuel Eff. (mpg)")
plt.title("Displacement vs Combined Fuel Eff.")
plt.show()

# Example 1 b. Scatter plot showing negative correlation between two variables
sb.regplot(data=fuel_econ, x="displ", y="comb")
plt.xlabel("Displacement (L)")
plt.ylabel("Combined Fuel Eff. (mpg)")
plt.title("Displacement vs Combined Fuel Eff.")
plt.show()


# Example 3. Plot the regression line on the transformed data
def log_trans(x, inverse=False):
    if not inverse:
        return np.log10(x)
    else:
        return np.power(10, x)


sb.regplot(data=fuel_econ, x=fuel_econ["displ"], y=fuel_econ["comb"].apply(log_trans))
tick_locs = [10, 20, 50, 100]
plt.yticks(log_trans(tick_locs), tick_locs)
plt.title("Displacement vs Combined Fuel Eff. log scale")
plt.show()
