---
tags:
source: 023_4.1 Why Use Data Models.pdf
title: 023_4.1 Why Use Data Models
---



**4.1  Why Use Data Models?**


**Data and** Although nothing reflects the truth better than data, understanding your
**information** data is difficult without the proper semantics. Also, since data points are
specific, they often just show a small part of the big picture. Therefore, you
may need to get datasets from multiple sources and relate them to each
other.


In general, data will need to be enriched by information to actually become
knowledge, as shown in Figure 4.1. This enrichment is a key idea of a data
model, which can equip data with semantics so that the data can be analyzed.

|Data|Col2|
|---|---|
|Data||


|Information|Col2|
|---|---|
|Information||



**Figure 4.1** From Data to Knowledge


SAP Analytics Cloud follows this principle and offers multiple options for
enriching data with information or with semantics so that your data can be
used for analysis and visualization.


**Data models** The foundation for this capability is the _data model_ . In SAP Analytics Cloud,
a data model can represent all kinds of data, independent of whether the
data is imported, retrieved from a live connection, or uploaded as a flat file.
In the case of a live connection, the data model is only stored partially in
SAP Analytics Cloud because of the connection design. When connecting to
SAP Business Warehouse (SAP BW), for example, the data model itself must
already be defined in the data source (SAP BW), and SAP Analytics Cloud or
the user simply consumes the data. This approach is also valid for other live
data sources. Although SAP Analytics Cloud allows you to define additional
semantics on top of live data, you can’t change the data or the model completely. When importing data into SAP Analytics Cloud, all modeling activities are performed in the solution.


**Models**


For simplicity’s sake, we’ll refer to data models simply as models from now
on. Both terms are synonymous in this case.


**Model types** SAP Analytics Cloud supports various model types that can be used for different scenarios. Some model types offer more flexibility but require more



![](temp_conversion_out/main/images/023_4.1 Why Use Data Models_023_4.1-Why-Use-Data-Models.pdf-0-0.png)








information and data. Others are only available with specific licenses. This
limitation applies to planning models, for example, which require a dedicated license to create them. We’ll describe model types in detail in Section
4.2.


When creating stories and applications or exploring data, users in SAP Ana- **Imported data**
lytics Cloud generally interact with models. These models can be created **model**
either up front or, depending on the data source, during the creation of a
new story. In general, the model carries multiple pieces of information.
Besides transactional and master data, a model also contains information
about the data sources and potential scheduling jobs, as shown in Figure
4.2. The _semantics_ of a model can be used to give your data meaningful
descriptions and interpretations.

|Model<br>Semantics<br>Data<br>Data Sources and Scheduling|Col2|Story|
|---|---|---|
|Data<br>**Model**<br>Semantics<br>Data Sources and Scheduling|Data<br>**Model**<br>Semantics<br>Data Sources and Scheduling|Data<br>**Model**<br>Semantics<br>Data Sources and Scheduling|
|Data Source|||



**Figure 4.2** Simple Version of Model for Import Connection


After successfully uploading or importing data into SAP Analytics Cloud, **Data wrangling**
the data wrangling process will be initiated. During this process, data can be
manipulated, and quality issues can be resolved. Users can use multiple
transformations to run various operations on the data. The data wrangling
process can be launched again later but should be used initially to define a
model structure. More information on data wrangling is presented in Section 4.3.


Semantics play an important role in data modeling by determining if a col- **Semantics**
umn represents a measure or a dimension. In addition, semantics also define
additional elements, like date columns or hierarchical relationships between
individual columns. Semantics are therefore essential to data models.


Models can be configured to automatically refresh their data from the data **Scheduling**
source, which is also called _scheduling_ . This feature, however, is only supported for import connections and a selection of data sources. More information on this topic can be found in Chapter 2, Section 2.2.2.










Ultimately, the model acts as the data source in a story or a report. The
architecture shown in Figure 4.2 is valid for imported data mainly. In general, SAP Analytics Cloud understands already defined semantics in data
sources but allows users to adjust semantics during the upload process.
Models can also be exported again.


**Models for live** When using a live connection, a data model is still needed but doesn’t play
**connections** such a big role. The model is still the layer between a story and a data source
and allows for minor adjustments or enhancements.


**Additional** To better understand what’s meant by additional semantics, as shown in
**semantics** Figure 4.3, let’s look an example. When using a live connection to an SAP
BW system, only SAP BW queries are accessed.

|Model<br>Additional Semantics|Col2|Story|
|---|---|---|
|**Model**<br>Additional Semantics|**Model**<br>Additional Semantics|**Model**<br>Additional Semantics|
|Data Source|||



**Figure 4.3** Simple Version of Model for Live Connection


These queries already expose modeled data. Queries can contain data from
multiple sources, and they already contain information about measures
and dimensions. Sometimes, they even expose a default layout or complex
calculations. You still must create a model in SAP Analytics Cloud to build a
story, but this model only contains information about the SAP BW query
(query name, system, list of dimensions and measures) and no transactional data. The model creator can still define additional semantics on top
of the model, like hidden or renamed dimensions. In a story, you can also
create calculations on top of an SAP BW query.


**Flexibility** Neither the data itself nor the SAP BW query definition can be modified in
the model anymore. Thus, the model is only able to enrich the existing data
source. The reason for this limitation lies behind the architecture of the live
connection. Because the browser directly accesses the data source, at no
point in time does SAP Analytics Cloud have access to the transactional
data. Therefore, no ability exists for manipulating the data in the cloud.
More information about these technical limitations can be found in Chapter 2, Section 2.2.1.


**Other live** Although our example uses an SAP BW connection, these considerations
**data sources** apply to other live data sources as well. Only in the case of connecting a live








