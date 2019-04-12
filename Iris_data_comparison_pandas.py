# Ard van Balkom 11-4-19
# Display data of the Iris flower data set, using Pandas

import numpy as np 
import pandas as pd 

ifds = pd.read_excel("iris.xls", usecols=4) #Read the file 'ifds' into the program and only use columns 0-4.

# Learned how to do this at: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-excel

# by entering print(iris), we are now able to print the entire table of data.

print(ifds.describe()) # This displays a quick summary of the data (mean, min and max amongst others).
print() # Print an empty line, to make it look a bit more presentable.

print(ifds.median()) # Display the median of all data, separated per column.
print()

print(ifds.mode())  # Display the mode of all data.
print()

setosa = ifds[ifds.iris == "Iris-setosa"] # Only show data for the species "setosa", by only using the rows with "Iris-setosa" in them.
# Used https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas as inspiration.

print(setosa.describe()) # Display a quick summary of all data of the "setosa".
print()

print(setosa.median()) # Display the median of all data of the species "setosa". Learned how to use median and mode at: 
# https://www.geeksforgeeks.org/python-pandas-dataframe-mode/
print()

print(setosa.mode()) # Diplay the mode of all data of the species "setosa".

versicolor = ifds[ifds.iris == "Iris-versicolor"] # Do the same for the species "versicolor"

print(versicolor.describe())
print()

print(versicolor.median())
print()

print(versicolor.mode())
print()

virginica = ifds[ifds.iris == "Iris-virginica"] # Do the same for the species "virginica"

print(virginica.describe())
print()

print(virginica.median())
print()

print(virginica.mode())
print()
