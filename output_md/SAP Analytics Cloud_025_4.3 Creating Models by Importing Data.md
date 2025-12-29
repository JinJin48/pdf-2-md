---
tags:
source: 025_4.3 Creating Models by Importing Data.pdf
title: 025_4.3 Creating Models by Importing Data
---



processes. Depending on your licenses, planning models may not be available to some or all of your users.


**4.2.4  Embedded Models**


An embedded model represents another special case. Similar to an analytical model, an embedded model is part of a story and can only be used
within it.


An embedded model is predominantly used by users who want to analyze **Use case**
their data without creating a model that could be potentially used for other
stories or use cases. In this case, a user can upload data into a story by
uploading a flat file or with import connections. When this workflow is triggered directly from within a story, an embedded model is automatically
created that is only accessible within this story.


Users can still perform data wrangling on these models. As long as the
model isn’t published explicitly, it’s only visible and accessible within the
story. To make the data model generally available for more stories, the
model can be published, which will thus convert the embedded model into
a full analytical model. Embedded models therefore can’t be created outside of a story. The creation and usage of an embedded model is described
in detail in Chapter 5, Section 5.11.1.


**4.3  Creating Models by Importing Data**


In this section, we’ll walk you through an example of creating a model
based on imported data. The data source is a list of sales activities. We’ll
upload this file to SAP Analytics Cloud and generate a model from it. These
steps are important and required to walk through the remaining chapters
of this book, which rely on this data model.


**Sample Data**


The model creation process we describe in this section is based on sample
data. The data used is contained in the _Sales Analysis.xlsx_ file, included as
part of the demo data package you can download from the website for this
book at _[www.sap-press.com/5753](http://www.sap-press.com/5753)_ .


The _Sales Analysis.xlsx_ file contains data about articles that were sold in **Sample data**
supermarkets across the state of California. We want to find out more about
these activities, including how high our revenue was and how many products were sold in total.











Table 4.1 shows an overview and description of all the columns found in the
Excel file.

|Column Name|Description|
|---|---|
|**ID**|Unique number to identify each record in the table|
|**Date**|Month of sale|
|**Supermarket**|Name of supermarket|
|**Chain**|Chain to which a supermarket belongs|
|**Longitude**|Geographical information|
|**Latitude**|Geographical information|
|**Street**|Street name|
|**City**|City name|
|**Product**|Product name|
|**Product group**|Product group to which a product belongs|
|**Unit price**|Measure|
|**Quantity**|Measure|
|**Revenue**|Measure|
|**Version**|Determines if the measure is an actual value (**Actual**) or<br>forecasted value (**Forecast**)|



**Table 4.1** Description of Sales Analysis.xlsx File Contents


As shown in Table 4.1, some columns directly relate to each other. Others
contain additional information like geographical information. In the following example, we’ll upload this file to SAP Analytics Cloud and create a
model based on it. This data will be analyzed and graphically reported on in
Chapter 5. Knowledge of the home screen (as described in Chapter 3, Section
3.1) and the folder structure (as described in Chapter 3, Section 3.3.5) are prerequisites for Chapter 5.


**4.3.1  Creating a Model**


You have two options for creating a new model:


- When in the folder structure, click on the **+** button and choose the **Model**
entry.


- Open the main menu of SAP Analytics Cloud and navigate to **Modeler**, as
shown in Figure 4.10. There click on **Model** .










**Figure 4.10** Creating New Models from Main Menu


Next, you’ll be asked to select the model type. In this step, you can choose **Starting with data**
to create a blank model or start with data. For our example, we’ll upload a
flat file. Choose the **Start with Data** option (see Figure 4.11).


**Figure 4.11** Model Creation



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-2-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-2-1.png)









Now, select the **File (Local File or File Server)** option, click on **Select Source**
**File** and select the _Sales Analysis.xlsx_ file that you downloaded earlier, as
shown in Figure 4.12. Select the **Use first row as column headers** checkbox if
this option was not activated automatically. This step ensures that the first
row in the Excel file is not used as transactional data. To upload the file,
click on the **Import** button.


**Figure 4.12** Selecting an Excel File


**Draft data** The data will be now uploaded in the background. Do not close to your
browser or navigate away from SAP Analytics Cloud, which would abort the
upload process. Notifications throughout the whole upload process will
inform you of the current status. After the file is uploaded successfully,
you’ll be automatically forwarded to the model overview into which the file
has been uploaded as shown in Figure 4.13.


**Saving models** Before we can fully edit the newly created model, we need to save it first.
Therefore, click on the **Save** button in the top bar. Now, you must specify
where the model should be stored. By default, you’ll be presented with your
own private folder. Click on the **New Folder** icon to create a new subfolder and call it “Sales Data.” Use the same name for the model and save it
by clicking on **OK**, as shown in Figure 4.14.


**Data wrangling** To continue with the model creation process, click on the **Transform Data**
button in the bottom right. The system will inform you that you’ll initially
work only on a data sample, as shown in Figure 4.15.



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-3-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-3-1.png)






![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-4-0.png)

**Figure 4.13** New Model after Successful File Upload


**Figure 4.14** Saving Models










![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-4-1.png)



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-5-0.png)

**Figure 4.15** Data Sample Notification


Because the amount of data in the file is too high for previewing it completely in the browser, only 2,000 randomly selected records will be shown.
However, all changes that you perform now will be applied to the full dataset.


The data wrangling area allows you to manipulate the data or to apply
transformations by using formulas, as shown in Figure 4.16.


**Figure 4.16** Data Wrangling Overview



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-5-1.png)








The data wrangling screen is separated into multiple areas. At the top, you’ll
find the action bar, which provides access to all functions, as shown in Figure 4.17, such as the following:


- The **Close Data Transformation** icon 1 returns back to the model overview. The model won’t be published, but the system will save its current
state in data wrangling.


- The **Undo** 2 and **Redo** 3 icons undo and redo the last change or action.


- The **Sorting** icon 4 can be used to determine the sorting order of the records.


- The **Transform** bar (shown in Figure 4.16 below the action bar) can be
made visible by clicking on the icon 5.


- The **Custom Expression Editor** icon 6 opens a dialog box to create a calculated column.


**Figure 4.17** Action Bar of Data Wrangling Section


Let’s now look at some examples to learn how to use these functionalities.


On the right, you’ll see a sidebar where you can configure the model or **Sidebar**
modify individual columns, as shown in Figure 4.18.


**Figure 4.18** Sidebar



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-6-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-6-1.png)









The sidebar initially shows general information and metrics about the
uploaded flat file. The **Columns** section provides information about the recognized columns and their classification as texts or digits.


**4.3.2  Creating Expressions**


In our case, the columns in our data have been correctly recognized in general, but some relationships must be modeled manually. Also, you can provide additional information for some of these columns.


Start by selecting the **Date** column. The sidebar will automatically adjust
itself, as shown in Figure 4.19. You can use the sidebar to change the data
type or get more information about data quality. The **Data Distribution** section shows you how the values of the column are distributed and therefore
can provide you early insights into the data.


**Figure 4.19** Sidebar of the Date Column



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-7-0.png)








Because the **Date** column contains date information, we need to change its **Column type**
**Type** to **Date** . To create or modify a column, we can use expressions. In this
case, SAP Analytics Cloud provides the toDate() function. This function can
be used to convert a column into a date column by applying a specific format. In our case, the format **YYYYMM** needs to be applied.


Open the expression editor in the action bar and fill in the formula [Date]

= toDate([Date], "YYYYMM") as shown in Figure 4.20. While typing the formula, you will notice how the editor will support you with suggestions.
Confirm the formula by pressing the (Enter) key on your keyboard.


**Figure 4.20** Creating an Expression


The columns **Longitude** and **Latitude** indicate that the model contains geo- **Geographical data**
graphical information as coordinates. This info can be converted into a _geo-_
_graphical hierarchy_ during data wrangling so that the data can be later
shown on a map.


Again, we will make use of the expression functionality. Open the expression editor again and apply the makeCoordinate() function this time. The
function can be used to convert latitudes and longitudes into geospatial
data the can be consumed in SAP Analytics Cloud. Enter the formula

[Stores] = makeCoordinate([Latitude], [Longitude]) as shown in Figure 4.21.


**Figure 4.21** Enriching Geographical Data


**4.3.3  Executing Transformations**


If you want to replace individual values, you can either click on the value or
create a new transformation rule. In our example sales data, we now know
that the supermarket brand Ludo Complex was renamed to Fresh Tasters.
However, this name change isn’t yet reflected in our dataset. Therefore, we
want to fix this issue now in data wrangling.



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-8-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-8-1.png)








Figure 4.22 shows multiple ways to replace the value, such as the following:


          - Click on the value you want to replace in the table 1 or in the sidebar 3.
In the popup menu, click on the **Transform** icon and select **Replace**
**value with…** to assign a new value.


          - By using the formula bar at the top 2, you can create a transformation
manually.


**Figure 4.22** Replacing Values


**Creating a** Now, we’ll use the first method to create the transformation. After you click
**transformation** on the **Transform** icon, you’ll see various proposals for replacements, as
shown in Figure 4.23. Select **Replace value with…** .


**Figure 4.23** Creating Transformations


A formula that’s already partially filled out will be shown in the formula
bar. Enter the new supermarket name (“Fresh Tasters”) in this formula, as
shown in Figure 4.24. Press (Enter) for the transformation to be applied.



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-9-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-9-1.png)









![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-10-0.png)

**Figure 4.24** Replacing Values by Applying Formulas


The formula bar allows you to perform the following additional operations:


- Concatenate


- Split


- Extract


- Replace


- Change


- Filter


Transformations are generally captured in a history that can be accessed by
clicking on the **Transform Log** button on the top right, as shown in Figure
4.25. In this history, you can view all transformations and roll them back if
desired.


**Figure 4.25** Transform Log


To verify the dimension, click on **Details** in the top right and return to the
initial sidebar view of the column, as shown in Figure 4.26.


Since we’ve finished all data transformations, we want to continue our data
preparation back in the modeler. Therefore, click on **Close Data Transfor-**
**mation** on the top left and select **Save Changes Before Closing**, as shown in
Figure 4.27.



**Additional**
**transformations**
**and log**



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-10-1.png)








**Figure 4.26** Dimension Sidebar View


**Figure 4.27** Closing Data Preparation


**Measures** To ensure that you can use your measures for reporting later, check if they
were recognized correctly. Verify that the **Unit price**, **Quantity**, and **Revenue**
columns have been recognized by looking at the **Measures** section, as
shown in Figure 4.28.


**Figure 4.28** Measures



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-11-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-11-1.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-11-2.png)








**4.3.4  Creating Hierarchies**


As shown earlier in Table 4.1, the dimension **Supermarket** is part of a hierarchy. The **Supermarket** column is a child of the **Chain** column.


The modeler allows you to create simple _parent-child hierarchies_ as well as **Hierarchies**
more complex _level-based hierarchies_ . The relationship is quite simple in
our case ( **Chain** is the parent of **Supermarket** ), so the parent-child hierarchy
is sufficient.


**Parent-Child Hierarchies**


A simple parent-child hierarchy simply consists of one parent and its children. In this example, the **Chain** is the parent, and each **Supermarket** is a
child. If another level above or below exists, a level-based hierarchy must be
created. The creation of both hierarchy types follows the same procedure.


To create a parent-child hierarchy, you must first select the parent column,
which in this case is the **Chain** column in the **Dimensions** overview. Click on
the three dots at the end of the line and select **Convert to Property**, as shown
in Figure 4.29.


**Figure 4.29** Converting a Dimension to a Property


Then select the **Target Dimension** as **Supermarket** and the Type as **Parent-**
**Child Hierarchy**, as shown in Figure 4.30. Confirm by clicking on **Next** .


**Figure 4.30** Selecting the Child Column



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-12-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-12-1.png)








In the next dialog, you will see the results of your selection. Verify your outcome, as shown in Figure 4.31, and confirm by clicking on **OK** .


**Figure 4.31** Preview of New Dimension


**Creating another** Now, let’s create a second hierarchy for the product dimension. Select the
**hierarchy** **Product Group** column and add the **Parent-Child Hierarchy** attribute to the
dimension. Indicate that the **Product** column is the child of the **Product**
**Group** column.


**4.3.5  Creating Versions**


**Versions** The last column in the file has the title **Version** . The file doesn’t only contain
actual values for 2023 ( **Actuals** version) but also forecasted values ( **Forecast**
version). This data can later be compared to check whether the forecasted
values were met, for example. Therefore, the model has a specific data type
called **Version** .


By default, if SAP Analytics Cloud doesn’t find a **Version** column, it automatically creates a new **Version** column. In our case, the column **Version2**
was created. Select the **Version2** entry in the dimensions overview, click on
the three icons at the end of the line and click on **Delete** as shown in Figure
4.32. Confirm the warning that appears by clicking on **Delete** again.



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-13-0.png)








**Figure 4.32** Deleting the Empty Version2 Column


Now you can change the type of the **Version** column. Select it in the **Dimen-**
**sions** list, click on the three dots at the end of the lines and click on **Change**
**Dimension Type** - **Version**, as shown in Figure 4.33. Confirm the dialog that
appears by clicking on **OK** .


**Figure 4.33** Changing the Dimension Type


Since we changed the dimension type, the versions need to be mapped cor- **Version mapping**
rectly, as shown in Figure 4.34. Correct version mapping is particularly
important because SAP Analytics Cloud offers various functionalities for
comparing different versions to each other. These functionalities include
various display options, as well as calculations.


**Figure 4.34** Version Mapping Issues



![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-14-0.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-14-1.png)

![](temp_conversion_out/main/images/025_4.3 Creating Models by Importing Data_025_4.3-Creating-Models-by-Importing-Data.pdf-14-2.png)






