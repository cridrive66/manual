.. important::
   This version of the manual is still under writing. 

.. _Flow_Estimation:

Flow Estimation
===============

The *Flow Estimation* provides an estimation of yearly mean flow and yearly mean low fow for each subcatchment or 
river section within a specified catchment area. This estimation is made by **Random Forest** (`source <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html>`_), 
which uses the catchment's geographical characteristics as predictors and water flow data collected from gauging stations
to calibrate and validate the approach.

This group of tools is divided in 4 different processes:

.. toctree::
  :maxdepth: 1

  fix_river
  contributing_area
  calculate_geofactors
  flow_estimation_model

Each tool is documented in the following sections with explanations of its functionality and step-by-step tutorials.