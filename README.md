# Modeling the residential distribution of enrolled students to assess boundary-induced disparities in public school access

This repository contains all of the code necessary to reproduce the results in *Modeling the residential distribution of enrolled students to assess boundary-induced disparities in public school access.*

## Instructions
Ensure the following packages are installed.  
• `cvxpy` 
• `cvxopt`  
• `geopandas` 
• `matplotlib` 
• `mpl_toolkits`
• `numpy`
• `pandas`
• `scipy`
• `seaborn`
• `statsmodels`

Perform the UK analysis by running the UK Analysis ipynb notebook.  

The PH analysis ipython notebook requires the 2002 Datos barangay shapefiles that can be requested from PSA at https://psa.gov.ph/content/how-request-data-psa which contains the barangay shape and 2000 population. The geocodes can be updated using the script barangay_preprocessor.py. The barangay dataframe should have the following headers:

"ProvinceName"  
"RegionName"  
"Country"  
"POP2K"  
"geometry" - shapefile of the barangay  
"RegionCode_PSGC" - standard geocode at the regional level  
"ProvinceCode" - standard geocode at the provincial level  
"MunicipalityCode" - standard geocode at the municipal level  

To run the comparison between the assignment by max matching and our potential-based approach, run the Comparison vs. max matching ipython notebook.

## Citations

If you use the code for academic research, you are highly encouraged to cite our paper:

Rubio LJM, Dailisan DN, Osorio MJP, David CC, Lim MT (2019). *Modeling the residential distribution of enrolled students to assess boundary-induced disparities in public school access.* PLoS ONE 14(10): e0222766. https://doi.org/10.1371/journal.pone.0222766

## Sources
### Philippines 
1. the Philippine Statistics Authority:  
- https://psa.gov.ph/classification/psgc/  (Geocodes used are frome the September 2017 publication)  
- Administrative boundary shapefiles with population contained in the Data Kit of Philippine Statistics [Datos] must be requested by interested researchers from https://psa.gov.ph/content/how-request-data-psa  

2. the Department of Education of the Philippines:  
https://www.deped.gov.ph/resources/facts-and-figures/datasheets/ (School enrollment for 2015 was downloaded on November 7, 2017)  
https://data.gov.ph/?q=dataset/public-elementary-school-enrollment-statistics/resource/278bdae4-3be2-4acb-80bf-91e902711900
https://deped.carto.com/tables/deped_school_location_with_enrolment_2014_2015/public  
Additional datasets can be requested from: action@deped.gov.ph  

### UK
* UK School Capacity - https://www.gov.uk/government/statistics/school-capacity-academic-year-2016-to-2017  
* Location of UK schools https://www.whatdotheyknow.com/request/312648/response/764882/attach/2/EduBase%20Extract%202016%200005414.zip  
* Estimates of population - https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland/mid2017/ukmidyearestimates2017finalversion.xls  
* Administrative boundaries - http://geoportal1ons.opendata.arcgis.com/datasets/8edafbe3276d4b56aec60991cbddda50_1.zip 
