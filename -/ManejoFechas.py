# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:06:40 2023

@author: Administrador
"""

import pandas as pd

ruta="c:/Borrar/"
data=pd.read_csv(ruta+"SB11-20121-RGSTRO-CLFCCN-V1-0-txt-csv.csv",low_memory=False)
data['FNACIO'] = pd.to_datetime(data['ESTU_NACIMIENTO_ANNO'] * 10000 + data['ESTU_NACIMIENTO_MES'] * 100 + data['ESTU_NACIMIENTO_DIA'], format='%Y%m%d')
data['FACTUAL']= pd.to_datetime(2012 * 10000 + data['ESTU_NACIMIENTO_MES'] * 100 + data['ESTU_NACIMIENTO_DIA'], format='%Y%m%d')

data['ESTU_ANNO_NACE']=data['FNACIO'].dt.year
data['ESTU_ANNO_ACTUAL']=data['FACTUAL'].dt.year
data['ESTU_EDAD']=data['ESTU_ANNO_ACTUAL']-data['ESTU_ANNO_NACE']

data['ESTU_EDAD']=data['ESTU_EDAD']//1
data.drop('ESTU_ANNO_NACE',axis=1,inplace=True)
data.drop('ESTU_ANNO_ACTUAL',axis=1,inplace=True)
data.drop('FACTUAL',axis=1,inplace=True)

rangos=[0,5,10,18,50,100,110]
nombrer=['A','B','C','D','E','F']
data['GEDAD']=pd.cut(data['ESTU_EDAD'],rangos,labels=nombrer)
data['ID']=range(1,len(data)+1)
data.set_index('ID',inplace=True)
data.to_csv(ruta+"Datos.csv")
print(data)