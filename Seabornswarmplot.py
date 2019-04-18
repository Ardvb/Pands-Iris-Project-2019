# Ard van Balkom, 12-4-19
# Show swarmplot of petal width of all 3 species, using Seaborn.


import seaborn as sns # I came across the Seaborn visualization library here: 
# https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
# It has the Iris flower data set built in, so that is very handy.
import matplotlib.pyplot as plt

# Because the dataset is built in, all we have to do is put in the right name: "Iris".
iris = sns.load_dataset("iris")

# Built the swarmplot:
sns.swarmplot(x="species", y="petal_width", data=iris) #By changing y to 'petal_length', 'sepal_length', or 'sepal_width', those will be plotted. 
# Screenshots of the other 3 swarmplots can be found seperately in the repository, as well as in the readme file: https://github.com/Ardvb/Pands-Iris-Project-2019/blob/master/README.md
# I have plotted them and attached the plots in separate files.

# Show plot.
plt.show()
