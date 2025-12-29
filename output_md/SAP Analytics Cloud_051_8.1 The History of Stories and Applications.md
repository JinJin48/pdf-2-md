---
tags:
source: 051_8.1 The History of Stories and Applications.pdf
title: 051_8.1 The History of Stories and Applications
---

# Chapter 8 **Advanced Development Environment**

_The advanced capabilities in SAP Analytics Cloud stories allow power users_
_to create advanced reports extended by scripting. This chapter will intro-_
_duce you to the concept of applications and provide simple examples to_
_help you learn to create your own applications._


In addition to stories, SAP Analytics Cloud provides another user interface
(UI) to develop complex reports. The _analytics designer_, which was released
in the second quarter of 2019, provides tools to create rather complex applications that meet individual needs by using scripting and programming.
Starting in 2023, SAP began merging both environments into the optimized
story. This concept is also called the unified story.


The advanced development environment, however, exclusively targets **Requirements**
advanced users who have programming or scripting expertise. Applications are developed by using a programming language that’s similar to
JavaScript. Developers who’ve already developed reports in SAP Lumira,
designer edition (formerly known as SAP BusinessObjects Design Studio)
can easily adapt to the environment in SAP Analytics Cloud. In this chapter,
you’ll first learn more about the differences between a simple story and an
application/advanced story and when to use what. Then, the advanced
development environment will be presented, where we’ll develop a small
basic application. This chapter will conclude with an outlook of future
developments and resources.


**8.1  The History of Stories and Applications**


While stories are covered in detail in Chapter 5, this chapter will introduce
you to the concept of _applications_ .



![](temp_conversion_out/main/images/051_8.1 The History of Stories and Applications_051_8.1-The-History-of-Stories-and-Applications.pdf-0-0.png)








**Story scope** A story primarily focuses on reporting and interactivity. By providing a
wide range of tools to create visualizations and interactive controls for
viewers, stories are flexible and can be used for many complex use cases.


The story environment guides the creator through most of the process. By
using guided dialog boxes and automatic functionalities, story creators can
easily add input controls or filters to a story, which can be used interactively by viewers, for instance, the input controls shown in Figure 8.1.


**Figure 8.1** Example Story Input Controls


**Application scope** The application, however, offers a significantly higher degree of freedom
but follows a less guided approach. The original analytics designer was
based on a separate development environment, shown in Figure 8.2, in
which a developer could use various tools and functions to create a complex dashboard.


**Development** Similar to developing computer programs, application developers can
**environment** implement their own algorithms and logic by writing code in SAP Analytics
Cloud. However, developers are still supported by graphical interfaces to
create charts and tables or to apply simple formatting. Developers can use
the standard tools for simple tasks and invest their time and effort mainly
into crafting complex scenarios.



![](temp_conversion_out/main/images/051_8.1 The History of Stories and Applications_051_8.1-The-History-of-Stories-and-Applications.pdf-1-0.png)








**Figure 8.2** Development Environment for Applications


Applications are usually executed by users in the business units of your **Executing**
company. These users interact with applications in the same way they **applications**
interact with stories. Some users may not even notice the difference. The
application shown in Figure 8.3 is separated into two views. The overview
shows various key performance indicator (KPI) tiles, which a user can click
to access more details about each KPI. Users can also click on the **Analytics**
button on the left to launch another view, which contains interactive elements and charts.


**Figure 8.3** Executed Application



![](temp_conversion_out/main/images/051_8.1 The History of Stories and Applications_051_8.1-The-History-of-Stories-and-Applications.pdf-2-0.png)

![](temp_conversion_out/main/images/051_8.1 The History of Stories and Applications_051_8.1-The-History-of-Stories-and-Applications.pdf-2-1.png)






