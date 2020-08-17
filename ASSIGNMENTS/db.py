#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv("encrypted.csv")


cols = data.columns

county_counts = (data['COUNTY'].value_counts())
#took 3rd most populous county
bexar_county = '406b783f721b16ffbe467c444fae075231ec3a21b14cff2a8f376338a89e339a'

day_counts = (data['ADMIT_WEEKDAY'].value_counts())
sunday = '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451'

gender_counts = (data['SEX_CODE'].value_counts())
man = '08f271887ce94707da822d5263bae19d5519cb3614e0daedc4c7ce5dab7473f1'

race_counts = (data['RACE'].value_counts())
white = '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a'

ethn_counts = (data['ETHNICITY'].value_counts())
hispanic_white = '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'

zip_counts = (data['PAT_ZIP'].value_counts())
out_state = '3d0a234093378eaffc3fe01cd6edbc3cd4302a37457b0c3bb3dd464a52c5a070'


filtered_patients = data[(data['ADMIT_WEEKDAY'] == sunday) & (data['SEX_CODE'] == man) & (data['RACE'] == white) & (data['ETHNICITY'] == hispanic_white) & (data['PAT_ZIP'] == out_state) ]['RECORD_ID']