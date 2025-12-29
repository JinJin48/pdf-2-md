---
tags:
source: 049_7.3 Smart Predict Predictive Scenarios.pdf
title: 049_7.3 Smart Predict Predictive Scenarios
---



**7.3  Smart Predict: Predictive Scenarios**


Smart predict can extend predictive scenarios, which can become rather
complex. We’ll create an example time series forecast in this section again
using the Sales Data dataset uploaded in Chapter 4, Section 4.2.1.


Then, we’ll briefly elaborate on regression and classification scenarios.
However, our focus will be on use cases and requirements. In general, we
recommend consulting the product help when creating predictive scenarios, which contains extensive information about using smart predict and
about creating scenarios.


**7.3.1  Time Series**


While the automatic time series forecast described in Section 7.2.5 can’t be
modified, the predictive scenario can be used to create extended forecasts.
These forecasts allow you to set your own variables and return statistical
evaluation criteria.


**Creating a** Let’s start by creating a new predictive scenario. Open the main menu and
**predictive scenario** click on **Predictive Scenario** . This step will prompt you to select a predictive
scenario type. Choose the **Time Series Forecast** option, as shown in Figure
7.27. Enter the name “Revenue Forecast” and click on **Save** .


**Figure 7.27** Selecting Predictive Scenarios


**Selecting a dataset** A message will remind you to configure the predictive model before training it. Use the sidebar on the right to configure the predictive model. Click
on the **Time Series Data Source** field to open the dataset selection dialog
box. Now, select the **Sales Data** dataset, which will prompt the sidebar to
show additional settings, as shown in Figure 7.28.


The **Predictive Goal** section is where you’ll specify the role of each column
in the dataset. The **Target** field should contain the measure for which you
want projected values for the future. For our example, select the **Revenue**
measure.



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-0-0.png)








Select **Date** for the **Date** field. The **Entity** field specifies the column with
which the measure should later be aggregated. Select **City** for the **Entity**
field.


**Figure 7.28** Dataset Selection and Configuration


In the **Predictive Model Training** section, you can exclude variables and **Training the model**
change further parameters. You can restrict the amount of data used for the
training and convert negative forecasted values to zeros. Let’s leave the
standard settings in place and start the model training process by clicking
on **Train & Forecast** as shown in Figure 7.29.



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-1-0.png)








**Figure 7.29** Training and Forecast Settings


The model training process may require several minutes to finish. However, the process performed in the background will result in a new predictive model generated for the time series forecast.


During the training process, you can view a list of available **Predictive Mod-**
**els** at the bottom of the page (as shown in Figure 7.30). This list includes all
active predictive models and errors if they occur. You’ll also see other predictive models that are part of the predictive scenario, if others are
included.


**Figure 7.30** List of Predictive Models



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-2-0.png)

![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-2-1.png)








After the model training process has been completed, you’ll see the results, **MAPE value**
which you can use to evaluate the prediction, as shown in Figure 7.31. The
overview focuses on the **Average Expected MAPE** value. The mean absolute
percentage error (MAPE) value indicates the probability of an erroneous
forecast. The lower this value, the lower the probability of an error occurring if the model is used to forecast values.


**Figure 7.31** Model Evaluation


**MAPE Value**


MAPE provides a good indication of a forecast’s quality. Although a low
MAPE value usually means that the model is sound, you should still check
its results and evaluate if these results are realistic. This evaluation should
be performed by analyzing the segments in detail.


If you run the training process on your own system, note that your results
may not exactly match the examples in this book.


By looking at the **Top Entities** and **Bottom Entities** lists, you’ll see for which
cities the model created good (or bad) forecasts. In general, a MAPE value of
2.3% indicates high model quality.



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-3-0.png)








**Detailed analysis** To evaluate the model in detail, you can analyze each segment (in this case,
each city) separately. Either click on a city in the **Top Entities** and **Bottom**
**Entities** list or scroll down to a table of segments and their MAPE values.


**Forecast versus** Select the city **Salinas** for our example. As shown in Figure 7.32, the inter**actual** face will now provide a chart to compare the forecasted values with the
actual data. The chart will also show the calculated value for the future (in
this case, January 2024).


**Figure 7.32** Detailed Analysis of Salinas


**Forecasts** The **Forecasts** area on the same page shows the exact values that were calculated. Next to the **Forecast** column, you’ll also see the upper and lower
bounds of potential developments ( **Error Max** and **Error Min** ). Based on historic developments, SAP Analytics Cloud estimates the revenue in Salinas
to range somewhere between these values.



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-4-0.png)








The **Explanation** tab provides more statistical information about the analy- **Time series**
sis of each segment. The **Time Series Breakdown** graph shows how values **breakdown**
develop over time and is especially interesting when conducting multiple
forecasts, as shown in Figure 7.33. The **Target Statistics** highlight statistical
key figures that were calculated during the model training process, as
shown in Figure 7.34.


**Figure 7.33** Time Series Breakdown for Salinas


**Figure 7.34** Target Statistics


After you’ve finished evaluating the model, you can publish the results into **Publishing the**
a new dataset, which can be also visualized in a story. Click on the **Save Fore-** **model**
**cast** icon at the top. A new dialog box will open you can enter a name,
for instance, “Sales Data (Forecast).” Click on **OK** to confirm you want the



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-5-0.png)

![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-5-1.png)








dataset to be created. The model will now be applied and published as a
dataset.


Because this process can take some time, you won’t receive direct feedback.
However, you can again track the status of the model. Once completed, the
model should have the **Applied** status, as shown in Figure 7.35.


**Figure 7.35** Model Status


**Dataset** Open the dataset we just created. During the model application process,
three new columns were added to the original dataset, as shown in Figure
7.36. The **Forecast** column shows the forecasted value for each data point as
generated by the model. Each segment (in this case, each city) was extended
by one additional line for the date January 1, 2024. This line contains the
forecasted value and a lower bound and upper bound.


**Figure 7.36** Extended Dataset


This dataset can now be used in a story as a data source and visualized.
More information about creating stories can be found in Chapter 5, Section
5.2.



![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-6-0.png)

![](temp_conversion_out/main/images/049_7.3 Smart Predict Predictive Scenarios_049_7.3-Smart-Predict-Predictive-Scenarios.pdf-6-1.png)






