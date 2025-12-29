---
tags:
source: 041_5.12 Optimized Story View Mode.pdf
title: 041_5.12 Optimized Story View Mode
---



When using planning models, you can also comment on specific data cells **Data point**
in a table. Similar to the normal commenting workflow, right-click on a **comments**
data cell in a table and choose **Add Comment** .


Comments placed on a specific data point will be stored along with the context.
Thus, a comment placed on the revenue for a specific product, for example, will
only be shown if that context is shown in the table. If the value changes, the
comment will show the value at the time the comment was placed.


**5.11.5  Bookmarks**


Especially in scenarios with multiple people accessing a story, each person **Views**
may have different requirements for setting up filters and hierarchies. If a
story viewer sets those views once, that user ideally wants to see this view
again the next time the story is opened.


Bookmarks can store the current view of a story, including its filters, input
controls, prompts, and explorer views. Bookmarks have a significant
advantage in that a story viewer can create them on top of a story without
replicating the original story. The viewer can even define a bookmark to be
shown by default when the viewer opens the story. Figure 5.126 shows the
bookmark menu in the action bar of the story. Story viewers can create
multiple views and select a default one. Also, story creators can create
global bookmarks that are available to all users (European view, North
American view, etc.).


**Figure 5.126** Bookmarks


**5.12  Optimized Story View Mode**


SAP introduced _optimized story view mode_ to improve the performance of
the SAP Analytics Cloud’s story for viewers and to deliver new functionality. Although you can follow various recommendations in story design and
content selection, story loading times can still become long if many charts
are used.



![](temp_conversion_out/main/images/041_5.12 Optimized Story View Mode_041_5.12-Optimized-Story-View-Mode.pdf-0-0.png)








**Performance** To tackle this challenge, SAP incorporated a feature called _active viewport_
**improvements** _rendering_ . This technology first loads the contents in the focus of the viewer
before proceeding with content in the background. In this way, a story
viewer can quickly get the first numbers and then navigate through the
story as before.


In addition, SAP introduced various other optimizations, including persisted queries, which cache common requests into the data model until a
change to the data structure or story design is introduced. Since many
viewers usually open the same context in a story, this feature can reduce
loading times significantly.


A full list of optimizations are documented in a blog post published by SAP,
available at _[http://s-prs.co/v218506](http://s-prs.co/v218506)_ .



**Activating**
**optimized**
**view mode**



The optimized view mode for stories must be activated explicitly for each
story in classic mode. When designing stories in optimized mode, they are
automatically viewed in optimized mode as well.


To begin, open a story which was built in classic design mode and switch to
edit mode in the top right. Then, open the **Story Details** menu under **File**, as
shown in Figure 5.127.


**Figure 5.127** Opening the Story Details


On this screen, you can define various settings, including the **View Time**
**Optimization** . Turn on the switch to **Enable Optimized Mode**, as shown in
Figure 5.128.


**Figure 5.128** Enabling Optimized View Mode



![](temp_conversion_out/main/images/041_5.12 Optimized Story View Mode_041_5.12-Optimized-Story-View-Mode.pdf-1-0.png)

![](temp_conversion_out/main/images/041_5.12 Optimized Story View Mode_041_5.12-Optimized-Story-View-Mode.pdf-1-1.png)






