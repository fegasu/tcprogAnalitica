# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:49:37 2023

@author: Administrador
"""

import pandas as pd

ruta="c:/Borrar/"
data=pd.read_csv(ruta+'SB11-20121-RGSTRO-CLFCCN-V1-0-txt-csv.csv',low_memory=False)
col=data.shape[1]

import csv
malos=[]
with open(ruta+'SB11-20121-RGSTRO-CLFCCN-V1-0-txt-csv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    data=pd.DataFrame(spamreader)
    data.to_csv(ruta+'x.csv',index=False)
        


        
