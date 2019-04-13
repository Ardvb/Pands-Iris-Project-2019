import matplotlib.pyplot as plt # Import matplotlib so we can plot functions.
import pandas as pd


ifds = pd.read_excel("iris.xls", usecols = 4) # read in the excel file 'iris'. Use only first 5 columns.


ifds_groupby = ifds.groupby(["Species"]) # Group the species of iris to use the data of each species separately

setosa = ifds_groupby.get_group("Iris-setosa") # use 'setosa' for all iris species that are called 'Iris-setosa' in the excel file.
versicolor = ifds_groupby.get_group("Iris-versicolor") # use 'versicolor' for all iris species that are called 'Iris-versicolor' in the excel file.
virginica = ifds_groupby.get_group("Iris-virginica") # use 'virginica' for all iris species that are called 'Iris-virginica' in the excel file.


column_name = "sepal length" # Only data in the column 'sepal length' will be used for this histogram
plt.title(column_name) # Automatically use the entered value for column name as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'column name'.
plt.xlabel( "Centimeters")
y1 = setosa[column_name] # Use the data from all setosa flowers and the entered column name as y1
y2 = versicolor[column_name]
y3 = virginica[column_name]
plt.hist(y1) # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2)
plt.hist(y3)
plt.show()

# To do the same for 'sepal width', 'petal length', or 'petal width' data, just change the input for column name, as shown below.

column_name = "sepal width" # Only data in the column 'sepal length' will be used for this histogram
plt.title(column_name) # Automatically use the entered value for column name as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'column name'.
plt.xlabel( "Centimeters")
y1 = setosa[column_name] # Use the data from all setosa flowers and the entered column name as y1
y2 = versicolor[column_name]
y3 = virginica[column_name]
plt.hist(y1) # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2)
plt.hist(y3)
plt.show()

column_name = "petal length" # Only data in the column 'sepal length' will be used for this histogram
plt.title(column_name) # Automatically use the entered value for column name as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'column name'.
plt.xlabel( "Centimeters")
y1 = setosa[column_name] # Use the data from all setosa flowers and the entered column name as y1
y2 = versicolor[column_name]
y3 = virginica[column_name]
plt.hist(y1) # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2)
plt.hist(y3)
plt.show()

column_name = "petal width" # Only data in the column 'sepal length' will be used for this histogram
plt.title(column_name) # Automatically use the entered value for column name as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'column name'.
plt.xlabel( "Centimeters")
y1 = setosa[column_name] # Use the data from all setosa flowers and the entered column name as y1
y2 = versicolor[column_name]
y3 = virginica[column_name]
plt.hist(y1) # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2)
plt.hist(y3)
plt.show()