.. _emission-loads:

Emission Loads
--------------
This tool calculates the load of previously selected APIs at each WWTP within a catchmment. 
The load is calculated according to the formula :math:numref:`load_equation`:

.. math::
    :label: load_equation

    m_{WW,eff} = i_{WWTP} \cdot m_{i,y} \cdot (1 - r_{WWTP}) / 1000
    

With:

- :math:`m_{WW,eff}` = load [:math:`kg/a`]
- :math:`i_{WWTP}` = connected inhabitants [:math:`inh`]
- :math:`m_{i,y}` = yearly consumption of y API [:math:`mg/inh/a`] 
- :math:`r_{WWTP}` = removal rate  [-]

The plugin retrieves the technical class assigned to each treatmant plant and identifies the corresponding removal rate for each API
from the data pool. This value (:math:`r_{WWTP}`) is then used as input for formula :math:numref:`load_equation` to calculate the
reduced emissions after treatment.

Input data
^^^^^^^^^^
One input data is necessary for this tool:

* **WWTP.shp**

The **WWTP.shp** is a point shapefile containing the emission point of the WWTPs as geometry and important information of the facilities in the attribute table. The required
information are: ID and name of the WWTP; number of connected inhabitant; number representing the type of treatment (1=primary, 2=secondary, 3=tertiary, 4=quaternary). An
example of these information can be summarized by :numref:`WWTP-attribute-table`.

.. _WWTP-attribute-table:

.. list-table:: Example of attribute table with required data for WWTPs.
    :header-rows: 1
    :widths: 15 30 20 20

    * - ID
      - Name
      - Connected Inhabitants
      - Type of treatment
    * - 163
      - KA Vorbeck
      - 98
      - 2
    * - 202
      - KA Groß Lüsewitz
      - 913
      - 1
    * - 691
      - KA Schwaan
      - 10004
      - 3
    * - 156
      - KA Hanstorf
      - 312
      - 2
    * - 169
      - KA Güstrow/Parum
      - 34333
      - 3


.. important::
    The column "Type of treatment" needs to be a number from 1 to 4.
    The emission point should be within 500 m to the closest river section.

Workflow
^^^^^^^^

1. Add the input data to the project by clicking on "Layer -> Add Layer -> Add Vector Layer"
2. Go in the Processing Toolbox and look for the *APRIORA* plugin. Click on *API emission* and open *5 - Emission Loads*
3. Choose **WWTP.shp** as input for *Emission Points of WWTP*
4. Select the correct field of **WWTP.shp** for *ID*, *Name*, *Connected Inhabitants* and *Technology Class*
5. If you created a custom table from the *Consumption Selection* tool, flag the next box, otherwise leave it empty

.. important::
    Under *Current API Selection* you can see the substances previously selected. This window is only displaying the selection, if you want
    to change the selection go back to :ref:`consumption-selection`.

6. Click on *Run*

.. raw:: html

   <figure>
     <video width="700" height="370" controls>
       <source src="_static/Emission_load_1.mp4" type="video/mp4">
       Your browser does not support the video tag.
     </video>
     <figcaption>Video: Worflow of the <i>Emission Loads</i> tool.</figcaption>
   </figure>

Output data:

* **emission_loads.shp**

The output is a point shapefile with the same geometry as the **WWTP.shp**. The attribute table contains the *ID* and *Name* columns from **WWTP.shp** and 
*n* columns related to the emission load of *n* selected APIs (e.g., if the user selects 3 APIs, 3 load columns are added). Finally, the load is expressed in *kg/a*.
