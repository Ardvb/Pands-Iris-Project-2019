# Iris-Data-Set-Project-2019

## Analysis of Fisher's Iris Data Set

### Author: Ard van Balkom
### Course: Higher diploma in data analytics
### Module: Programming and scripting

This repository contains my research on Fisher's Iris data set, as well as my documentation and code based on this research.

## How to download the repository

1. Go to my Github profile: https://github.com/Ardvb/
2. Click on the download button and copy/paste the link: https://github.com/Ardvb/Pands-Iris-Project-2019

## How to run the code:

1. Make sure you have python installed on your device: https://www.python.org/downloads/

## Table of Contents

1. Background information

2. Analysis of Iris data set
  
     2.1 Libraries
      
        2.1.1 Numpy
      
        2.1.2 Matplotlib
      
        2.1.3 Seaborn
      
        2.1.4 Pandas
    
     2.2 Coding and data visualization
  
        2.2.1 Describe, median and mode
      
        2.2.2 Comparing the species
      
        2.2.3 Histograms
      
        2.2.4 Swarmplots
      
        2.2.5 Possible correlations, visualized in scatterplots
    
 3. Conclusions
 
 4. References

## 1. Background information

### The Iris flower data set

![irises](https://user-images.githubusercontent.com/47186083/56307201-35335780-613c-11e9-8191-827eca81c80e.png)

This data set was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species.
Two of the species were collected from the same pasture, on the same day, and measured at the same time by the same person with the same apparatus.
The iris data set consists of 50 samples each, of three iris species (Iris setosa, Iris virginica and Iris versicolor). 
From every sample four features were measured: the length and width of both the sepals and petals, in centimetres.


![Ronald Fisher](https://user-images.githubusercontent.com/47186083/56324720-902e7400-6167-11e9-9ab9-881e84d8a6c2.jpg)


British statistician and biologist Ronald Fisher used this dataset to develop a linear discriminant model to distinguish the species from each other.
Ronald Fisher is one of the most celebrated statisticians of all time. 
He is described as “a genius who almost single-handedly created the foundations for modern statistical science”.
The data set has some key features that make it very useful in all sorts of data analytics, from data visualisation to machine learning.
It is small, but not trivial. It consists of real data of good quality. 
The goal of the dataset, to discriminate between three species of Iris, based on measurements is simple, yet challenging.
Also, the fact someone as famous as Ronald Fisher used the dataset makes it more interesting to a lot of statisticians.
No wonder it is one of the most used data sets in the world of statistics.


## 2. Analysis of Iris data set

### 2.1 Libraries used

#### 2.1.1 Numpy

Numpy is a fundamental library for scientific computing in Python. It adds support for large, multi dimensional arrays and matrices. It also includes a large collection of high level mathematical functions to operate on these arrays.

#### 2.1.2 Matplotlib

Matplotlib is the plotting library of Numpy. It provides an object-oriented API for embedding plots into applications.
I used this library to plot histograms, amongst other things.

#### 2.1.3 Seaborn

Seaborn is a Python visualization library based on matplotlib, providing a high-level interface for drawing statistical graphics.
I found this library to be easy to use and used it to plot swarmplots and scatterplots.

#### 2.1.4 Pandas

Pandas is a library providing high-performance, and easily usable data structures and data analysis tools for Python.
I have used it to read in the excel file containing the Iris date set, amongst other things.


### 2.2 Coding and data visualization

#### 2.2.1 describe, median and mode

I have written Python code to try and find some interesting information about this data set.
In this readme I will show my code and the output it returns.

First I wanted to get a good look at the data set by visualizing some basic features.

![image](https://user-images.githubusercontent.com/47186083/56310182-28fec880-6143-11e9-8edc-210f58f89ab9.png)

![image](https://user-images.githubusercontent.com/47186083/56310252-564b7680-6143-11e9-8ca4-2de350f58915.png)

By reading the Iris data set Excel file into my program I am able to project in onto the screen using cmder. 

Now we can start looking into what some of the more interesting features of the data set. By using the _.describe_ command, I can see lots of useful information, such as the mean, the standard deviation, the minimum and maximum etc.


![image](https://user-images.githubusercontent.com/47186083/56310349-9dd20280-6143-11e9-85b8-de1e17f8b4e5.png)
![image](https://user-images.githubusercontent.com/47186083/56310392-b17d6900-6143-11e9-9662-068cbbd72524.png)


By using the _.median_ and _.mode_ commands, I am able to see what the median(the number that is halfway into the set) and the mode(most frequently occurring number).

![image](https://user-images.githubusercontent.com/47186083/56310565-205ac200-6144-11e9-9f1f-e74069197ae3.png)
![image](https://user-images.githubusercontent.com/47186083/56310596-310b3800-6144-11e9-8ad5-46d73e3347c8.png)

![image](https://user-images.githubusercontent.com/47186083/56310641-4e400680-6144-11e9-8fde-742a08ce4192.png)
![image](https://user-images.githubusercontent.com/47186083/56311063-08377280-6145-11e9-9bcc-cc65739adc8f.png)


#### 2.2.2 Comparing the species

The next step was to seperate the species by comparing the data from each species to the others.
I wrote some code to only display the data of 'Iris setosa':

![image](https://user-images.githubusercontent.com/47186083/56311174-49c81d80-6145-11e9-8481-19aab85ee9db.png)
![image](https://user-images.githubusercontent.com/47186083/56311201-59dffd00-6145-11e9-9aa3-d0952774d727.png)

And the median and mode:

![image](https://user-images.githubusercontent.com/47186083/56311337-b04d3b80-6145-11e9-8bd8-917e02d3fffa.png)
![image](https://user-images.githubusercontent.com/47186083/56311371-c5c26580-6145-11e9-9606-b5f62285dbaa.png)

![image](https://user-images.githubusercontent.com/47186083/56311389-d4108180-6145-11e9-9584-f809802352a6.png)
![image](https://user-images.githubusercontent.com/47186083/56311422-e38fca80-6145-11e9-911f-c847ecdec2bd.png)


I have done the same for both other species. However, the differences between the species was even more pronounced in the following visualizations, so I haven't included all screenshots of mode and median here.

From looking at this data, we can already spot some differences between the species. Especially between Iris setosa and the other two.
However, to make it even easier to see, I have plotted some histograms and other plots.


#### 2.2.3 Histograms

First I have plotted a histogram of the sepal length of all three species using the matplotlib.pyplot library. With the sepal length in centimeters on the x-axis, and the frequency on the y-axis.

![image](https://user-images.githubusercontent.com/47186083/56308930-59913300-6140-11e9-924c-0b371f6c22c9.png)
![image](https://user-images.githubusercontent.com/47186083/56309064-b7257f80-6140-11e9-9047-aa38b5f36ac1.png)


I have also plotted histograms of the other features with virtually the same coding:

![image](https://user-images.githubusercontent.com/47186083/56309125-d3292100-6140-11e9-9078-ff3e1afbf12e.png)
![image](https://user-images.githubusercontent.com/47186083/56309163-e2a86a00-6140-11e9-9cbb-e8bbbf8f58ba.png)
![image](https://user-images.githubusercontent.com/47186083/56309171-e76d1e00-6140-11e9-9b1e-01df2a5af9df.png)

Here we can start to see clearly that especially the petal length and width of the Iris setosa is much shorter than the other two species.


#### 2.2.4 Swarmplots

Another interesting and suitable way of visualizing if the swarmplot, than can be created using seaborn. Using the swarmplot, you can see the features of the different species in the blink of an eye.

![image](https://user-images.githubusercontent.com/47186083/56309335-4cc10f00-6141-11e9-8071-925c9314e7ce.png)

![image](https://user-images.githubusercontent.com/47186083/56309415-6f532800-6141-11e9-864d-84f9d16bdf00.png)

And the other features:

![image](https://user-images.githubusercontent.com/47186083/56324986-73df0700-6168-11e9-9572-4c271c8b7b4a.png)
![image](https://user-images.githubusercontent.com/47186083/56325024-9b35d400-6168-11e9-943b-bdf096049929.png)
![image](https://user-images.githubusercontent.com/47186083/56325001-85c0aa00-6168-11e9-97ba-a883c7956d56.png)

As we can see, the setosa is clearly smaller than the other two species (except for the sepal width), and virginica is the largest for 3 out of 4 features (sepal length, petal length and petal width). 
The best way to try and distinguish the virginica from the versicolor, is by looking at petal length and petal width, which are larger. However, there is still some overlap and the difference is not as pronounced as that between between setosa and the other 2 species.


#### 2.2.5 Possible correlations, visualized in scatterplots

To further try to differentiate between virginica and versicolor, I have looked at possible correlations in any of the 4 measured features.
To visualize these correlations, I have chosen to use the scatterplot. I have plotted all 6 possible correlations and attached screenshots of code and output below.

![image](https://user-images.githubusercontent.com/47186083/56311850-d7f0d380-6146-11e9-8dd6-a82be70ec6ed.png)

![image](https://user-images.githubusercontent.com/47186083/56312187-8dbc2200-6147-11e9-8600-034425152cd2.png)
![image](https://user-images.githubusercontent.com/47186083/56312198-94e33000-6147-11e9-9374-256411ad3811.png)
![image](https://user-images.githubusercontent.com/47186083/56313428-83e7ee00-614a-11e9-9363-ea7465cf701e.png)
![image](https://user-images.githubusercontent.com/47186083/56313481-9bbf7200-614a-11e9-820f-f159519e063f.png)
![image](https://user-images.githubusercontent.com/47186083/56313275-294e9200-614a-11e9-94fa-19f0ae1fd5c1.png)
![image](https://user-images.githubusercontent.com/47186083/56313183-e42a6000-6149-11e9-84f5-b2dad7d2a85b.png)

Here we see some interesting things. For instance, looking at the correlation between sepal length and petal length, the Iris setosa has none or very little correlation, whereas the other two species both have a strong linear correlation. Something similar can be seen, to a slightly lesser extent, in all but one of the plots. Only in the sepal length and sepal width correlation does the Iris setosa have a linear correlation, where the other two species correlate in a linear way more or less in all 6 plots.
When looking at the correlation between petal length and petal width
Overall the Iris virginica seems to correlate in a slightly more linear way compared to the Iris versicolor, but this is not enough to clearly distinguish between the two. 


## 3. Conclusions and summary

Looking at all data, and data visualizations, I have used for this analysis, a few conclusions can be drawn.
First of all, it is an interesting data set. To distinguish between the setosa and the other two species was easy, but to differentiate between virginica and versicolor was very challenging. Even though it is quite easy to see in the histograms, that the virginica has, in general, taller features than the versicolor species, there was some overlap.
Therefore I tried to find a defining feature to seperate the two, by looking at correlations between the different features. Here I encountered the same phenomenon. A difference in size, but not definitive enough to tell which is which from the measurements alone.

I learned a lot about visualizing data, and especially the seaborn library was a real eye-opener for me. Very easy to split the data and produce good looking plots.


## 4. References


1. https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas

2. https://www.geeksforgeeks.org/python-pandas-dataframe-mode/

3. https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-excel

4. https://www.datacamp.com/community/tutorials/seaborn-python-tutorial

5. https://seaborn.pydata.org/tutorial/relational.html#relational-tutorial

6. https://seaborn.pydata.org/generated/seaborn.scatterplot.html

7. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

8. https://stackoverflow.com/questions/41213346/python-matplotlib-label-in-histogram

9. Video lecture Ian McLoughlin: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7

10. Data set downloaded from: www.saedsayad.com/datasets/Iris.xls

### Photos:

11. Iris setosa photo: https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg

12. Iris versicolor photo: https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_versicolor_3.jpg

13. Iris virginica photo: https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_virginica.jpg

14. Photo of 3 Iris flowers combined: https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers

15. Ronald Fisher photo: http://www.genetics.org/content/genetics/154/4/1419/F1.large.jpg?width=800&height=600&carousel=1


