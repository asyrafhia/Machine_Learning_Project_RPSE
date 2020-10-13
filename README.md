# Final_Project_Revenue_Planning_System_For_E-Commerce

by: Asyraf Ilmansyah Hia

Dataset: online_shoppers_intention.csv

*The dataset is separate from the repository because it exceeds github file size limit.


Source : [kaggle](https://www.kaggle.com/roshansharma/online-shoppers-intention)


PROJECT DESCRIPTION
---

The Revenue Planning System for E-Commerce is a system that can predict and visualize the impact of revenue in a e-commerce website.

The dataset consists of 10 numerical and 8 categorical attributes.

The 'Revenue' attribute can be used as the class label.

"Administrative", "Administrative Duration", "Informational", "Informational Duration", "Product Related" and "Product Related Duration" represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories. The values of these features are derived from the URL information of the pages visited by the user and updated in real time when a user takes an action, e.g. moving from one page to another. The "Bounce Rate", "Exit Rate" and "Page Value" features represent the metrics measured by "Google Analytics" for each page in the e-commerce site. The value of "Bounce Rate" feature for a web page refers to the percentage of visitors who enter the site from that page and then leave ("bounce") without triggering any other requests to the analytics server during that session. The value of "Exit Rate" feature for a specific web page is calculated as for all pageviews to the page, the percentage that were the last in the session. The "Page Value" feature represents the average value for a web page that a user visited before completing an e-commerce transaction. The "Special Day" feature indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with transaction. The value of this attribute is determined by considering the dynamics of e-commerce such as the duration between the order date and delivery date. For example, for Valentina’s day, this value takes a nonzero value between February 2 and February 12, zero before and after this date unless it is close to another special day, and its maximum value of 1 on February 8. The dataset also includes operating system, browser, region, traffic type, visitor type as returning or new visitor, a Boolean value indicating whether the date of the visit is weekend, and month of the year.

In this final project I will build a Flask-based web app that can recommend whether the e-commerce website can make revenue or not based on the given term and google analytics of the website. I use Random Forest Classifier algorithm to do prediction for Revenue. The algorithm was chosen after going through various analyses on datasets and after making some comparison with other machine learning models.


PROJECT GOALS
---

The goal of the project is to reduce the risk of placing the marketing budget, that should allocate to something that clearly adds to revenue, by making machine learning-based applications to determine the revenue of an e-commerce website based on historical data.


APPS
---
The App is installed in Localhost


HOME PAGE
---
Home Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Home.png)

About Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/About.png)

PREDICTION PAGE 
---
Prediction Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Revenue%20Prediction.png)

The application user can input data as described below:
- `Number of Administrative Page`  : Represent the number of administrative pages category visited by the visitor in that session. The administrative page is like profile, address, user account, etc.
- `Number of Informational Page`   : Represent the number of informational pages category visited by the visitor in that session. The informational page is like article, information, etc.
- `Number of Product Related Page` : Represent the number of product related pages category visited by the visitor in that session. The product related page is like the description of the product, price, stock, etc.
- `Accumulation of Exit Rates`     : Represent the metrics Exit Rates measured by "Google Analytics" for each page in the e-commerce site. The value of "Exit Rate" feature for a specific web page is calculated as for all pageviews to the page, the percentage that were the last in the session.
- `Number of Page Values`          : Represent the metrics Page Values measured by "Google Analytics" for each page in the e-commerce site. The "Page Value" feature represents the average value for a web page that a user visited before completing an e-commerce transaction.
- `Time Gap to Special Day`        : The "Special Day" feature indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with transaction.
- `Month`               		   : Name of the month
- `Region`               		   : Name of the region
- `Traffic Type`                   : Name of the traffic type
- `Visitor Type`                   : Name of the visitor type
- `Weekend`               		   : Name of the weekend

PREDICTION RESULT
---
Prediction Result Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Result.png)

VISUALIZATION PAGE
---
Histogram Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Histogram.png)

Boxplot Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Boxplot.png)

Scatter Plot Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Scatter.png)

Pie Chart Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Pie.png)

DATA MANAGEMENT PAGE
---
List of Data Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/List%20of%20Data.png)

Create New Data Interface:
![](https://github.com/asyrafhia/Final_Project_RPSE/blob/main/Interface/Create%20New%20Data.png)
