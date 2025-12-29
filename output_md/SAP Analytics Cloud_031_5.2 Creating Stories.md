---
tags:
source: 031_5.2 Creating Stories.pdf
title: 031_5.2 Creating Stories
---




![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-0-0.png)









**Figure 5.2** Simplified Story Architecture


**5.2  Creating Stories**


In this section, we’ll present each story functionality step by step. Therefore, we’ll create a story from scratch and extend it throughout the whole
chapter. First, we’ll present the different site types available in a story.


**Optimized and Classic Design Experience**


In 2021, SAP first introduced the optimized story design experience. The
optimized story marked a major change in the evolution of SAP Analytics
Cloud. Due to its new underlying concept, it allows SAP Analytics Cloud to
deliver innovative functionality and better performance.


To protect existing work, SAP currently offers two experiences during story
creation: the optimized design experience and the classic design experience. While not all functionality of the classic story is available in the optimized story, it is equipped with an additional functionality set that is not
available within the classic mode. Therefore, in this chapter, we will primarily focus on the optimized story. If functionalities are only available in
classic mode, they will be marked as such.


**New story** You can create a new story either in the folder view or via the main menu.
Open the main menu and choose **Stories**     - **Create**, which will launch the
starting page of a story, as shown in Figure 5.3.


To initiate a story, multiple options are available, such as the following:


      - If available, you can use predefined templates. Templates can be defined
to contain design guidelines as well as to contain multiple page layouts.
Templates ensure that color and design guidelines can be enforced. We’ll
present templates in detail in Section 5.11.2.










- Besides running smart discovery (more details can be found in Chapter

7, Section 7.2.1), you can also create your first page by directly choosing a
page type. You can choose from responsive, canvas, and grid pages. Then,
you can immediately add charts, tables, pictures, or other elements.


**Figure 5.3** Creating New Stories


We’ll describe these elements in detail in the following sections and provide examples of how to use them.


**5.2.1  Pages**


Stories can consist of one or more pages that can be filled with content. A
story can contain multiple page types. Before creating your first story, you
become familiar with each page type.


In general, page types can be described in the following ways: **Page types**


- **Canvas pages**
Canvas pages allow the freeform creation of pages that can contain
charts, tables, or other elements. You’re basically working on a virtual
canvas, which can be filled with any content. You can also overlap charts
or mix different graphical elements together.


- **Responsive pages**
When using responsive pages, you’re giving up some degree of freedom.
For example, you won’t be able to overlap charts anymore, and you must
follow some arrangement rules, which are enforced automatically. However, responsive pages can be opened on all kinds of devices (mobile
phone, laptop, 4K TV, etc.) and automatically adjust themselves.


- **Grid pages**
The grid page is based on a tabular grid and only supports tables. This
page type is mainly used in planning workflows because a grid can be
used, for example, for side calculations next to tables. The grid page is
only available in the classic story design experience.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-1-0.png)








**Canvas pages** The canvas page behaves like a virtual canvas and is useful in most scenarios since it allows the free placement of all elements (charts, tables, pictures,
texts, widgets, etc.) and can be adjusted in detail. Figure 5.4 shows a simple
example of a canvas page.


**Figure 5.4** Simple Canvas Page


A canvas page is suitable for most scenarios: Its creation follows an intuitive concept, and its flexibility allows for broad usage across multiple scenarios. Also, a canvas page can be freely formatted and adjusted in size so
that reports can be optimized and exported for printing.


Canvas pages are not very flexible, however, and therefore can only be
accessed in browsers on desktop PCs. If you want to be able to view your
stories on multiple device types, a canvas page may not suit your use case.


**Responsive pages** If your use case scenario explicitly requires that your story be accessed on
different device types, like smartphones or big screens, you should consider using responsive pages. In general, the handling is quite similar to
canvas pages, but the content is spread across multiple _lanes_ . Charts,
tables, and other elements are structured into these lanes. A lane can
contain multiple elements, which are either next to or below/above each
other. However, elements cannot overlap. Figure 5.5 shows a responsive
page with two lanes.


Once a story is opened on a device, SAP Analytics Cloud will automatically
adjust it to fit the screen size properly. The screen width determines in that
moment if the lane ordering is respected or is changed. If necessary, even
the layout within lanes is displayed differently.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-2-0.png)








**Figure 5.5** Responsive Page with Two Lanes


To see how a story looks on each device, SAP Analytics Cloud offers a built- **Device preview**
in device preview to simulate different device types. Figure 5.6 shows an
example of a story previewed for a smartphone. Besides changing the element order, SAP Analytics Cloud also adjusts text sizes and some other elements based on the device.


**Figure 5.6** Device Preview



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-3-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-3-1.png)








Instructions on how to build a story with responsive pages are presented in
Section 5.10.2.


**Grid pages** Both canvas and responsive pages support displaying tables to analyze
data. However, the table is used as a chart and can be surrounded by other
elements, like charts or texts. If you need a full tabular view that allows, for
example, additional cell operations or side calculations, you should consider using grid pages.


This page type supports displaying multiple tables below each other and
referencing single cells in formulas. Especially in planning scenarios, this
capability can be quite helpful to create calculations on the side.


The grid page solely supports displaying tables and is not responsive, so it
doesn’t adjust itself automatically to different device types. Therefore, grid
pages aren’t used often in BI scenarios. More details on this page type can
be found in Chapter 6, Section 6.3. Figure 5.7 shows a grid page with a table.


**Figure 5.7** Grid Page


**5.2.2  Classic Data Exploration and Your First Charts**


Now that we’ve discussed the different page types, it’s time for your first
data analysis. We’ll use the _data exploration mode_ of a story. Our example
story will be completely built on canvas pages. Instructions for responsive
page design can be found in Section 5.10.2.


Data exploration mode is only available in classic mode. Since this mode is no
longer recommended by SAP, the rest of the chapter will be based on the optimized mode. To launch the story in optimized mode, head to Section 5.2.3.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-4-0.png)








To start the data exploration mode, open the **Stories** section of the main
menu and select any page type (e.g., **Canvas** ). Once asked, make sure to
choose **Classic Design Experience** . Then, click on **Add data** on the left side of
the story launch screen, as shown in Figure 5.8.


**Figure 5.8** Launching Data Exploration Mode


Next, you’ll choose the data source you want to access. Three options are **Selecting a**
available, as shown in Figure 5.9: **data source**








**Figure 5.9** Selecting Data Sources



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-5-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-5-1.png)








Because we already created our data model in Chapter 4, select the **Data**
**from an existing dataset or model** button 3. Now, open the **Sales Data**
model. You can either navigate to the subfolder or use the search function
in the top right of the dialog box. Your screen should now match the screen
shown in Figure 5.10.


**Figure 5.10** Initial View in Data Exploration Mode


**Visualizing data** The data exploration mode offers a quick overview of all measures, dimensions, and data in the model. You can also create your first chart in just a
few clicks. To see all dimensions, click on the **+** button next to the **Show**
**Dimensions** text. Then, select the **Show All** option to add all dimensions at
once, as shown in Figure 5.11.


**Figure 5.11** Showing All Dimensions



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-6-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-6-1.png)








To create your first chart, simply click on the desired dimensions and fea- **Creating a chart**
tures. The first chart should show the revenue for each chain. Therefore,
click on the **Revenue** measure and the header of the **Supermarket** column,
as shown in Figure 5.12.


**Figure 5.12** Creating Your First Chart


By selecting an entry in one of the dimension columns, you can add filters **Filters**
to the chart. Click, for example, on **Ludo** (in the **Supermarket** column) to see
how the filter is applied. However, we want to use this chart as an overview
chart, so click again on **Ludo** to remove the filter. More information about
filters is presented in Section 5.7.1.


The chart type selection in data exploration mode is not random. SAP Ana- **Changing the**
lytics Cloud recommends a chart type based on the selected data. If you **chart type**
want to change the chart type, you can explicitly select another one. The
chart type can be adjusted at any point in time.


To change the chart type, click on the text showing the current type, which
is displayed in the top right of the chart, as shown in Figure 5.13. You can
select another chart type. However, the bar chart is well suited for our data,
so don’t change the chart type for this example.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-7-0.png)








**Figure 5.13** Selecting Chart Types


**Display options** Finally, you can adjust the display options for the chart. Because the revenue analysis should show which chain had the highest revenue, sort the
chart by revenue in descending order, as shown in Figure 5.14.


In general, all display and sorting options are still available later when editing the chart in the story. Detailed descriptions of these options can be
found in Section 5.3.


**Figure 5.14** Sorting Charts


**Copying to a story** To continue using the chart you just created, the data exploration mode
allows you to copy the chart into the story. Click the **Copy** button in
the top right and select the **Copy to New Canvas Page** option, as shown in
Figure 5.15. Alternatively, you can just copy the chart without determining
a target. The chart will then be stored in your clipboard, from which you can
paste it later into the story. You can also choose to copy the chart to a new
responsive page.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-8-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-8-1.png)








**Figure 5.15** Copying Charts


The chart will automatically be pasted into the top-left corner of the new
page, as shown in Figure 5.16. After copying the chart, you can still fully edit
and modify it.


**Figure 5.16** First Story Chart


Data exploration mode can be opened as often as desired. To access data **Accessing data**
exploration mode from a story, click on the **Data** button in the top left. **exploration mode**


**5.2.3  Launch a New Story**


To launch a new story, open the **Stories** section in the main menu and
choose the page type **Canvas** . Alternatively, you can launch the story creation by clicking the + symbol in the files overview.


Then choose **Optimized Design Experience** (see Figure 5.17). Afterwards, an
empty story will be launched.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-9-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-9-1.png)








**Figure 5.17** Choosing the Design Experience


In the following sections, we will only use the optimized design experience.
However, some functionality is presented which is only supported in the
classic design experience. The functionality will be marked as such and can
be applied by creating a second story in the classic design mode.


**5.2.4  Story Interface**


Now that you’ve created the first page of your story, you’ll see the full story
interface, as shown in Figure 5.18. At this stage, you can access all functionalities and tools of a story.


**Main area** In general, as shown in Figure 5.18, the story interface can be separated into
four areas:




# 2 The buttons in the top right allow you to switch between the **Edit** mode
and **View** mode of the story.


# 3 The left sidebar contains an overview of all widgets that can be added to
the story. You can simply drag the elements from this list to the canvas.


# 4 The charting area contains the actual content of the story. Depending on
the page type, this area may look different. More information about page
types can be found in Section 5.2.1.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-10-0.png)








**Figure 5.18** Story Interface


The top bar is separated into multiple sections, which are used to group **Top bar**
functionalities that belong together. We’ll list these sections ahead and
explain them in the following sections.


The **File** section provides access to some general functionalities, as shown **File section**
in Figure 5.19:


# 1 With the **Save** icon, not only can you save a story, but you can also create
templates.


# 2 With the **Export** icon, you can export the story as a PDF file. This button
is only available in view mode.


# 3 The **Sharing** button offers access to the sharing interface. In view mode,
you can also schedule publications here to be regularly created.


# 4 The wrench icon provides access to story details, preferences, and query
settings for live data connections.


**Figure 5.19** File Section


Next, the **Edit** section contains elements which are helpful in edit mode, as **Edit section**
shown in Figure 5.20:


# 1 By clicking on this button, you can jump one step back and revert the last
change.




# 3 With this option, you can refresh the data from the data source and configure automatic and regular refreshes.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-11-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-11-1.png)








# 4 The **Copy** icon can be used to copy an object to the clipboard or directly
to another page. It also can be used to paste content.


**Figure 5.20** Edit Section


**Insert section** The **Insert** section contains all buttons that are used to add new elements to
a story, as shown in Figure 5.21:








# 4 Further elements: **Panel**, **Geo Map**, **Image**, **Shape**, **Text**, **RSS Reader**, **Web**
**Page**, **Value Driver Tree**, **Data Action Trigger**, **Multi Action Trigger**, **BPC**
**Planning Sequence Trigger**, **Custom Widgets**, **Composites**, **R Visualization**,
and **Symbol** .


**Figure 5.21** Insert Section


**Tools section** The **Tools** section contains several workflows that are only necessary in
some workflows, as shown in Figure 5.22:


# 1 By clicking on this icon, you can add additional data models and sources
to the story.


# 2 If the data model contains any prompts, they can be accessed with this
option.


# 3 Linked dimensions can be used to link two data models which carry the
same column to each other.


# 4 Chart scaling makes it possible to set fixed scales for specific measures.


# 5 Conditional formatting can be used to define thresholds which define
how measures are colored based on their value.


# 6 The formula bar can be used in tables and the grid pages to fill specific cells.


In addition, you can access interfaces for value lock management 7, marking and unmarking cells as read-only 8, and showing cell references and
formulas in cells 9. However, these tools are mainly used in planning scenarios.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-12-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-12-1.png)








Last, the linked widgets diagram j shows which widgets are in a relationship to each other. Smart discovery k can be used to automatically generate complete stories. It's only available in classic mode.


**Figure 5.22** Tools Section


Finally, the **Format** and **View** sections allow you to apply layouts or toggle **Format & View**
between different views, as shown in Figure 5.23:


# 1 The **Layouts** icon opens the layout sidebar in which you can select
among predefined layouts and apply them to your story.


# 2 The **Theme** icon allows you to toggle between various story themes.


# 3 The **CSS** icon provides access to manipulate the story appearance by
inserting CSS code. This requires deeper knowledge.


# 4 This icon opens the left sidebar from where you can access all available
widgets that can be added to the story.


# 5 By clicking on this icon, the right sidebar can be shown or hidden. It is
used to modify elements of the story.


# 6 With this icon, you can configure all story filters and prompts that are
used in the story.


# 7 This icon toggles the advanced mode which enables more complex functionality. This mode will be presented in Chapter 8.


# 8 By turning off and on this setting, the device preview bar in the bottom
can shown or hidden.


# 9 This option allows you to turn off and on the comment mode.



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-13-0.png)








**Figure 5.23** Format and View Section


**More buttons** Based on your screen resolution, SAP Analytics Cloud may move some elements into a list at the end of the top bar.


In the top right of the action bar, you’ll find additional buttons, as shown in
Figure 5.24, that allow you to toggle between **Edit** and **View** mode. One of
the key concepts of SAP Analytics Cloud is the intuitive user interface (UI).
The **View** button allows story creators at any point in time to preview their
current story from a story viewer’s perspective.


**Figure 5.24** More Buttons


**Saving a story** In general, you can always save a story to continue working on it later. Click
on the **Save** button in the top bar and choose the **Save** option. Store the
story in the **Sales Data** subfolder we created earlier and name it, as shown
in Figure 5.25.


**Figure 5.25** Saving Stories



![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-14-0.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-14-1.png)

![](temp_conversion_out/main/images/031_5.2 Creating Stories_031_5.2-Creating-Stories.pdf-14-2.png)






