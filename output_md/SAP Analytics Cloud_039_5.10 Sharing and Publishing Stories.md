---
tags:
source: 039_5.10 Sharing and Publishing Stories.pdf
title: 039_5.10 Sharing and Publishing Stories
---



- **Page 3: Detailed Analysis**


  - Two input controls (filters) for the **Product** and **Supermarket** dimensions.


  - A date filter on the month level.


  - A table with the **Quantity** and **Revenue** measures and the **City**, **Super-**
**market**, and **Product** dimensions.


In addition, we’ve defined the **Revenue Forecast** (variable) calculated measure, which multiplies the **Revenue** measure by an input control created
within the formula editor. The input control is based on a static list of values and ranges from 0.5 to 2 with intervals of 0.1.


**5.10  Sharing and Publishing Stories**


Once you’ve completed a story, now, we’re ready share and publish it. You
can either use the folder structure described in Chapter 3, Section 3.3.5, or
publish stories outside of SAP Analytics Cloud. In this section, we’ll first discuss sharing and publishing stories in general and then focus on publishing
to mobile devices. (Refer to Section 5.2.4 to recall how stories are saved.)


**5.10.1  Sharing, Exporting, and Publishing Stories**


To share a story stored in your private folder or to a folder where you want **Sharing stories**
to assign individual access rights, use the sharing engine of the story. Click
on the **Share** button in the action bar of the story and select **Share…**, as
shown in Figure 5.107.


**Figure 5.107** Sharing Stories


The sharing dialog box will open, as shown in Figure 5.108, where you’ll find
the story URL, which you can use to directly access the story. The URL can
also be customized in this dialog box. You can also add users or teams and
directly assign them story rights. In addition, you can turn off email notifications for newly added users and determine if the global bookmark should
be applied by default (see Section 5.11.5). Users or teams must be added in
this dialog box to get access to the story. Simply having the link is not sufficient for access.



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-0-0.png)








**Figure 5.108** Sharing Interface


**Embedding Stories**


In general, stories built in SAP Analytics Cloud can also be embedded into
external websites. With embedding, pages can also be parameterized to
set filters or prompt values while loading the page. More information on
how to embed stories and which requirements must be met can be found
at _[http://s-prs.co/v502619](http://s-prs.co/v502619)_ .


**Exports** If your audience is not using SAP Analytics Cloud or you want to print out the
report, you can also export the story as a PDF file. In classic mode, you can
also export to a PowerPoint file or to Google Slides. However, the report will
not be interactive in those formats. Click on **Export…** in the **Save** menu of the
story, as shown in Figure 5.109. This option is only available in view mode.


**Figure 5.109** Exporting Stories


**Export options** A dialog box will open where you can define the export settings, as shown
in Figure 5.110. Besides setting the export format, you can indicate whether



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-1-0.png)

![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-1-1.png)








all or only selected pages should be exported. If you activate background
exporting, you don’t have to wait until the export is completed. The appendix, which is optional, contains a list of all filters applied in the story and the
URL to access the story.


**Figure 5.110** Export Options


If the story contains a story filter, you can also perform batched exports. **Batch exporting**
This option will use the selected story filter to create an export for each
dimension member. If you use a country dimension, for example, the story
can be exported for each country separately.


Sharing or exporting a story is done manually, but you can also automate **Scheduled**
the exporting process. Story export scheduling can be accessed in a story **publications**
via the **Files** menu ( **Schedule Publication…** ) in view mode. Once selected, a
dialog box lets you create one-time or recurring schedules, as shown in Figure 5.111. The story exports can be distributed as links or as PDFs or PowerPoint files via email to a specified audience.



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-2-0.png)








**Figure 5.111** Scheduling Publication


In addition, the publication process can be adjusted to apply individual filters and control authorizations.


Since the number of publications per hour is limited by SAP, users can click
on **Check Availability** to see if scheduling slots are free within their desired
timeframes.



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-3-0.png)








The sharing menu also includes the **Publish to Catalog…** option. This dialog **Catalog**
box can be used to create an analytics catalog for SAP Analytics Cloud asset
for this story, as shown in Figure 5.112. You can control who will see this card
by assigning teams. The published card will be previewed and can be customized by clicking on **Edit details…** . where you can modify the title and
description. Screenshots, pictures, or even more links to other stories or
assets can be added as well. More information about the analytics catalog
can be found in Chapter 10, Section 10.3.


**Figure 5.112** Publishing Stories to Catalogs


**5.10.2  Publishing to Mobile Devices**


SAP Analytics Cloud offers a mobile app as an alternative to the desktop **Mobile app**
version of its interface. This app is compatible with smartphones and tablets and can be installed on iOS and Android devices. You can download the
app either in Google Play (for Android) or the App Store (for iOS).


To make a story accessible on a mobile device, the story must contain **Requirements**
responsive pages. In general, a responsive page is quite similar to a canvas
page. However, responsive pages use a lane concept to group and arrange
content; the lanes automatically adjust themselves to the mobile device
screen. More information about responsive pages can be found in Section
5.2.1. Now, let’s create a story based on responsive pages, which we’ll also
need for Chapter 9 when we create a digital boardroom.



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-4-0.png)








**Converting stories** To quickly convert an existing story based on canvas pages into a mobilefriendly story, you can create new responsive pages in your story. You can
then either recreate the charts or use copy and paste to copy existing charts
to it.


To select multiple objects at once, hold the (Ctrl) key down while clicking
on objects. Then, copy and paste these objects to the responsive page and
rearrange them as needed.


Use the device preview at the bottom of the story to simulate what the
story looks like on a mobile device, then save the story. The mobile app will
automatically show all stories that contain responsive pages and are shared
with you.


**Example story** We’ll create a story that contains responsive pages only. These pages provide less freedom when it comes to arranging elements. We’ll use the Sales
Data model created in Chapter 4, Section 4.3 and Section 4.5.


**Lanes** In general, you can add the same elements to a responsive page as you can
on a canvas page. The story interface is almost identical (Section 5.2.4). The
lane concept helps group charts, tables, and other elements and lets you
choose which charts should be shown together if possible. Lanes can differ
in height and width and are not limited in quantity. They can be placed to
the left, to the right, on top of, and below each other.


**Formatting lanes** When you right-click on the header of a lane (the top strip with four dots in
the middle), the lane’s context menu is shown, as shown in Figure 5.113.
With this menu, you can add new lanes, copy a lane, or remove a lane.


**Figure 5.113** Responsive Page with Three Lanes


You can adjust a lane’s size by clicking on its border and holding the left
mouse button down while dragging. SAP Analytics Cloud will automatically
show a grid to visually support aligning lanes, as shown in Figure 5.114. This
grid is also shown when you move individual objects on the page.


**Responsive page** Let’s create a new story and add a responsive page to it. To start, the story
contains two lanes. However, we want three lanes, so we’ll add a third lane



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-5-0.png)








right next to the second lane by clicking on the lane header and selecting
**Add Lane** - **Add Lane to Right**, as shown earlier in Figure 5.113.


**Figure 5.114** Grid to Adjust Lanes


Rename the title of the first lane to “Overview.” Create the following charts, **First lane**
referring to the screen shown in Figure 5.115 to verify your progress:


- A numeric point chart for the **Revenue** measure. Add a variance for the
version dimension.


- A numeric point chart for the **Quantity** measure.


- A bar/column chart for the **Quantity** measure and the **Product** dimension.


**Figure 5.115** First Lane



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-6-0.png)

![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-6-1.png)








**Second lane** Rename the title of the second lane to “Time Series.” Create the following
charts and refer to the screen shown in Figure 5.116 to verify your progress:


          - A waterfall chart for the **Revenue** measure and the **Date** dimension. You
may need to drill into the date hierarchy.


          - A time series chart for the **Quantity** measure and the **Date** dimension.


**Figure 5.116** Second Lane


**Third lane** Change the title of the third lane to “Geo map.” Add a geo map and refer to
the screen shown in Figure 5.117 as a template. Add a bubble layer showing
the **Stores** dimension. Use the **Revenue** measure for the bubble color and
**Quantity** for the bubble size.


Rename the whole page to “Overview.” Validate your progress against the
_Checkpoint 8 – Section 5.10.2.pdf_ file from the demo data package.


**Second page** Now, create a second responsive page with two lanes. Rename the page to
“Detail.”


Call the first lane “Tabular Analysis” and add the following elements:


          - Three input controls (filters) for the following dimensions (always add all
elements):



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-7-0.png)








 - **Product**


 - **Supermarket**


 - **Version**


- A table with the **Revenue** measure and **Quantity** as well as the **City**, **Super-**
**market**, and **Product** dimensions.


- Enable the explorer for the table and include all dimensions and measures.


**Figure 5.117** Third Lane


Rename the title of the second lane to “Dynamic Analysis” and add the following elements to it:


- A new bar/column chart that contains a dimension and measure input
control.


- The measure input control that includes the **Quantity, Unit Price**, and
**Revenue** measures.


- A dimension input control that includes the **Date**, **Product**, **Street**, and
**Supermarket** dimensions.


Validate your progress against the _Checkpoint 9 – Section 5.10.2.pdf_ file from
the demo data package.



![](temp_conversion_out/main/images/039_5.10 Sharing and Publishing Stories_039_5.10-Sharing-and-Publishing-Stories.pdf-8-0.png)






