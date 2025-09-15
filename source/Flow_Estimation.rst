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


Fix River Network
-----------------

Here we discuss what the Fix River Network is about.

Importance of NET_ID and NET_TO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NET_ID and NET_TO are very important because they explain the relationship of the river network.

Non-aligned river sections
^^^^^^^^^^^^^^^^^^^^^^^^^^

It can happen that there is a misalignment between the river sections and the subcatchments. Here we fix it.

Why to fix it?
""""""""""""""

We fix it because otherwise the model struggle to understand where the water is flowing and it can cause errors or over/under estimation during the flow model.


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