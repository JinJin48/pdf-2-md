---
tags:
source: 053_8.3 Custom Widgets.pdf
title: 053_8.3 Custom Widgets
---



**Figure 8.32** OData Service Configuration


**Further Resources**


Because the analytics designer is a development environment that provides endless possibilities, we can’t cover it in full in this book. However,
SAP provides extensive and free documentation offering a great collection
of code samples and use cases.


You can download the Analytics Designer Handbook for free at _[http://s-](http://s-prs.co/v218507)_
_[prs.co/v218507](http://s-prs.co/v218507)_ as a PDF file. The document is updated regularly and is the
recommended resource for all information about the analytics designer
and supported functionalities.


**8.3  Custom Widgets**


Because applications can become rather unique and the need for customization is quite high in some use cases, SAP Analytics Cloud provides a custom widget software development kit (SDK). With this SDK, you can create
your own JavaScript widgets and integrate them into your applications.


**Custom Widgets** A custom widget is a chart or other data visualization element which was
built custom and is not delivered out-of-the-box. It is very useful for individual use cases in which the standard charts are not sufficient. An example
for a custom widget is shown in Figure 8.33. It shows the seatmap of an airplane for a specific flight and the airplane’s seating capacity.



![](temp_conversion_out/main/images/053_8.3 Custom Widgets_053_8.3-Custom-Widgets.pdf-0-0.png)








**Figure 8.33** Custom Widget Example


Creating custom widgets requires advanced programming knowledge, but **Requirements**
custom widgets are powerful because they behave like any other widget on
the canvas and can even expose endpoints, which can be called by any
other script in the application. To create widgets, you must be familiar with
HTML, CSS, and JavaScript. On top of that, you must be able to host parts of
the widget code on servers that you own and that are reachable for your
end users.


**Using Custom Widgets**


Custom widgets are developed outside of SAP Analytics Cloud and are only
embedded within SAP Analytics Cloud. You can use any development environment compatible with JavaScript to create them. The code must then
be uploaded to your own web server, which must be publicly reachable
from the internet. If you have access to such an environment, you can follow the examples in this chapter.


In general, a custom widget contains the following elements, which you
must provide when creating them:


- **Custom widget as a JSON file**
This file contains the metadata of the custom widget (such as name, ID,
version, etc.)


- **Web component as a JavaScript file**
This is the actual widget implementation. You can provide multiple files
for complex widgets.



![](temp_conversion_out/main/images/053_8.3 Custom Widgets_053_8.3-Custom-Widgets.pdf-1-0.png)








          - **Web component as a JavaScript file for the builder (optional)**
If you want your users to be able to modify the custom widget in the
builder, you can implement these settings in this file.


          - **Web component as a JavaScript file for the** **Formatting** **tab (optional)**
Similar to the JavaScript file for the builder, this file defines the contents
for the **Formatting** tab for a custom widget.


          - **Icon file**
This is the icon that appears for the custom widget in the overview.


**Code samples for** Creating a custom widget also requires additional resources. We will now
**this section** go through an example of this. You can find all code elements in the SAP
Help Portal at _[http://s-prs.co/v502620](http://s-prs.co/v502620)_ . In this example, we will create a colored box chart. All code elements are described in detail in the SAP Help
Portal.


**Preparing custom** First, create the files _coloredbox.js_, _coloredbox_styling.js,_ and _coloredbox__
**widgets** _builder.js_ on your server. You can find the contents of each file in the SAP
Help Portal. On top of that, you need the file _icon.png_ . That file must be
stored on the server as well. For the icon, you can use any image with a size
of 16x16px. A sample file can be found within the downloadable material on
the publisher's website at _[www.sap-press.com/5753](http://www.sap-press.com/5753)_ under **Product supple-**
**ments** .


You also have to create the _coloredbox.json_ file on your own computer
based on the sample code in the product help. Replace all URLs in the code
that contain “sample.com” with the URL or IP address of your own web
server. The relevant part of the file is shown in Listing 8.5.


{
"id": "com.sap.sample.coloredbox",
"version": "1.0.0",
"name": "Colored Box",
"description": "A colored box",
"newInstancePrefix": "ColoredBox",
"icon": "https://www.sample.com/customwidgets/coloredbox/icon.png",
"vendor": "SAP",
"eula": "",
"license": "",
"webcomponents": [
{
"kind": "main",
"tag": "com-sap-sample-coloredbox",
"url": "https://www.sample.com/customwidgets/coloredbox/
coloredbox.js",
"integrity": "",










"ignoreIntegrity": true
},
{
"kind": "styling",
"tag": "com-sap-sample-coloredbox-styling",
"url": "https://www.sample.com/customwidgets/coloredbox/coloredbox_
styling.js",
"integrity": "",
"ignoreIntegrity": true
},
{
"kind": "builder",
"tag": "com-sap-sample-coloredbox-builder",
"url": "https://www.sample.com/customwidgets/coloredbox/coloredbox_
builder.js",
"integrity": "",
"ignoreIntegrity": true
}
],


**Listing 8.5** Excerpt from the Coloredbox.json File


After adjusting this file and uploading the other files to your webserver, **Embedding custom**
you can embed the custom widget into SAP Analytics Cloud. Open the main **widgets**
menu and navigate to **Analytic Applications** - **Custom Widgets** and click on
the Plus button on the top right. Click on **Select File** and choose the _colored-_
_box.json_ file from your computer, then click on the **OK** button as shown in
Figure 8.34.


**Figure 8.34** Uploading the JSON File


After successfully embedding the file, the list of custom widgets will contain a new entry (see Figure 8.35). The yellow triangle indicates that the custom widget is not yet available for productive usage.



![](temp_conversion_out/main/images/053_8.3 Custom Widgets_053_8.3-Custom-Widgets.pdf-3-0.png)






