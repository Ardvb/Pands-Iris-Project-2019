# Ard van Balkom, 12-4-19
# Plot scatterplots, using data of the Iris flower data set. 

import seaborn as sns # I came across the Seaborn visualization library here: 
# https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
# It has the Iris flower data set built in, so that is very handy.
import matplotlib.pyplot as plt

# Because the dataset is built in, all we have to do is put in the right name: "Iris".
iris = sns.load_dataset("iris")

sns.scatterplot(x=iris.sepal_length, y=iris.sepal_width, hue=iris.species) # Create a scatterplot that shows the correlation between sepal length and sepal width. 
# Using the sepal length on the x-axis and the sepal width on the y-axis. By using 'hue', I am able to give the points different colors for every species.
plt.show()

sns.scatterplot(x=iris.sepal_length, y=iris.petal_length, hue=iris.species) # Do the same for the correlation between sepal length and petal length.
plt.show()

sns.scatterplot(x=iris.sepal_length, y=iris.petal_width, hue=iris.species) # Do the same for other possible correlations
plt.show()

sns.scatterplot(x=iris.sepal_width, y=iris.petal_length, hue=iris.species)
plt.show()

sns.scatterplot(x=iris.sepal_width, y=iris.petal_width, hue=iris.species)
plt.show()

sns.scatterplot(x=iris.petal_length, y=iris.petal_width, hue=iris.species)
plt.show()

# Learned about scatterplots here: https://seaborn.pydata.org/tutorial/relational.html#relational-tutorial and how to do a multidimensional one here: https://seaborn.pydata.org/generated/seaborn.scatterplot.html