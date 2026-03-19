# Input and Output filepath
INPUT_filepath = "../INPUT/"
geospat_data_filepath = INPUT_filepath+"00_geospatial_data/"
ancillary_data_filepath = INPUT_filepath+"00_ancillary_data/"
basin_atlas_filepath = INPUT_filepath+"04_static_basinatlas_catchment_characteristics/"
metadata_filepath = INPUT_filepath+"01_metadata/"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
water_quality_filepath = INPUT_filepath + "02_waterquality_timeseries/"
discharge_filepath = INPUT_filepath + "09_streamflow_discharge/"
OUTPUT_filepath = "../OUTPUT/"

params_pretty_dict = {'WTemp_C':'Temp',
                      'DO_mgL':'DO',
                      'SpC_uScm':'SpC',
                      'Turb_FNU':'Turb. (FNU)',
                      'Turb_NTU':'Turb. (NTU)',
                      'NO3_mgNL':'NO3',
                      'fDOM_QSU':'fDOM (QSU)',
                      'fDOM_RFU':'fDOM (RFU)',
                      'DOC_mgL':'DOC',
                      'PO4_mgL':'PO4',
                      'Chla_ugL':'Chla',
                      'Chla_RFU':'Ch;a (RFU)',
                      'PC_ugL':'PC',
                      'PC_RFU':'PC (RFU)',
                      'pH':'pH'}