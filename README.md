# Final_Project_Revenue_Planning_System_E-Commerce

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


HOMEPAGE
---
Home interface:
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/home-interface.png)

About interface:
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/about-interface.png)

PREDICTION PAGE 
---
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/predict-interface.png)

The application user can input data as described below:
- `NewExist`               : Business Condition when the loan is set.
- `RevLineCr`              : Revolving line of credit which means that if the loan has been paid, the borrower can be able to immediately borrow again.
- `LowDoc            `     : LowDoc Loan Program means the borrower can borrow with little administration..
- `NAICS`                  : North American industry classification system code
- `Term`                   : The term provides information on how long the loan will take
- `GrAppv`                 : Gross amount of loan approved by bank
- `SBA_Appv`               : SBA's guaranteed amount of approved loan

PREDICTION RESULT
---
The prediction result interface:
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/result-interface.png)

VISUALISATION PAGE
---
Histogram
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/boxplot-interface.png)

Boxplot
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/histogram-interface.png)

Scatter Plot
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/scatter-interface.png)

Pie Chart
![](https://github.com/bagjasatia/Final_Project_SBA_Loan_Approval/blob/master/Interface/pie-chart-interface.png)

