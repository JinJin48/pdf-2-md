---
tags:
source: 048_7.2 Smart Assist.pdf
title: 048_7.2 Smart Assist
---



**7.2  Smart Assist**


This section covers all functionalities of the smart assist area in detail.
Some of our examples may use models or stories that we created in previous chapters. Of course, you can also use the features we present with your
own data. Be aware that our demonstrations are based on fictional data
from the demo data package, which may not always lead to useful results.


**7.2.1  Smart Discovery**


Now, let’s use smart discovery to determine what factors most influence
the **Revenue** measure in our Sales Data model. Smart discovery is only
available for stories in classic mode, not for optimized story mode.


Create a new story and choose **Run a Smart Discovery** . Instructions on how
to create a story can be found in Chapter 5, Section 5.2. Choose the **Sales**
**Data** model we created in Chapter 4, Section 4.3 and Section 4.5.


**Configuring** You’ll now see the smart discovery sidebar, where you can further config**smart discovery** ure some parameters, as shown in Figure 7.7. For instance, you can specify
which target variable (measure or dimension) you want to explore in more
detail. Click on **Select a dimension or a measure** below **Target** and select the
**Revenue** measure. For the **Entity**, choose the dimensions **Product**, **City**, and
**Supermarket** .


**Figure 7.7** Setting Up Smart Discovery



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-0-0.png)








Leave the **Version** dropdown list set to **Actual.** Remove all measures so that **Advanced settings**
only **Revenue** remains. Then, remove the **ID**, **Stores**, and **Street** dimensions
because they provide no value for our analysis and are directly related to
revenue. (Both **ID** and **Street** are dimensions with a close relation to their
respective data points. One value can exist per ID, and only a few values can
exist for a street, which would result in a rather high mathematical influence on the revenue. However, this insight has no real-world value.) Initiate
the process by clicking on **Run** .


Wait a few seconds until the automatic story generation process is com- **Automatically**
pleted. Smart discovery will generate four pages in total: **generated story**


- **Overview**


- **Key Influencers**


- **Unexpected Values**


- **Simulation**


If smart discovery is executed for a dimension instead of a measure, only
the first two pages are generated.


The **Overview** **of Revenue for Product, City, Supermarket** page shows gen- **Overview**
eral information about the analyzed measure and includes overview charts
and texts that outline strong relationships that have been found within the
data, as shown in Figure 7.8.


**Figure 7.8** Excerpt of Overview Page



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-1-0.png)








In general, the overview page offers a high-level overview of your data and
highlights how several factors contribute to the measure. Some charts are
interactive and allow you to generate further analyses.


**Key influencers** On the **Key Influencers** page, you’ll find information about all the prominent relationships that were found in your data, accompanied by automatically generated texts that provide explanations of the results of the
analysis and their quality, as shown in Figure 7.9.


**Figure 7.9** Key Influencers


Based on the results of the analysis, this page may show additional charts,
which focus on one or more key influencers. Every individual chart allows
you to select the key influencers to manually adjust them.


**Unexpected values** Smart discovery also generates a model in the background, which it uses to
measure the relationships within the data and determine the influence of
each dimension. This background model is only an approximation of reality, however, and thus, the model cannot explain all the values that occur in
the dataset. The **Unexpected Values** page shows a list of all values that don’t
fit the model, as shown in Figure 7.10. These values are displayed in a table
and then again in more detail in the charts. If you click on a value, the charts
will automatically adjust.


**Simulation** The final page, **Simulation**, provides a powerful tool where you can adjust
individual influencers and directly measure their influence on the measure.


For each influencer, you can change the dimension member, and the revenue will change based on your decision, as shown in Figure 7.11. In addition,
the **Simulation** page directly shows the size of the impact of a dimension.



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-2-0.png)









![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-3-0.png)

**Figure 7.10** Unexpected Values


**Figure 7.11** Simulation





![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-3-1.png)





**Simulating a change** Change the parameters by using the input controls of one of the dimensions to start a simulation, as shown in Figure 7.12. Choose another product,
for example, and click on **Simulate** to see the effects of the change.


**Figure 7.12** Adjusting Simulations


**7.2.2  Smart Insights**


While smart discovery analyzes a measure or dimension in general, smart
insights helps you find out more about a specific data point. In general,
smart insights can be activated for every chart built on a supported data
source. If the amount of data is insufficient or if the context is too detailed,
smart insights may fail to produce results. Smart insights are only available
in stories in classic mode. Therefore, to use the functionalities, you have to
create a story in classic design mode.


Open a new story in classic design experience mode and create a new
numeric chart. Let the chart show the revenue measure and add a variance as
shown in Figure 7.13. Click on the chart and open the action bar by clicking on
the three dots icon. Now, select **Add Smart Insights**, as shown in Figure 7.13.


**Figure 7.13** Adding Smart Insights


**Accessing smart** Smart insights are automatically added as text below the chart showing the
**insights** most prominent finding, as shown in Figure 7.14. You can either access the



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-4-0.png)

![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-4-1.png)









smart insights by right-clicking on the chart or by clicking on **View more…**
at the end of the text.


**Figure 7.14** Chart with Smart Insights


After you open smart insights, a sidebar will be appear on the right, as
shown in Figure 7.15. This sidebar contains details about all findings that
lead to the data point. You can click on each finding to see more details and
related charts.


**Figure 7.15** Smart Insights Sidebar



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-5-0.png)

![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-5-1.png)








**7.2.3  Search to Insight**


**Explore data** Smart assist functionalities are designed to provide easy and intuitive
access to data. While the data exploration mode already eases this process
(see Chapter 5, Section 5.2.2), search to insight allows you to use natural language to analyze data.


**Opening the search** Search to insight is directly called from the home screen (see Chapter 3, Section 3.1). Navigate to your home screen, click on **Ask a Question**, and click on
**Go to Search to Insight**, as shown in Figure 7.16. You can also access search
to insight within a story by clicking the **Search** icon at the top.


**Figure 7.16** Opening Search to Insight


After you open search to insight, the search screen shown in Figure 7.17
appears. You can directly enter your question in the bottom, but the interface also proposes some searches and actions you can perform.


**Figure 7.17** Search to Insight



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-6-0.png)

![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-6-1.png)








SAP Analytics Cloud automatically indexes all models so that search to **Searching for data**
insight can search through them. Enter the search term “Show Revenue by
Supermarket” and press (Enter). You’ll also see automatic recommendations while entering the question. Especially when you have many models
in your system, these proposals can be helpful for finding the right model.
Once you’ve submitted the search query, a chart will be generated, as
shown in Figure 7.18.


**Figure 7.18** Generated Chart


You can extend the search by adding filter criteria (e.g., “for last year”) or by **Filter criteria**
clicking the buttons below a chart to submit a proposed question. If you
want to use the chart within a story, you can directly copy it from this
screen by clicking the **Copy** icon and selecting **Copy** .


**7.2.4  R Visualizations**


If you’re missing a chart in the standard portfolio or if you want to perform
individual statistical transformations before visualizing a specific context,
R visualizations can be used to overcome this challenge. By using the opensource programming language R, you can create individual charts. _R servers_
provide packages that include predefined charts and functions to manipulate and visualize data.



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-7-0.png)








**Scope** In general, you can use R to transform your data and implement data science scenarios. Because R can be used to generate charts and graphical elements, R components can also be used within a story. An R component in a
story also can be used to manipulate and transform data, but the results
can only be visualized and cannot be stored in a data model.


**Differences from** R visualizations are also not interactive. Although R allows you to create
**standard charts** interactive charts, this process must be performed completely in R script
and isn’t compatible with other charts in the story. You also cannot use the
builder or formatting options in R visualizations (see Chapter 5, Section 5.6).
R visualizations are created in their own builder, which is only available for
this scenario.


**Requirements** Because R is a statistical programming language, some knowledge is
required to use it properly. SAP Analytics Cloud only provides a limited
number of examples, which can’t be applied easily to your own data.


**More Information about R**


The following links provide more information about R and further
resources to learn the language:


            - **R Project,** _**[https://www.r-project.org/](https://www.r-project.org/)**_
You’ll find general information about R at this website as well as
download R for your own desktop computer. This software is not required to use R in SAP Analytics Cloud.


            - **R for Beginners,** _**[http://s-prs.co/v218502](http://s-prs.co/v218502)**_
This tutorial can help you get started learning R and performing your
first steps.


**R visualizations** The following example will demonstrate how to create R visualizations.
We’ll use a simple script to get familiar with R in SAP Analytics Cloud and
the working environment. To start, create a new story in optimized mode
and add a canvas page to it. Click on the plus icon **+** in the top bar and select
**R Visualization**, as shown in Figure 7.19.


**Builder** The builder for R visualizations, shown in Figure 7.20, will appear in the
sidebar to the right of the story.



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-8-0.png)








**Figure 7.19** Adding R Visualizations


**Figure 7.20** Builder for R Visualizations


Because R can only work with data in flat tables, you must first select a set **Adding input data**
of data that then will be made available for the R script. Click on **Add Input**
**Data** in the builder to start the data selection process. Select the **Sales Data**
model and select all dimensions for the rows. Confirm the selection by
clicking on **OK** .


Then, click on **Add Script** to start the script editor. Go into full screen mode
by clicking on the **Expand** icon in the top-right corner of the builder.
The screen should now match the screen shown in Figure 7.21.



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-9-0.png)

![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-9-1.png)








**Figure 7.21** Script Environment


**Script environment** The script environment is separated into four main parts:


          - **Editor**
All R scripts are entered into this field. You can also access code snippets
in this area or search through the code.


          - **Environment**
This area lists all available datasets. By clicking on the three dots icon
next to each entry, you’ll see a preview of the included data.


          - **Console**
Because R can also return console entries (e.g., error messages), these
messages are shown in this area.


          - **Preview**
This section previews the visualization that will later be added to the story.


**List all packages** First, we need to find out which packages are installed on the R server. Enter
the following script into the **Editor** area and click on **Execute** :


installed.packages(lib.loc = NULL, priority = NULL,
noCache = FALSE, fields = NULL,
subarch = .Platform$r_arch)


This code shows a list of all packages installed on the R server, which will be
returned in the console. By going through this list, you can find out if the
necessary R packages are available to solve your challenge. If you’re missing
a package, you must install it first, which, however, is only possible on your
own R servers. To use a dataset in an R script, you must first attach the dataset. Enter and execute the following code:


attach(Sales_Data)


From now on, you can directly reference dimensions and measures by simply writing their names.



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-10-0.png)








Remove all code from the script editor and then paste in the code shown in **Creating a**
Listing 7.1. **word cloud**


# This code loads the required libraries.
library(wordcloud)
library(RColorBrewer)
library(tm)
library(NLP)
# Attaches the dataset.
attach(Sales_Data)
# Creates the word cloud.
wordcloud(Supermarket, rot.per=0.6, use.r.layout=FALSE)


**Listing 7.1** Example R Script


This script will create a word cloud for the **Supermarket** dimension. A _word_
_cloud_ visualizes the words in a dimension in the shape of a cloud and can
use a measure to determine which words occur most. You can ignore all
lines in the code that start with a hash (#), which are just comments that
won’t be processed by the R server.


After clicking on **Execute**, a preview of the chart will be displayed, as shown
in Figure 7.22. To use the chart in a story, click on the **Apply** button.


**Figure 7.22** Word Cloud


R scripts will always be re-executed when opening a story. If the script con- **Script execution**
tains random functions (like in our example), different outcomes should
occur each time the story is opened. In our case, the word cloud function
randomly defines the final layout.


**7.2.5  Automatic Forecasts for Time Series**


You can extend a time series chart by activating the automated forecast. **Creating a time**
This functionality is only available in classic mode. **series forecast**


Create a new story in classic mode with a new canvas page and add a new
chart of the type **Time Series** . Select the **Sales Data** model. Add the **Date**



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-11-0.png)








dimension and the **Revenue** measure. You can also use the time series chart
we created in Chapter 5, Section 5.3.1.


Open the action bar of the chart and select **Add**           - **Forecast**           - **Automatic Fore-**
**cast**, as shown in Figure 7.23. The time series forecast for the chart will be
immediately activated, and the projected values (shown earlier in Figure
7.5) will be displayed. In addition, you can change the forecast method
(under **Advanced Options** ).


**Figure 7.23** Adding Automatic Forecasts


The projected forecast will be added to the end of the time series automatically, as shown in Figure 7.24. The forecast will be shown in a blue area,
which indicates the upper and lower bounds of possible future developments. The projected values are shown in the middle of that area on a dotted line.


**Figure 7.24** Time Series with Forecast



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-12-0.png)

![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-12-1.png)








**7.2.6  Smart Grouping**


When using the bubble diagram or scatterplot chart type in a classic story, **Supported chart**
you can activate an additional function to group values. An algorithm is exe- **types**
cuted in the background to check which data points are similar to each other,
and these data points are grouped together automatically and assigned different colors. You can compare this procedure to a K-means algorithm. This
algorithm works in a similar way by searching through the dataset for values
that are similar to each other and that can be put in groups.


You can activate and configure smart grouping in the builder of a chart. **Enabling smart**
Specify the number of groups and custom labels and optionally include **grouping**
tooltip measures, as shown in Figure 7.25.


**Figure 7.25** Smart Grouping


The algorithm then automatically calculates groups of data points and colors the data points in the chart accordingly. In addition, a legend will be displayed, as shown in Figure 7.26.


**Figure 7.26** Scatterplot with Smart Grouping



![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-13-0.png)

![](temp_conversion_out/main/images/048_7.2 Smart Assist_048_7.2-Smart-Assist.pdf-13-1.png)






