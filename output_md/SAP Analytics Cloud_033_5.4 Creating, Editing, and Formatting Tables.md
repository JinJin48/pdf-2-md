---
tags:
source: 033_5.4 Creating, Editing, and Formatting Tables.pdf
title: 033_5.4 Creating, Editing, and Formatting Tables
---



**5.3.8  Hierarchies**


SAP Analytics Cloud supports the creation and display of hierarchies from
selected data sources (both live connections and import connections). If the
chart contains a hierarchical dimension, you can expand this dimension, as
shown in Figure 5.52 by either clicking on the **Hierarchy** icon in the action
bar or right-clicking on a data point 1 and then selecting the **Drill Down**
option 2. When drilling down into a hierarchy, the chart will automatically
only show the children of the previously selected node. If you want to display all children of all nodes, select the **Expand** option 3.


**Figure 5.52** Drilling Down into Hierarchies


**5.4  Creating, Editing, and Formatting Tables**


In addition to charts, tables are another commonly used element in stories.
If a table is added to a canvas or responsive page, it will be treated like a
chart but still support the full table functionality. It can be placed and
resized freely within the page.


Create a new page by hovering your mouse next to **Page 1** in the page bar. A **Creating a**
**+** button will appear. Click on it and select **Canvas** . Then, click on the **Table** **new table**
button in the **Insert** section of the top bar. The table will initially show a
small amount of data, as shown in Figure 5.53. If you create a table based on



![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-0-0.png)

![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-0-1.png)








a live data source that already provides a table layout, for instance, a query
layout in an SAP Business Warehouse (SAP BW) query, that table will be
automatically shown on this canvas page.


**Figure 5.53** A New Table


**Builder** As with charts, tables are also edited in the builder (see Section 5.3.1). Use the
builder to add the **Product** and **Supermarket** dimensions to the rows in the
table. Then, sort the dimensions so that supermarkets are shown first. To
change the dimension order, hover over the four dots shown to the left of
the dimension in the builder, as shown in Figure 5.54. Then, drag and drop
the dimension to the desired position.


**Figure 5.54** Dragging Dimensions in the Builder


**Measures** Let’s say we also want to see other measures in this table. Remove the **Unit**
**price** measure and show the **Revenue**, **Quantity**, and **Fixed Revenue Forecast**
measures. Click on the filter icon shown to the right of the **Account** dimension, as shown in Figure 5.55.



![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-1-0.png)

![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-1-1.png)








**Figure 5.55** Account Dimension in the Builder


Now, choose the measures, as shown in Figure 5.56. To display hierarchies
(depending on their availability) or the IDs of each measure, click on the up
arrow icon, next to the magnifying glass.


**Figure 5.56** Selecting Measures


Now, extend the size of the table so that it shows enough data, as shown, for
example, in Figure 5.57. Like charts, tables also have an action bar that you
can access either to the right of the chart or by right-clicking the table (see
Section 5.3.5). The following actions are available in tables only:


- **Drill**
If a hierarchy is available in a table, you can drill down into it.


- **Freeze**
You can freeze the table up to a specific row or column so that those rows
or columns are always displayed.


- **Swap Axis**
This functionality swaps the row and column axes.


- **Resize Table to Fit Content**
This functionality automatically resizes the table to show the current
content.



![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-2-0.png)

![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-2-1.png)








          - **Mass Data Entry**
If a planning model is shown in the table and the mass data entry functionality is activated, users can enter multiple data points before the
data is changed.


**Figure 5.57** Extended Table


By right-clicking on a specific data cell, you can call data-related functionalities.


**Formatting and IBCS** The formatting of tables is quite similar to charts. Special settings, however,
are grouped under **Table Properties** . With these options, you can select a
table template and change how thresholds are shown. If you choose the
**Report-Styling** template, as shown in Figure 5.58, for example, the table will
automatically comply with IBCS, as described in Section 5.3.4.


You can also format individual cells or rows and columns of the table. Click
on the specific object you want to format. The sidebar will automatically
adjust and show you all available options. Close the formatting panel by
clicking on the **Designer** button or return to the builder to continue editing
the table.


**In-cell charts** You can also add further elements to the table. First, let’s improve how single cell values are compared by adding a chart to each row. Right-click on
the header of the **Revenue** column and activate **In-Cell Chart**, as shown in
Figure 5.59.



![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-3-0.png)








**Figure 5.58** Selecting a Table Template


**Figure 5.59** Activating In-Cell Charts


Now, in-cell charts will be automatically generated and displayed. Figure
## 5.60 shows the in-cell charts we just created in our table. By using the
builder, you can configure these charts as well.


**Figure 5.60** In-Cell Charts in Table


By using the action bar, you can add additional elements to the table or per- **Additional elements**
form additional configurations. You can define thresholds or sorting options
and even insert new rows and columns. In addition, SAP Analytics Cloud
delivers predefined calculations that you can apply to a table. Right-click on
the header of the **Revenue** column and select **Add client calculation** - **Rank**
**Number** - **Single**, as shown in Figure 5.61. A new column will be added that



![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-4-0.png)

![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-4-1.png)

![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-4-2.png)








assigns a rank to each row. If you select the **Single** option, the ranks are calculated for each combination of dimension member separately. If you select
**Repeating**, the calculation will be repeated for each occurrence of the dimension member.


**Figure 5.61** Calculating Ranks


**Hierarchies** Tables also support displaying hierarchies. To expand these hierarchies,
either select the **Hierarchy** option in the action bar or click on one of the
arrows next to each supermarket chain or product group, as shown in Figure 5.62. An arrow indicates that the entry has children.


**Figure 5.62** Hierarchies Displayed in a Table



![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-5-0.png)

![](temp_conversion_out/main/images/033_5.4 Creating, Editing, and Formatting Tables_033_5.4-Creating,-Editing,-and-Formatting-Tables.pdf-5-1.png)






