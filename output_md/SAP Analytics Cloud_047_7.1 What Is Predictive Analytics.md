---
tags:
source: 047_7.1 What Is Predictive Analytics.pdf
title: 047_7.1 What Is Predictive Analytics
---

# Chapter 7 **Predictive Analytics**

_While most analytics use cases focus on analyzing historical data, predic-_
_tive analytics aims to forecast potential future developments. To facilitate_
_this process, various practices like machine learning are embedded in SAP_
_Analytics Cloud._


When analyzing historical data, you can often observe patterns that
occurred in the past or learn from decisions that were made. However, this
data can also be used to gain insights about future developments or relationships between data points that may not be visible at first.


SAP Analytics Cloud offers a dedicated predictive analytics component that **Smart assist and**
provides various functionalities to support users in performing these kinds **smart predict**
of analyses. Those functionalities are either automated ( _smart assist_ ) or
require users to define explicit predictive scenarios ( _smart predict_ ).


In this chapter, you’ll first learn about both smart assist and smart predict;
then, we’ll offer examples of their functionality. Smart predict allows users
to create complex scenarios that can’t be covered in detail in this book. However, a sample time series analysis will be created throughout this chapter.
Section 7.3 describes how to access more information about smart predict.



![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-0-0.png)

**7.1  What Is Predictive Analytics?**


This section will focus on _predictive analytics_ and its differentiation from the
classic analytics field. Because the area of data science is rather big and can










be separated into a lot of different fields, we won’t focus on this topic in this
chapter. SAP Analytics Cloud supports users by providing easy access to
machine learning algorithms and tools. Machine learning algorithms are
mathematical methods that can, for example, recognize patterns in data or
relationships among data points. Those algorithms are usually applied automatically within SAP Analytics Cloud and can’t be influenced by a user. However, for some cases, a special environment is available where extended
analyses can be created.


We’ll explore all functionalities that belong to predictive analytics through
practical examples.


**Smart assist** The term _smart assist_ groups all functionalities that support users by automatically applying algorithms and functions to enable the analysis of data for
patterns and highlights. Smart assist includes the following functionalities:


**Smart discovery**   - **Smart discovery**
With smart discovery, you can create an automated analysis of a model,
as shown in Figure 7.1, which can be used to determine key influencers
for a specific dimension or measure.


**Figure 7.1** Smart Discovery


This function will automatically generate a story that contains various
charts and tables showing highlights and relationships. In addition, all
values that don’t fit the automatically recognized relationships (outliers)
will be shown. Finally, smart discovery also provides a simulation model
that allows you to change individual dimensions and measure the effect
of the change.


**Smart insights**    - **Smart insights**
This functionality can be activated for each chart in a story and provides
explanations for specific data points, as shown in Figure 7.2. Once you click
on a data point in a chart (e.g., a bar in a bar/column chart), smart insights



![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-1-0.png)








can be launched to find out which influencers contribute to this data point.
Smart insights must be activated for each chart or table manually.


**Figure 7.2** Smart Insights


Search to insight is another functionality to quickly access data and explore **Search to insight**
relationships between data points. This function can be launched from the
home screen or within the story. With this functionality, you can type in
natural language questions, as shown in Figure 7.3.


**Figure 7.3** Search to Insight



![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-2-0.png)

![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-2-1.png)








Search to insight uses various machine learning algorithms to determine
which data model you want to search and which information you request.
The generated chart can be copied into a story.


**R visualizations** Although R visualizations are part of the story and behave like charts,
they’ll be covered in this chapter because they also allow you to apply algorithms to forecast data. An example R visualization is shown in Figure 7.4.


**What Is R?**


R is a programming language commonly used in statistics. This opensource language is maintained by a large community. The language allows
extensive data operations and is extended by packages.


**Figure 7.4** Sample R Visualization


**Data transforma-** R can only be used in SAP Analytics Cloud to create visualizations that
**tions in R** aren’t included in the standard portfolio of elements used in stories. However, you’ll require knowledge of R. Data operations or transformations
that are performed within an R script can be executed, but the resulting
data can’t be stored in a data model. Instead, the result can be shown in a
chart or table by using R.


**Automatic forecast** When using a time series chart, you can activate the automatic forecast feature, which extends the time series chart by adding a forecast of how the
values may develop in the future, as shown in Figure 7.5. The parameters of
an automatic forecast can only be slightly adjusted.


**Smart predict** In addition to the smart assist functionalities, SAP Analytics Cloud also
offers an extended working environment for power users called _smart pre-_
_dict_ . In general, users create predictive scenarios based on datasets trained
on their own contents, as shown in Figure 7.6. Smart predict supports the
following predictive scenarios:



![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-3-0.png)








- Classification


- Regression


- Time series


**Figure 7.5** Time Series Chart with Forecast


**Figure 7.6** Training Predictive Scenarios


Based on the use case, these scenarios can answer various questions and
conduct analyses, including, for example, customer churn analysis, time
series forecasts, or future developments. A detailed description of these
scenarios can be found in Section 7.3.



![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-4-0.png)

![](temp_conversion_out/main/images/047_7.1 What Is Predictive Analytics_047_7.1-What-Is-Predictive-Analytics.pdf-4-1.png)






