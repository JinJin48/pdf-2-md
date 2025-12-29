---
tags:
source: 038_5.9 Story Design.pdf
title: 038_5.9 Story Design
---



**Figure 5.104** Creating Account-Based Dimensions


**5.9  Story Design**


Now that we’ve taken a close look at the story interface, this section will
focus on clear story design and discuss some best practices. We also want to
validate what you’ve learned so far, and you’ll also see how templates can
be used to create a new story.


**Formatting pages** Every page in a story can be formatted separately. To access the pages, simply click on any empty space of a page and open the formatting interface by
clicking on **Designer** in the top right, as shown in Figure 5.105.


**Formatting options** You can change the **Background Color** of a page completely and activate **Show**
**Grid** option to see the alignment grid. By using the grid, you can align charts,
tables, and other elements on a page easily. When using canvas pages, you can
define a fixed **Page Size** (e.g., **Letter** ) to make the story printer friendly.



![](temp_conversion_out/main/images/038_5.9 Story Design_038_5.9-Story-Design.pdf-0-0.png)

![](temp_conversion_out/main/images/038_5.9 Story Design_038_5.9-Story-Design.pdf-0-1.png)








**Figure 5.105** Formatting Pages


You also can define story-wide settings and coloring guidelines. Open the **Theme preferences**
**Theme Preferences** from the **Format** section in the top bar. You can define
default values for color palettes, text sizes, or other graphical elements, as
shown in Figure 5.106, and in this way implement your company’s design
guidelines. Theme preferences can also be configured afterwards and then
applied to all existing elements.


Let’s now create a new story and use formatting options to make it clean **Sample story**
and intuitive. However, for this section, you’ll be only provided with the
final story as a PDF file. Refer to the _Checkpoint 7 – Sales Analysis 2023 –_
_Section 5.9.pdf_ file from the demo data package for orientation and try to



![](temp_conversion_out/main/images/038_5.9 Story Design_038_5.9-Story-Design.pdf-1-0.png)








rebuild the story. Feel free to try out all the functionalities and add your
own flavor to the story.


**Figure 5.106** Theme Preferences


Our example story, called Sales Analysis 2023, contains three pages with
charts, tables, and input controls. We won’t explicitly mention text elements or shapes. Go ahead and try out the formatting options to get familiar with their impact. All pages are canvas pages and have a fixed size
(letter). This story uses the Sales Data model.


Let’s break down the three pages of this story next:


          - **Page 1: Overview**


             - Two input controls (filters) for the **Product** and **Supermarket** dimensions.


           - Two numeric point charts for the **Revenue** and **Quantity** measures,
with a variance based on the version.


           - A bar chart that shows the **Revenue** measure and **Product** dimension.
The version is colored based on IBCS.


            - A pie chart with the **Revenue** measure and **Product** dimension.


           - A waterfall chart to show the **Revenue** measure based on the **Date**
dimension and the ability to drill down into the date hierarchy.


          - **Page 2: Geospatial Analysis**


            - Two input controls (filters) for the **Product** and **Supermarket** dimensions.


           - A geo map using the **OpenStreetMap** base layer and a content layer of
type **Heat Map** . Shows the **Revenue** measure by **Stores** .



![](temp_conversion_out/main/images/038_5.9 Story Design_038_5.9-Story-Design.pdf-2-0.png)






