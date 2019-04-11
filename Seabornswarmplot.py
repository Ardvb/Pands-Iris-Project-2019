import seaborn as sns # I came across the Seaborn visualization library here: 
# https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
# It has the Iris flower data set built in, so that is very handy.
import matplotlib.pyplot as plt

# Because the dataset is built in, all we have to do is put in the right name: "Iris"
iris = sns.load_dataset("iris")

# Built the Iris plot, using the swarmplot option:
sns.swarmplot(x="species", y="petal_width", data=iris)

# Show plot
plt.show()




# Used https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas

# Used https://www.geeksforgeeks.org/python-pandas-dataframe-mode/

# Used https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-excel to learn how to read in an excel file and how to only use a certain amount of columns)