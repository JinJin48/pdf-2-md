---
tags:
source: 027_4.5 Editing Models in the Modeler.pdf
title: 027_4.5 Editing Models in the Modeler
---



connection data model is completely controlled by the data source itself.
SAP Analytics Cloud is not able to override any authorizations defined in a
data source.


**Figure 4.46** Grouped Dimensions


**4.5  Editing Models in the Modeler**


The _modeler_ is the central tool for editing models in SAP Analytics Cloud.
However, for models based on a live connection, only limited functionality
is available in the model, as documented in Section 4.4. In this section, we’ll
modify the model we created in Section 4.3.


**The modeler** Using the modeler is the final but important step in the process of creating
and maintaining models. The modeler provides tools, not only for maintaining master data but also for activating additional functionality or add
additional data sources. You can also always jump back to the data wrangling step in the modeler if you forgot to perform a data manipulation or a
quality fix. The modeler is explicitly designed to maintain models and
shouldn’t be considered equal to a table editing tool.


**Opening the** To open the modeler, simply click on a model in the folder structure. After**modeler** wards, the modeler will be opened with the model automatically. To open
the model we created in Section 4.3, navigate to the **Sales Data** folder where
we saved the model, as shown in Figure 4.47.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-0-0.png)








Alternatively, you can open the modeler from the main menu. The modeler
will list all your recently edited and created models.


**Figure 4.47** Sales Data Folder


After you click on a model name, the modeler will open. Initially, the modeler shows an overview of the model and its content, as shown in Figure
4.48.


**Figure 4.48** Modeler Overview and Content



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-1-0.png)

![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-1-1.png)








To provide quick access to commonly used functionalities, the modeler is
separated into several areas. At the bottom, the **Data Foundation** area
shows a preview of the data in the model. In the following sections, we’ll
first describe the various areas of the modeler before modifying the model
itself to demonstrate each functionality.


**4.5.1  Areas of the Modeler**


**Action bar** Figure 4.49 shows the action bar of the modeler, which is the central point
to access each area of the modeler. To toggle between the model overview,
calculation management, and data management, click on the **Workspace**
dropdown menu 1. When you click on **Data Management**, you’ll open the
data management interface, where you’ll see all the data sources of the
model. You can also access the **Calculations** overview here. There, you can
create calculations on top of the existing data.


**Figure 4.49** Modeler Action Bar


The **Save** icon 2 saves all changes that you’ve applied to the model. The
model’s settings can be opened by clicking the wrench icon 3. To share a
model with other users or teams, click on the **Share** icon 4. Changes can be
undone 5 or repeated 6. Click on the plus icon **+** 7 to create a new dimension and click on the **Remove** icon 8 to delete a dimension.


The **Variables** icon 9 allows you to add variable prompts to the model. The
**Locking** icon j is only activated for planning models and can be used to
introduce data locks. Data locks are used to prevent the data in planning
models from getting changed or overwritten.


If you want to clear all transactional data from a model, click on the eraser
icon k. This icon allows you to empty the model without deleting master
data. To turn off the data preview on the bottom of the model overview, use
the **View** icon l.


The **Validation** section m displays issues and problems, if they exist. If these
issues are not resolved, you won’t be able to save the model.


The **Model View** n dropdown allows you to toggle between a list view and a
graphical view of the model. The **Search** function o can be used to search
the model.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-2-0.png)








**New Model Type**


In 2021, SAP introduced a new model type for SAP Analytics Cloud. This
model type introduces new features that are specifically important for
planning scenarios. However, at the time of this writing, the new model
type is still limited by some restrictions.


Major limitations include the missing link formula feature between models, as well as cross-model copy steps in data actions if models from both
the classical type and the new type are used. This can be resolved by using
the link function. Also, blending and table thresholds are not supported
within the story if models contain an account dimension. Enrichment of
areas for geo maps are also not currently supported. Since 2024, all models
uploaded from flat files are automatically created as new models.


For more information about the new model type, more details are available in the official product help: _[http://s-prs.co/v218503](http://s-prs.co/v218503)_ . In addition, Pravin
Datar published _Introducing the New Model in SAP Analytics Cloud_ with
SAP PRESS that contains detailed examples on the new model: _[https://](https://www.sap-press.com/5470)_
_[www.sap-press.com/5470](https://www.sap-press.com/5470)_ .


The dimension overview shown in Figure 4.50 provides a quick overview of **Dimension**
all dimensions and their attributes. The number of members and the num- **overview**
ber of hierarchies in each dimension are also shown on this overview
screen. If additional properties are activated for a dimension, these properties will be shown on this screen as well.


**Figure 4.50** Dimension Overview


Dimensions can be shown both in a list and graphically to easily distinguish among different dimension types.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-3-0.png)








**Sidebar** The sidebar of the model shows contextual information that either refers
to the model itself or to a dimension, as shown in Figure 4.51. If you click on
a dimension in the overview, the sidebar automatically adjusts.


If no dimension is selected, the sidebar shows general information about
the model. In the sidebar, now, you can also see which data sources are feeding the model. Stories or applications using the model are shown in the
**Related Objects** area. If a model is used in a story or application, that model
cannot be deleted.


**Figure 4.51** Sidebar for Model


**Data management** The **Data Management** workspace, shown in Figure 4.52, shows all data
sources that are feeding the model and also allows you to add more data
sources, maintain existing import jobs, and track historical data activities.
You can also export a model or create a regular export job.


The **API Subscriptions** tab allows external application to consume data from
models on a regular basis. This way, data can be extracted to other tools or
written back into source systems.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-4-0.png)








**Figure 4.52** Data Management Interface


**4.5.2  Editing Models**


In this section, we’ll change some model settings slightly to demonstrate
the functionalities of the modeler. Switch back to the overview to follow
these instructions.


First, let’s modify the measures. The measures are directly shown in the **Measures**
model overview, as shown in Figure 4.53. If you want to bulk edit multiple
measures at once, you can use the check boxes to select them.


**Figure 4.53** Measures Overview


To add a new calculated measure, click on **Switch to Calculation Manage-** **Creating a new**
**ment** . Click on the plus icon **+** next to **Calculated Measures** at the top of the **measure**
screen to create a new measure. Enter “RevenueForecastFixed” in the **Mem-**
**ber ID** field and “Fixed Revenue Forecast” in the **Description** field in the
sidebar on the right, as shown in Figure 4.54.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-5-0.png)

![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-5-1.png)








**Figure 4.54** Creating New Measure


**Formula editor** Now, click on the **Formula Editor** button in the sidebar to open the formula editor, as shown in Figure 4.55. Enter the formula “[Revenue] * 1.5.” The
formula editor allows for the creation of complex calculations. More details
on this tool can be found in Chapter 5, Section 5.8.


Confirm the formula by clicking on **OK**, then click on the left arrow at the
top of the account list to return to the model overview. Save your current
progress.


**Figure 4.55** Formula Editor



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-6-0.png)

![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-6-1.png)








Let’s say that, after we created the model, we got news that a supermarket **Dimensions**
brand was sold from one chain to another chain. Now, we need to adjust the
supermarket hierarchy to reflect this change. Open the **Supermarket**
dimension by clicking on the button in the **Type** column, which will
show you all dimension members in a list. The sidebar also shows contextual information about the dimension. As long as you don’t click on a specific dimension member, the sidebar will show general information about
the dimension, as shown in Figure 4.56.


**Figure 4.56** Sidebar of Dimension


You can see all available hierarchies or turn on currency conversion for this
specific dimension. You can also turn on **Data Access Control**, hide parents,
set responsible persons, or turn on **Data Locking Ownership**, which is relevant for planning scenarios.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-7-0.png)








To change the supermarket hierarchy, either click on the **Chain** hierarchy in
the sidebar, as shown in Figure 4.57, or click on the **Hierarchy** icon at the
top of your screens.


**Figure 4.57** Options to Open Hierarchy Management


**Hierarchy** Hierarchy management is conducted in a separate interface where the hier**maintenance** archy can be modified and new hierarchies can be created, as shown in Figure 4.58. The interface can be used to maintain all hierarchies that belong to
the dimension from which the interface was opened.


The sidebar on the left allows you to search through all dimension members. To see a specific member of the tree on the right, search for it in the list
and then click on the **Hierarchy** icon next to the dimension member.


**Moving members** As stated earlier, a supermarket brand was sold from one chain to another.
In our scenario, the supermarket brand Cent Town was sold by the Beverly
Markets chain to the Camill chain. Find the **Cent Town** entry by using the
sidebar on the left and jump to the entry in the hierarchy tree by clicking on
the **Hierarchy** icon next to the member name.


To move **Cent Town** to **Camill**, simply use drag and drop: Place your cursor
on top of the **Cent Town** entry in the hierarchy view. Now, click the left
mouse button and keep holding it down while moving **Cent Town** on top of
**Camill**, as shown in Figure 4.59. Then, release your mouse button. You’ll see
a live preview while moving the member.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-8-0.png)






![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-9-0.png)

**Figure 4.58** Hierarchy Maintenance


**Figure 4.59** Moving Hierarchy Member










![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-9-1.png)


Once you’re done, click on **Close** in the top left to return to the dimension
overview. Then, save the model.


**Authorizations** You also can use the modeler to maintain data authorizations on the
**for dimensions** dimension member level. In this way, you can ensure that users can only
see the data they’re allowed to see. For example, a European sales head
should only be able to see European sales data. We’ll now demonstrate how
to set up data authorizations. However, since we don’t need these authorizations for subsequent chapters, we won’t save these settings.


**Data access control** First, you must activate _data access control_ for the dimension that you want
to use to control data access. This feature can be activated in the sidebar of
a dimension. For our example, turn on **Data Access Control** for the **Super-**
**market** dimension, as shown in Figure 4.60.


**Figure 4.60** Enabling Data Access Control


After you activate data access control, open the dimension itself by clicking
on its name. Now, click on a dimension member (e.g., **A.B. Markets** ). The sidebar will now display information for this specific dimension member. You’ll
see dedicated fields that allow you to specify which users are able to read data
and write data, although writing data is only possible for planning models, as
shown in Figure 4.61. You can enter users and teams in this sidebar.


After you’ve finished all model edits, the model is ready for use in stories
and applications. Especially when creating models for broader usage, you
should plan enough time for detailed configuration, which can be quite
time consuming. You can still adjust your models afterwards, but doing so
may heavily impact existing stories or applications.



![](temp_conversion_out/main/images/027_4.5 Editing Models in the Modeler_027_4.5-Editing-Models-in-the-Modeler.pdf-10-0.png)






