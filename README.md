# ECommerce-Data-Analysis
A simple analysis of an e-commerce data set found on Kaggle. Contains data cleaning via Pandas, an overview-heatmap via Seaborn and Matplotlib, and further dashboards on PowerBI.

## Introduction
The data set contains 3500 rows of sales data, with Product Name, Region, date, # of sales, and profit per sale. The goal of my analysis was to clean and investigate the data, and generate some insights on how different products were performing over time and over regions. I also aimed to come up with a couple of recommendations.

## Python step
Note that the Python file is attached in the "Raw Data" folder.
I first cleaned the data using dropna(). Subsequently I created two new columns: "Subsection" and "Profit per Sale". Then, using Seaborn and matplotlib, I created one heat-map matrix, showing the profit per sale of each product, by region. I added a color-scale for clarity. This aims to provide a very brief overview of the data before moving onto the graphs.

<img width="1270" height="1087" alt="image" src="https://github.com/user-attachments/assets/956bf24e-2d20-4df7-a40e-6a19507fab31" />

We can see that the North region has some standout good and bad products; Smart Watches, Laptops, and Cameras do good, while Printers, Mice, and Smartphones do not. We can also see Cameras have the most profit per sale overall, while Tablets have the least. Already, then, we start to get an idea on which products perform well. For example, we can consider focusing on Smartphones in the East rather than the South. However, since this is only one metric, more insight needs to be generated before we can start making recommendations.


## PowerBI Charts

### Main Dashboard

![Main Dashboard](Dashboards/Main_Dashboard.png)
