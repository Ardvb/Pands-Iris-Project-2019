import matplotlib.pyplot as plt # Import matplotlib so we can plot functions.
import pandas as pd


ifds = pd.read_excel("iris.xls", usecols = 4)


ifds_groupby = ifds.groupby(["Species"]) # Group the species of iris to use the data of each species separately

setosa = ifds_groupby.get_group("Iris-setosa")
versicolor = ifds_groupby.get_group("Iris-versicolor")
virginica = ifds_groupby.get_group("Iris-virginica")


    
plt.title("Sepal Length")
plt.xlabel( "Sepal Length in Centimeters")


ifds_groupby.plot.hist()

plt.show()


