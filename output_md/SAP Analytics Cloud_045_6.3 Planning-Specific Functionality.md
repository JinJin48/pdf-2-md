---
tags:
source: 045_6.3 Planning-Specific Functionality.pdf
title: 045_6.3 Planning-Specific Functionality
---



**6.3  Planning-Specific Functionality**


Because the planning component of SAP Analytics Cloud is not always separated from other areas of the product (especially the story), this section
will cover all functionalities specific to planning. General story functionality is described in detail in Chapter 5, which is also required reading to follow along with the examples in this section.


All examples in this section are demonstrated using the Operating Income
model created in Section 6.2. By using this model, we’ll walk through various planning workflows for establishing planning processes.


**6.3.1  Versions and Data Entry**


Version management and data entry are two crucial tools to solve planning
tasks. Ahead, we’ll first create a model based on the planning model. Then,
we’ll create a private version and manipulate the data in it.


First, create a new, story as described in Chapter 5, Section 5.2. For this exam- **Creating a table**
ple, create a new canvas page in optimized mode. Add a table to the page and
use the **Operating Income** model. Open the builder and add the **Date** dimension to the columns. Expand the hierarchies for **Finance** and **Date** so that
these tables match the screen shown in Figure 6.40. Be aware that revenues
have a negative sign and costs carry a positive sign in our scenario.


**Figure 6.40** Finance Table


Open the version management dialog box by clicking the icon in the top **Version**
bar, as shown in Figure 6.41. The interface shows all versions currently avail- **management**
able in this model and allows you to create private versions. You may need
to disable the **Show versions in use only** option to show all versions. Private
versions are initially only visible to their creator. They can be shared with
selected users, however, or published for general usage by all users who also
have access to the model.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-0-0.png)








**Figure 6.41** Version Management


**Copying the** Now, let’s create a copy of the **Forecast** version, which we’ll then use to exe**forecast** cute our planning workflow. Click on the **Copy** icon next to the **Forecast**
version. A new dialog box will open where you should change the **Version**
**Name** to “Private Forecast”.


You can also select the category to which the new version belongs. The dialog
box also offers multiple options for defining precisely what data is copied to
the new version. Alternatively, the new version can be blank. Leave the settings as shown in Figure 6.42 and confirm these settings by clicking on **OK** .
Afterwards, close the version management dialog box by clicking on **Close** .


**Figure 6.42** Copying Versions



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-1-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-1-1.png)








If you want to share a version, view all changes that are performed on the **Publishing versions**
version, or delete a version, click on the three dots icon next to it. Versions can be published by clicking on the icon.


The version will be automatically added to the table and will carry a copy of
the forecast values. Drill into the date hierarchy for the new version ( **Private**
**Forecast** ) to quarter level for the year **2022**, as shown in Figure 6.43. If the
version isn’t visible in the table, you may need to first change the **Version**
dimension filter in the builder (see Chapter 5, Section 5.7.1).


**Figure 6.43** Private Forecast in a Table


Click on a cell to enter data into the model. New values can be entered as **Data entry**
absolute changes (e.g., +30,000,000) or percentage changes (e.g., +1%). Alternatively, you can just enter the new value directly. Click on the value showing the **Operating Income** key figure for the year **2022** and type in “+1%” as
shown in Figure 6.44. Confirm the entry by pressing the (Enter) key.


**Figure 6.44** Entering Data into a Table


After you’ve entered the data, the value is increased by 1%. Also, as this table
has two hierarchies, the change is propagated down both hierarchies and
applied accordingly. SAP Analytics Cloud keeps the weights of each child



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-2-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-2-1.png)








identical (in this case, each quarter is a child) and raises their values accordingly. The changed values are marked in yellow, as shown in Figure 6.45.


**Figure 6.45** Yellow Background for Changed Values


**6.3.2  Distributing Values**


**Planning area** If you want to distribute values across a hierarchy (e.g., over the course of
year) by using different weights, you can use the _distribution_ functionality.
This functionality is always context based, which means that the interface
for this action is always based on a specific cell in the table.


**Figure 6.46** Opening the Planning Interface



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-3-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-3-1.png)








Right-click on the **Operating Income** value for the year **2023** in the table.
Select the **Distribute Value** option to open the planning interface, as shown
in Figure 6.46, which will open the dialog box shown in Figure 6.47.


**Figure 6.47** Distributing Values


The planning interface allows you to perform several planning processes in **Recommendations**
a single environment. Commonly used or suggested processes are displayed to you as **Recommendations** . If you click on a recommendation, it is
applied automatically.


To distribute values across a hierarchy (for example, across a year) using **Distributing values**
individual weightings, you must use the **Distribute** functionality. To determine which targets should be used for the value distribution, you must
select them directly in the table. In our example, we selected the cells **Q1**
**(2023)** to **Q4 (2023)** for the **Operating Income** measure. The planning interface will then automatically adjust itself, as shown in Figure 6.48.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-4-0.png)








**Figure 6.48** Distributing Values


You can use the **Driver** dropdown menu to determine how the weights are
determined. The following options are available:


          - **Input Values**
You enter the values manually. For this step, you’ll simply type in the
value into the fields.


          - **Input Weights**
Note that, instead of absolute values, you can enter percentages for the
weights.


          - **Equally**
The value will be divided by the number of targets (in our example, four)
and distributed among those targets.


          - **Proportionally**
The existing weighting of the current values will be used to distribute
the new value accordingly.


Choose one of these four options and enter values for the quarters accordingly, if required. Then, click on **Apply** to perform the distribution.


**Moving values** Besides distributing values, you can also move values. In this scenario, we
want to move values from one dimension member to another. This scenario may arise, for example, when a projected deal for the current year is
delayed to the next year and your revenue forecasts need to be adjusted.


To move the **Operating Income** for 2022, first click on this value in the table
and open the planning interface again as before. Now, we want to move the
value across the **Date** dimension. Since we selected the value for 2022, we
can only move it to other years, in this case 2023. Therefore, click on the



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-5-0.png)








# 2023 value for **Operating Income** so that the planning interface adjusts
itself, as shown in Figure 6.49.


**Figure 6.49** Assigning Values


Now, click on the empty input field and enter the value that you want to
move from one dimension member to the other. In this case, we want to
move the value **-200,000,000** from the year 2022 to the year 2023. After
entering the value, you’ll be immediately presented with a preview of the
changes, as shown in Figure 6.50. After clicking on **Apply**, the changes will
be performed.


**Figure 6.50** Preview of Moved Values


To assign new values (if you’re expecting a revenue increase, for example), **Assigning values**
you can perform this task in the planning interface as well. In this scenario,



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-6-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-6-1.png)









you’ll enter a value and have it added to one or more dimension members
in the table.


Select the **Operating Income** values for the years 2022 and 2023 in the table.
Then, open the planning interface as before by right-clicking on the
selected values and selecting **Redistribute values** .


Now, enter the value “-500,000,000” to both years. Next, change the distribution method to **Distribute source amount to targets**, as shown in Figure 6.51,
by clicking on the dropdown menu below the **What amount?** heading. Enter
the value “-500,000,000” into the empty cell next to the dropdown menu.


**Figure 6.51** Changing the Distribution Method


For our example, we want to distribute the new value equally. Enter the
value “-250,000,000” for each target. The table will provide an immediate
preview of your changes, as shown in Figure 6.52. Click on **Apply** to submit
these changes.


**Figure 6.52** Preview of the Assignment



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-7-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-7-1.png)








**6.3.3  Allocations**


The allocations tool is a powerful functionality to allocate a total value into
multiple values by using drivers. For a better understanding of this procedure, we’ll create a basic allocation to allocate our **IT Expenses**, which is a
single total value that applies to multiple products. The allocation should
be driven by the **Gross Sales** for each product.


Although allocations are executed within stories, they must first be created **Creating allocation**
as processes. Click on the main menu and then select **Data Actions** - **Create** **processes**
**New** - **Data Action** . Rename the data action to “IT Expenses” and select the
**Operating Income** model as the **Default Model**, as shown in Figure 6.53.


**Figure 6.53** Creating New Data Actions


Now click on the **Add Allocation Step** icon in the top bar. The allocation **Creating an**
processes consist of allocation steps that are executed when performing **allocation step**
the allocation process in a story. These steps can be reused across multiple
data actions once they’re created. Alternatively, you can create a new allocation step directly within the data action interface. The new empty step is
shown in Figure 6.54. Rename the new allocation step “IT Expense” and
select the **OP_Accounts** dimension from the **Source Dimension** dropdown
list and the **OP_Product** dimension from the **Target Dimension** dropdown
list. As **Driver Dimension** choose **OP_Accounts**, as shown in Figure 6.55. Confirm the allocation step by clicking on the **Save** icon in the top bar and save
the data action into the **Sales Planning** folder.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-8-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-8-1.png)









![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-9-0.png)

**Figure 6.54** Empty Allocation Step


**Figure 6.55** Creating New Allocation Steps



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-9-1.png)








After you’ve created the allocation step, you must define its allocation **Allocation rules**
rules. Click on the value helper icon below **Source Dimension**, which will
open a new dialog box, as shown in Figure 6.56. Select the **IT Expenses** member in the hierarchy.


**Figure 6.56** Selecting a Source Member


Under **Driver Dimension**, select the **Gross Sales** measure by using the value
helper, and under **Target**, choose the **All Products** dimension as shown in
Figure 6.57. Save the data action by clicking on the **Save** icon .


**Figure 6.57** Allocation Rules


To execute the allocation process, you must create a new story (or use an **Executing**
existing one). Add a new canvas page in optimized mode with a table using **allocations**



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-10-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-10-1.png)








the **Operating Income** model. Modify the **Version** filter in the builder to
show the **Private Forecast** version only, which we created in Section 6.3.1.
Then, add the dimension to the columns and drill into the accounts and
product hierarchy, as shown in Figure 6.58.


**Figure 6.58** New Canvas Page with a Table


In the table shown in Figure 6.58, the **IT Expenses** aren’t maintained for individual products right now. We want to fix this problem by executing an
allocation.


**Executing alloca-** In previous version of SAP Analytics Cloud, you used to click on the **Allocate**
**tions** **Values** icon in the top bar of the story and select **Execute Allocation** .
This method is still supported but is no longer recommended by SAP. Also,
since we created our allocation step within a data action, we need to add a
data action to the story to access it.


Choose **Data Action Trigger** from the **Insert** area in the top bar to add it to
the page. Label it as “Execute Allocation Step” and select our previously-created data action. Confirm the entries as shown in Figure 6.59. The other settings allow to you determine if the executed changes should be directly
published to the version and if you want set a fixed target version or let the
user choose it upon execution.


The new data action trigger can be placed freely around the table. It can be
executed in **Design** and **View** mode. Click on the data action to execute it.
You will be then prompted to select the version as shown in Figure 6.60.
Select the **Private Forecast** and confirm by clicking on **Run** .



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-11-0.png)






![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-12-0.png)

**Figure 6.59** Creating a New Data Action Trigger


**Figure 6.60** Executing a Data Action










![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-12-1.png)


SAP Analytics Cloud now executes the allocation process and allocates IT
expenses to each product using the gross sales for each product as drivers.
Once the allocation process is completed, you’ll see IT expenses for individual products in the table as well, as shown in Figure 6.61.


**Figure 6.61** Results of Allocation Process


**6.3.4  Grid Pages**


As described in Chapter 5, Section 5.2.1, a story also offers the grid page type.
This page type allows you to work with a grid view of your data. The grid
page is only available in classic design mode.


**Creating a table** This page type is especially helpful for planning workflows. Create a new
story and select the **Grid** page type. Click on the **Insert** icon in the top bar
and choose the **Operating Income** model. Add the **OP_Product** dimension
to the columns and drill down into the hierarchies, as shown in Figure 6.62.


Grid pages can only show tables. However, you can add multiple tables
from different data sources to one grid page, and they’re automatically put
below each other. Interactivity with a table on a grid page is similar to a
table on a canvas or responsive page. However, a grid page allows you to use
all cells that are not used by a table for calculations.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-13-0.png)








**Figure 6.62** Grid Page with Table


Click on the **Cost of Goods Sold** measure for the product group **Apparel** (cell **E9** ) **Cell references**
and copy the value of the cell by pressing (Ctrl)+(C) on a PC or (Command)+(C)
on a Mac. Now, click into an empty cell (e.g., cell **G2** ) and paste the value by
pressing (Ctrl)+(V) on a PC or (Command)+(V) on a Mac. The **G2** cell should now
show same the value as **E9**, as shown in Figure 6.63.


**Figure 6.63** Copied Value in G2


Instead of simply copying the value into the new cell, you’ve created a _cell_
_reference_ by performing this action. With a cell reference, the value itself is
not copied, but instead a context is pasted into the cell that leads to the
original value. Specifically, the **G2** cell will now always show the value for
**Cost of Goods Sold** for the product group **Apparel** .



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-14-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-14-1.png)








**Formulas** In addition to cell references, you can also enter formulas into empty
cells. Double-click on an empty cell (e.g., **G4** ) and type in a formula. The
formula bar at the top automatically shows all available functions. You
also can directly reference cells by entering their addresses. Type the
formula “=D9+D8” in, as shown in Figure 6.64.


Because both functionalities can quickly lead to a high number of cell references, keeping track of all of them can become difficult. However, the story
interface offers a way to display cell references. Click on the **Cell References**
**and Formulas** icon in the top bar and select **Show References** and
**Show Formulas** . While cell references will be highlighted in color, formulabased cells will simply show the raw formula, as shown in Figure 6.65.


**Figure 6.64** Entering Formulas


**Figure 6.65** Showing Cell References and Formulas



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-15-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-15-1.png)








**6.3.5  Value Driver Tree**


The value driver tree, which we mentioned in Section 6.1.3, is a powerful
tool for visualizing complex relationships among key figures and run simulations on them.


In the following section, you’ll create a value driver tree to learn its basic **Creating a value**
functionalities. For this process, we’ll visualize a subset of the measure rela- **driver tree**
tions that are stored in the model. Value driver trees are directly created
within stories.


Create a new story in optimized mode and add a new **Canvas** page. Now,
click on the plus **+** icon in the **Insert** area of the story toolbar and select the
**Value Driver Tree** option. Choose the previously-created **Operating Income**
model in the **Based on** section, as shown in Figure 6.66.


**Figure 6.66** Creating a Value Driver Tree


Figure 6.67 shows our newly created and empty value driver tree.


**Figure 6.67** Empty Value Driver Tree



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-16-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-16-1.png)








**Creating Value Driver Trees**


Until SAP released the Q3 2020 version of SAP Analytics Cloud, value driver
trees could only be designed in a dedicated environment, which can still be
accessed by opening the main menu and clicking on **Value Driver Trees** .
Although this path is still supported, SAP is officially recommending the
new value driver tree designer found within stories. Therefore, we’ll only
demonstrate how to create a value driver tree in a new story.


**Filling the value** Click on the blue **Auto-Create Value Driver Tree from Model…** text in the
**driver tree with data** middle of the new value driver tree. You can now directly choose which
parts of the model you want to visualize. To keep it simple, only choose the
account **Gross Revenue** (under **Finance**          - **Operating Income**          - **Gross Profit**          **Net Revenue**, as shown in Figure 6.68).


**Figure 6.68** Account Selection


After you selected the account, the sidebar will automatically adjust and
reflect the selection only. Click on **OK** to confirm the selection. Afterwards,
add a new **Measure** on the sidebar of the value driver tree. Here, choose the
**SignedData** measure.


SAP Analytics Cloud now automatically creates a new value driver tree to
visualize the relationships between the selected accounts, as shown in Figure 6.69. Based on the node type, you may need to add additional information like the data source or calculation method.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-17-0.png)








**Figure 6.69** Automatically Generated Value Driver Tree


The sidebar now allows you to adjust the dates and versions that should be **Date and version**
used by the value driver tree and the simulations. You can also adjust the
planning horizon. Adjust the **Version** filter to **Private Forecast** and the **Date**
filter to reflect the years **2022** to **2023**, as shown in Figure 6.70. You may
need to click on the **Fit to Screen** icon on the bottom left to rearrange the
value driver tree and make it fully visible again.


**Figure 6.70** Adjusted Value Driver Tree



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-18-0.png)

![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-18-1.png)








**Further** By using the **Builder**, as shown in Figure 6.71, you can configure the value
**configurations** driver tree further. Not only can you base the value driver tree on measures
from the model; you can also show calculated measures. This feature can be
quite helpful if you want to extend existing simulations with your own
simulation calculations. These calculations can be created in the **Account**
and **Cross Calculation** sections if required.


**Figure 6.71** Value Driver Tree Builder


**Cross-calculations**


Cross-calculations are especially useful the compare key figures with each
other. These calculations are also created in the builder and allow you to
access additional functionalities. Cross-calculations can, for example,
include currency conversions or rolling forecasts.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-19-0.png)








The **Presentation Date Range** area provides options for restricting the visualized date range further. In our case, such a filter would still keep the simulation running across our selected years (2018 to 2021) but would only
visualize the years that are specified within the **Presentation Date Range**
**Filter** . This feature allows you to hide years that you need for simulation
purposes but don’t want to be displayed.


The **Node List** allows you to search for every single node of the tree and configure each node individually. You can also create new nodes in this list
manually which, for example, can form unions with other nodes by adding
or multiplying their values.


The value driver tree is directly executed within the story in which it was
created.


Once you’ve maintained the node creation settings, save the value driver
tree by clicking the **Save** icon .


To use the value driver tree, you must add it to a canvas or responsive page **Using value**
of a story. The usage of the value driver tree is described in Section 6.1.3. **driver trees**


**6.3.6  Data Actions**


Data actions are helpful tools for accelerating planning processes and automating routine tasks. A data action is designed within its own interface but
executed within a story.


Open the main menu and select **Data Action** - **Create New** - **Data Action** to **Creating data**
create a new data action. Assign the name “Initialize version” and select the **actions**
**Operating Income** model as the **Default Model**, as shown in Figure 6.72. Save
the data action by clicking on the **Save** icon .


**Figure 6.72** Creating New Data Actions


You can create various types of data actions and access them through the **Data action types**
top bar of the interface. The following types are available:



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-20-0.png)








          - **Copy action**
This action allows users to copy data within a dimension from one
dimension member to one or more other members and apply aggregations or filters. You can, for example, create a routine that copies the data
for 2023 automatically to the years 2024 to 2026.


          - **Cross-model copy action**
This action can be used to copy data from one model into another
model, set filters, and assign dimensions so that the copy workflow can
be executed without any manual effort.


          - **Allocation action**
This action can be used to execute an allocation step directly within a
story and set all required parameters and filters up front.


          - **Embedded data action**
This action can be used to embed an existing data action directly into the
data action you’re actively creating. This action allows you to create basic
steps and later reuse them.


          - **Currency conversion**
This action can be used to convert accounts from one currency to another.


          - **Advanced formulas action**
This data action provides users an interface to define transformation
scripts (visual scripting and coding are supported) to transform your
data. Various functions can be called to cover complex scenarios.


**Creating a** Now, let’s say want to create a copy action: Click on the icon to add a
**copy action** copy action. Name the action “Copy to next year” and click on **Add Copy**
**Rule** . Choose the **Date** dimension and select the **2022** value for the **From**
field. Select **2023** for the **To** field, as shown in Figure 6.73.


The **Filters** and **Aggregate To** options can be used to further define whether
only a specific set of data should be used and whether you want to perform
any aggregations while copying. **Write Mode** determines if existing values
are overwritten or if new values are appended. Save the copy action by
clicking on the **Save** icon .


**Using data actions** Data actions must be executed within a story or application. Add a new
table based on the **Operating Income** model and add the **Date** dimension to
either rows or columns. Add the data action to the page as well and place it
next to the table. If you now execute the data action, you’ll observe that the
year 2023 will be automatically filled in with the values from 2022.


**Multi Actions**


When opening the main menu, you’ll also find the **Multi Actions** section. In
this area, you can create multi actions that include data actions and










version management steps across multiple models and versions. Like data
actions, multi actions can be triggered within a story and provide a powerful tool to establish your planning process.


Multi actions are helpful if you want to first build small data actions that
you’ll reuse across multiple workflows. You can create data actions to perform single steps (e.g. create a new version or copy data) and then create
multi actions to reuse them in separate scenarios and orders.


**Figure 6.73** Creating Copy Actions


**6.3.7  Calendar**


Introduced in Section 6.1.3, the calendar is another tool for establishing **Accessing**
planning workflows. This tool is helpful for tracking planning tasks and **the calendar**
reminding users of open activities. Open the main menu and click on **Cal-**
**endar** . Within the calendar, you can switch between displaying the day,
week, or month or show a list or Gantt view of all tasks (using the options
shown in Figure 6.74, in the top left). The Gantt view represents the timelines of tasks as bars in a list, which provide an immediate overview of all
ongoing projects.



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-22-0.png)









![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-23-0.png)

**Figure 6.74** Calendar


Within the calendar, you can create tasks and events, which again can be
used to govern and establish planning workflows. To create a new task, click
on the plus icon in the top bar. You must first select the task type, then
name the task and provide start and end dates, as shown in Figure 6.75. You
can also add a recurrence to the task (e.g., every month) or add a parent process if this tasks belong to a larger task.


**Figure 6.75** Creating a New Task



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-23-1.png)








Within a task, many options exist for maintaining its contents, as shown in **Task settings**
Figure 6.76. You can add a description to a task and add links to all relevant
stories, applications, or files that are needed to complete the task ( **Work Files** ).


**Figure 6.76** Maintaining a Task


In addition, you’ll need to specify an owner in the **Owner** field who will be **Owners, assignees,**
responsible for the task, as shown in Figure 6.77. The **Assignee** is also man- **and reviewers**
datory and defines the user who must actually complete the task. You can
also add a **Reviewer** who validates the task before the task is considered
complete. If the task is part of a bigger planning process, you can indicate
that in the **Hierarchy** section.


In addition, you can maintain reminders, add more files, or leave private **Working with tasks**
notes that are only visible to you. Once a task is created and published,



![](temp_conversion_out/main/images/045_6.3 Planning-Specific Functionality_045_6.3-Planning-Specific-Functionality.pdf-24-0.png)






