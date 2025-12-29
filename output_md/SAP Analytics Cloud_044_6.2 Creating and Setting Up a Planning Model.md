---
tags:
source: 044_6.2 Creating and Setting Up a Planning Model.pdf
title: 044_6.2 Creating and Setting Up a Planning Model
---




![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-0-0.png)

**Figure 6.9** Values Marked after Modification


Because planning processes are often rather complex and usually involve
multiple people, SAP Analytics Cloud provides an embedded calendar that is
directly accessible from the main menu. This calendar allows you to create
specific tasks, as shown in Figure 6.10, which can have start and end dates.
You can also assign these tasks to specific users and enrich them with additional information, related processes, validation steps, reminders, and notes.


**Figure 6.10** Tasks in Calendar


The functionalities we described in this section only reflect a small portion
of the available functionalities. We tried to show how planning tools are
tightly integrated in SAP Analytics Cloud. In the next section, we’ll create a
new planning model. Afterwards, we’ll walk you through a selection of
planning functionalities.


**6.2  Creating and Setting Up a Planning Model**


Planning workflows can only be established when using planning models
as data sources. For a better understanding of various model types, consult
Chapter 4, Section 4.2. Now, in this section, we’ll create a new planning



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-0-1.png)








model from scratch. First, we’ll create a currency table with conversion
rates. Then, we’ll create the data model by using master data. The process
will conclude with uploading transactional data for the actuals and forecast
versions of the model.


**Demo Data Package**


In this section, we’ll go through the model creation process. You’ll need to
download the demo data package from the publisher’s website at _[https://](https://www.sap-press.com/5753)_
_[www.sap-press.com/5753](https://www.sap-press.com/5753)_ . You’ll find a compressed archive at the bottom
of the page in the **Product supplements** section. All three files required for
this section can be found in the **Planning Data** folder.


The planning model we’ll build in this section is based on sales data for var- **Data for the**
ious sporting goods (clothes and accessories). The planning process will be **planning model**
performed for regions and products on a monthly granularity.


The files with the sample data contain the following contents:


- **Operating Income Master Data.xlsx**
This file contains the master data for the planning model and the currency conversion table. Both tables are essential for the initial model creation. This workbook contains four sheets:


 - **Accounts**
This sheet contains all accounts and their attributes.


 - **Region**
This sheet defines the regional hierarchy of sales regions.


 - **Product Groups**
This sheet contains the product hierarchy.


 - **Currency**
This table contains currency conversion rates, which we’ll use to create a currency table.


- **Operating Income Actuals (2023).csv**
This file contains actual transactional data for 2022 and 2023.


- **Operating Income Forecast (2023).csv**
This file contains forecasted transactional data for 2022 and 2023.


Note that you’ll need a program like Microsoft Excel to open XLSX files.


**6.2.1  Creating a Currency Conversion Table**


To establish our planning workflow, we first need to create a currency conversion table. This table will be used later within planning models to show
values in other currencies.










**Creating a currency** Open the main menu and select **Modeler** - **Currency Conversions** - **Currency**
**conversion table** **Conversion Table**, as shown in Figure 6.11.


Select the **New Currency Conversion Table** entry and enter the title, as
shown in Figure 6.12: "OperatingIncome_Currency". Then, click on **Create** .


**Figure 6.11** Creating a New Currency Conversion Table


**Figure 6.12** New Table Name and Description


**Adding conversion** You’ll be automatically redirected to an empty table in which you can enter
**rates** conversion rates line by line. For each entry, you must maintain the **Source**
**Currency**, **Valid From**, **Target Currency**, **Rate Type**, and **Exchange Rate** fields.
You also can maintain different exchange rates for different versions.


Enter the values from the **Currency** sheet from the _Operating Income Master_
_Data.xlsx_ Excel file. To make this process easier for you, the sheet already
matches the structure of the table in SAP Analytics Cloud so that you simply copy and paste the rates. However, make sure you do not copy the
header line.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-2-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-2-1.png)








The results should match the table shown in Figure 6.13. Now, click on the
**Save** icon to save the table.


**Figure 6.13** New Currency Conversion Table


The currency conversion table is not automatically used but must be
explicitly referenced in a planning model, which we’ll set up during the
model creation process.


**6.2.2  Creating a Master Data Model**


First, we’ll create the model and master data manually. We’ll create the **Creating a model**
model and all dimensions first and upload any transactional data later. This **manually**
modeling procedure is common in planning workflows and will also show
you how to create a model manually.


Follow the initial steps described in Chapter 4, Section 4.3. Create a new
model by opening the main menu and clicking on **Modeler** - **Model**, as
shown in Figure 6.14.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-3-0.png)








**Figure 6.14** Creating New Models


**Start with empty** Choose the **Start with an empty model** option, as shown in Figure 6.15. SAP
**model** introduced a new data model type in 2021. However, since this model was
introduced after the product launched, some restrictions apply. Some features are also only supported in the new model. More information about
this topic can be found in Chapter 4, Section 4.5.1.


**Figure 6.15** Choosing a Model Type


The empty model initially has a version dimension and a date dimension,
as shown in Figure 6.16. These dimensions must be maintained first before
you can upload any data to the model.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-4-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-4-1.png)








**Figure 6.16** New Model with Version and Date Dimensions


Initially, we want to activate the currency conversion and validate the date **Model preferences**
settings. Click on the **Model** **Preferences** icon and click the **Planning** tab.
Ensure that the **Planning Capabilities** slider is on and the **Date Dimensions**
**used for Planning** dropdown has **Date** selected, as shown in Figure 6.17.


**Figure 6.17** Planning



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-5-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-5-1.png)








**Enabling currency** Switch to the **Currency** tab and activate the **Currency Conversion** option, as
**conversion** shown in Figure 6.18. Make sure that the **Currency Rate Tables** field shows
your previously created table, **OperatingIncome_Currency** and confirm
these settings by clicking on **OK** .


**Figure 6.18** Enabling Currency Conversion


**Adding an account** Now, click on the **+** button and select the **Add New Dimension** entry.
**dimension** Rename the title of the dimension to “OP_Accounts” and make sure that
the **Type** field is set to **Account** and confirm these settings by clicking on
**Add**, as shown in Figure 6.19.


**Figure 6.19** Adding New Account Dimensions



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-6-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-6-1.png)








**Public Dimensions**


A public dimension is saved independently from its model and thus can be
used across multiple models. One advantage of a public dimension is that
it is maintained centrally and thus reduces maintenance effort. Public
dimensions only contain master data; the necessary transactional data
must be provided in each model separately. These dimensions are suitable
for account structures or real-world structures like organizations, regions,
or products.


In the new model type, not every dimension type can be set as a public
dimension. In this case, the setting is greyed out.


A new dimension will now be added to the list. Open the dimension by **Dimension**
clicking on the icon in the **Type** column and switch to the grid view by **overview**
clicking on the icon in the top right, as shown in Figure 6.20. Open the
_Operating Income Master Data.xlsx_ Excel file and switch to the **Accounts**
sheet. Select the contents of this sheet (except for the first line, which contains the headers) and copy this data. Then, paste this data into the grid
view of the account dimension in SAP Analytics Cloud. The result should
match the table shown in Figure 6.20.


**Figure 6.20** Account Dimension



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-7-0.png)








Click on the **Back** icon in the top left to navigate back to the model overview. Now, create another public dimension with the following parameters:


          - **Name** : “OP_Region”


          - **Type** : **Organization**


          - **Make This a Public Dimension** : No


**Creating a hierarchy** Open this new dimension by clicking on its name in the list. Click on the **+**
**Create Hierarchy** button in the sidebar and choose the **Parent-Child Hierar-**
**chy** option. Enter “Hierarchy” into the **ID** field and leave the **Description**
field empty.


Again, switch to the grid view (via the icon). Similar to the account
dimension, the _Operating Income Master Data.xlsx_ Excel file contains the
necessary data. Open the file and navigate to the **Region** tab. Then, copy its
content (except the header info in the first line) and paste it into SAP Analytics Cloud. The view should match the table shown in Figure 6.21.


**Figure 6.21** OP_Region Dimension


**Creating a generic** Return to the dimension overview and create a new dimension with the fol**dimension** lowing parameters:


          - **Name** : “OP_Product”


          - **Type** : **Generic**


          - **Make This a Public Dimension** : No


Similar to the dimension before, open the dimension by clicking on its
name. Create a new parent-child hierarchy with the ID “Hierarchy.” Again,
the _Operating Income Master Data.xlsx_ Excel file provides the contents.
Open this file, navigate to the **Product** tab, and copy all contents (except the
first line of header info) into the grid view of SAP Analytics Cloud. The result
should match the table shown in Figure 6.22.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-8-0.png)








**Figure 6.22** OP_Product Dimension


Return to the model overview and open the sidebar of the OP_Region
dimension by clicking on the dimension title in the **Type** column on the left
side of the screen. Check the **Properties** section. It should show the **Currency**
entry, as shown in Figure 6.23.


**Figure 6.23** Currency Property


Since the new model requires at least one measure, we need to create an **Creating a measure**
empty measure which we won’t use during our planning activities. Switch
to the **Calculations** overview by clicking on the dropdown on the top left of
the modeler (below **Workspace** ).


Click on the + icon next to **Measures** to add a new measure. Name the measure “SignedData” as shown in Figure 6.24.


**Figure 6.24** Creating a New Measure



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-9-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-9-1.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-9-2.png)








**Measures and**
**accounts in one**
**model**



The new model type allows models to carry both single measures and
account dimensions. This can lead to conflicting situations where measures and accounts have inconsistent properties. To prevent issues caused
by this, you can open the model preferences and determine if properties
and calculations are prioritized either from measures or the account
dimension. Depending on which you select, the properties of the selection
will be respected first. In our case, there is no potential for conflict as we
don’t apply any properties here.



**Date dimension** Last, we need to validate the **Date** dimension. By default, it is set to a specific range which may not match our data. Click on the **Date** dimension in
the **Type** column to open the dimension settings in the right sidebar.


Scroll down to the **Date** settings and make sure to set the **From/To Year** setting to **2022** to **2023** as shown in Figure 6.25. Otherwise, the data upload will
fail as our data is mapped from 2022 to 2023.


**Figure 6.25** Setting the Date Range


We’re now done with the initial steps for creating our planning model, so
let’s save it by clicking on the **Save** icon. Now, create a new subfolder called
**Sales Planning** and save the model with the title “Operating Income.” Validate your model against the screen shown in Figure 6.26.


**Figure 6.26** Final Model



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-10-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-10-1.png)








**6.2.3  Uploading Transactional Data to the Model**


After creating the model, now is the time for uploading transactional data
to it. The demo data package contains two files in the **Planning Data** folder
that contain those numbers.


Make sure that you’re on the model overview screen and click on **Data** **Data management**
**Management** in the top left. This area can be used to import new data. You
can also set up scheduled imports and exports, as shown in Figure 6.27.


**Figure 6.27** Data Management


In the following sections, we’ll first upload actual data and then forecast
data.


**Actual Data**


First, let’s import the actual data. Click on the **Import** icon in the **Import**
**Jobs** section. There, select **File (Local File or File Server)**, as shown in Figure
6.28. Click on **Select Source File** and select the _Operating Income Actuals_
_(2023).csv_ file on your computer. Confirm by clicking on **Import** .


**Figure 6.28** Uploading New Data



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-11-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-11-1.png)








**Data mapping** After you’ve successfully uploaded the file, it will be displayed under the
**Import Jobs** tab. Click on **Set Up Import** and then click on **Next** to skip the
data wrangling step and open the mapping dialog, as shown in Figure 6.29,
where you can define how the uploaded file should be mapped to the
model.


**Figure 6.29** Data Mapping


Because the file’s structure is very similar to the model, SAP Analytics Cloud
automatically recognizes almost all columns. If a column can’t be mapped
automatically, you’ll be notified in the left sidebar. You then must map this
column to an account dimension by using drag and drop. The dimensions
are shown in the card view in the middle of the screen. The **Version** column
on the left will stay unmapped as the version values on the right side are
filled out with default values.


The import preferences, which can be accessed from the bar on the top,
offer various options, as shown in Figure 6.30, to further configure the data
import job. As new values are added, you can click on **View All Options** to
determine how data is treated that doesn’t match the master data.


**Import method** The **Import Method** section allows you to choose among four options:


          - **Update**
Updates all existing records with the uploaded ones. New entries will be
added to the model.


          - **Append**
Adds all uploaded records to the model, including new entries.


          - **Clean and replace selected version data**
Deletes existing data and replaces it with imported records. This process
only applies to the indicated version. New entries will be added to the
model.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-12-0.png)








- **Clean and replace subset of data**
Deletes a subset of existing data defined using either versions or dimensions. Then, the data is replaced with the newly uploaded data. New
entries will be added to the model.


Make sure that the **Update** option is selected.


**Figure 6.30** Import Settings


By default the **Version** column is set to a default value. In our case, this is **Mapping versions**
**public.Actual** which is correct for this step. Later, we will upload our forecast
data. We will then adjust this setting.


Finalize the mapping by clicking on the **Next** button on the bottom right
twice. SAP Analytics Cloud will now validate the data. After this step is completed successfully, click on the **Run Import** button to complete the import
job. Finally confirm by clicking on **Finish** . After some time, the upload will
finish and you will receive a success confirmation.


**Forecast Data**


Now, we want to import the forecasted data. For now, the new model in SAP
Analytics Cloud does not support the creation of new versions directly in
the modeler. A workaround is necessary in which we will open a story and



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-13-0.png)









create a version there. Then we will return to the modeler to upload the
forecast data. Once SAP delivers this functionality, the workaround can be
skipped and you can directly upload the second file.


Leave the modeler and head to the stories overview. Create a new **Canvas** page
in optimized mode and add a new table which populates its data from the
**Operating Income** model we just created. Now open the **Version Management**
interface from the **Tools** section in the top bar (see Figure 6.31).


**Figure 6.31** Version Management


Click on the **+** next to **Public Versions** to create a new version. Set the **Ver-**
**sion Name** to “Forecast” and the **Category** to **Forecast** as shown in Figure
6.32. Confirm by clicking on **Create** .


**Figure 6.32** Creating a New Public Version


Afterwards, leave the story without saving it. Return to the modeler and
open the **Operating Income** model again. Switch back to the **Data Manage-**
**ment** screen.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-14-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-14-1.png)








Again, click on the **Import** icon and select the **File (Local File or File**
**Server)** option. Click on **Select Source File** and choose the _Operating Income_
_Forecast (2023).csv_ file from your computer. Start the upload process by
clicking on **Import** .


Open the file by clicking on **Set Up Import** . Skip the data wrangling step **Appending data**
again by clicking **Next** to reach the **Mapping** screen. First, in the **Job Settings**
that can be accessed by clicking on the icon in the top bar, under **Import**
**Method**, select the **Append** option, as shown in Figure 6.33.


**Figure 6.33** Changing Import Methods


Again, we must make sure that all dimension are mapped correctly.


By default, the **Version** dimension is mapped to a default value. Therefore,
we will again leave the **Version** column on the left side unassigned. First
click on the **X** next to **Default Value** in the right sidebar as shown in Figure
6.34.


**Figure 6.34** Unmapping Versions


Now, the **Version** will appear as **Unmapped** in the middle. Click on the three
dots as shown in Figure 6.35 and choose **Set default value…** . In the newlyappearing dialog, select the **public.Forecast** version.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-15-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-15-1.png)








**Figure 6.35** Unmapped Targets


**Figure 6.36** Mapped Columns


The **Mapped** column should now match Figure 6.36. Again, click on **Next**
two times to complete the import job. After successful validation, click on
**Run Import** and **Finish** to upload the data to the model. The model is now
filled with data and ready to use.


**6.2.4  Setting Up a Planning Model**


In addition to the settings described in Chapter 4, Section 4.5, the modeler
provides specific settings that only apply to planning models and enable
you to further configure planning models. These settings will be presented
in this section.


**Model preferences** Open the modeler for any planning model (you can use the Operating
Income model we just created) and open the model preferences . The
model preferences screen provides various options to further configure the
model.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-16-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-16-1.png)








**Access and Privacy**


The **Access and Privacy** tab combines all functionality for managing the
security and privacy of a model and prevents unauthorized access, as
shown in Figure 6.37.


**Figure 6.37** Model Preferences: Access and Privacy


If you turn on the **Data Audit** option, all data changes performed in the **Data audit**
model (e.g., through data entry) are captured in a log file. More information
on this topic can be found in Chapter 3, Section 3.3.1.


The **Data Locking** switch can be turned on to lock the values in a model. Once **Data locking**
the option is activated, users can lock individual values in the planning process so that these values can’t be modified by other users. This feature is helpful for ensuring that data entries are not accidentally overwritten by others.
You must indicate whether values are generally locked automatically or only
locked manually ( **Default Lock State** ).


Turning on the **Restricted Export** option will disable the exporting func- **Restricted export**
tionality of all charts and tables that use this model. This option can be used
to protect sensitive data from being easily exported to other systems.


The **Access and Privacy** section also provides options to steer data access, as **Model data privacy**
shown in Figure 6.38. Once the **Model Data Privacy** switch is enabled, the
model is only visible to the owner and users that carry the necessary role.
However, this option shouldn’t be selected if possible since model visibility
can also be controlled by using the folder structure, as described in Chapter
3, Section 3.3.5.



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-17-0.png)








**Data access control** The **Data Access Control** **in Dimensions** tab can be used to turn on data
access control for single dimensions. When this option is activated, you can
restrict data access by using individual dimension members. More information on this topic can be found in Chapter 4, Section 4.5.2.


**Figure 6.38** Access and Privacy: Further Options


**Date Settings**


The **Date Settings** tab provides options for defining a fiscal year that deviates from the calendar year, as shown in Figure 6.39. To use this function,
you must first enable the **Apply Fiscal Year Settings** switch for the date
dimension. Then, you can determine individual start and end dates.


**Figure 6.39** Date Settings



![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-18-0.png)

![](temp_conversion_out/main/images/044_6.2 Creating and Setting Up a Planning Model_044_6.2-Creating-and-Setting-Up-a-Planning-Model.pdf-18-1.png)






