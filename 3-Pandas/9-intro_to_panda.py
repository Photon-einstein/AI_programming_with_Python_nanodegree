import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("\ns =\n", s)

# Creating a Series by passing a list of values, letting pandas create a default RangeIndex.
dates = pd.date_range("20130101", periods=6)
print("\ndates:\n", dates)

# Creating a DataFrame by passing a NumPy array with a datetime index using date_range() 
# and labeled columns:
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print("\ndf:\n", df)

# Creating a DataFrame by passing a dictionary of objects where the keys are the column
# labels and the values are the column values.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print("\ndf2:\n", df2)

# The columns of the resulting DataFrame have different dtypes:
print("\nResulting DataFrame have different dtypes:\n", df2.dtypes)

# Viewing data
# Use DataFrame.head() and DataFrame.tail() to view the top and bottom rows of the frame
# respectively:
print("\ndf head:\n", df.head())
print("\ndf tail:\n", df.tail(3))

# Display the DataFrame.index or DataFrame.columns:
print("\ndf index:\n", df.index)
print("\ndf columns:\n", df.columns)

# Return a NumPy representation of the underlying data with DataFrame.to_numpy() without
# the index or column labels:
print("\nNumPy representation of the underlying data without the index or column labels:\n", df.to_numpy())

# describe() shows a quick statistic summary of your data:
print("\nQuick statistic summary of your data:\n", df.describe())

# Transposing your data:
print("\nData transposed:\n", df.T)

# Data:
print("\nData:\n", df)

# DataFrame.sort_index() sorts by an axis:
print("\nDataFrame.sort_index() sorts by an axis:\n", df.sort_index(axis=1, ascending=False))

# DataFrame.sort_values() sorts by values:
print("\nDataFrame.sort_values() sorts by values:\n", df.sort_values(by="B"))

# For a DataFrame, passing a single label selects a columns and yields a Series equivalent to df.A:
print("\nFor a DataFrame, passing a single label selects a columns and yields a Series equivalent to df.A:\n", df["A"])

# For a DataFrame, passing a slice : selects matching rows:
print("\nFor a DataFrame, passing a slice : selects matching rows:\n", df[0:3])

# Selecting a row matching a label:
print("\nSelecting a row matching a label:\n", df.loc[dates[0]])

# Selecting all rows (:) with a select column labels:
print("\nSelecting all rows (:) with a select column labels:\n", df.loc[:, ["A", "B"]])

# For label slicing, both endpoints are included:
print("\nFor label slicing, both endpoints are included:\n", df.loc["20130102":"20130104", ["A", "B"]])

# Selecting a single row and column label returns a scalar:
print("\nSelecting a single row and column label returns a scalar:\n", df.loc[dates[0], "A"])

# For getting fast access to a scalar (equivalent to the prior method):
print("\nFor getting fast access to a scalar (equivalent to the prior method):\n", df.at[dates[0], "A"])

# Select via the position of the passed integers:
print("\nSelect via the position of the passed integers:\n", df.iloc[3])

# Integer slices acts similar to NumPy/Python:
print("\nInteger slices acts similar to NumPy/Python:\n", df.iloc[3:5, 0:2])
