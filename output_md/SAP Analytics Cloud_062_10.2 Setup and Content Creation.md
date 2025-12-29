---
tags:
source: 062_10.2 Setup and Content Creation.pdf
title: 062_10.2 Setup and Content Creation
---

# 10 SAP Analytics Hub and the Analytics Catalog for SAP Analytics Cloud


**Figure 10.3** Single Asset in SAP Analytics Hub


All configurations and adjustments to SAP Analytics Hub itself are performed in its administration cockpit (see Section 10.2.1). The contents of the
assets are managed within a dedicated interface (see Section 10.2.2). Users
require a specific role to see both views. However, administrator rights are
not needed to just create content for SAP Analytics Hub.


User management for SAP Analytics Hub is completely managed in SAP
Analytics Cloud (see Chapter 3, Section 3.3.1). Within the user management
interface, you can unlock SAP Analytics Hub for specific users or roles.


**10.2  Setup and Content Creation**


In this section, we’ll set up SAP Analytics Hub and add content to it. If you
want to follow along fully with this section, you’ll need the Analytics Hub
Admin role assigned (see Chapter 3, Section 3.3.1). Users who want to add
content to SAP Analytics Hub need at least the Analytics Hub Content Creator role. For simple access to the hub, you must assign users the Analytics
Hub Viewer role. In general, all users and roles are managed within SAP
Analytics Cloud, as shown in Figure 10.4. As this topic was covered in Chapter 3, Section 3.3.1, in detail, we won’t expand further here.



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-0-0.png)








**Figure 10.4** Roles for SAP Analytics Hub


SAP Analytics Hub can be accessed from SAP Analytics Cloud directly. **Launching**
Either use the app switch in the top right or select **Browse** - **Analytics Hub** **SAP Analytics Hub**
from the main menu. If you can’t see the entry, you may not have sufficient
licenses or roles assigned to your user.


**10.2.1  SAP Analytics Hub Cockpit**


Click on the main menu of SAP Analytics Hub in the top left and select **Opening the cockpit**
the **Cockpit** option, as shown in Figure 10.5.


**Figure 10.5** Main Menu of SAP Analytics Hub


The overview page of the cockpit provides quick access to all the settings and **Overview**
statistics for SAP Analytics Hub, as shown in Figure 10.6. All these settings
and dialog boxes can also be accessed from the navigation pane on the left.


**Figure 10.6** SAP Analytics Hub Cockpit



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-1-0.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-1-1.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-1-2.png)






# 10 SAP Analytics Hub and the Analytics Catalog for SAP Analytics Cloud


**Usage statistics** The statistics on the overview page provide initial insights about the usage
of SAP Analytics Hub and the most viewed assets. The **Usage Statistics** page
offers more details and shows all available data. Use this page to analyze
SAP Analytics Hub usage in detail, as shown in Figure 10.7.


**Figure 10.7** Usage Statistics


**Maintenance** SAP Analytics Hub must be put into maintenance mode before changing
any essential elements like the asset structure. This screen can be accessed
by clicking on **Maintenance** in the menu. On the maintenance page, you
can set up how long the maintenance mode will last and which user groups
should be affected, as shown in Figure 10.8.


**Figure 10.8** Maintenance


You must first click on the **Edit** button to perform changes to the timeframe. All changes are saved after clicking on **Update** . The maintenance
mode can be activated by clicking on the switch next to **Activate** .



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-2-0.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-2-1.png)








By default, all assets in SAP Analytics Hub are stored in one language (e.g., **Translation**
English). If you want to provide your content in more than one language,
you can active the translation dashboard on the **Translation** page, as shown
in Figure 10.9. Note that all assets should be stored in one language before
activating the translation feature.


**Figure 10.9** Translation


The general template for each asset in SAP Analytics Hub can be changed on **Layout**
the **Layout** page. You can move, edit, and remove fields, as shown in Figure
10.10. All changes are made via a graphical interface that provides an
instant preview of the template.


**Figure 10.10** Editing Asset Layout



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-3-0.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-3-1.png)






# 10 SAP Analytics Hub and the Analytics Catalog for SAP Analytics Cloud


**Adding sections** New sections can be added below each section by clicking on **Add Section** .
When hovering your mouse over any section, you’ll see options for removing or replacing the section with another section. Those sections are later
filled in with content by content creators.


You can also hide and show fields. These fields are not shown in the asset
view but can still be used in searches and to refine filter selections in SAP
Analytics Hub.


**Fields** All fields that are available in SAP Analytics Hub are maintained on the
**Fields** screen, as shown in Figure 10.11. Fields can contain texts, links, or a list
of values defined separately.


**Figure 10.11** Creating Fields


**List of values** If a field references a list of values, these values must be maintained on the
**List of Values** screen, as shown in Figure 10.12. The list of values can be used
later within assets and provides a predefined selection to avoid typos or
incorrect entries. When creating the list of values, you can automatically
create a field based on this list (by selecting the **Create a field based on this**
**LOV** checkbox).


**Facets** If the list of values should appear in the filter sidebar of SAP Analytics Hub,
it must be activated as such on the **Facets** screen, as shown in Figure 10.13.
You can change the order of appearance and the order in which the values
are sorted. The live preview on the right shows the effect of your changes
immediately.



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-4-0.png)








**Figure 10.12** Creating List of Values


**Figure 10.13** Facets


The **Branding** area gives you the ability to customize the design of SAP Ana- **Branding**
lytics Hub and adjust it meet to your company’s style guidelines. Figure
## 10.14 shows the header management section where you can upload a custom logo and change the background of the header. If you select the **Use**
**logo as favicon** option, the logo will also be shown in the address bar of the
browser. Alternatively, you can upload a dedicated favicon.



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-5-0.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-5-1.png)






# 10 SAP Analytics Hub and the Analytics Catalog for SAP Analytics Cloud


**Figure 10.14** Adjusting Headers


**Home screen** The homepage layout can be modified as well. The process is quite similar
to modifying the asset layout, as shown in Figure 10.15.


**Figure 10.15** Adjusting Homepage


New sections can be added that contain either a fixed selection of assets or
contain a search query to only show specific topics. All sections can be
renamed, removed, or changed in their position.


**Hub data and** The **Hub Data** and **Audit Log** menu items provide interfaces to export and
**audit log** import SAP Analytics Hub configurations and structures and to monitor all
activities in SAP Analytics Hub.


You can switch back to the content view of SAP Analytics Hub by clicking on
the **Go to Hub** button in the top right.


**10.2.2  Edit Mode and Content Management**


SAP Analytics Hub content is directly edited within the repository view. If a
user has at least the Analytics Hub Content Creator role, that user can
switch to edit mode for content and lifecycle management.



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-6-0.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-6-1.png)








Go to **All Assets** and click on the **Edit mode** button in the top right to switch to **Edit mode**
edit mode, as shown in Figure 10.16. Then, click on any asset in the repository.


**Figure 10.16** Editing Assets in Edit Mode


The buttons shown in Figure 10.16 can be used to perform the following
actions:


# 1 By clicking on the plus icon **+**, you can add a new asset and fill it with contents of a new report. Once you save the asset, it will be saved as a draft
that has to be validated in content management.




# 3 Click on the pencil icon to edit the currently selected asset.


# 4 If you don’t want an asset to be shown in the list, you can hide it by clicking on the **Hide** icon.




SAP Analytics Hub also provides lifecycle content management capabilities to **Content**
validate new assets and make hidden assets visible again. Click on the **Asset** **management**
**Management** tab on the top to navigate to the content management area, as
shown in Figure 10.17. Make sure you’re still in edit mode and select an asset.


**Figure 10.17** Content Management



![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-7-0.png)

![](temp_conversion_out/main/images/062_10.2 Setup and Content Creation_062_10.2-Setup-and-Content-Creation.pdf-7-1.png)






