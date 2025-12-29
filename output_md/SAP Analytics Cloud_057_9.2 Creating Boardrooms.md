---
tags:
source: 057_9.2 Creating Boardrooms.pdf
title: 057_9.2 Creating Boardrooms
---



**9.2  Creating Boardrooms**


In this section, we’ll create some simple example boardrooms. These examples are designed to demonstrate all the important functionalities of SAP
Digital Boardroom.


First, you’ll learn about the differences between the two boardroom types:
_agenda_ and _dashboard_ . Then, we’ll create one boardroom of each type.


**9.2.1  Boardroom Types**


When creating a new boardroom, you’ll choose either the **Agenda** type or
the **Dashboard** type, as shown in Figure 9.8. Both types allow you to combine pages from multiple stories into one presentation. However, these
options are built to meet different use cases.


**Figure 9.8** Boardroom Type Selection


The agenda type follows a designated order of topics and is suitable for **Agenda**
meetings that are structured. The discussion of business activities is set up
in a defined order.


This boardroom type consists of agenda items, which can consolidate multiple subtopics into one meeting point. Each subtopic can be filled with one
or multiple pages from one or multiple stories. Figure 9.9 shows the structure of an agenda in boardroom edit mode.


The dashboard type, however, doesn’t follow a chronological order and **Dashboard**
allows you to create boardrooms in which different subtopics can be linked
to each other. No dedicated order is followed when opening this kind of
boardroom. Dashboards rely on content relations, which make them flexible for boardroom viewers, as shown in Figure 9.10.


Seeing all relations that are defined in a dashboard immediately may not be
easy. Therefore, you should carefully analyze the contents while designing
the boardroom and creating links between them.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-0-0.png)








**Ambiguous** Dashboards also allow you to create _ambiguous relations_ . While an agenda
**relations** defines a fixed order of topics, sections in the dashboard can be connected
to each other individually and even be connected to multiple other sections simultaneously. Sections in dashboards are called _topics_, which are
displayed as boxes, as shown in Figure 9.10. Each topic can contain one or
more pages, which are spread across the available displays attached to the
presentation device on which the boardroom is opened. If the hardware
setup has fewer screens than the boardroom is designed for, navigation elements will be made available, as shown earlier in Figure 9.4. Within each
topic, jumps can be defined for single charts, tables, or widgets, which again
lead to other topics.


**Figure 9.9** Agenda Structure



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-1-0.png)








**Figure 9.10** Dashboard Structure


**Agenda or Dashboard?**


If you don’t know which boardroom type is right for you, verify your use
case first by asking the following questions:


 - If the boardroom is built to support a meeting that usually follows the
same defined order of topics, choose an agenda.


 - If the boardroom is built for exploring data and answering questions
that change from meeting to meeting, a dashboard will provide the
flexibility you need.


**9.2.2  Using Charts in a Boardroom**


Because SAP Digital Boardroom doesn’t provide any dedicated environment to create stories, all charts, tables, and other elements are created
within the story environment of SAP Analytics Cloud. A story provides a lot
of functionality that can also be used in SAP Digital Boardroom. Story functionality is almost completely documented in Chapter 5 and thus won’t be
described again in this chapter. However, in this section, we’ll provide a
quick overview of some story functionalities that are especially relevant for
boardrooms.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-2-0.png)








**Boardroom** Within a story, each chart can be configured to provide additional function**properties** alities in the boardroom view. Therefore, the formatting sidebar for each
chart contains a **Boardroom Properties** section, as shown in Figure 9.11. In
these settings, you can specify, for each chart or table, whether the viewer is
allowed to turn on sorting, enable a top _N_ option for the chart, or show variances within the chart.


**Figure 9.11** Boardroom Properties of Charts


**Filters** Because the boardroom is optimized for touch input, you should prefer
using input controls over story or chart filters. These filters allow easy interaction and can be used without a keyboard if designed properly. Consult
Chapter 5, Section 5.7, for more information about filters.


In general, you should evaluate all filter concepts. Linked analysis in particular allows you to analyze data easily while interacting with charts or tables.


**Explorer** Initially, SAP designed the explorer for the boardroom only but added it to
the story later. The explorer should be activated wherever possible so that
boardroom viewers can easily manipulate charts or tables and answer additional questions. The explorer is documented in Chapter 5, Section 5.7.3.


**Predictive analytics** You can also utilize predictive analytics in a boardroom. Both smart
insights and smart discovery offer great value as they automatically point
out highlights and outliers in the data (see Chapter 7).


Because almost all story functionality is available within the boardroom,
you should consider its correct usage while designing the story.


**9.2.3  Creating an Agenda**


**Creating a new** Now, let’s create a new boardroom, first of the agenda type. Either select
**boardroom** **Create**    - **Digital Boardroom** from the main menu or start within the file
repository by clicking on the plus icon and selecting the **Digital Board-**
**room** option.


Let’s call the boardroom “Agenda” and save it in the **Sales Data** folder.
Select the **Agenda** boardroom type, as shown in Figure 9.12. The agenda
builder will open, as shown in Figure 9.13.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-3-0.png)








**Figure 9.12** Selecting a Boardroom Type


**Figure 9.13** Agenda Builder


The agenda follows a defined structure. The structure is determined by the **Library**
agenda elements, which again consist of topics. You must first import stories before you can use them to fill in topics. Click on the **Library** button in
the top right to open the library, as shown in Figure 9.14.


**Figure 9.14** Library


To keep the boardroom designer easy to use and avoid overloading it with
information, stories must be first imported into the library. In this way,
boardroom creators only see the stories they need. Click on the **Import**



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-4-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-4-1.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-4-2.png)








button next to the **Search** field, as shown in Figure 9.14. Now, choose the
**Sales Analysis (Responsive)** story we created in Chapter 5, Section 5.10.2.
Click on **Expand** to show all pages. The outcome should match the view
shown in Figure 9.15.


**Figure 9.15** Imported Story in the Library


**Creating an** Start creating the agenda. Rename the first agenda element “Overview” and
**agenda element** enter any name as the presenter and any time. An agenda element can be
understood as a topic area. Agenda elements should match the agenda of
the actual meeting in which you want to present the boardroom.


**Creating a topic** Click on the plus icon to create a new topic. Name this topic “Introduction” so that your screen resembles the screen shown in Figure 9.16.


**Figure 9.16** Agenda Element with Topic Added



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-5-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-5-1.png)








To add content to a topic, you can insert single pages or whole stories from
the library via drag and drop. Let’s do this step for the overview page of our
story. Click and hold on the **Overview** page in the library and drag the page
onto the **Introduction** topic, as shown in Figure 9.17, and then release your
mouse button. Add the **Detail** page as well.


**Figure 9.17** Adding a Page to a Topic


Now, create a second agenda element. Click on the plus icon in the **Adding more items**
**Insert** section of the top bar, as shown in Figure 9.18. Select the **New Agenda**
**Item** option.


**Figure 9.18** Adding a New Agenda Item


Assign any name as the presenter and enter a time. Change the title to
“More reports.” Then, add a new topic called “More” and add the **More** page
via drag and drop. The result is shown in Figure 9.19.


**Figure 9.19** Adding a Second Agenda Item



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-6-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-6-1.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-6-2.png)








**Context menu** You can change additional settings for each topic by opening the context
menu for a topic, as shown in Figure 9.20. The topic can be hidden in the
presentation and mobile app. You can also promote it as a featured topic so
that it’s highlighted in the boardroom.


**Figure 9.20** Context Menu for Topic


**Topic filters** Another way to make it easier for viewers to interact with the agenda is to
use topic filters. To add a topic filter, click on the frame of the **Introduction**
topic first so that the topic is highlighted in blue. Then, click on the **Topic Fil-**
**ter** button in the top bar, which will open the filter sidebar. Add a topic
filter for the **Product** dimension and select the **All Members** option to
include all elements, as shown in Figure 9.21.


**Figure 9.21** Creating Topic Filters


**Details** Sometimes, you may be asked for additional information during a presentation. For this scenario, you can add additional pages to a page within a topic
that are only shown when needed. Select any page and click on the **Details**
button . The sidebar will open, where you can identify detail pages.


**Launching the** Save the boardroom and click on the **Start Presentation** button to
**boardroom** launch the boardroom. Try out the navigation features described in Section
9.1. If you aren’t working with a touch-based display, you can open the context menu of the boardroom by right-clicking it. The final agenda is shown
in Figure 9.22.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-7-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-7-1.png)








**Figure 9.22** Boardroom Agenda


**9.2.4  Creating a Dashboard**


Let’s create another boardroom, this time, a dashboard. Either click on **Cre-** **Creating a new**
**ate** - **Digital Boardroom** from the main menu or start within the file reposi- **boardroom**
tory by clicking on the plus button and selecting the **Digital Boardroom**
option.


Name the boardroom “Dashboard” and save it in the **Sales Data** folder.
Select the **Dashboard** boardroom type, as shown earlier in Figure 9.12. The
agenda builder will open, as shown in Figure 9.23.


**Figure 9.23** Dashboard Builder



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-8-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-8-1.png)








**Root topic** The dashboard initially contains an empty topic, which is created as a root
topic to provide a starting point for the boardroom. The root topic should
contain pages that either provide a graphical structure for the boardroom
or at least provide an overview of all information in the boardroom.


**Library** The dashboard doesn’t follow any fixed order. Instead, you’ll create topics
that contain one or more pages. These pages are linked to each other, which
creates relations between them. Stories first must be imported into the
library before you can add them. Click on the **Library** button to open the
library, as shown in Figure 9.24.


**Figure 9.24** Library


To keep the boardroom designer easy to use and avoid overloading information, stories first must be imported into the library. Thus, boardroom
creators only see the stories they need. Click on the **Import** button next
to the **Search** field, as shown in Figure 9.24. Now, choose the **Sales Analysis**
**(Responsive)** story we created in Chapter 5, Section 5.10.2. Click on **Expand** to
show all pages. The outcome should match the view shown in Figure 9.25.


**Figure 9.25** Imported Story in the Library


Start creating the boardroom by filling the automatically generated root
topic with contents. Rename it to “Overview” and add the **Overview** page to
it. Click and hold on the page in the library and drag it onto the root topic,
as shown in Figure 9.26.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-9-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-9-1.png)








**Figure 9.26** Adding Page to Root Topic


Topics can be moved around the boardroom designer freely—to improve
graphical visibility, for example. Click on the header of a topic (the four dots
on top) and move the topic around while keeping the left mouse button
pressed. Because a topic can have multiple relationships to other topics,
this feature can be quite helpful to keep track of the boardroom’s structure.
Each topic can contain one or more pages, which are shown on one or more
displays if available. Moving topics around doesn’t affect the relationships
between them, which are defined separately and explicitly.


Now, create a new subtopic. Click on the plus icon below the root topic. **Adding subtopics**
Rename the new subtopic “Details” and add the **Detail** page from the library
to it, as shown in Figure 9.27.


**Figure 9.27** Subtopic in Dashboard



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-10-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-10-1.png)








**Creating new topics** Next, create a new topic. However, this topic shouldn’t be a subtopic;
instead, this topic should act as an independent tile. This separation is later
displayed in the tables of contents of the boardroom. Topics can be shown
in a tree structure and expanded there. Click on the plus icon in the
**Insert** section of the top bar and choose **New Topic**, as shown in Figure 9.28.


**Figure 9.28** Creating New Topic


Rename the topic “More information” and add the **More** page from the
library to it. The result should now match the screen shown in Figure 9.29.


**Figure 9.29** Dashboard with Two Topics and One Subtopic


**Navigation** Because the agenda was defined as a fixed order of presentation topics, you
didn’t model any jumps there. But in dashboards, jumps are defined on the
widget level or the page level separately and must be activated for each
chart, table, or page first.


Click on the **Overview** page in the dashboard so that the page is highlighted
in blue. Then, click on the **Navigation** button in the top bar, which will
open the navigation sidebar for the page, as shown in Figure 9.30.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-11-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-11-1.png)








**Figure 9.30** Navigation


Create a jump for the whole page first. Select **Details** from the **Topic** drop- **Jump from**
down list and select **Detail** from the **Page** dropdown list as the navigation **page to page**
target. Assign the “Detailed view” label to the jump, as shown in Figure 9.31.
Whenever a viewer opens the context menu on the **Overview** page, the user
will be offered the chance to jump to the **Detail** page.


**Figure 9.31** Creating Jump to Another Page


Let’s also create a jump for a specific chart. Click on the plus icon next to **Jump from a widget**
the **Tile** text in the navigation sidebar. The story preview will open, where
you can select a widget. Select the **Quantity by Product** chart and click on
**Add** . Define the **More information** topic and the **More** page as the jump target. Assign the “More information” label and activate the **Apply selected**
**dimension as a filter** option, as shown in Figure 9.32. If the context menu is
opened for this chart in the boardroom, the jump will be offered to the
viewer.


Like the agenda, the dashboard supports topic filters. This function behaves **Topic filters and**
similarly to the agenda, as described in Section 9.2.3. Each topic can be con- **context menu**
figured separately by using its context menu, which is also described in Section 9.2.3.



![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-12-0.png)

![](temp_conversion_out/main/images/057_9.2 Creating Boardrooms_057_9.2-Creating-Boardrooms.pdf-12-1.png)






