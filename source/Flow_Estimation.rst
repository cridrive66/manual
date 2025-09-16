.. _Flow_Estimation:

Flow Estimation
===============

The *Flow Estimation* provides an estimation of yearly mean flow and yearly mean low fow for each subcatchment or 
river section within a specified catchment area. This estimation is made by **Random Forest** (insert link), which
uses the catchment's geographical characteristics as predictors and water flow data collected from gauging stations
to calibrate and validate the approach.

This group of tools is divided 4 different processes:

* Fix River Network
* Contributing Area
* Calculate Geofactors
* Flow Estimation


**insert plugin scheme**


Fix River Network
-----------------
Understanding the flow direction (where the water is going and which other river section it contributes to) is a critical aspect of the river network.
This information is very important for calculating the flow of each river section and determining accumulated values. 
Also, in many cases the intersection between the river network and the subcatchments is not perfectly aligned. This misalignment can cause issue in later 
steps of the plugin, so better fix the input beforehand! 

This algorithm was developed from the plugin *WaterNetAnalyzer* by Jannik Schilling (insert link).

NET_ID and NET_TO are very important because they explain the relationship of the river network.

It can happen that there is a misalignment between the river sections and the subcatchments. Here we fix it.
We fix it because otherwise the model struggle to understand where the water is flowing and it can cause errors or over/under estimation during the flow model.

**insert picture of river and subcatchments misalignment**

If the misalignment is greater than 10 cm, the plugin will not fix it and it is necessary to manually adjust the input file. Check the :ref:`Troubleshooting` section
for more information about it.

Input data
^^^^^^^^^^
Two input data are necessary for this tool:

* **subcatchments.shp**
* **river_network.shp**

The **subcatchments.shp** is a polygon shapefile that describes the division of the catchment in water basins.
The **river_network.shp** is a line shapefile that represents the river network within the catchment. It is important that all the sections are connected
to each others without gaps. It is also required a precise alignment between the river network and the subcatchments (like already explained above).


Workflow
^^^^^^^^

1. Add all the input data to the project by clicking on "Layer --> Add Layer --> Add Vector Layer"
2. Go in the Processing Toolbox and look for the *APRIORA* plugin. Click on *Flow estimation* and open *1 - Fix River Network*
3. Choose **subcatchments.shp** as input for *Catchment areas*
4. Choose **river_network.shp** as input for *River network*
5. Click on the three dots and click on the outlet point of the river network. The point selected does not have to be exactly on the outlet, just approximately there.
6. Click on *Run*

.. image:: images/Fix_river_network_1.png

Output data:

* **fixed_river_network.shp**

Two new columns have been added to the attribute table: NET_ID and NET_TO. These columns represent the river network ID of each specific section and the river network ID of
where the water is going. Before continue, it is important to check if the new colums are populated correctly for all river sections. If any value under NET_TO is unconnected,
it might be due to the fact that the river sections are not connected with each others. Check the geometry of the unconnected river sections, manually adjust them and re-run the
tool until there are no unconnected values in the NET_TO column. Important: apply the changes to **river_network.shp** and not to **fixed_river_network.shp**. 


Contributing Area
-----------------
We have gauging stations and we want to calculate their contributing area.

How to do it?
^^^^^^^^^^^^^
We do it using it a nice algorithm.


Calculate Geofactors
--------------------
The geofactors are very important for the model. They are the predictors of the model and they are describing certain characteristics of the subcatchments.


Flow Estimation
---------------
This is the last part of the model where we estimate the flow.

Random Forest Regressor
^^^^^^^^^^^^^^^^^^^^^^^
This is the model used for estimating the flow.