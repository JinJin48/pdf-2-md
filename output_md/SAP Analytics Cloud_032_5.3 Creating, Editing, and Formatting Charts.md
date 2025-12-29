---
tags:
source: 032_5.3 Creating, Editing, and Formatting Charts.pdf
title: 032_5.3 Creating, Editing, and Formatting Charts
---



**5.3  Creating, Editing, and Formatting Charts**


Let’s now continue editing the story we created in Section 5.2.2. First, let’s
add some charts. Then, we’ll extend them via various display options and
format them. Finally, we’ll go over how to interact with hierarchies in the
chart.


**5.3.1  Creating a New Chart**


By clicking on the **Chart** icon in the **Insert** section of the top menu bar, you’ll
add a new chart to your story, as shown in Figure 5.26. The chart will automatically connect to the most recently used data model in this story. However, the model can be exchanged immediately with another one.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-0-0.png)



If no data source was selected before, you are asked to choose one. In our
case, choose our data model Sales Data which we created in Chapter 4.


**Figure 5.26** Editing New Chart in Builder



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-0-1.png)








**Builder** The **Builder** panel will automatically open so that you can start editing and
designing your first chart in the sidebar on the right, as shown in Figure
5.26. The **Builder** provides the most important tools and utilities to configure a chart and format it. You can also activate various interactions and filters here. You can always access and close the builder by clicking on the
right sidebar panel icon.


If not explicitly deactivated in the settings for the data model, each change
in the builder will be applied immediately to the chart. You can perform the
following actions in the builder, as shown in Figure 5.27:


# 1 You can change the data source from which the chart retrieves its data or
add a second model via blending. More information about blending can
be found in Section 5.11.3.


**Figure 5.27** Builder Panel



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-1-0.png)








# 2 The **Currently Selected Chart** and **Chart Orientation** area can be used to
change the chart type. Charts are grouped into clusters for better organization. A list of all chart types is shown in Table 5.1. If you select a chart
type, you’ll see what information is required to display the chart.


# 3 Dimensions and measures can be added by clicking on the **Add Measure**
and **Add Dimension** buttons. These buttons will open dropdown lists of
all available measures and dimensions from which to choose.


# 4 Every chart can have its own coloring scheme, which is assigned in the
**Color** area. More information can be found at the end of this section.


# 5 To a limited extent, if you want to add a filter to the chart, you can do it
in the **Filters** area. Because a story offers complex filtering functionality,
we’ll provide more details about this topic in Section 5.7.1.


# 6 This section allows you to extend the chart with additional elements and
components (e.g., hyperlinks or variances).


# 7 In this section, you can control various **Chart Properties** . You can activate
the data analyzer for a specific chart by activating the **Enable Data Ana-**
**lyzer** option. The explorer can be accessed later by story viewers to individually adjust the chart to their needs without modifying the story itself.


# 8 This button opens the **Chart Formatting** tab, with which you can design
and format the chart.


Table 5.1 shows a list of all available chart types shipped by default with SAP **Chart types**
Analytics Cloud. Based on the chart type, the builder will show specific
options and configurations. These settings will be discarded again if you
change the chart type and the new chart type doesn’t support those particular options.

|Category|Chart Types|
|---|---|
|**Comparison**|<br>Bar/column<br><br>Combination column and line<br><br>Combination stacked column and line<br><br>Stacked bar/column<br><br>Waterfall|
|**Trend**|<br>Stacked area<br><br>Line<br><br>Time series|
|**Distribution**|<br>Box plot<br><br>Heat map<br><br>Histogram<br><br>Radar<br><br>Tree map|



**Table 5.1** Supported Chart Types in SAP Analytics Cloud









|Category|Chart Types|
|---|---|
|**Correlation**|<br>Bubble<br><br>Cluster bubble<br><br>Scatterplot|
|**Indicator**|<br>Bullet<br><br>Numeric point|
|**More**|<br>Donut<br><br>Marimekko<br><br>Pie|



**Table 5.1** Supported Chart Types in SAP Analytics Cloud (Cont.)


**Time series** Let’s say we want to display a time series in the chart we just created. The
chart should show the number of products sold over the year. Go the chart
builder and select the **Time Series** chart type, as shown in Figure 5.28.


**Figure 5.28** Selecting the Time Series Chart Option



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-3-0.png)








Initially, the chart will show no data because you didn’t select any dimension or measure. Select the **Revenue** measure and the **Date** dimension. The
dimension selection automatically adjusts to the chart type. Because the
time series chart requires a date dimension, only one entry is displayed, as
shown in Figure 5.29.


**Figure 5.29** Selecting Measures and Dimensions



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-4-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-4-1.png)



Another special option for time series charts is the **Properties** tab, which **Additional options**
shows up in the builder. This tab allows you to determine the time period is
used in the diagram. You can either set your own selection and save these
settings as the default view for all story viewers, or you can specify that the
time series should always show the newest data. You can also collapse dates
that carry no data, as shown in Figure 5.30.


**Figure 5.30** Additional Options for Time Series Charts


Because the default size of a new chart is too small to display our time series **Adjusting the**
chart properly, we want to extend its width. Click on the time series chart so **chart size**



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-4-2.png)








that its blue frame is activated. Now, click in the middle of the right border,
which appears thicker and keep the left mouse button pressed. Drag your
mouse to the right and set the chart’s width to approximately twice its initial size, as shown in Figure 5.31.


**Figure 5.31** Adjusting the Chart Size


**Adjusting the** Time series charts offer various options for analyzing the time period in
**granularity** more detail. One option is to use the small chart below the data and adjust
its size, time frame, and zoom level. Another option is to change the data
level and show more granular data. Because our chart should only show
data for each quarter, select **Drill**           - **Date**           - **Month**, as shown in Figure 5.32.


**Figure 5.32** Selecting a Date Hierarchy Level



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-5-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-5-1.png)








**5.3.2  Adding More Charts**


Let’s add another chart to our sample story. This chart will be placed below
the first chart. Click again on the button to add a new chart in the **Insert** section of the top bar.


By default, the chart will be placed below the first one. However, in some **Moving charts**
cases, it may appear somewhere else (e.g., next to the time series chart). You
can easily move charts via drag and drop. Click anywhere on the border of
the newly created chart and keep the left mouse button pressed down. Now,
move the chart to the desired position. As shown in Figure 5.33, the story
automatically shows visual guidelines. These lines allow you to align charts
exactly next to each other.


**Figure 5.33** Moving Charts


Use the builder again to fill in the chart with content. For our example, you
can build the following charts:


- First chart:


  - Chart type: **Bar/Column** (under the **Comparison** group)


 - Accounts: **Revenue**


 - **Dimensions: Supermarket**


- Section chart:


  - Chart type: **Numeric Point** (under the **Indicator** group)


  - Primary values: **Revenue**



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-6-0.png)








**5.3.3  Conditional Formatting**


Now, let’s say want to extend our new chart by adding threshold-based coloring to it. This formatting can be used to change the colors of values or to
show symbols based on the numbers they assume. Viewers can then immediately see if numbers are critical or not. For this feature, we must define
thresholds that determine if a value is critical.


**Creating thresholds** To create rules for conditional formatting, click on the **Conditional Format-**
**ting** icon in **Tools** section of the top menu bar and then choose the **Add**
**Threshold** option. Alternatively, you can open the builder for a chart and
choose the **Create Threshold** option. Create a rule for the numeric point
chart we just created, as shown in Figure 5.34.


**Figure 5.34** Creating Thresholds in the Builder


A new dialog box will open. Choose the **Revenue** measure and assign values
for its conditional formatting, as shown in Figure 5.35. Start entering the
values and click on **Add Range** to add more range options. Define the
thresholds as shown in Table 5.2.


**Figure 5.35** Definition of Thresholds



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-7-0.png)







|Range|Color|Minimum|Maximum|
|---|---|---|---|
|**OK**|Green|≥ 6,000,000|No value|
|**Warning**|Yellow|≥ 3,500,000|< 6,000,000|
|**Critical**|Red|≥ 0|< 3,500,000|



**Table 5.2** Thresholds for Our Example Numeric Point Chart


Now, click on the **Apply** button to save these thresholds, which will be
applied automatically to the chart. The numeric point should now be green.


**5.3.4  Showing Variances**


Next, let’s adjust the chart to show how the actual value compares to the
forecasted value. To add variances to a chart, you can use the builder as
shown in Figure 5.36. Open the **Chart Add-Ons** section and then the **Vari-**
**ance…** option. The variance panel will open in the sidebar on the right,
where you can now configure the comparison.


**Figure 5.36** Adding Variances


You can create the following variance types, as shown in Figure 5.37:


- Between two different measures


- Between two versions of a measure (e.g., actuals versus forecast)


- Between two time periods of a measure (e.g., previous year versus current year)


You also can specify the measure for which a similar variance should be calculated for each measure in the chart. You can also determine display
options to indicate where and how the variance is shown.


Choose the **Revenue** measure for both **COMPARE (A)** and **TO (B)** . Afterwards,
click on **Add Version/Time** and select **Version** . This step will automatically
populate the **Actual** and **Forecast** versions to be compared against. Now,
change the display option to show the variance in percentages instead of
absolute numbers. Click on **OK** to confirm these settings.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-8-0.png)








**Figure 5.37** Creating Variances


The variance will automatically be shown in red if the value negative and
green if positive, as shown in Figure 5.38.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-9-0.png)








**Figure 5.38** Numeric Point Chart with Variance


An alternative way to display variances is to follow International Business **IBCS**
Communication Standards (IBCS), which were developed to establish common design guidelines in reporting for charts and tables. These standards
are fully implemented in SAP Analytics Cloud and can be used throughout
the whole solution.


**International Business Communication Standards**


IBCS provides various recommendations and rules for coloring and designing charts, tables, and reports and uses patterns within charts to make
common information more recognizable and easier to spot. SAP Analytics
Cloud is officially IBCS-certified and supports the standards within its
product out of the box. More information about the IBCS certification can
be found at the following URL: _[http://s-prs.co/v218504](http://s-prs.co/v218504)_ .


The IBCS also includes recommendations on how to compare versions of **Applying IBCS**
measures against each other (e.g., actual versus forecast). With a new example chart, let’s now apply IBCS.


Create a new chart with the following properties:


- **Chart Type** : Bar/column


- **Measure** : Quantity


- **Dimension** : Product


Place the new chart next to the numeric point we created earlier. To activate an IBCS-compliant variance, open the builder for the chart and add a
**Version** dimension to the **Color** selection. Then, click on **Add Version** and
select the **Forecast** version, as shown in Figure 5.39.


**Figure 5.39** Adding Second Version



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-10-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-10-1.png)








If versions are mapped correctly in the model, SAP Analytics Cloud will
automatically assign patterns based on the IBCS, as shown in Figure 5.40. If
you want to change these patterns, use the **Show As** and **Pattern** dropdown
lists in the builder.


**Figure 5.40** IBCS-Compliant Chart


**Examples of International Business Communication Standards-**
**Compliant Charts**


You can find more examples of IBCS-compliant charts in SAP Analytics
Cloud at _[http://s-prs.co/v218505](http://s-prs.co/v218505)_ .


**5.3.5  Other Chart Functionalities**


You can use either the builder or the action bar of a chart to further customize and configure the chart. To show the action bar, simply click on a chart
and then the three dots icon appearing right next to the chart. Alternatively, you can also right-click anywhere in the chart.


**Action bar** To access other chart functionalities, open the action bar, as shown in Figure 5.41.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-11-0.png)








**Figure 5.41** Chart’s Action Bar


You can use the action bar to access various tools and functions that
directly influence the chart, such as the following:


# 1 This option shows all controls and filters that are applied to this chart.


# 2 If a hierarchy is present, it can be drilled down here. Alternatively, you
can toggle between different hierarchies if more than one are available
for a dimension.


# 3 Sorting options can be used to influence the sorting behavior of the
chart. You can use complex sorting functionality to adjust the sorting
order to meet your individual needs.


# 4 This option allows you to activate various ranking features. You display
only the top or bottom _N_ entries of a chart (e.g., top 20 supermarkets by
revenue) for example.


# 5 With this option, you can activate the **Linked Analysis** feature. More
information about **Linked Analysis** can be found in Section 5.7.3.


# 6 This submenu provides various elements that can be added to a chart,
including thresholds, reference lines, and tooltips.


# 7 Use this submenu to show and hide specific elements of a chart like its
title, subtitle, or legend.


# 8 With this option, you can configure the axis settings of a chart.


# 9 If the chart’s title is too long, you can collapse the title with this option.


j The **Export** option allows you to export the data used to render the chart
either as a Microsoft Excel or CSV file.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-12-0.png)








k With this option, you can activate comparisons and variances between
measures in a chart. In optimized mode, it can currently only be accessed
via the builder.


l If a script is used to modify the chart’s behavior, it can be edited here.


m This option is identical to clicking the **Copy** button in the top bar. You
can copy the chart to the clipboard or to a specific page.


n This option opens the formatting sidebar for the chart.


           - To see a chart in detail, you can open the fullscreen view with this button.


p If you want to block all interactions for a chart in view mode, you can
activate this option.


q This option deletes the chart. Alternatively, you can simply select a chart
by clicking on it and press (Delete) or (Backspace).


The context menu may change in look and behavior depending on the
chart type currently in use.


**Reference lines** Now, let’s add a reference line to the chart. Open the action bar and choose
the **More Options**           - **Add**           - **Reference Line** options. Reference lines provide an
immediate comparison of measures in a chart to a reference value. You can
define either a fixed value or dynamic value. Switch the reference line **Type**
to **Dynamic** in the right sidebar. Choose the **Revenue** measure and **Average**
for the **Aggregation** method, as shown in Figure 5.42. Alternatively, you can
choose to use the maximum or minimum value.


**Figure 5.42** Creating Reference Lines



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-13-0.png)








The other settings can be used to modify the label and appearance of the
reference line. Also, a filter can be set to calculate the reference line for specific dimension members only. Leave those settings in their default state
and confirm the creation of the reference line by clicking on **OK** . The result
should match the chart shown in Figure 5.43.


**Figure 5.43** Chart with Reference Line (Average)


In addition, we can add a _tooltip_ to the chart. A tooltip is shown when a user **Tooltip**
hovers the mouse over a data point in a chart. Tooltips can show additional
measures or dimensions.


Use either the builder or the chart action bar to create a new tooltip. Choose
the **More Options** - **Add** - **Tooltip** - **Dimension** options in the action bar of the
first chart we created. This step will add a new entry to the builder in which
you can select the **Tooltip Dimensions** . Click on **Add Dimension** and choose
the **City** dimension, as shown in Figure 5.44.


**Figure 5.44** Adding Tooltip Dimensions


If you now hover your mouse over one of the bars in the chart, you’ll see
a tooltip listing all cities in which this specific store is represented, as
shown in Figure 5.45. Alternatively, you can also show additional measures in a tooltip.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-14-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-14-1.png)








**Figure 5.45** Tooltip for Lion Chain Cities


**Top 5** We described sorting options earlier in Section 5.2.2, but now let’s add a
ranking to the chart. In this example, we only want to see the five strongest
chains by revenue. Select the **Top 5** option from the **Rank** menu of the
action bar, as shown in Figure 5.46.


**Figure 5.46** Selecting Top 5 Option


If you want to customize the rank settings to show the top ten, for example,
select **Top N Options** . You can also show the lowest-performing supermarkets.


**Additional elements** The action bar or the builder provides various other elements that can be
added to charts to extend their insights, which we’ll present briefly.


**Trellis** A _trellis_ can be enabled to show a chart multiple times per dimension for
each member of each dimension. If you base a trellis on a time dimension,
you’ll see multiple charts of the same type, with each chart representing a
specific period, as shown, for example, in Figure 5.47.


The **Error Bar** menu adds a thin line to each data point that can be used to
display potential error values. These error values can be either determined



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-15-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-15-1.png)








by using fixed deviations (e.g., 10% above and below) or by indicating
another measure from the model. Figure 5.48 shows a chart with an error
bar ranging 10% above and below the actual value. The error bar is currently
not supported in optimized mode.


**Figure 5.47** Trellis for Date Dimension


**Figure 5.48** Chart with Error Bar


The **Hyperlink** option can be used to define jumps to other stories or pages. **Hyperlinks**
This option is described in detail in Section 5.7.3. Hyperlinks are also used in
SAP Digital Boardroom (see Chapter 9).


**5.3.6  Defining Colors**


You can also adjust the coloring of a chart and further customize it. The **Color palettes**
builder provides a set of predefined color palettes, as shown in Figure 5.49.
These color palettes are applied when a chart carries more than one dimension or measure to provide optical separation.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-16-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-16-1.png)








**Figure 5.49** Color Palettes


**Customer color** In addition to using the default color palettes, you can also create your own
**palettes** custom color palettes. Click on **+ Create New Palette** to open the color palette. In this dialog box, you can define up to nine custom colors. You can
define each color either by moving your mouse over a color palette or
entering specific color codes (in RGB, HSV, or hex formats). In addition, you
can also use the conditional formatting feature, described in Section 5.3.3,
to define specific colors for individual dimension members.


**5.3.7  Formatting Charts**


The formatting engine of SAP Analytics Cloud is quite detailed and can be
accessed either via the action bar of the chart ( **Edit Styling…** ) or by clicking
the **Brush** icon in the top right of the builder, as shown in Figure 5.50.


**Figure 5.50** Accessing Chart Formatting Options


**Formatting options** The formatting options automatically adjust to the object that you’re formatting. Based on the chart type, you’ll see the following options, as shown
in Figure 5.51:



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-17-0.png)

![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-17-1.png)








- **Generic Properties**
Here, you can rename the ID of the chart and assign it to a CSS class.


- **Quick Menus**
This allows you determine which options are available for viewers in the
chart.


- **Size and Position**
If you want to adjust the size and position of the chart manually, you can
enter the values here.


- **Widget**
You can change the color of the chart background with this option. You
can also activate a partial or full frame around the chart.


- **Actions**
If you’re working on a canvas page, objects can overlap each other. These
buttons allow you to arrange objects and determine which objects are
put in the foreground and background.


- **Boardroom Properties**
These properties are described in detail in Chapter 9. This option is only
available in classic mode.


- **Data Points**
This option fills the data points with a color if desired.


- **Font**
With these properties, you can change the font, text size, color, and text
styles. You can also change these settings for specific elements of the
chart.


- **Number Format**
With these properties, you can change the scale settings and scale format
for all or specific measures. You can also determine how many decimal
places are shown and how signs are shown.


- **Legend**
This option lets you change the placement and alignment of the chart
legend.


- **Labels**
This option allows you to change the direction and truncation of axis
labels. You can also specify whether data labels can overlap each other
and whether their values should be rounded or not.


- **Axis**
You can change the color of the axis line.










**Figure 5.51** Formatting Options


Try out the various formatting options with the chart we created earlier and
observe how the chart changes. Extend this knowledge to other charts
you’ve created and get familiar with the different formatting options for
each chart type.


**Chart titles** You can also edit the chart’s title and its subtitle. Double-click on the title or
subtitle so that the text is selected. Now, you can enter any text you want.



![](temp_conversion_out/main/images/032_5.3 Creating, Editing, and Formatting Charts_032_5.3-Creating,-Editing,-and-Formatting-Charts.pdf-19-0.png)






