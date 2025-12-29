---
tags:
source: 040_5.11 Additional Story Functionalities.pdf
title: 040_5.11 Additional Story Functionalities
---



**Third page** Now, create a third responsive page and rename it to “More.” This page only
has one lane, so remove the second lane.


Rename the lane title to “More information” and add the following elements:


          - A heat map with **Product** on the X axis and **Supermarket** on the Y axis.
Use the **Revenue** measure to determine the colors.


          - A radar chart with the **Revenue** measure and the **Supermarket** dimension. Use the **Product** dimension for the color.


Save the story as “Sales Analysis (responsive)” in the **Sales Data** folder. Validate your progress against the _Checkpoint 10 – Section 5.10.2.pdf_ file from


the demo data package.


Finally, install the mobile application on your own smartphone or tablet.
After connecting to your SAP Analytics Cloud tenant, open the story and
explore it.


**5.11  Additional Story Functionalities**


**Other workflows** Since a story can provide a vast amount of functionality, not all of these
functionalities could be covered in this chapter. In this section, we’ll present additional workflows that are part of the BI field. Similar to Section 5.2,
we’ll again use the demo files downloaded from the publisher’s website.


**5.11.1  Creating an Embedded Model within a Story**


In Chapter 4, Section 4.3, we covered the use case of creating a model in the
modeler, but another option is creating a model directly within a story. This
procedure is recommended for workflows in which business users want to
visualize small amounts of data on their own but don’t need to create a full
model and/or don’t have the necessary permissions for this task (see Chapter 4, Section 4.2.4). Models that are embedded into a story can only be used
within that story or can be published into a public model.


**Creating a model** Create a new story (as described in Section 5.2.2). Click on the **Add New Data**
**within a story** icon in the top bar in the **Tools** section, choose **Add New Data…** and click on
the **Data Uploaded from a File** button, as shown earlier in Figure 5.9 1.


After you’ve uploaded the file successfully, you’ll see the data wrangling
interface. Now, you can clean or enrich the data (see Chapter 4, Section 4.3).
An embedded model can always be manipulated by returning to the data
view of the story.










**5.11.2  Story Templates**


As described in Section 5.2.2, stories can also be built by using templates.
The template contains all story settings, as well as pictures and texts.
Instead of charts, a template has placeholders, which can be either replaced
by the recommended chart (e.g., geo map and bar/column chart shown in
Figure 5.118) or any other chart type.


**Figure 5.118** Story Template


Story templates can contain multiple pages. To create a new template, first **Creating templates**
create a story and fill it with content. Then, apply all desired story settings.
Selecting the **Save as Template…** option will save the story as template. In
the saved template, all charts, tables, and input controls will be replaced by
placeholders.


**5.11.3  Blending**


Another important BI workflow is blending. When performing a blend, two **Blending**
data models will be linked by a common dimension so that data can be **and joining**
combined and shown in a single chart or table. An important distinction to
keep in mind is that _blending_ is always performed on the aggregation level
currently defined in the charts, while _joins_ always happen on the lowest
possible data level.



![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-1-0.png)








**Performing a blend** Let’s perform a blend using the Sales Data model created in Chapter 4, Section 4.3 and Section 4.5. In addition, we’ll use the _Blending-Data.xlsx_ file
from the demo data package. Blending is currently only supported in classic
mode. Create a new story in **Classic Design Experience** mode and add a canvas page. Add a new table to the page that retrieves its data from the Sales
Data model. Add the **Quantity** and **Revenue** measures to the columns and
the **City** dimension to the rows. Switch over to the data (click on the **Data**
button in the top left) and select **+ Add New Data…**, as shown in Figure 5.119.


**Figure 5.119** Adding New Data


Now, choose the **Data Uploaded from a File** option and upload the _Blending-_
_Data.xlsx_ file. Make sure that the **Potential Customers** column is recognized
as a measure (see Chapter 4, Section 4.3). Click on **Story** in the top left to
return to the story. Now, open the **Link Dimensions** interface from the top
bar of the story. Link both models on the **City** dimension. Make sure that
the ID of the city is used, as shown in Figure 5.120. Confirm the blend by
clicking on **Set** .


**Figure 5.120** Linking Dimensions



![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-2-0.png)

![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-2-1.png)








Open the builder of the table and click on **Add Linked Models**, as shown in
Figure 5.121. Select the _Blending-Data.xlsx_ model.


**Figure 5.121** Adding Linked Models


Now, create a new calculated measure in the builder, as shown in Figure
5.122. Enter the formula “Revenue/Potential customers” manually and
make sure you select the proposed values with the value help. While typing,
the proposals appear automatically. Confirm these selections by pressing

(Enter). Call the measure “Revenue per customer,” as shown in Figure 5.123.


**Figure 5.122** Adding Calculations to Tables


**Figure 5.123** Calculations in Editor


The table now shows a new column that contains the calculation (for example, as shown later in Figure 5.125).


If desired, blending options can be configured in the builder, as shown in **Blending settings**
Figure 5.124. You can change the link type ( **All Primary Data**, **All Data**, or



![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-3-0.png)

![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-3-1.png)

![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-3-2.png)








**Intersecting Data Only** ) and change various parameters to control the
blending behavior.


**Figure 5.124** Blending Settings


**Blending**


Blends can only be created within a story, but blending isn’t available for
all live data sources. You can use more than one dimension to define a
blend if your unique key can only be achieved in this way. Also, you can create more than one blend, which allows you to create triangular or square
relationships between models, for example.


**5.11.4  Comments**


Users can also leave comments on the charts, tables, and pages of a story.
This feature is available to all story viewers.


To create a comment, click on chart and open the action bar. Select **Add**          **Comment** to open the comment form. Users can enter any text and place
the comment, as shown in Figure 5.125.


**Figure 5.125** Placing New Comments


**Page comments** Comments will be stored with the date and time of their creation as well as
the name of the person who wrote the comment. You can also place comments on pages by clicking on the page title and selecting the **Comment**
entry.



![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-4-0.png)

![](temp_conversion_out/main/images/040_5.11 Additional Story Functionalities_040_5.11-Additional-Story-Functionalities.pdf-4-1.png)






