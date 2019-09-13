# Modeling the residential distribution of enrolled students to assess boundary-induced disparities in public school access

This repository contains all of the code necessary to reproduce the results in *Modeling the residential distribution of enrolled students to assess boundary-induced disparities in public school access.*

## Instructions
Ensure the following packages are installed.
• cvxpy
• cvxopt
• geopandas
• matplotlib
• mpl_toolkits
• numpy
• pandas
• scipy
• seaborn
• statsmodels

Perform the UK analysis by running the UK Analysis ipynb notebook file.
The PH analysis requires the 2002 Datos barangay shapefiles that can be requested from PSA at https://psa.gov.ph/content/how-request-data-psa which contains the barangay shape and 2000 population. The geocodes can be updated using the script barangay_preprocessor.py. The barangay dataframe should have the following headers:

"ProvinceName"
"RegionName"
"Country"
"POP2K"
"geometry" - shapefile of the barangay
"RegionCode_PSGC" - standard geocode at the regional level
"ProvinceCode" - standard geocode at the provincial level
"MunicipalityCode" - standard geocode at the municipal level

## Citations

If you use the code for academic research, you are highly encouraged to cite our paper:

L. Rubio, D. Dailisan, J. Osorio, C. David, M. Lim. "Modeling the residential distribution of enrolled students to assess boundary-induced disparities in public school access," PLoS One.

## Sources
[Philippines] 
PSGC data from https://psa.gov.ph/classification/psgc/ 
Administrative boundary shapefiles contained in the Data Kit of Philippine Statistics 
[Datos] must be directly requested by interested parties from https://psa.gov.ph/content/how-request-data-psa
DepEd dataset that used to be available from http://deped.gov.ph/datasets can be requested from action@deped.gov.ph. 
[UK] 
School capacity - https://www.gov.uk/government/statistics/school-capacity-academic-year-2016-to-2017
Location of UK schools - https://www.whatdotheyknow.com/request/312648/response/764882/attach/2/EduBase%20Extract%202016%200005414.zip; Estimates of population - https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland/mid2017/ukmidyearestimates2017finalversion.xls
Administrative boundaries - http://geoportal1-ons.opendata.arcgis.com/datasets/8edafbe3276d4b56aec60991cbddda50_1.zip 
