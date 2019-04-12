# Ard van Balkom, 12-4-19
# Show plot of petal width of all 3 species


import seaborn as sns # I came across the Seaborn visualization library here: 
# https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
# It has the Iris flower data set built in, so that is very handy.
import matplotlib.pyplot as plt

# Because the dataset is built in, all we have to do is put in the right name: "Iris".
iris = sns.load_dataset("iris")

# Built the Iris plot, using the swarmplot option:
sns.swarmplot(x="species", y="petal_width", data=iris) #By changing y to 'petal_length', 'sepal_length', or 'sepal_width', those will be plotted.
# I have plotted them and attached the plots in separate files.

# Show plot.
plt.show()

