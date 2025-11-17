.. _risk-assessment:

Risk Assessment
---------------
This tool calculates the final risk for each river section. So far, only environmental risk assessment (ERA) is considered and can be calculated like 
shown in :math:numref:`ERA_equation`.

.. math::
    :label: ERA_equation

    ERA = \frac{PEC}{PNEC_{ERA}}
    

With:

- :math:`ERA` = Environmental Risk Assessment [-] 
- :math:`PEC` = Predicted Environmental Concentration [:math:`ng/L`]
- :math:`PNEC_{ERA}` = Predicted No Effect Concentration for ERA [:math:`ng/L`]

In addition to individual PNEC calculations, a cumulative Risk Quotient (RQ) coefficient is calculated to provide an overall assessment when
multiple APIs are selected. This single value summarizes the combined risk from all tested substances in each river section, giving the 
user a quick, comprehensive view of the situation. The Risk Quotient is calculated using formula :math:numref:`logistic-function`.

.. math::
    :label: logistic-function

    RQ(x) = \frac{s}{1 + e^{-k(x-x_0)}}
    

With:

- :math:`RQ` = Risk Coefficient [-] 
- :math:`x` = sum of ERA values > 1 [-]
- :math:`s` = height parameter [-]
- :math:`k` = scale factor [-]
- :math:`x0` = midpoint value [-]


Input data
^^^^^^^^^^
Only one input file is necessary:

* **river_accumulation.shp**

This file is the output of the :ref:`accumulation` tool. The key columns for this process are the ones containing concentration values. For each river section,
formula :math:numref:`ERA_equation` is applied and a PNEC value is calculated. 

Workflow
^^^^^^^^

1. If not already in the project, add the input data by clicking on "Layer -> Add Layer -> Add Vector Layer"
2. Go in the Processing Toolbox and look for the *APRIORA* plugin. Click on *API emission* and open *8 - Risk Assessment*
3. Choose **river_accumulation.shp** as input for *River network*
4. Select the fields containing the concentration of APIs for the risk assessment. This selection should include only columns containing concentrations in ng/L.
5. If you added custom PNEC values from the *API parameter selection* tool, flag the next box, otherwise leave it empty
6. Click on *Run*

.. raw:: html

   <figure>
     <video width="700" height="370" controls>
       <source src="_static/video/risk_assessment_2.mp4" type="video/mp4">
       Your browser does not support the video tag.
     </video>
     <figcaption>Video: Worflow of the <i>Risk Assessment</i> tool.</figcaption>
   </figure>


Output data:

* **risk_assessment.shp**

The output is a line shapefile containing the same geometry of **river_accumulation.shp**. The attribute table instead, has the same API concentration columns 
plus ERA fields for both condition (mean flow and mean low flow) for each API selected. Finally, the last two columns represent RQ for the same two condition.
:numref:`risk_assessment_table` shows an example of a part of the attribute table.

.. _risk_assessment_table:

.. list-table:: Example of attribute table of risk_assessment.shp.
    :header-rows: 1
    :widths: 15 15 15 15 15 15

    * - conc_Carb [#f1]_
      - conL_Carb [#f2]_
      - era_Carb [#f3]_
      - eraL_Carb [#f4]_
      - cumul_RQ [#f5]_
      - cumul_RQ_L [#f6]_
    * - 89.309
      - 459.004
      - 0.035
      - 0.183
      - 0.999
      - 1
    * - 77.771
      - 399.703
      - 0.031
      - 0.159
      - 0.999
      - 1
    * - 36.737
      - 188.808
      - 0.015
      - 0.075
      - 0.007
      - 1
    * - 5.778
      - 29.699
      - 0.002
      - 0.012
      - 0.007
      - 0.007
    * - 0.789
      - 4.056
      - 0.0003
      - 0.002
      - 0.007
      - 0.007
    
.. [#f1] Concentration of Carbamazepine in normal conditions [:math:`ng/L`]
.. [#f2] Concentration of Carbamazepine in low flow conditions [:math:`ng/L`]    
.. [#f3] Environmental Risk Assessment of Carbamazepine in normal conditions [-]
.. [#f4] Environmental Risk Assessment of Carbamazepine in low flow conditions [-]
.. [#f5] Risk Quotient in normal conditions [-]
.. [#f6] Risk Quotient in low flow conditions [-]

The style of **risk_assessment.shp** is based on the value of RQ and it is possible to change it by going on "Layer Properties" -> "Symbology".
