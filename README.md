# ogc-gdc-usecase
A collection of scripts for access to test data for the OGC GeoDataCubes working group

We will be making two datasets available for our use case. These can both be accessed through our polytope client library which will then pull the data from MARS. Instructions to install the packages can be found here https://github.com/ecmwf-projects/polytope-client, polytope is a python library and can be installed using pip. To access the data you must create an account at www.ecmwf.int and then your api key can be found at https://api.ecmwf.int/v1/key/. 

## Access using your ECMWF credentials

1. Install polytope-client from PyPI:
```
pip install --upgrade polytope-client
```

2. Register for an ECMWF account at ecmwf.int and retrieve your API key from https://api.ecmwf.int/v1/key/

3. Modify the example scripts in this repository to include your email address and API key. Or alternatively see the documentation at https://github.com/ecmwf/polytope-client to see how to set this globally.

## Datasets available

The two datasets are from two medicanes:

* Trixie, initial dates [2016-10-26,  2016-10-28]

* anos, initial dates [2020-09-15, 2020-09-16]

The two experiments are expver ht3e (Tco2559, 4.4km) and expver hsvs (Tco1279, 9km). 

They each contain parameters for Divergence, Geopotential, Relative humidity, Specific humidity, Temperature, U component of wind, V component of wind, Vertical velocity, Vorticity (relative). Conversion of the parameter to its corresponding param ID which is used in the scripts can be found here https://codes.ecmwf.int/grib/param-db/. 

Explanations of fields within the requests can be found here https://confluence.ecmwf.int/display/UDOC/Keywords+in+MARS+and+Dissemination+requests. 

The entire ht3e experiment is 340 GB and hsvs is 85 GB.
The current scripts download between 22 and 24 GB for each experiment.

This repo contains scripts to download the experiments some of the data but the requests can be changed to make them smaller or request all the data as large requests can be slow. This can be done by editing the MARS request in the scripts. You can edit the MARS request here https://apps.ecmwf.int/mars-catalogue/?class=rd&expver=hsvs&stream=oper&type=fc&levtype=pl&date=2020-09-15 for hsvs, and here https://apps.ecmwf.int/mars-catalogue/?class=rd&expver=ht3e&stream=oper&type=fc&levtype=pl&date=2016-10-28 for ht3e and generate a new MARS request that can be used in the scripts.

If you have any questions or issues please contact Adam Warde adam.warde@ecmwf.int or James Hawkes james.hawkes@ecmwf.int.
