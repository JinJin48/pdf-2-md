---
tags:
source: 024_4.2 Types of Data Models.pdf
title: 024_4.2 Types of Data Models
---



source to an SAP BusinessObjects universe is the model creator presented
with a dialog box for selecting the dimensions and measures from the universe to be exposed in the model. We’ll describe all the available model
types, and you’ll learn how to differentiate among them in following chapters, in addition to learning how to create and use those models.


**4.2  Types of Data Models**


SAP Analytics Cloud offers various types of data models, which we’ll
describe in this section. As mentioned earlier in this chapter, not every
model type is available for every license. In Section 4.3 and Section 4.4, we’ll
explore some examples of creating various kinds of models. You’ll learn
how to create a dataset in Section 4.2.1. We’ll show you how to use datasets,
which are required to create predictive scenarios, in Chapter 7, Section 7.3.


In general, SAP Analytics Cloud differentiates among _analytical models_,
_planning models_, and _datasets_ . Every model type has specific characteristics
that determine for which activity the model is used. In addition, with
embedded models, the model is part of a story and belongs to it. The creation of embedded models is described in detail in Chapter 5, Section 5.11.1.


**4.2.1  Datasets**


Datasets represent simple tables in SAP Analytics Cloud and allow no additional semantics. These tables can be either uploaded as flat files, created
via an import connection from various data sources, or from SAP HANA
live connections. All datasets are stored as objects in the folder structure.


**Sample Files for This Section**


To demonstrate the creation of the dataset, we’ll use the _Dataset.xlsx_ file,
which is part of the demo data package download for this book found at
_[www.sap-press.com/5753](http://www.sap-press.com/5753)_ .


Datasets can be created in one of the following ways: **Starting points**


- From the main menu, select **Datasets** - **Create New**, as shown in Figure

4.4.


- When browsing through the folder structure, click on the plus icon **+** in
the action bar at the top. Then, you can choose to create a new dataset.
More information on this topic can be found in Chapter 3, Section 3.3.5.










**Figure 4.4** Creating New Datasets


**Select data source** After navigating to the **Datasets** menu, you’ll be prompted to select a data
source. Click on **From a CSV or Excel File** to upload a flat file. Alternatively,
you can import a dataset from an SAP S/4HANA system, create a live connection to SAP HANA, or acquire data from numerous other supported data
sources.


In the next step, you’ll choose the location of the file on your computer.
Click on the **Select Source File** button, as shown in Figure 4.5. Now, the file
selection dialog box for your operating system will open. Choose the _Data-_
_set.xlsx_ file, which is part of the demo data package.


**Figure 4.5** Selecting Files to Upload


If not done automatically, make sure the **Use first row as column headers**
checkbox has been selected. This step ensures that the first row of the flat
file is correctly used for the labeling of each column.


**Saving datasets** After clicking the **Import** button, provide a name and location for the dataset. For our example, let’s save this dataset directly into your personal
folder and call it “Sales Data,” as shown in Figure 4.6.



![](temp_conversion_out/main/images/024_4.2 Types of Data Models_024_4.2-Types-of-Data-Models.pdf-1-0.png)

![](temp_conversion_out/main/images/024_4.2 Types of Data Models_024_4.2-Types-of-Data-Models.pdf-1-1.png)








**Figure 4.6** Determining Locations for Datasets


After successful upload, the folder will be opened and displayed. Click on the
dataset to open it, and you’ll see its contents again, as shown in Figure 4.7.


**Figure 4.7** Dataset Preview



![](temp_conversion_out/main/images/024_4.2 Types of Data Models_024_4.2-Types-of-Data-Models.pdf-2-0.png)

![](temp_conversion_out/main/images/024_4.2 Types of Data Models_024_4.2-Types-of-Data-Models.pdf-2-1.png)









If you’ve chosen to import a dataset from a data source instead of upload

ing a flat file, the process is similar. Instead of selecting a file on your com

puter, you must first connect to the data source. Then, you can select from


among the available data providers. Within a data provider, either drag and


drop or click on items to select specific dimensions and measures, which


will be then imported as a dataset.


Datasets are needed to run predictive scenarios, which are presented in


detail in Chapter 7.


**4.2.2  Analytical Models**


While datasets solely represent tables and allow no additional semantics,


models can be more complex. A model represents data and enriches it with


additional information—like hierarchies, for example. A model also allows


the definition of additional measures or groupings of dimension members.


As long as you only want to analyze data without entering any planning


data, an analytical model offers all necessary tools and functionalities.


**Analytical model** Let’s now look at analytical models in detail. In Section 4.2.3, we’ll present
**details** planning models, which extend analytical models with some capabilities. A


special case is an analytical model based on a live connection, which is


described in Section 4.4.


**Structure of** In general, an analytical model follows a common structure. The model usu**analytical models** ally contains dimensions (including an **Account** dimension and optional


**Date** dimension), data sources, and additional information about the model.


Within the model, additional options like data access control over specific


dimensions and performance optimizations can be activated.


Figure 4.8 shows the individual components of an analytical model. In gen

eral, a model should be first filled with data. In the beginning, you can also


start with _master data_ only. Data can be, for example, acquired from a table


that imported from a data source to SAP Analytics Cloud or uploaded as a


flat file.


**Data wrangling** After the data import, you’ll be presented with the optional data wrangling


step. In this step, you can transform the data and ensure that dimensions


and measures are identified correctly. The data will be then automatically


split into master and transactional data. If you started with a blank model


without uploading any file, you must create the master data first and then


later upload the transactional data.


In addition, if supported by the data source, scheduling can be set up, which


will automatically and regularly import data from the data sources below










the model. Scheduling can be activated for each combination of model and


data source.



![](temp_conversion_out/main/images/024_4.2 Types of Data Models_024_4.2-Types-of-Data-Models.pdf-4-0.png)









**Figure 4.8** Detailed Model Structure, Based on Data Import


After successfully importing the data, it will be structured and saved in **Dimensions**
dimensions. These dimension structures follow the master data layout
(such as IDs, descriptions, and hierarchies) and are referenced by transactional data when accessing the model. A dimension can be global or private.
_Global dimensions_ can be used across multiple models, whereas _private_
_dimensions_ are only available to the model in which they were created.
Global dimensions should be used when their contents are relevant across
multiple contexts. Some examples include dimensions for products, cost
centers, or regions, which are usually maintained centrally and can be
directly reused across multiple models.


Besides master data, dimensions can carry additional information, like
hierarchies or authorizations. This info is maintained on the dimension
level. Measures are structured in account dimensions (following the
account-based model).


Model-wide settings also can be configured, including the following: **Model settings**


- Currencies


- Performance optimizations


- Model privacy


- Data access control


We’ll discuss each of these settings in detail in Section 4.5.2.


An analytical model based on a live connection is a special case. Because **Analytical models**
live data sources usually aren’t directly exposed to users, they’re repre- **for live connections**
sented by models. As a result, the general model concept still applies in this
case. The components of this special kind of model are shown in Figure 4.9.











![](temp_conversion_out/main/images/024_4.2 Types of Data Models_024_4.2-Types-of-Data-Models.pdf-5-0.png)







**Figure 4.9** Detailed Model Structure, Based on Live Connections


**Metadata** In this scenario, the data is completely virtual. The model only points to the
actual data source and simply carries information about its columns and
measures. More information about this data, which is also called _metadata_,
can be found in Chapter 2, Section 2.2.1.


**Semantics** However, models based on live connections still allow you to define additional semantics. Depending on the data source, dimensions can be grouped,
renamed, or hidden. If a data source supports geographical data, this aspect
can be indicated in the model. In addition, some data sources support the creation of additional measures or calculations in the model via formulas.


**4.2.3  Planning Models**


The general structure of a planning model is rather similar to that of an analytical model. Therefore, not every element will be described in detail in
this section. However, a planning model extends an analytical model by
various functionalities that are necessary for planning activities later and
to establish planning workflows.



**Additional**
**configurations**
**and functionality**



Examples of additional functionalities in planning models include the following:


- Categories to map versions (e.g., budget, plan, forecast)


- Preconfigured time dimensions, which can be adjusted to match the
dates in your data


- Audit functionality to track and trace model changes


- Additional data authorization features to control data visibility


Also, only planning models allow users to enter data into them. Specifically,
workflows enable users to enter new values or modify existing ones by
editing existing versions (e.g., actual or forecast) or by the creation of new
private versions that are later published. Planning models also support
comments on specific data points, the allocation of values, and data entry








