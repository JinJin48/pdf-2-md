---
tags:
source: 043_6.1 Planning in SAP Analytics Cloud.pdf
title: 043_6.1 Planning in SAP Analytics Cloud
---

# Chapter 6 **Planning**

_Another component of SAP Analytics Cloud is the planning engine, which_
_provides various tools and functionalities to establish full planning pro-_
_cesses. In this chapter, you’ll learn more about planning in SAP Analytics_
_Cloud, and we’ll walk through an example for you to better understand_
_each functionality._


An almost impossible (or at least quite hard) task is to correctly estimate
how a business will develop and to then meet this forecast exactly, and
thus, planning is especially important for businesses. However, as this field
is rather complex, planning is often perceived as its own science. In many
businesses, the controller is responsible for ensuring that budgets, goals,
and long-term strategies are maintained correctly and ideally are met by
the business. To support a tabular planning process with visual and intuitive functionalities, SAP Analytics Cloud offers a full-fledged planning component to establish planning processes and track their execution.


In this chapter, we’ll take a detailed look at the planning component in SAP
Analytics Cloud. We’ll show you a selection of important functionalities
through examples and cover how they influence the planning process.
Then, you’ll perform selected basic planning tasks to make you familiar
with the toolset. But first, you’ll create a new planning model, which we’ll
then use to walk through the exercises.



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-0-0.png)



**6.1  Planning in SAP Analytics Cloud**


The area of planning is often seen as its own world. Challenges and tasks
are mostly resolved by a small group of employees in a company, like










controllers or other financial workers. These users have high expectations for planning solutions, which are often complex and go above simple data entry.


**Planning models** Planning in SAP Analytics Cloud either requires a planning model (see
Chapter 4, Section 4.2.3) or a model based on a live connection to embedded
SAP Business Planning and Consolidation (SAP BPC; see Chapter 2, Section
2.1). Planning models can only be created by users who carry the necessary
license and must be created as planning models from the beginning. Note
that you cannot convert an analytical model into a planning model after
the model is created.


In the following sections, we’ll go over several prominent planning tools
and functionalities and describe how they’re integrated with a story.


**6.1.1  Data Entry and Version Management**


**Data entry** The grid shown in Figure 6.1 displays an account dimension with a hierarchy of key figures across a date dimension. This normal table chart was created within a story and shows data from a planning model.


**Figure 6.1** Table with Plan Data


Not only can the data in a planning model be analyzed, it can also be
directly modified within a table in a story. These changes would be directly
applied to the data in the model.



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-1-0.png)








This task is performed by clicking on the value in the table that you want to
change. Then, simply type in a new value or add or subtract a value, as
shown in Figure 6.2.


**Figure 6.2** Entering Data into Tables


Now that you’ve seen how data is entered, note that this feature isn’t
restricted to previously created versions. Another important feature of the
planning component is version management, which is directly integrated
into a story and can be accessed quickly. Not only can you edit existing versions (if you have the necessary rights); you can also create private versions, as shown in Figure 6.3. In this process, you can have multiple options,
which include changing the currency or selecting a category for the new
version.


You can also indicate if the new version should copy all the data from
another version or be created blank. You can also specify a scope to copy
only a selection of data.


Initially, private versions are only visible to their creators who alone can **Private versions**
modify, without fear of interference from other users. However, a private
version can also be shared with selected colleagues so that they can support
you in the process. You can also differentiate between read and write
access.


As shown in Figure 6.4, the new version will appear in the table, like every
other version of the model, and can be modified the same way. Once all
activities in the version are completed, this version can be published and
converted into a public version. A full workflow can be established to govern this process, including a validation step that requires the version to be
checked first before it is published. We’ll describe this in more detail in Section 6.3.1.



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-2-0.png)








**Figure 6.3** Creating Private Versions


**Figure 6.4** New Private Version


**6.1.2  Planning within Stories**


**Distribution** Within a story, several functionalities support users during planning processes. With the _distribution_ functionality, you can, for example, distribute



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-3-0.png)

![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-3-1.png)








values from a hierarchy node to its children and assign weights to determine how the value is spread. Before opening the interface, you must first
select the value you want to distribute. This process is described in detail in
Section 6.3.2.


Figure 6.5 shows how the **-6,718,911,705.11** value is distributed proportionally across all quarters of a year. The weights can be used to specify how
much of the total value is assigned to each quarter without changing it. The
weights can be entered as either absolute values or as ratios (e.g., “1, 1, 1, 1”
for an equal distribution).


**Figure 6.5** Spreading Values


Values are usually distributed across a hierarchy (in our case, the **Date** hierarchy of the following year) and can be performed at every level of the hierarchy.


Another common workflow in planning scenarios is increasing or decreas- **Assigning**
ing the overall outlook. The interface also allows you to enter a number and
assign it to each dimension member based on a weight or absolute values.
Again, you must select the target hierarchy that you want to increase in the
table.


Figure 6.6 shows an example in which we want to add the **−500,000** value
to the operating income for both years. While 10% of this total is assigned



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-4-0.png)








to 2018, the other 90% is assigned to 2019. The dialog box shows clearly how
your assignments will look once finished.


**Figure 6.6** Assigning Values


**6.1.3  Planning Tools**


**Value driver trees** In addition to the planning tools available within a story, which are presented in detail in Section 6.3, additional tools are available for planning
and simulation workflows that make these processes easier and faster. The
value driver tree is one such tool. Like a chart, a value driver tree can be
embedded as an object in a story.


Figure 6.7 shows an excerpt of a value driver tree. In general, this tool allows
you to split a key figure down into its individual components. In this case,
the value driver tree displays the **Profit** measure and some of its components. The tree can become rather big and complex, you can use your
mouse to zoom in and out of and navigate through it. The window in the
bottom left shows the current position of the tree and which part is covered
by the view.


**Simulation** However, value driver trees do not just display dependencies. You can also
run simulations and access a broad set of functionalities. Simply click on a
value in one of the drivers and change it (by either using absolute values or
a percentage), as shown in Figure 6.8.



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-5-0.png)








**Figure 6.7** Excerpt of a Value Driver Tree


**Figure 6.8** Changing Individual Values


If a value has been modified, it will be colored yellow, as shown in Figure **Calculation rules**
6.9. In addition, you can implement calculation rules in a value driver tree
that influence how a change in one value affects other values along the tree.
The value driver tree therefore provides instant feedback on proposed
changes or their impacts on estimations. All values that change because of
the modified entry will be marked in yellow as well.



![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-6-0.png)

![](temp_conversion_out/main/images/043_6.1 Planning in SAP Analytics Cloud_043_6.1-Planning-in-SAP-Analytics-Cloud.pdf-6-1.png)






