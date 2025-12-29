---
tags:
source: 052_8.2 Creating Applications.pdf
title: 052_8.2 Creating Applications
---



**Limitations of the** The analytics designer was made generally available to subscribers of SAP
**analytics designer** Analytics Cloud since the second quarter of 2019. In 2023, SAP introduced
the concept of the unified story and started to add functionality from the
analytics designer directly into the story. Once you turn on the advanced
mode of the story, the widgets become visible.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-0-0.png)



**Accessing the**
**development**
**environment**



**8.2  Creating Applications**


As stated at the beginning of this chapter, applications have historically
been developed in a dedicated development environment. For legacy applications (and if necessary functionality is not available in the optimized
story), you can access this environment from the main menu via **Analytic**
**Application** - **Create New Application**, as shown in Figure 8.4.


**Figure 8.4** Creating New Applications in the Legacy Environment


However, for this this section, we’ll create some basic workflows within the
optimized story environment. Therefore, switch to the **Stories** menu
which was already introduced in Chapter 5 and create a new canvas page in



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-0-1.png)








**Optimized Design Experience** mode. Although we will technically build a
story again, we will refer to it as an application in this chapter. By default,
the story launches in advanced mode.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-1-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-1-1.png)

**8.2.1  Development Environment**


The development environment for applications, shown in Figure 8.6, is the
same as the story development environment. However, in this case, the
extended mode is turned on, enabling more widgets to be added to the story.


The main additions are the Info Panel, various widgets which we will discuss on the following pages and the Scripting overview in the **Outline** sidebar on the left. This area will show a list of all scripts that are added to the
application.










**Figure 8.6** Story Environment in Advanced Mode


**Info panel** The visibility of the **Info Panel** can be toggled by clicking on the **Show/Hide**
**Info Panel** icon . This panel shows all script errors under the **Errors** tab
and shows a list of references under the **Reference List** tab. The reference list
shows which objects or functions are used by the application’s elements, as
shown in Figure 8.7.


**Figure 8.7** Info Panel


Because applications can be compared to computer programs in general,
they’re executed separately. Applications are launched by clicking on the
**View** button located in the top right. The **Edit** buttons can be used to unlock
the configuration and allow modification of elements in the application.


**Script editor** Scripts can be inserted into almost every element on the canvas of an application and even into the application itself. The script editor for each object
can be opened by clicking on the icon next to a chart or table on the canvas or an entry under **Outline**, as shown in Figure 8.8.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-2-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-2-1.png)








**Figure 8.8** Script Editor


The script editor both allows for freeform code entry and provides graphi- **Syntax check**
cal support while entering code. When entering code that contains errors,
errors are highlighted and explained if possible (via a syntax check). Figure
## 8.9 shows a scenario in which the same code is entered two times in line 1
and line 3. The editor adds a red background to all line numbers that may
contain erroneous code (here line 1 and line 3). When hovering the mouse
above a line number (as shown in Figure 8.9, line 3), a detailed error message will be displayed.


**Figure 8.9** Erroneous Code


Another helpful feature in the script editor is the built-in formula help, **Formula help**
shown in Figure 8.10, which can be called from any position by pressing
(Ctrl)+(Space) on a PC or (Control)+(Space) on a Mac.


**Figure 8.10** Formula Help



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-3-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-3-1.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-3-2.png)








The formula help displays all available functions and properties, including
descriptions, and allows you to quickly browse through all the available
options. When working with dimensions or measures, you can also open
member selectors with the help set to specific filter criteria, for example.


**8.2.2  Creating New Application Elements**


While some elements of the story were already introduced in Chapter 5,
other elements are only available in advanced mode, as shown in Figure
8.11. We therefore won’t cover all elements again in this chapter.


**Figure 8.11** Elements of Applications



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-4-0.png)









![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-5-0.png)

In this section, we’ll create some application elements through some simple examples. Then, we’ll introduce you to some additional elements and
provide references to further information. Because of the vast number of
possibilities in the advanced mode of the story, we will only display a selection of widgets. This will help us to gain a basic understanding of the concepts of scripting.


First, let’s create a standard table based on the Sales Data model we created
earlier in Chapter 4, Section 4.3 and Section 4.5. Show the **Revenue** and
**Quantity** measures and add the **Supermarket** and **Product** dimensions.
Increase the table’s size so that its contents are visible, as shown in Figure
8.12. The table will be now called **Table_1**, under **Outline**, on the left.


**Figure 8.12** Table and Outline



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-5-1.png)








**Dropdown**


A **Dropdown** element can be added to the canvas and contain a dropdown
list of customized elements. If the user clicks on the dropdown list and
selects an entry, an _action_ will be executed.


**Creating dropdown** Click on the plus icon, in the **Insert** area of the top menu bar, shown
**lists** earlier in Figure 8.11, to add a new dropdown element. This element type has
its own builder, which provides an interface to define the values that are
available for selection in the dropdown list, as shown in Figure 8.13.


**Figure 8.13** Configuring Dropdowns


**Adding values** Create two entries and insert the contents shown in Table 8.1. Click on the
plus icon **+** at the top of the table in the builder to add new values. Once
you’ve entered all these values, verify the values in the dropdown list, as
shown in Figure 8.14.

|Value|Text (Optional)|Default|
|---|---|---|
|Hide|Hide|No|
|Show|Show|Yes|



**Table 8.1** Dropdown Values


**Figure 8.14** Adding Values to Dropdowns



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-6-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-6-1.png)








Open the script editor for the dropdown element to attach actions to each **Accessing the**
entry in the list. Click on the dropdown element on the canvas and click **script editor**
on the three dots icon next to it. Then, select **Edit Scripts…**, as shown in
Figure 8.15.


**Figure 8.15** Opening Script Editor


The script editor will open, indicating when the actions defined in the script **Creating scripts**
are executed. In our example shown in Figure 8.16, the selection of an entry
by the user (onSelect) will cause the execution of the script.


**Figure 8.16** Script Editor for a Dropdown Element


Now, insert the code snippet shown in Listing 8.1. The script will show or
hide the table when selecting the **Hide** or **Show** entries in the dropdown list.


// Defines the variable sel which contains the values
// of the dropdown.
var sel = Dropdown_1.getSelectedKey();


// Hides the table.
if (sel === "Hide") {
Table_1.setVisible(false);
}


// Shows the table.
if (sel === "Show") {
Table_1.setVisible(true);
}


**Listing 8.1** Sample Script to Show and Hide Tables



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-7-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-7-1.png)








**Launching the** Save the application with a name of your choice. Save the story and launch
**application** the application by clicking on the **View** button in the top right. Try out the
dropdown list options for hiding and showing the table.


**Checkbox Group**


A checkbox group offers the ability to provide multiple selections to users,
who can check one or more boxes. Each combination of selections can follow a different logic.


We must extend our application to demonstrate this functionality. Create a
new chart with the **Numeric Point** type that shows the **Revenue** measure.
Place this chart below the table, as shown in Figure 8.17.


**Figure 8.17** Table and Chart on Canvas


**Creating checkbox** Click on the plus icon in the **Insert** section in the top menu bar and add
**groups** a new checkbox group to the canvas. As with the dropdown element, a
checkbox group has its own builder in which all entries can be defined, as
shown in Figure 8.18.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-8-0.png)








**Figure 8.18** Configuring Checkbox Groups


Create two entries and insert the contents shown in Table 8.2. Select the
checkboxes in the **Default** column for both entries. Once you’ve entered all
these values, verify the checkbox group, as shown in Figure 8.19.

|Value|Text (Optional)|Default|
|---|---|---|
|Tab|Show Table|Yes|
|Cha|Show Chart|Yes|



**Table 8.2** Checkbox Group Values


**Figure 8.19** Adding Values to Checkbox Groups


Open the script editor for the checkbox group to attach actions to each **Accessing the**
selection in the list. Click on the checkbox group on the canvas and click on **script editor**
the three dots icon next to it. Then, click on **Edit Scripts…**, as shown in Figure 8.20.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-9-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-9-1.png)








**Figure 8.20** Opening Script Editor


Insert the script shown in Listing 8.2. Based on which checkbox the user
selects, the chart, the table, or both will be shown or hidden.


// Defines the variable sel which contains the values
// of the checkbox group.
var sel = CheckboxGroup_1.getSelectedKeys();


// Checks which boxes are set
// in the checkbox group.
var isChartSelected = sel.includes("Cha");
var isTableSelected = sel.includes("Tab");
// Shows the chart and/or table.
Chart_1.setVisible(isChartSelected);
Table_1.setVisible(isTableSelected);


**Listing 8.2** Sample Script to Show or Hide Tables and/or Charts


**Launching the** Save the application with a name of your choice. Save the story and launch
**application** the application by clicking on the **View** button in the top right. Try out the
checkbox for hiding and showing the table/chart.


**Radio Button Group**


A radio button group allows you to provide your users multiple options
from which they can only select one. This element is similar to a dropdown
element but all entries are displayed immediately.


The following example requires the table we created at the beginning of
Section 8.2.2.


**Creating radio** Click on the plus icon **+** in the **Insert** section in the top menu bar and add a
**button groups** new radio button group to the canvas. Like the dropdown element, a radio
button group has its own builder in which all entries can be defined, as
shown in Figure 8.21.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-10-0.png)








**Figure 8.21** Configuring Radio Button Groups


Create two entries and insert the contents shown in Table 8.3. Select the
checkboxes in the **Default** column for both entries. Once you’ve entered all
values, verify the radio button group, as shown in Figure 8.22.

|Value|Text (Optional)|Default|
|---|---|---|
|All|All Products|Yes|
|NoAlc|Non-Alcoholic|No|



**Table 8.3** Radio Button Group Values


**Figure 8.22** Adding Values to Radio Button Groups


Open the script editor for the radio button group to attach actions to each **Accessing the**
selection in the list. Click on the radio button group on the canvas and click **script editor**
on the three dots icon next to it. Then, click on **Edit Scripts…**, as shown in
Figure 8.23.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-11-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-11-1.png)








**Figure 8.23** Opening Script Editor


Insert the script shown in Listing 8.3. This radio button group allows the
user to filter down all data in the table to nonalcoholic products only (basically by applying a filter). In addition, a user can switch back to showing all
products.


// Defines the variable sel which contains the values
// of the radio button group.
var sel = RadioButtonGroup_1.getSelectedKey();


// Removes all filter for the dimension “Product”.
if (sel === "All") {
Table_1.getDataSource().removeDimensionFilter("Product");
}


// Selects all products that are nonalcoholic.
if (sel === "NoAlc") {
Table_1.getDataSource().setDimensionFilter("Product",["[Product].

[Product_Group].&[Juices]","[Product].[Product_Group].&[
Soft Drinks]",
"[Product].[Product_Group].&[Mineral water]"]);
}


**Listing 8.3** Sample Script to Filter Product Dimension


**Using the Formula Help**


In this sample script, a filter is applied to the **Product** dimension. To reduce
the workload involved with entering the filter values manually, press
(Ctrl)+(Space) on a PC or (Command)+(Space) on a Mac once you’ve arrived
at the position where you must indicate the dimension name. The value
help will then show a list of all dimensions. You can also use the formula
help to open the member selector and select the values you want to filter.


**Launching the** Save the application with a name of your choice. Save the story and launch
**application** the application by clicking on the **View** button in the top right. Try out the
radio button to filter the values.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-12-0.png)








**Button**


A button is a prominent element on the screen and an often used functionality in applications: Developers can create buttons through which users
can execute all kinds of actions. Buttons can be designed to hide elements
or modify elements while analyzing the current context. Buttons can also
be used to execute just about any action.


The following example requires the table we created at the beginning of **Creating buttons**
Section 8.2.2. Click on the plus icon **+** in the **Insert** section in the top menu
bar and add a new button to the canvas.


A button has no builder but can be formatted. The **Formatting** tab can be **Labeling buttons**
launched from the story sidebar on the right and can be used to rename the
button, as shown in Figure 8.24. For our example, enter “Show City” into the
**Text** field.


**Figure 8.24** Formatting Buttons


Open the script editor for the button to attach an action to it. Click on the **Accessing the**
button on the canvas and click on the three dots icon next to it. Then, click **script editor**
on **Edit Scripts…**, as shown in Figure 8.25.


**Figure 8.25** Opening Script Editor



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-13-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-13-1.png)








Insert the script shown in Listing 8.4. Whenever a user clicks on the button,
the **City** dimension will be added to the table. The button automatically
changes its label and can be clicked again to remove the **City** column.


// Defines a variable that contains the text
// of the button.
var buttonText = Button_1.getText();


// Adds the City dimension if it doesn‘t
// exist in the table yet and adjusts the button.
if (buttonText === "Show City") {
Table_1.addDimensionToRows("City");
Button_1.setText("Hide City");
}


// Hides the City dimension if it exists
// in the table and adjusts the button.
if (buttonText === "Hide City") {
Table_1.removeDimension("City");
Button_1.setText("Show City");
}


**Listing 8.4** Sample Script to Implement Button Action


**Launching the** Save the application with a name of your choice. Save the story and launch
**application** the application by clicking on the **View** button in the top right. Try out the
button to hide and show the **City** column.


**Filter Line**


Creating buttons or other fields like dropdown lists for a simple filter may
become too time consuming, so the _filter line_ can be used to quickly enable
filters for charts and tables. The filter line itself can’t be extended or manipulated by scripting, however, and is therefore only feasible for filtering
charts and tables on the canvas.


**Creating filter lines** The following example requires the table created in Section 8.2.2. Click on
the plus icon **+** in the **Insert** section in the top menu bar and add a new filter
line to the canvas. The filter line has its own builder, which can be used to
add dimensions to it, as shown in Figure 8.26.


**Setting up the** Before you add dimensions to the filter line, you must first select a **Source**
**filter line** **Widget** (a chart or table). Select the table (in our case, **Table_1** ) that should
be influenced by the filter line. Now, add some dimensions (e.g., **Product**,
**City**, **Street**, and **Supermarket** ), as shown in Figure 8.27. By selecting the
**Mode**, you can determine if the filter bar is only applied to one widget or a
group of widgets.










**Figure 8.26** Configuring Filter Lines


The filter line won’t show any content right away, which is purposeful since
application viewers should be able to later click on the **Filter** icon to specify
their own dimension filters.


**Figure 8.27** Creating Filter Line for Table_1


Save the application with a name of your choice. Save the story and launch **Launching the**
the application by clicking on the **View** button in the top right. The filter **application**
line initially shows only the icon. Once you click on this icon, you can
select the dimensions to be filtered, as shown in Figure 8.28.


**Figure 8.28** Using Filter Lines



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-15-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-15-1.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-15-2.png)








**Other Elements**


The application interface also provides additional programmable elements
that we won’t present in detail. In this section, we’ll offer a brief description
just a few and describe how they work.


**Input field** An _input field_ is a programmable text field, shown in Figure 8.29, that can be
filled in by the application viewer while working with the application.


**Figure 8.29** Input Field


The contents of an input field can be read via code modified during the
application runtime. Therefore, these fields can also be used as parameters
or sent to other applications via OData services. The script behind an input
field is executed every time a user enters any text into the field and clicks
somewhere outside of the field.


**Slider** A _slider_ can be added to the canvas so that an application viewer can select
values. The slider can be again referenced in a script. A slider element and
its builder are shown in Figure 8.30.


**Figure 8.30** Slider



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-16-0.png)

![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-16-1.png)








You can define the range in the slider ( **Min Value** and **Maximum Value** ) and
which value is selected by default ( **Current Value** ). The **Options** section
allows you to modify its display settings and input behaviors.


The script added to the slider will always be executed once a user sets a
value and clicks anywhere outside of the slider.


In addition, a _range slider_, shown in Figure 8.31, is available. This element is **Range slider**
almost identical to a slider but allows users to select a value range instead
of selecting a single value.


**Figure 8.31** Range Slider


A _new OData service_ can be created by clicking on the plus icon next to **Creating OData**
**OData Services** under **Outline** on the left. The builder for this service will **services**
open on the right side of the screen, as shown in Figure 8.32. OData services
are only available in the legacy analytics designer.


You must create a connection to an OData service and provide the endpoint
URL for the service. Both are provided by your OData application.


After entering the information, you must click the **Refresh** button to
check if the service is available and which functions it exposes. Those functions will be displayed in the **Metadata** section and can be accessed within
the application via scripts.



![](temp_conversion_out/main/images/052_8.2 Creating Applications_052_8.2-Creating-Applications.pdf-17-0.png)






