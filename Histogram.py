import matplotlib.pyplot as plt # Import matplotlib so we can plot functions.
import pandas as pd


ifds = pd.read_excel("iris.xls", usecols = 4) # read in the excel file 'iris'. Use only first 5 columns.


ifds_groupby = ifds.groupby(["Species"]) # Group the species of iris to use the data of each species separately

setosa = ifds_groupby.get_group("Iris-setosa") # use 'setosa' for all iris species that are called 'Iris-setosa' in the excel file.
versicolor = ifds_groupby.get_group("Iris-versicolor") # use 'versicolor' for all iris species that are called 'Iris-versicolor' in the excel file.
virginica = ifds_groupby.get_group("Iris-virginica") # use 'virginica' for all iris species that are called 'Iris-virginica' in the excel file.


feature = "sepal length" # Only data from the "sepal length" column will be used for this histogram.
plt.title(feature) # Automatically use the entered value for feature as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'feature'.
plt.xlabel( "Centimeters") # Name the x-axis 'Centimeters'
plt.ylabel("Frequency") # Name the y-axis 'Frequency'
y1 = setosa[feature] # Use the data from all setosa flowers and the entered feature as y1
y2 = versicolor[feature]
y3 = virginica[feature]
plt.hist(y1, label="Setosa") # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2, label ="Versicolor") # Add label to make the histogram easier to read.
plt.hist(y3, label ="Virginica")
plt.legend() # Show the legend with the labels.
plt.show()

# To do the same for 'sepal width', 'petal length', or 'petal width' data, just change the input for feature, as shown below.

feature = "sepal width" # Only data from the "sepal width" column will be used for this histogram.
plt.title(feature) # Automatically use the entered value for feature as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'feature'.
plt.xlabel( "Centimeters") #
plt.ylabel("Frequency")
y1 = setosa[feature] # Use the data from all setosa flowers and the entered feature as y1
y2 = versicolor[feature]
y3 = virginica[feature]
plt.hist(y1, label="Setosa") # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2, label ="Versicolor") # Add label to make the histogram easier to read.
plt.hist(y3, label ="Virginica")
plt.legend() # Show the legend with the labels.
plt.show()

feature = "petal length" # Only data from the "petal length" column will be used for this histogram.
plt.title(feature) # Automatically use the entered value for feature as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'feature'.
plt.xlabel( "Centimeters")
plt.ylabel("Frequency")
y1 = setosa[feature] # Use the data from all setosa flowers and the entered feature as y1
y2 = versicolor[feature]
y3 = virginica[feature]
plt.hist(y1, label="Setosa") # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2, label ="Versicolor") # Add label to make the histogram easier to read.
plt.hist(y3, label ="Virginica")
plt.legend() # Show the legend with the labels.
plt.show()

feature = "petal width" # Only data from the "petal width" column will be used for this histogram.
plt.title(feature) # Automatically use the entered value for feature as the title.
# This way, when you want to plot a histogram for the sepal width for instance, you only have to change the input for 'feature'.
plt.xlabel( "Centimeters")
plt.ylabel("Frequency")
y1 = setosa[feature] # Use the data from all setosa flowers and the entered feature as y1
y2 = versicolor[feature]
y3 = virginica[feature]
plt.hist(y1, label="Setosa") # Plot the histogram for y1. No need to use bins, as they are automatically done right.
plt.hist(y2, label ="Versicolor") # Add label to make the histogram easier to read.
plt.hist(y3, label ="Virginica")
plt.legend() # Show the legend with the labels.
plt.show()

# Used: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html to learn about groupby function