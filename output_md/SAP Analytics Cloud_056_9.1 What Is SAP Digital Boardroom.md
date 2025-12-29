---
tags:
source: 056_9.1 What Is SAP Digital Boardroom.pdf
title: 056_9.1 What Is SAP Digital Boardroom
---



**9.1  What Is SAP Digital Boardroom?**


**Boardrooms** SAP Digital Boardroom is integrated into SAP Analytics Cloud as an add-on
and extends it by adding another presentation layer. This layer enables you
to combine multiple stories or multiples pages from stories into a single
presentation. These presentations are called _boardrooms_ and must be created manually. In general, boardrooms are designed to be viewed on big
screens or displays that provide touch-based input. These devices must be
connected to computers and pass touch inputs from the screen to the computer.


**Boardroom pages** Figure 9.1 shows a small excerpt of a boardroom developed by SAP for
demonstration purposes. The demo scenario shows a dashboard used by a
city to centrally monitor the current state of affairs and evaluate potential
situations.


**Figure 9.1** Boardroom Overview Page


The idea of the boardroom is to consolidate stories from multiple areas of a
company (or in this case a public authority) into a holistic view. For this reason, boardrooms are usually designed to launch with an overview page that
shows the current situation. This overview provides a quick summary and
helps viewers evaluate the overall situation within a few seconds. Figure 9.2
shows an excerpt of an overview page.


**Responsive pages** All pages in the boardroom (including the overview page) are created
within stories in SAP Analytics Cloud and are then consolidated in a dedicated environment. SAP recommends using responsive pages because they
automatically adjust themselves to different display sizes. Nevertheless,
SAP Digital Boardroom also supports canvas and grid pages. However,



![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-0-0.png)








using these kinds of pages may result in unexpected display behaviors on
big screens and/or make the boardroom not accessible on mobile devices.


**Figure 9.2** Excerpt from an Overview Page


A boardroom can be shown on multiple displays simultaneously. During **Multiple screens**
boardroom design, you can explicitly specify which content is shown on
which screen. No limitation exists on the number of screens. Figure 9.3
shows a picture from a product brochure for SAP Digital Boardroom
demonstrating what a typical boardroom setup with multiple screens
might look like.


**Figure 9.3** Advertisement for SAP Digital Boardroom


If you’re using fewer screens than the boardroom design was initially desig- **Navigation**
nated for, you can still access the boardroom. In this case, all pages are
shown at the top of the boardroom, and you can use swipe interactions to
move among the pages. You can also click on each page’s title to access it



![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-1-0.png)

![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-1-1.png)








directly. Navigation buttons in the bottom left are also available, as shown
in Figure 9.4.


**Figure 9.4** Sample Boardroom with Multiple Pages


This navigation method is especially suitable for boardrooms shown on
single large screens on which only one page is shown at a time. You can still
design the boardroom to show multiple pages so that you can access them
faster.


**Jumps** However, more ways exist for navigating within a boardroom. The most
important functionality is the _jump_, with which you can jump from one
page in the boardroom to any other page and optionally apply filters. Jumps
must be configured in the boardroom design up front, which ensures that
jumps are only available when desired by the boardroom creator.


Jumps are defined on the chart, table, or widget level so that a clear relationship can be defined. Especially when using overview pages, jumps can be
immensely helpful. Overview pages can contain charts for each section of
the boardroom and provide initial insights. If the viewer then wants to



![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-2-0.png)








access a detailed view, the user can directly jump from each chart to its
related section.


Most of the action in the boardroom is performed within the context **Context menu**
menu, which can be opened with a long press on a chart or any other element in the boardroom and provides various ways to interact with the
boardroom, as shown in Figure 9.5.


**Figure 9.5** Boardroom Context Menu


The context menu provides access to the following functionalities:


- The boardroom content structure can be opened by clicking on **Dash-**
**board** .


- All display settings can be changed under **Preferences** .


- The boardroom can be searched through by clicking on the **Search** button.


- If the context menu is opened for a specific chart of a data point in a
chart or table, the **Filter** button can be used to set this value as a filter.


- If a jump is defined for a specific widget, this jump will be listed behind
the **Jump To…** button.


- If the story designer activated chart actions for a specific chart or table,
these actions can be opened by clicking on **Chart Actions** .


- The **Explorer** can also be used in the boardroom. More details about this
tool can be found in Chapter 5, Section 5.7.3.


- If the context menu is open for a value driver tree, the **VDT** button will
provide additional interactions.


Another navigation method in the boardroom is the **Tree Structure**, which **Tree structure**
contains a table of contents of all pages in the boardroom. The **Tree Struc-**
**ture** can be shown and hidden anywhere in the boardroom and provides
direct access to all sections, as shown in Figure 9.6. If some of the boardroom pages are used often or must be promoted, they can be highlighted
accordingly, and then, these pages will show up in the **Featured Topics** list.



![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-3-0.png)








**Figure 9.6** Boardroom Table of Contents


**Boardroom design** The boardroom is designed in a dedicated environment, as shown in Figure
9.7. In this interface, all sections of the boardroom are defined and filled in
with pages from different stories. Jumps are defined in this interface as well.


In edit mode, you can graphically view all relations between the sections of
a boardroom. You can extend these sections or add new sections to a boardroom here as well.


**Figure 9.7** Boardroom in Edit Mode



![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-4-0.png)

![](temp_conversion_out/main/images/056_9.1 What Is SAP Digital Boardroom_056_9.1-What-Is-SAP-Digital-Boardroom.pdf-4-1.png)






