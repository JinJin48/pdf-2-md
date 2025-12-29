---
tags:
source: 021_3.5 Summary.pdf
title: 021_3.5 Summary
---



you connect to a live data source, this information will not be persisted and
is instead only used once to test the connection. If other users want to use
this connection later, users must provide their own credentials to authenticate against the data source.


Within the **Advanced Features** area of the connection, the SAP BW connection can be made available for scheduling and access through SAP Support
(see Figure 3.45). In this scenario, data has to be processed through SAP servers, but it allows you to create reports automatically on a scheduled basis.


**Figure 3.45** Advanced Features of an SAP BW Live Connection


When setting up an import connection, however, you have the option to **Credentials for**
persist the user name and password and have it automatically shared once **import connections**
you share the connection (see Chapter 2, Section 2.2).


Live connections don’t have to be shared since they are visible to every user
by default. When importing data, SAP Analytics Cloud will use the provided
credentials to import all data. You can then set permissions on the
imported data in the model. The model creation process is described in
detail in Chapter 4.


**3.5  Summary**


In general, SAP Analytics Cloud is marketed as an intuitive and easy-to-use
solution that provides users a jumpstart into reporting. Nevertheless,
preparation may need to be performed up front and planned out in detail.
Before using SAP Analytics Cloud productively, administrators should



![](temp_conversion_out/main/images/021_3.5 Summary_021_3.5-Summary.pdf-0-0.png)








think of an operational concept first. Depending on the size of the planned
landscape, additional effort may be necessary. Therefore, you should discuss the questions listed in Section 3.2 carefully. All tools for configuring
and setting up SAP Analytics Cloud are described in detail in Section 3.3.
You should also make sure to create connections that will be used by a
broad number of users.


Now that you’ve finished setting up SAP Analytics Cloud, you’re ready to
upload some data into the system. In the next chapter, you’ll learn about
various model types and create your own data model.








