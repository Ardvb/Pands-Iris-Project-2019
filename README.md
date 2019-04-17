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


### The differences between the species

The next step was to seperate the species by comparing the data from each species to the others.
I wrote some code to only display the data of 'Iris setosa':

![image](https://user-images.githubusercontent.com/47186083/56311174-49c81d80-6145-11e9-8481-19aab85ee9db.png)
![image](https://user-images.githubusercontent.com/47186083/56311201-59dffd00-6145-11e9-9aa3-d0952774d727.png)

And the median and mode:

![image](https://user-images.githubusercontent.com/47186083/56311337-b04d3b80-6145-11e9-8bd8-917e02d3fffa.png)
![image](https://user-images.githubusercontent.com/47186083/56311371-c5c26580-6145-11e9-9606-b5f62285dbaa.png)

![image](https://user-images.githubusercontent.com/47186083/56311389-d4108180-6145-11e9-9584-f809802352a6.png)
![image](https://user-images.githubusercontent.com/47186083/56311422-e38fca80-6145-11e9-911f-c847ecdec2bd.png)


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

Another interesting and suitable way of visualizing if the swarmplot. With the swarmplot, you can tell the difference in the blink of an eye.

![image](https://user-images.githubusercontent.com/47186083/56309335-4cc10f00-6141-11e9-8071-925c9314e7ce.png)

![image](https://user-images.githubusercontent.com/47186083/56309415-6f532800-6141-11e9-864d-84f9d16bdf00.png)

And the other features:

![image](https://user-images.githubusercontent.com/47186083/56309442-7ed27100-6141-11e9-976c-92d4d5e148d5.png)
![image](https://user-images.githubusercontent.com/47186083/56309456-84c85200-6141-11e9-8782-4e006e7b7fa5.png)
![image](https://user-images.githubusercontent.com/47186083/56309473-8abe3300-6141-11e9-84b8-4b35191ff71f.png)

As we can see, the setosa is clearly smaller than the other two species (except for the sepal width), and virginica is the tallest for 3 out of 4 features (sepal length, petal length and petal width). However, the difference between virginica and versicolor is not as pronounced as the difference between setosa and the other 2 species.

## Possible correlations

To further try to differentiate between virginica and versicolor, I have looked at possible correlations in any of the 4 measured features.
To visualize these correlations, I have chosen to use the scatterplot. I have plotted all 6 possible correlations and attached screenshots of code and output below.

![image](https://user-images.githubusercontent.com/47186083/56311850-d7f0d380-6146-11e9-8dd6-a82be70ec6ed.png)

![image](https://user-images.githubusercontent.com/47186083/56312187-8dbc2200-6147-11e9-8600-034425152cd2.png)
![image](https://user-images.githubusercontent.com/47186083/56312198-94e33000-6147-11e9-9374-256411ad3811.png)
![image](https://user-images.githubusercontent.com/47186083/56313428-83e7ee00-614a-11e9-9363-ea7465cf701e.png)
![image](https://user-images.githubusercontent.com/47186083/56312551-44b89d80-6148-11e9-8cf0-fac7342988a8.png)
![image](https://user-images.githubusercontent.com/47186083/56313275-294e9200-614a-11e9-94fa-19f0ae1fd5c1.png)
![image](https://user-images.githubusercontent.com/47186083/56313183-e42a6000-6149-11e9-84f5-b2dad7d2a85b.png)
