import pandas as pd
import geopandas as gpd
import numpy as np

def barangays_preprocess():
    #Initial loading of barangay shape files
    
    barangays = gpd.read_file("bgy-population.shp")
    barangays.crs = {'init' :'epsg:4326'} # prs92
    barangays["area"] = barangays.geometry.area/1e6
    barangays["perimeter"] = barangays.geometry.apply(lambda x: x.length)/1e3
    barangays["accessibility"] = barangays["area"]/barangays["perimeter"]**2 * (np.pi*4)

    barangays["RegionCode"] = barangays.GEOCODE.apply(lambda x: x[:2])
    barangays["ProvinceCode"] = barangays.GEOCODE.apply(lambda x: x[:4])
    barangays["MunicipalityCode"] = barangays.GEOCODE.apply(lambda x: x[:6])
    barangays["centroid"] = barangays.geometry.centroid

    region_dicts = {"01":"Region I", "02": "Region II", "03":"Region III", "04":"Region IV", "05":"Region V", "06":"Region VI", "07":"Region VII", "08":"Region VIII", "09":"Region IX", "10":"Region X", "11":"Region XI", "12":"Region XII", "13":"Region XIII", "97":"ARMM", "98":"CAR", "99":"NCR"  }
    
    barangays["RegionName_2002"] = barangays.RegionCode.map(region_dicts)
    barangays["Country"] = 1
    
    #Load Sept2017 PSGC regions
    PSGC_Sept2017 = pd.read_excel("PSGC_Sept2017.xlsx", dtype = str)
    PSGC_Sept2017["RegionCode"] = PSGC_Sept2017.loc[:,"GEOCODE"].apply(lambda x: x[:2])
    PSGC_Sept2017["ProvinceCode"] = PSGC_Sept2017.loc[:,"GEOCODE"].apply(lambda x: x[2:4])
    PSGC_Sept2017["MunicipalityCode"] = PSGC_Sept2017.loc[:,"GEOCODE"].apply(lambda x: x[4:6])

    PSGC_Provinces = PSGC_Sept2017[np.bitwise_and(PSGC_Sept2017.MunicipalityCode == "00",PSGC_Sept2017.ProvinceCode != "00")].sort_values(by = "ProvinceCode").reset_index(drop = True)
    PSGC_ProvinceCodes = PSGC_Provinces.ProvinceCode.values
    
    PSGC_ProvincesAll = PSGC_Sept2017[PSGC_Sept2017.ProvinceCode != "00"].sort_values(by = ["ProvinceCode","MunicipalityCode"]).reset_index(drop = True)
    PSGC_ProvincesAll = PSGC_ProvincesAll.drop_duplicates(subset = "ProvinceCode") #Only retain the first possible MunicipalCode
    
    #Updates the barangays df with shorter code (for matching)
    barangays["ProvinceCode"] = barangays.GEOCODE.apply(lambda x: x[2:4])
    barangays["MunicipalityCode"] = barangays.GEOCODE.apply(lambda x: x[4:6])
    barangays["BarangayCode"] = barangays.GEOCODE.apply(lambda x: x[6:])

    Datos_Provinces = barangays[barangays.ProvinceCode != "00"].drop_duplicates(subset = "ProvinceCode").sort_values(by = "ProvinceCode")
    Datos_ProvinceCodes = barangays[barangays.ProvinceCode != "00"].drop_duplicates(subset = "ProvinceCode").sort_values(by = "ProvinceCode").ProvinceCode.values
    
    Datos_Provinces_reduced = Datos_Provinces.loc[:,["RegionCode","ProvinceCode","RegionName_2002"]]
    Datos_Provinces_reduced = Datos_Provinces_reduced.reset_index(drop = True)
    
    RegionTable = barangays.drop_duplicates(subset = "RegionName_2002").loc[:,["RegionCode","RegionName_2002"]]
    RegionDi1 = {"ARMM":"15","CAR":"14","NCR":"13","Region XIII":"16"}

    RegionTable["RegionCode"].update(RegionTable["RegionName_2002"].map(RegionDi1).dropna())
    RegionTable = RegionTable.sort_values(by = "RegionCode").reset_index(drop = True)
    RegionTable = RegionTable.append({"RegionCode":"17","RegionName_2002":"Region IV-B"}, ignore_index = True)
    RegionTable.RegionName_2002[3] = 'Region IV-A'
    RegionTable.columns = ["RegionCode","RegionName"]

    OldRegionCodes = barangays.drop_duplicates(subset = "RegionName_2002").loc[:,["RegionCode","RegionName_2002"]]

    #Create a df of the mapping of old RegionCode to new RegionCode
    RegionTableSummary = pd.merge(RegionTable, OldRegionCodes, how = "left", left_on = "RegionName", right_on = "RegionName_2002", suffixes = ["_new","_old"])
    RegionTableSummary.loc[3,["RegionCode_old", "RegionName_2002"]] = "04", "Region IV" 
    
    #Update PSGC_ProvincesAll with RegionTable 
    PSGC_ProvincesAll = pd.merge(PSGC_ProvincesAll, RegionTable, on = "RegionCode")

    Datos_PSGC_lookuptable = pd.merge(Datos_Provinces_reduced, PSGC_ProvincesAll, how = "left", on = "ProvinceCode", suffixes = ["_Datos","_PSGC"])
    Datos_PSGC_lookuptable = Datos_PSGC_lookuptable.loc[:,["GEOCODE","NAME", "RegionCode_Datos", "RegionCode_PSGC", "ProvinceCode", "MunicipalityCode", "RegionName_2002", "RegionName"]]
    
    barangays_PSGC_merge = barangays.merge(Datos_PSGC_lookuptable.loc[:,["NAME","RegionCode_PSGC", "ProvinceCode", "RegionName"]], on = "ProvinceCode")
    barangays_PSGC_merge = barangays_PSGC_merge.rename(columns = {"NAME":"ProvinceName"})
    reorder = ['ID_', 'NAMEMR2000', 'NAMEJN2002', 'GEOCODE', 'ProvinceName', 'POP2K',
       'geometry', 'area', 'centroid', 'perimeter', 'accessibility',  'RegionCode',
               'RegionCode_PSGC', 'Country', 'ProvinceCode', 'MunicipalityCode',
               'BarangayCode', 'RegionName_2002', 'RegionName']
 
    barangays_PSGC_merge = barangays_PSGC_merge.reindex(reorder, axis = 1)
    
    return barangays_PSGC_merge

def create_shapes(barangays_PSGC_merge):
    provinces_2017 = barangays_PSGC_merge.loc[:,["RegionCode_PSGC","RegionName","ProvinceCode","ProvinceName","geometry"]].copy()
    provinces_2017["geometry"] = provinces_2017["geometry"].buffer(0)
    provinces_2017 = provinces_2017.dissolve(by = "ProvinceCode",as_index = False)

    regions_2017 = provinces_2017.loc[:,["RegionCode_PSGC","RegionName","geometry"]].copy()
    regions_2017["geometry"] = regions_2017["geometry"].buffer(0)
    regions_2017 = regions_2017.dissolve(by = "RegionCode_PSGC", as_index = False)
    
    return regions_2017, provinces_2017

def aggregate_by(barangays, agg_level='RegionCode', eps=10):
    agg = barangays.loc[:,[agg_level,"geometry"]].copy()
    agg["geometry"] = agg["geometry"].buffer(0)
    
    agg = agg.loc[:,[agg_level,"geometry"]].dissolve(by=agg_level)
    agg["geometry"] = agg["geometry"].buffer(eps).buffer(-eps)
    return agg

########################