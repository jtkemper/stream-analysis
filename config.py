# Input and Output filepath
INPUT_filepath = "../INPUT/"
geospat_data_filepath = INPUT_filepath+"00_geospatial_data/"
ancillary_data_filepath = INPUT_filepath+"00_ancillary_data/"
basin_atlas_filepath = INPUT_filepath+"04_static_catchment_characteristics/"
metadata_filepath = INPUT_filepath+"01_metadata/"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
water_quality_filepath = INPUT_filepath + "02_waterquality_timeseries/"
discharge_filepath = INPUT_filepath + "08_streamflow_discharge/"
landuse_filepath = INPUT_filepath + "06_dynamic_lulc/"
OUTPUT_filepath = "../OUTPUT/"


solutes = ['SpC_uScm', 'DO_mgL', 'Turb_FNU', 'WTemp_C', 'NO3_mgNL', 'fDOM_QSU']
solute_pretty = {"DO_mgL":"DO (mg/L)",
                 "SpC_uScm":"SpC (µS/cm)",
                 "Turb_FNU":"Turbidity (FNU)",
                 "WTemp_C":"Temp ($^{o}$C)",
                 "NO3_mgNL":"NO$_{3}$-N (mg/L)",
                 "fDOM_QSU":"fDOM (QSU)"
                }
    
PARAM_COLORS = {
    'DO_mgL':    {'fill': '#FEDCBB', 'edge': '#7F2704', 'cmap':'Oranges'}, 
    'SpC_uScm':  {'fill': '#E2EDF8', 'edge': '#08306B', 'cmap':'Blues'}, 
    'Turb_FNU':  {'fill': '#CEECC8', 'edge': '#00431A', 'cmap':'Greens'}, 
    'WTemp_C':   {'fill': '#DADAEB', 'edge': '#3F007D', 'cmap':'Purples'},
    'NO3_mgNL':  {'fill': '#FEE0D2', 'edge': '#67000D', 'cmap':'Reds'},
    'fDOM_QSU':  {'fill': '#D9F0A3', 'edge': '#238443', 'cmap':'YlGn'},
}
