---
tags:
source: 036_5.7 How Viewers Interact with Stories.pdf
title: 036_5.7 How Viewers Interact with Stories
---



publications. Special URLs are provided, usually with the _.rss_ extension, to
access a list of news or announcements. These URLs can also be used in SAP
Analytics Cloud.


Click on the **+** button in the top bar of the story and select **RSS Reader** . The
builder will now open. Click on **Add Another RSS URL** . Enter “SAP News” into
the **Title** field. Then, enter the URL _[https://news.sap.com/feed/](https://news.sap.com/feed/)_ into the **RSS**
**URL** field. The configuration of the reader is shown in Figure 5.69.


**Figure 5.69** RSS Reader


Save the story and use the _Checkpoint 4 – Section 5.6.pdf_ file from the demo
data package to verify your progress.


**5.7  How Viewers Interact with Stories**



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-0-0.png)

Data can become quite large and complex, and sometimes, insights can
only be gained by applying filters. In addition, chart interactions can help
users access additional information or better understand the whole. So far,
all the features we’ve presented required you to be the story creator or at
least have rights to edit a story. In this section, we’ll discuss various tools

that can be activated by story creators so that viewers can interact with stories. The following features will be discussed:


- Filters


- Input controls for dimensions and measures


- Linked analysis


- Hyperlinks


- Explorer


- Edit and view modes



**Filters and**
**interactions**










Note that these tools are activated in the story editing mode, but they can
be tested immediately by switching into view mode. How you navigate
between the edit mode and the view mode is shown in Section 5.2.4. In the
following sections, we consider story owners as any user authorized to edit
the story.


**5.7.1  Filters**


**Filter types** The filtering capabilities in stories in SAP Analytics Cloud are quite strong.
You can use filters to represent a specific context or identify single data
points. A story can contain three different filter types:


          - Chart filters


          - Input controls


          - Story filters


Let’s make sure you understand these types so that you can apply the correct filters.


**Chart Filters**


A chart filter is created on the chart level and initially only affects the chart
for which it is created. However, you can extend its scope to include other
charts by turning on **Linked Analysis**, which we’ll describe in Section 5.7.3.


Chart filters can be used by story creators and story viewers. If the filter is
set by a story creator, that filter will be saved with the story and set for all
people accessing the story. To create a chart filter as a story creator, you can
either enter the chart itself or the builder. Use the first page of the story we
created earlier to follow along with the next examples.


**Filtering in a chart** To filter a chart based on a specific data point, click on the data point and
then select the filter icon, as shown in Figure 5.70. The chart will be reduced
to show the selected data point only. Story viewers can apply a similar filter
in the same way.


**Figure 5.70** Applying Filters to Charts


To find out if a filter has been applied to a chart, check the chart’s action bar,
which will show additional information, as shown in Figure 5.71. To remove
the filter, click on the **X** symbol.



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-1-0.png)








**Figure 5.71** Removing Chart Filters


In addition, story creators can use the chart builder to create filters. Open **Filtering charts**
the builder and click on **Add Filters** in the **Filters** section, as shown in Figure **in the builder**
5.72. Select the **Product** dimension.


**Figure 5.72** Creating Chart Filters in the Builder


The filter dialog box will open. Select the **Juices** and **Alcohol** entries. You can
also indicate whether the filter should exclude the selected items instead of
including them. By default, this setting is turned off so that the filter only
keeps the items you selected. When you turn on this setting, all items that
are selected will be excluded while the remaining will appear in the chart.
You can also specify if story viewers can modify the filter and if the filter
allows multiple or single selections only, as shown in Figure 5.73.


**Figure 5.73** Selecting Items to Be Filtered



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-2-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-2-1.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-2-2.png)








After you create the filter, you can later delete it by clicking the **X** icon to the
top right of the filter in the builder, as shown in Figure 5.74.


**Figure 5.74** Deleting Chart Filters


The chart filter should only be used if the chart is designed to meet a specific context and the filter is applicable to this context only. Furthermore,
chart filters are more relevant for story viewers who can use them to drive
their own filtering workflows, which we’ll describe in detail in Section 5.7.3.


**Page Filters**


Page filters are recommended to filter entire pages or to provide story viewers with an intuitive filtering experience. These filters are added as objects
to story pages and are therefore directly visible.


Story creators can fully steer the extent to which a story viewer can use the
input controls. Also, the scope of the input control can be limited to affect
only a selection of charts on the same page. If models are linked, the filter
will also be applied to linked models.


**Figure 5.75** Creating New Input Controls



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-3-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-3-1.png)








Click on the icon to add a new input control in the **Insert** section of the **Creating a new**
top bar. The input control can be created for dimensions and measures. **page filter**
Click on the newly-created input control and choose the **Product** dimension, as shown in Figure 5.75.


Now, the filter dialog box will open. As a story creator, you must decide **Member selection**
which dimension members will be available to the story viewer for filtering. Choose **All Members** so that story viewers can decide for themselves if
they want to see all products or only specific ones, as shown in Figure 5.76.
Also make sure that story viewers are allowed to modify the selection and
that the **Multiple Selection Hierarchy** option is activated. You also can use
these options to forbid viewers from making changes to the filter criteria.


**Figure 5.76** Member Selection for Input Controls


Confirm the creation of the input control by clicking on **OK** . Afterwards,
extend the size of the input control to show it completely, as shown in Figure 5.77.


**Figure 5.77** Input Control



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-4-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-4-1.png)








**Using input controls** Now, switch to the view mode (click on **View** at the top right of your screen)
and try out the filter. Observe how the charts start changing and showing
additional or fewer dimensions. In the end, set the filter to show all values
again.


**Configuration** Return to the edit mode. Click on the input control to open the action bar
**options** either by clicking on the three dots icon or right-clicking anywhere on the
input control, as shown in Figure 5.78.


**Figure 5.78** Action Bar of Input Control


The action bar of the input control provides various options to modify the
input control. You can determine the selection of charts that are affected by
the filter ( **Linked Analysis** ). However, the input control can only affect
charts and tables on the same page. The **Edit Input Control** option can be
used to modify the filter itself and return to the dialog box shown earlier in
Figure 5.76. When the **Cascading Effect** option is activated, the input control
can react to other story filters or input controls. If they already reduce the
amount of data, the input control will automatically only show available
values if this option is turned on. An input control can only affect the page
it’s placed on, but you can use **Convert to Story Filter** to transform the input
control into a filter applied to all pages of the story. However, this option
will make the input control disappear from the page and move it to the filter bar of the story.


**Input control for** When creating an input control for a date dimension, a different layout is
**date dimensions** available as an alternative to the checkboxes. This layout uses date ranges
and can be either fixed or dynamic. Create a new input control and select
**Dimensions**         - **Date**         - **Filter by Range…** .


**Fixed date filters** When you create a fixed date dimension filter, you must provide specific
date ranges, as shown in Figure 5.79. The deeper your date hierarchy goes
(in our example, we have monthly data), the more granular the filter can
become. You can also allow the story viewer to change the selection.



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-5-0.png)








**Figure 5.79** Fixed Date Filter


While fixed date filters require you to choose dates in all fields, dynamic fil- **Dynamic date filters**
ters allow your viewers to reference a current or custom date. Viewers then
define how many days, weeks, months, quarters, or years before and after the
date should be displayed, as shown in Figure 5.80. In addition, you can also
set filters to just use data from the current day, week, month, quarter, or year.


**Figure 5.80** Dynamic Date Filter



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-6-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-6-1.png)








**Current date** By default, the dynamic filter will use the current system date as a reference.
If you want to use a custom date, you can use the **Current Date** dropdown box
to create an additional input control that allows the user to set a custom reference date. Create a fixed time filter on the month level for the period from
January 2023 to December 2023 and make sure that the viewer is allowed to
modify the selection. Afterwards, extend the filter’s size so that it’s shown
completely. The result should match the screen shown in Figure 5.81.


**Figure 5.81** Date Input Control


**Input controls** Another filter criterion for input controls can be a measure. In this case,
**for measures** the filter will not be driven by a selected dimension member but by the
value of a measure (e.g., all supermarkets that have a revenue of USD
300,000 and more). Create a new input control and click on it. Select **Mea-**
**sure**          - **Quantity** to open the filter creation dialog box. Define the first range
to span from 0 to 1,000,000 and allow story viewers to modify the filter.
The **Dimension Context** option is useful for restricting the aggregation
behavior to a specific dimension. Select the **Version** and **Supermarket**
dimensions from this dropdown list, as shown in Figure 5.82.


**Figure 5.82** Input Control for a Measure



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-7-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-7-1.png)








Confirm the input control by clicking on **OK** . Extend its size so that it
becomes fully visible. This filter can be used now to only show supermarkets where the selected value lies within the selected range.


The input control also supports more complex scenarios, including com- **Advanced filters**
bining multiple filter conditions with AND and OR relationships. Create a
new input control and choose the **Advanced Filtering…** option.


First, choose which operator should connect both filter criteria. Click on the
arrow icon to see the available options. You can also specify whether viewers are allowed to change the relation. The following options are available:


- **Filter: AND**
All values that meet all criteria are included.


- **Filter: OR**
All values that meet at least one of the criteria are included.


- **Exclude: AND**
All values that meet all criteria are excluded.


- **Exclude: OR**
All values that meet at least one of the criteria are excluded.


Advanced filters can become quite complex and be nested (one criteria can
again consist of multiple criteria). Nesting allows you to create multiple criteria in a tree structure, which are checked level by level. For our example,
create a filter with an **AND** relation. Set the filter to show the **Actual** member
for the **Version** dimension and **Soft Drinks** for the **Product** dimension, as
shown in Figure 5.83.


**Figure 5.83** Advanced Filter



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-8-0.png)








After you create the filter, try it out and see how it changes the charts.
Delete the filter when you’re done; we won’t use it in later examples.


**Story Filters**


If a filter should be applied to all pages of a story, we recommend using
story filters, which are created in the side bar of the story. Open the story filter bar by clicking on the **Filter** icon.


A story filter supports the same features as an input control, as shown in
Figure 5.84. The only difference is that story filters are always applied to all
charts on all pages of a story that are using the same model or a linked

model. For more on input controls, refer to the previous section on page filters.


Save the story again and validate your progress against the _Checkpoint 5 –_
_Section 5.7.1.pdf_ file from the demo data package.


**Figure 5.84** Creating New Story Filters


**5.7.2  Dimension and Measure Input Controls**


Another important feature of dashboards is the compact display of greater
amounts of information. Often charts are created multiple times to show
different dimensions. To avoid a high number of charts, the story offers
dimension and measure input controls. These controls allow the story
viewer to dynamically choose the measure or dimension shown in a chart.
These input controls do not filter the data; they just exchange the dimension or measure in a chart.



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-9-0.png)









Open the builder for the **Quantity by Product** chart you created earlier. Click
on **Add Dimension** below **Dimensions** and select **Add Dimension Input Con-**
**trol**, as shown in Figure 5.85.


**Figure 5.85** Creating Dimension Input Controls


Now, you can specify which dimensions will be available for story viewers
to choose from. Choose the **Product**, **Supermarket**, and **Street** dimensions.
Now, click on **OK** .



**Creating a**
**dimension**
**input control**



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-10-0.png)

Because the chart is now showing the same dimension ( **Product** ) twice, **Showing the same**
you’ll see an error message. Remove the **Product** dimension from the chart **dimension again**
in the builder so that it only contains the **New Dimension Input Control**
dimension. The input control is now used as a placeholder and will show
the dimension selected by the viewer.


You’ll now see a new object on the page that contains the input control.
Move this option next to the chart to which it belongs (you may need to
move away the other input controls) and extend its size to make it completely visible, as shown in Figure 5.86.


**Figure 5.86** Chart with Dimension Input Control



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-10-1.png)









**Measure input**
**controls**



Measure-based input controls can be created as well to switch measures in
a chart. The procedure is quite similar. However, in the builder, you must
add a new measure (click on **Add Measure** ) and select **Create Measure Input**
**Control** . The procedure is otherwise identical to the previous example, so
we won’t repeat these steps.


Save the story and validate your progress by against the _Checkpoint 6 – Section_
_5.7.2.pdf_ file from the demo data package.


**5.7.3  Chart Interactions**



**Linked analysis** Reports are usually designed to show a high-level overview first before
more details are exposed. Simple diagrams provide a current overview of
the data. However, data will need to be filtered down to provide more
details. To support this workflow graphically, SAP Analytics Cloud provides
the _linked analysis_ feature. To access this feature, you must first select a
chart or table (we’ll use the **Revenue by Supermarket** chart created earlier)
and then select **Linked Analysis** in the chart action bar.


**Scope** The panel offers various options to drive the filtering behavior of the chart,
as shown in Figure 5.87. If the chart shouldn’t interact with any other object,
select the **Only this Widget** option. The chart can also be used to automatically filter down all objects in a story that use the same or a linked data
model ( **All Widgets in the Story** ). The same is applicable for the same page
only ( **All Widgets on the Page** ).


**Figure 5.87** Linked Analysis


**Individual selection** If you want to specify which widgets should be affected by a filter applied to
the chart, select the **Only Selected Widgets** entry. Besides selecting the



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-11-0.png)








specific widgets, you can also activate the **Automatically Connect Newly**
**Created Widgets** setting. Once activated, every new chart or table that is
created thereafter will also be affected by this chart. If you activate the **Filter**
**on data point selection** option, viewers only need to click on a data point to
filter down all the other charts.


Choose the **All Widgets on the Page** option and select the **Filter on Data**
**Point Selection** checkbox. Confirm these settings by clicking on **Apply** and
try them out afterwards by clicking on any data point in the chart.


_Hyperlinks_ can be added to charts and tables to allow viewers to navigate to **Hyperlinks**
other pages, stories, or external websites from the chart. To create a new
hyperlink, click on the **Revenue by Supermarket** chart and select **More**
**Options** - **Add** - **Hyperlink…** in the action bar, as shown in Figure 5.88.


**Figure 5.88** Adding Hyperlinks


As shown in Figure 5.89, multiple types of hyperlinks can be added to a **Hyperlink types**
chart, as follows:


- The **Mobile App URL** type defines hyperlinks to other mobile apps if the
story is opened on a mobile device.


- The **External URL** type navigates to an external website. In addition, you
can use the contents of the chart to parameterize the URL. If you click on
a specific supermarket in a chart that contains hyperlinks, for example,
the URL can be configured to contain the name of the supermarket and
thus lead to that supermarket’s specific website.


- With the **Page** and **Story** types, you can create navigation to other pages
or stories within SAP Analytics Cloud. You can also choose to use the
dimension as a filter in the other story or page. However, in this scenario,
the charts or tables on the page must use the same data model.



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-12-0.png)








**Figure 5.89** Hyperlink Types


For our example, choose the **Page** option and create a hyperlink to **Page 2** .
Activate the **Apply Selected Dimension as a Filter** option, as shown in Figure
5.90, and click on **Done** to confirm the configuration.


**Figure 5.90** Creating Hyperlink to Another Page


**Explorer** Another option to provide more flexibility to story viewers is the _explorer_ .
This mode allows viewers to modify the chart or table on their own without
modifying the original story. The story creator determines which dimensions and measures are available via the explorer.


**Enabling the** To activate the explorer in our example story, open the builder for the **Rev-**
**explorer** **enue by Supermarket** chart. Then, activate the **Enable Explorer** option, as
shown in Figure 5.91. Explorer mode is only available in classic mode. In
optimized mode, you can enable the data analyzer. However, no further
configuration is possible as of right now.



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-13-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-13-1.png)








**Figure 5.91** Enabling the Explorer


Next, click on **Configure Measures & Dimensions** . A dialog box will open
where you can specify which measures and dimensions should be available
to story viewers in the explorer. Select all the measures and dimensions
and confirm these settings by clicking on **OK**, as shown in Figure 5.92.


**Figure 5.92** Setting Up the Explorer


Viewers will see the **Explorer** **Available** note for every configured chart. To **Accessing the**
open the explorer, open the action bar and click on **Open Explorer**, as shown **explorer**
in Figure 5.93.


**Figure 5.93** Opening the Explorer



![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-14-0.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-14-1.png)

![](temp_conversion_out/main/images/036_5.7 How Viewers Interact with Stories_036_5.7-How-Viewers-Interact-with-Stories.pdf-14-2.png)






