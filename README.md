# Pands-Iris-Project-2019

This repository contains my research on Fisher's Iris data set, as well as my documentation and code based on this research.

## How to download the repository

1. Go to my Github profile: https://github.com/Ardvb/
2. Click on the download button and copy/paste the link: https://github.com/Ardvb/Pands-Iris-Project-2019

## How to run the code:

1. Make sure you have python installed on your device: https://www.python.org/downloads/


## The Iris flower data set

This data set was collected by Edgar Anderson to quantify the morphologic variation of Iris flowers of three related species.
Two of the species were collected from the same pasture, on the same day, and measured at the same time by the same person with the same apparatus.
The iris data set consists of 50 samples each, of three iris species (Iris setosa, Iris virginica and Iris versicolor). 
From every sample four features were measured: the length and width of both the sepals and petals, in centimetres.

![irises](https://user-images.githubusercontent.com/47186083/56307201-35335780-613c-11e9-8191-827eca81c80e.png)
###### Source: https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers

British statistician and biologist Ronald Fisher used this dataset to develop a linear discriminant model to distinguish the species from each other.
Ronald Fisher is one of the most celebrated statisticians of all time. 
He is described as “a genius who almost single-handedly created the foundations for modern statistical science”.
The data set has some key features that make it very useful in all sorts of data analytics, from data visualisation to machine learning.
It is small, but not trivial. It consists of real data of good quality. 
The goal of the dataset, to discriminate between three species of Iris, based on measurements is simple, yet challenging.
Also, the fact someone as famous as Ronald Fisher used the dataset makes it more interesting to a lot of statisticians.
No wonder it is one of the most used data sets in the world of statistics.

## My research

I have written Python code to try and find some interesting information about this data set.
In this readme I will show my code and the output it returns.

First I wanted to get a good look at the data set by visualisizing some basic features.

![image](https://user-images.githubusercontent.com/47186083/56310090-dfae7900-6142-11e9-8e3d-ec1f8d5f5e0d.png)
![image](https://user-images.githubusercontent.com/47186083/56307904-d7077400-613d-11e9-8ab2-b6ba6d73b547.png)

![image](https://user-images.githubusercontent.com/47186083/56307945-f1415200-613d-11e9-9929-1df4cd1d4d79.png)

By reading the Iris data set Excel file into my program I am able to project in onto the screen using cmder. 

Now we can start looking into what some of the more interesting features of the data set. By using the _.describe_ command, I can see lots of useful information, such as the mean, the standard deviation, the minimum and maximum etc.

![image](https://user-images.githubusercontent.com/47186083/56308155-79bff280-613e-11e9-9fee-c7298f2e96c3.png)
![image](https://user-images.githubusercontent.com/47186083/56308155-79bff280-613e-11e9-9fee-c7298f2e96c3.png)

By using the _.median_ and _.mode_ commands, I am able to see what the median(the number that is halfway into the set) and the mode(most frequently occurring number).

![image](https://user-images.githubusercontent.com/47186083/56308302-e1763d80-613e-11e9-8d34-25080d535d7b.png)
![image](https://user-images.githubusercontent.com/47186083/56308312-eb983c00-613e-11e9-8410-928ffaf52bdd.png)

![image](https://user-images.githubusercontent.com/47186083/56308322-f357e080-613e-11e9-9032-a8f317597a0a.png)
![image](https://user-images.githubusercontent.com/47186083/56308335-f9e65800-613e-11e9-91c5-043c36688957.png)

### The differences between the species

The next step was to seperate the species by only comparing the data from each species to the others.
I wrote some simple code to only display the data of 'Iris setosa':

![image](https://user-images.githubusercontent.com/47186083/56308459-45990180-613f-11e9-9bd5-ef3284493405.png)
![image](https://user-images.githubusercontent.com/47186083/56308523-65302a00-613f-11e9-8e94-eba6afca58df.png)

![image](https://user-images.githubusercontent.com/47186083/56308618-a7596b80-613f-11e9-977e-9296df0f1fc7.png)
![image](https://user-images.githubusercontent.com/47186083/56308628-b0e2d380-613f-11e9-8286-06e8be911469.png)

And the median and mode:

![image](https://user-images.githubusercontent.com/47186083/56308675-cb1cb180-613f-11e9-8297-5184dde90a9f.png)
![image](https://user-images.githubusercontent.com/47186083/56308692-d2dc5600-613f-11e9-809a-bbf1e0199b4f.png)

![image](https://user-images.githubusercontent.com/47186083/56308713-dc65be00-613f-11e9-8356-1b4d770d22c5.png)
![image](https://user-images.githubusercontent.com/47186083/56308731-e38ccc00-613f-11e9-8c0d-2411083356a0.png)

I have done the same for both other species.

From looking at this data, we can already spot some differences between the species. Especially between Iris setosa and the other two.
However, to make it even easier to see, I have plotted some histograms and other plots.

## Data visualization

First I have plotted a histogram of the sepal length of all three species. With the sepal length in centimeters on the x-axis, and the frequency on the y-axis.

![image](https://user-images.githubusercontent.com/47186083/56308930-59913300-6140-11e9-924c-0b371f6c22c9.png)
![image](https://user-images.githubusercontent.com/47186083/56309064-b7257f80-6140-11e9-9047-aa38b5f36ac1.png)


I have also plotted histograms of the other features with virtually the same coding:

![image](https://user-images.githubusercontent.com/47186083/56309125-d3292100-6140-11e9-9078-ff3e1afbf12e.png)
![image](https://user-images.githubusercontent.com/47186083/56309163-e2a86a00-6140-11e9-9cbb-e8bbbf8f58ba.png)
![image](https://user-images.githubusercontent.com/47186083/56309171-e76d1e00-6140-11e9-9b1e-01df2a5af9df.png)

Here we can start to see clearly that especially the petal length and width of the Iris setosa is much smaller (and shorter) than the other two species.

Another interesting and suitable way of visualizing if the swarmplot.

![image](https://user-images.githubusercontent.com/47186083/56309335-4cc10f00-6141-11e9-8071-925c9314e7ce.png)

![image](https://user-images.githubusercontent.com/47186083/56309415-6f532800-6141-11e9-864d-84f9d16bdf00.png)

And the other features:

![image](https://user-images.githubusercontent.com/47186083/56309442-7ed27100-6141-11e9-976c-92d4d5e148d5.png)
![image](https://user-images.githubusercontent.com/47186083/56309456-84c85200-6141-11e9-8782-4e006e7b7fa5.png)
![image](https://user-images.githubusercontent.com/47186083/56309473-8abe3300-6141-11e9-84b8-4b35191ff71f.png)

As we can see, the setosa is clearly smaller than the other two species (except for the sepal width), and virginica is the tallest for 3 out of 4 features (sepal length, petal length and petal width). However, the difference between virginica and versicolor is not as pronounced as the difference between setosa and the other 2 species.

## Possible correlations

To visualize possible correlations between features, I have used scatterplots.
