# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:13:31 2026

@author: danyk
"""

from pynhd import NLDI, WaterData, NHDPlusHR
import pynhd as nhd
import pandas as pd
from config import *

nldi = NLDI()
md = pd.read_csv(metadata_filepath+'metadata.csv', dtype={'sourceID':str})

comid_id= []

for i, row in md.iterrows():
    try:
        comid_closest = nldi.comid_byloc((row['longitude_wgs84'], 
                                          row['latitude_wgs84']),
                                         loc_crs=4326)
        comid_closest['STREAM_ID'] = row['STREAM_ID']
        comid_id.append(comid_closest[['STREAM_ID', 'reachcode', 'comid']])
        print(i)
        
    except Exception as e:
        print(f"Failed for row {i}: {e}")
        comid_id.append(None)
    
comid_df = pd.concat([x for x in comid_id if x is not None], ignore_index=True)



vaa = nhd.nhdplus_vaa()
comid_df['comid'] = comid_df['comid'].astype(int)
comid_df = comid_df.merge(vaa[['comid', 'pathlength']], on='comid', how='left')
comid_df.to_csv(INPUT_filepath+'00_ancillary_data/geomorph_data/nhdplus_pathlength.csv')