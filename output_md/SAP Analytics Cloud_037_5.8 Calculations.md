---
tags:
source: 037_5.8 Calculations.pdf
title: 037_5.8 Calculations
---



**Using the explorer** The explorer is quite similar to the data exploration mode described in Section 5.2.2. However, viewers can’t copy the charts to a new story. They can,
however, save their customizations as new explorer views and open these
views later again. Viewers don’t need any edit rights for the story for this
feature.


**5.8  Calculations**



**Calculated**
**measures and**
**dimensions**



In self-service scenarios, business users often express a desire to create
additional _calculations_ on top of the measures or to create _calculated_
_dimensions_ . These features can be used to easily create new elements in a
chart or reflect individual business requirements. Both calculated measures and dimensions can be created during the modeling process. More
information can be found in Chapter 4, Section 4.3 and Section 4.4.


In this section, we’ll cover various examples of calculated measures and
dimensions. Feel free to create your own calculations to experiment with
these features.



**Creating** Calculations in a story are created within the builder. Open the builder for a
**calculations** chart or table and click on **Add Account**   - **Add Calculation**, as shown in Figure 5.94.


**Figure 5.94** Adding New Calculated Measure


**Calculation types** The following calculation types can be created via this dialog box:


         - **Calculated Account**
Allows the creation of a new measure by applying a formula.


         - **Restricted Account**
Restricts a measure by one or more dimensions.


         - **Difference From**
Calculates the difference between two dates.


         - **Aggregation**
Used for calculations based on aggregation.



![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-0-0.png)








- **Dimension to Account**
Converts a dimension that contains numeric values into a measure.


- **Running Total**
Accumulates a number while running through a dimension and its
dimension members. For each dimension member, the measure is
added to the previous one.


**5.8.1  Calculated Accounts**


A calculated account is created in the **Calculation Editor**, which offers a formula editor and various operators, as shown in Figure 5.95.


**Figure 5.95** Calculation Editor


Formulas can be typed in directly and include various mathematical opera- **Creating formulas**
tions and functions. The calculation editor automatically recognizes some
inputs and offers visual help to accelerate the formula creation and support
you in selecting measures and functions, as shown in Figure 5.96. On the
right, all available functions, operators, and conditions can be accessed
directly.


**Figure 5.96** Automatic Recognition of Entered Text



![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-1-0.png)

![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-1-1.png)








You can also add an input control to the formula to act as a placeholder for a
value. With the input control, story viewers can influence a calculated measure.


**Formula help** To access the formula help, to help you find all the applicable functions and
elements of your model, press (Ctrl)+(Space) on a PC or (Command)+(Space)
on a Mac. The formula help shows examples for each function to help you
better understand them, as shown in Figure 5.97.


**Figure 5.97** Formula Help


**Syntax check** The syntax check feature automatically checks the formula and shows
potential errors immediately, along with providing information on how to
resolve these errors.


**Restricted measures** The **Restricted Account** calculation type allows you to restrict a measure
based on one or more dimensions. Dimension members can be either preselected or dynamically chosen by an input control while in view mode. Figure 5.98 shows an example where we’ve restricted the **Unit price** measure
by the **City** dimension.


**Figure 5.98** Creating Restricted Accounts



![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-2-0.png)

![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-2-1.png)








If you select the **Constant Selection** checkbox, the measure will always
show the restriction that was defined for this formula. Even if a filter is
applied that further restricts the dimension, the measure will ignore this
filter and keep its original definition.


If you want to calculate how a measure deviates over time, select the **Differ-** **Difference from**
**ence From** option. You can, for example, calculate how a measure has
changed in comparison to a period in the previous year. You can also define
which measure should be compared. Differences can be compared dynamically (e.g., last quarter) or by using fixed dates, as shown in Figure 5.99.


**Figure 5.99** Calculating Deviations


The **Aggregation** calculation provides various aggregation options for mea- **Aggregations**
sures. including, for example, summing up a measure based on a specific
dimension or counting all the members of a dimension. This calculation
supports the **SUM**, **COUNT (DIMENSIONS)**, **COUNT (excl. 0, NULL)**, **MIN**,
**MAX**, **AVERAGE (excl. 0, NULL)**, **FIRST**, and **LAST** operations, as shown in Figure 5.100.


The **Aggregation Dimensions** dropdown list determines which dimensions **Aggregation**
are used for the aggregation of the measure. If you select the **Use condi-** **options**
**tional aggregation** checkbox, you can add additional conditions. With this
option, you can, for example, specify that the aggregation is only applied to
dimension members that are indicated explicitly.


Sometimes, a measure is erroneously created as a dimension, or a dimen- **Dimension to**
sion contains only numeric values. In this case, you can use the **Dimension** **account**
**to Account** calculation type to convert dimensions to measures, as shown
in Figure 5.101. If a dimension contains non-numeric values, those values
will be ignored.



![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-3-0.png)








**Figure 5.100** Creating Aggregations


**Figure 5.101** Converting Dimensions to Accounts


**5.8.2  Calculated Dimensions**


Similar to calculated measures, you can create calculated dimensions in the
builder. Click on **Add Dimensions** and choose **+ Add Calculated Dimension**,
as shown in Figure 5.102.



![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-4-0.png)

![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-4-1.png)








**Figure 5.102** Adding Calculated Dimensions


A calculated dimension is based on a formula that you define through text **Text operations**
operations. Text operations can be used to analyze, modify, or create text
columns. The editor provides various functions, conditions, and operators
to define the calculation, as shown in Figure 5.103.


**Figure 5.103** Using Formulas to Create Calculated Dimensions


Alternatively, the **Account-Based Dimension** calculation type can define **Measure-based**
thresholds for measures. You can also convert a measure to a dimension. **dimensions**
Figure 5.104 shows an example in which supermarkets are grouped by revenue. The supermarkets that generate a revenue higher than 50,000 are
tagged as **High** ; the others are tagged as **Low** .



![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-5-0.png)

![](temp_conversion_out/main/images/037_5.8 Calculations_037_5.8-Calculations.pdf-5-1.png)






