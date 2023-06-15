# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 14:00:28 2023

@author: Jose Fernando Galindo Suarez
@email: jgalindos@sena.edu.co

1-ESTU_LIMITA_BAJAVISION
2-ESTU_LIMITA_SORDOCEGUERA
4-ESTU_LIMITA_COGNITIVA
8-ESTU_LIMITA_INVIDENTE
16-ESTU_LIMITA_MOTRIZ
32-ESTU_LIMITA_SORDOINTERPRETE
64-ESTU_LIMITA_SORDONOINTERPRETEx
"""

import pandas as pd

ruta="c:/Borrar/"
data=pd.read_csv(ruta+'SB11-20121-RGSTRO-CLFCCN-V1-0-txt-csv.csv',low_memory=False)
print(data.shape)
data['ESTU_NACIMIENTO_ANNO'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_ANNO']=data['ESTU_NACIMIENTO_ANNO'].astype('int')
data['ESTU_NACIMIENTO_MES'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_MES']=data['ESTU_NACIMIENTO_MES'].astype('int')
data['ESTU_NACIMIENTO_DIA'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_DIA']=data['ESTU_NACIMIENTO_DIA'].astype('int')

data['LIMITA']=0
data.loc[data['ESTU_LIMITA_SORDOCEGUERA']=='C','LIMITA']=data['LIMITA']+2
data.loc[data['ESTU_LIMITA_COGNITIVA']=='G','LIMITA']=data['LIMITA']+4
data.loc[data['ESTU_LIMITA_INVIDENTE']=='I','LIMITA']=data['LIMITA']+8
data.loc[data['ESTU_LIMITA_MOTRIZ']=='M','LIMITA']=data['LIMITA']+16
data.loc[data['ESTU_LIMITA_SORDOINTERPRETE']=='R','LIMITA']=data['LIMITA']+32
data.loc[data['ESTU_LIMITA_SORDONOINTERPRETE']=='S','LIMITA']=data['LIMITA']+64

data1=data.loc[data['LIMITA']>0]
data1.to_csv(ruta+"/Limitacion.csv",index=False)