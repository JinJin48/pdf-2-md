---
tags:
source: 034_5.5 Geo Maps.pdf
title: 034_5.5 Geo Maps
---



Because we want to have the total at the end of the table, open the builder
and activate the **Arrange Totals/Parental Nodes Below** option. Now, all
totals and parental nodes will be displayed below their children.


Save the story and validate your progress by comparing your story to the
_Checkpoint 2 – Section 5.4.pdf_ file from the demo data package.


**5.5  Geo Maps**


An especially useful feature of SAP Analytics Cloud is its embedded geo
map functionality. Shipped by default with the product, the data model
must include geographical information (see Chapter 4, Section 4.3.2). A geo
map is inserted into a story as a separate object but is treated like any normal chart.


Let’s add a third page to our story of the type **Canvas** . Then, click on the **+** **Creating geo maps**
button in the top bar and choose **Geo Map** . Extend the size of the geo map.


The geo map generally follows a content layer-based concept. Starting with **Content layers**
the base layer, you can add multiple layers to one geo map, with which you
can visualize geographical data. The base layer is used to determine the
map shown in the background. The content layers then retrieve data from
models and show the location dimension members on the map.


**Figure 5.63** Builder for Geo Maps



![](temp_conversion_out/main/images/034_5.5 Geo Maps_034_5.5-Geo-Maps.pdf-0-0.png)








**Builder** The builder for a geo map is different from the one used for charts and
tables, as shown in Figure 5.63. You can create all content layers in the
builder and choose which map is used for the base layer. You can also configure which zoom level should be shown by default. If a filter is set, the
map can automatically zoom in on the filtered data.


**Creating content** First, we’ll change the base layer map. Click on the map icon next to **Base-**
**layers** **map** and select the **Streets** map. Then, click on **Add Layer** to add a new content layer. The newly created content layer will be empty, which means you
must select a model first. Click on the pen button and select the **Sales Data**
model. Next, you must select the layer type. An overview of all layer types
is shown in Table 5.3. Leave the default settings so that the **Bubble Layer**
type is selected.

|Layer Type|Use Case|
|---|---|
|**Bubble Layer**|Shows individual points at specific locations that can<br>differ in color and/or size based on measures.|
|**Point of Interest Layer**|Shows locations without measures. This layer is only<br>available in classic mode.|
|**Heat Map Layer**|Shows the distribution of values around individual<br>locations and how high or low they are.|
|**Choropleth/Drill Layer**|Supports displaying geographical hierarchies.|
|**Feature Layer**|This layer can embed external shapefiles provided by<br>an Esri ArcGIS server. These files can be used to show<br>roads, specific regions, or streets, for example. This<br>layer is only available in classic mode.|
|**Flow Layer**|Shows flows between two locations. The thickness and<br>color of each line can be driven by a measure. This layer<br>is only available in classic mode.|



**Table 5.3** Layer Types for Geo Maps


Select the **Stores** dimension and select **Quantity** for the **Bubble Color** option
and **Revenue** for the **Bubble Size** option. Compare your screen to the screen
shown in Figure 5.64. In the builder, you can further define how bubble colors and sizes are affected by a measure.


**Cluster properties** Under **Cluster Properties**, you can turn **Location Clustering** off and on. Clustering will automatically group locations that are close to each other to reduce
the number of data points on a map. This option also greatly improves the
loading time for a story if many data points are shown on the map. Let’s keep
this option activated and confirm the content layer by clicking on **OK** . The










resulting map should match the screen shown in Figure 5.65. Rename the
map’s title to “Supermarkets.”


Double-click anywhere on the map to zoom in or use your mouse’s scroll **Zooming and**
wheel to zoom in and out of the map. You can move around the map by **moving**
clicking on it and then holding the left mouse button down while moving
around the mouse.


**Figure 5.64** Creating New Content Layer



![](temp_conversion_out/main/images/034_5.5 Geo Maps_034_5.5-Geo-Maps.pdf-2-0.png)






