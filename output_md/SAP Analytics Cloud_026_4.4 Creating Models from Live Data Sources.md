---
tags:
source: 026_4.4 Creating Models from Live Data Sources.pdf
title: 026_4.4 Creating Models from Live Data Sources
---



Click on the **Review** button to open the version mapping dialog. Map the
version as shown in Figure 4.35 by matching **Actuals** to **Actual** and **Forecast**
to **Forecast** . Confirm by clicking on **OK** .


**Figure 4.35** Version Mapping


**Working with Versions**


Versions are often irrelevant since they aren’t captured in many scenarios
outside of planning, where they are common. If your data contains version
information, we strongly recommend you assign the data correctly, which
will allow you to later compare versions or run calculations based on versions.
You don’t need to create a planning model just to analyze version data.


After editing the column types, you can perform additional operations
within data wrangling to improve the quality of the data or to otherwise
manipulate it.


**Finalize model** The data is now edited and ready for analysis, so now we want to save the
final model. Click on the **Save** button in the top action bar of your screen. A
validation process will check if the changes you’ve performed so far are
valid for the whole dataset. If no errors or problems are detected, the model
is saved.


Models are stored in folders like stories. A model can be later edited in the
modeler, which is presented in detail in Section 4.5.


**4.4  Creating Models from Live Data Sources**


When using live data sources, you still must create a model first if you want
to analyze your data in SAP Analytics Cloud. In this scenario, however, SAP
Analytics Cloud will technically create a reference that can be enriched with
additional information. More information about the architecture of a live
model can be found in Section 4.2.2.



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-0-0.png)








In the following example, a model will be built on top of a live connection
to an SAP HANA instance. The data source is an SAP HANA view, which we’ll
enrich with date and geographical information. We’ll also add version
information to the model. The process is quite similar to connecting to
other live data sources.


Similar to the procedure described in Section 4.3, start by opening the **Selecting a**
model menu. Open the main menu and click on **Modeler** . Next, select the **data source**
**Live Data Model** option, as shown in Figure 4.36.


**Figure 4.36** Selecting Data Sources


You’ll now see a dialog box for selecting the system and data source, as **System selection**
shown in Figure 4.37. In our scenario, we’ll connect to the SAP HANA system
called **DB3** . The data is provided in the **SUPERMARKET_CA_GEO_CALC** view.
This view is similar to the Excel file described in Section 4.3.


After clicking on **OK**, the SAP HANA view will be accessed and shown in the
modeling view, which is also called the modeler, as shown in Figure 4.38. In
the modeler, you can define additional semantics or parameters. If you
don’t need to perform any additional tasks here and the data source already
provides the final model, you can directly proceed with saving and analyzing the model.



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-1-0.png)

![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-1-1.png)








**Settings and**
**changing the**
**data source**



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-2-0.png)

**Figure 4.37** Selecting an SAP HANA View


**Figure 4.38** Modeler for Live Data Source


The action bar at the top of the screen provides direct access to commonly
used functionalities, as shown in Figure 4.39. By clicking on the wrench icon
1, you can open various dialog boxes. Besides adjusting model settings,
you can also configure parameters, including changing the data source.
Specifically, you can select a new SAP HANA view. This step is required if
you want to change a model from using nonproductive to using productive
data, for example.


**Figure 4.39** Action Bar in Modeler for Live Data Sources



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-2-1.png)








Click on the **Save** icon 2 to save the model. The other icons allow you to
map versions 3, enrich a geolocation 4, or create a date dimension based
on a text column 5. You can also view all dimensions 6 and all measures 7.


First, we’ll enrich the model with additional information to unlock further **Version mapping**
functionalities. A version mapping, as shown in Figure 4.40, allows you to
map data to actual values ( **Actuals** ) or forecasted values ( **Forecast** ). This allocation later can be used in visualizations to compare versions to each other.
After opening the dialog box, you must first indicate which column contains the version information. Then, you map all unique values in this column to versions.


**Figure 4.40** Mapping Versions


If the data model also contains geographical data and SAP Analytics Cloud **Geolocation**
supports the feature for the data source, you can enrich the model with
geographical information. Click on the ( **Location** ) icon to open the dialog box for creating a location dimension. Now, indicate the **View Name**
that contains the geographical information, as shown in Figure 4.41. You
also must indicate which column should be used to match records from the
SAP HANA view to the view that contains the geographical information
( **Location Identifier** and **Identifier for Mapping** ).


**Geolocations from Live Data Sources**


When using geolocation data from live data sources, you must meet various requirements up front. First, you must verify if SAP Analytics Cloud
supports geolocations for your data source. Based on the data source, you
may have to prepare the data model as documented in the product help of
SAP Analytics Cloud in detail for each data source.



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-3-0.png)








**Figure 4.41** Creating Location Dimensions for an SAP HANA View


**Date hierarchies** Another feature for live connections to SAP HANA views is the conversion
**from text columns** of text columns to date columns. In general, you can also directly model
date columns in an SAP HANA view. However, in some scenarios (when
connecting to external data sources in SAP HANA, for example), date information is only stored as text.


**Creating time** If you want to use some of the date features in SAP Analytics Cloud, you
**dimensions** must convert the text columns into date columns. You can either perform
this conversion in the data source itself or use the modeler in SAP Analytics
Cloud. In the latter approach, click on the **Create Time Dimension** icon to
open the dialog box shown in Figure 4.42.


**Figure 4.42** Maintaining Time Dimensions


Because you can convert multiple columns into dates, you must click on
the plus icon **+** to create a new date hierarchy. Afterwards, select the column
in your SAP HANA view that contains the date information.



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-4-0.png)

![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-4-1.png)








**Prerequisites for Date Columns**


A text column in the SAP HANA view must carry the data type NVARCHAR for
SAP Analytics Cloud to correctly recognize it as a potential date column.
Also, the column length is used to determine the date level: 4 characters
indicate year information, 6 characters are recognized as a combination of
year and month, and 8 characters are interpreted as full days.


Once selected, you can determine which date level (year, day, or month) is
represented by the column, as shown in Figure 4.43. You can also define
which levels the generated date hierarchy should contain.


**Figure 4.43** Creating Time Dimensions


Besides enriching a model with additional hierarchies or date columns, you **Measure overview**
can also create additional measures or modify existing measures. To create
a new measure, you must navigate to the measure overview by clicking on
**Measures** in the top bar. Now, you can create new measures by simply
entering values in an empty row for the **ID** and **Description** columns, as
shown in Figure 4.44. Afterwards, enter a formula into the **Formula** field to
calculate the new measure.


**Figure 4.44** Creating New Calculated Measures


Figure 4.44 shows a newly created measure called **Optimal Forecast** . This **Additional**
measure is calculated by multiplying the **Revenue** measure by a factor of 1.5, **calculated measures**
as indicated in the **Formula** column. The measure will now be available to
all users in SAP Analytics Cloud that have access to this model.



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-5-0.png)

![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-5-1.png)









![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-6-0.png)

**Measure attributes** Table 4.2 shows all attributes of measures that can be defined in the modeler.







|Column Name|Description|
|---|---|
|**ID**|Unique ID of a measure. If the measure is already<br>modeled in the data source, the ID can’t be changed in<br>the modeler.|
|**Description**|Description of the measure that is shown to the user.<br>This value can be changed for existing and new mea-<br>sures.|
|**Aggregation Type**|Determines the aggregation type applied to the mea-<br>sure.|
|**Exception** <br>**Aggregation**|Allows the definition of an exception aggregation.|
|**Exception** <br>**Aggregation** <br>**Dimension**|Determines which dimension is used for the exception<br>aggregation.|
|**Required Dimension**|If a dimension is selected in this column, the measure<br>can be only used in a story if the dimension is also part of<br>the chart or table.|
|**Scale**|Determines the scale of a measure (e.g., thousands or<br>percentages).|
|**Decimal Places**|Determines the number of decimal places shown for the<br>measure.|
|**Formula**|If you create a new measure, you must provide a formula<br>for the calculation in this column.|
|**Hide**|If you want to hide a measure, turn this option on. This<br>option will make the measure invisible in all stories and<br>applications.|
|**Threshold**|Can be used to define global thresholds for the measure.|


**Table 4.2** Options to Extend and Modify Measures










The _exception aggregation_ concept isn’t widely known and therefore con- **Exception**
fuses many users of SAP Analytics Cloud. While normal aggregations are **aggregation**
usually performed on the row level, exception aggregations are performed
on the dimension member level of the indicated dimension. In this way,
you can compare aggregated values against single values in the same table,
for example.


Exception aggregations should only be used if your use case requires them.
Otherwise, they are irrelevant for most users.


The model also allows you to rename or hide dimensions. Click on **All** **Modifying**
**Dimensions** to open the dimension overview, as shown in Figure 4.45. Now, **dimensions**
you can enter individual texts into the **Description** field. If you want to
group multiple dimensions into one group, enter a group name into the
**Group** field.


**Figure 4.45** Overview of Dimensions


Once you start entering values into the **Group** field, you’ll see a live preview
in the sidebar on the right, as shown in Figure 4.46.


Once you’re done, you must save the model to make the model accessible **Saving the model**
to other users. As for imported models, the model will be stored as an object
in the folder structure of SAP Analytics Cloud.


The authorization concept of SAP Analytics Cloud controls which models **Authorizations**
are visible to which users. However, the visibility of data within a live



![](temp_conversion_out/main/images/026_4.4 Creating Models from Live Data Sources_026_4.4-Creating-Models-from-Live-Data-Sources.pdf-7-0.png)






