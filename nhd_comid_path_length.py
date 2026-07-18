# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:13:31 2026

@author: danyk
"""

from pynhd import NLDI #, WaterData, NHDPlusHR
import pynhd as nhd
import pandas as pd
from config import *

nldi = NLDI()
comid_df = pd.read_csv(metadata_filepath+'metadata.csv', dtype={'sourceID':str})
vaa = nhd.nhdplus_vaa()
comid_df['comid'] = comid_df['comid'].astype(int)

comid_df.to_csv(INPUT_filepath+'00_ancillary_data/geomorph_data/nhdplus_pathlength.csv',
               index=False)