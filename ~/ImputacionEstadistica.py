# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 14:00:28 2023

@author: Jose Fernando Galindo Suarez
@email: jgalindos@sena.edu.co
"""

import pandas as pd

ruta="c:/Borrar/"
data=pd.read_csv(ruta+'SB11-20121-RGSTRO-CLFCCN-V1-0-txt-csv.csv',low_memory=False)
print(data.shape)
#data.info()

promedio=data['ESTU_NACIMIENTO_ANNO'].mean()
promedio=promedio.astype('int')

mediana=data['ESTU_NACIMIENTO_ANNO'].median()
mediana=int(mediana)

moda=data['ESTU_NACIMIENTO_ANNO'].mode()[0]
moda=int(moda)

#data['ESTU_NACIMIENTO_ANNO'].fillna(mediana)

medianad=data['ESTU_NACIMIENTO_DIA'].median()
medianad=int(medianad)

modam=data['ESTU_NACIMIENTO_MES'].mode()[0]
modam=int(modam)

por_defecto={"ESTU_NACIMIENTO_ANNO":moda, "ESTU_NACIMIENTO_DIA":medianad,"ESTU_NACIMIENTO_MES":modam}

data.fillna(value=por_defecto,inplace=True)

medianad=data['ESTU_NACIMIENTO_DIA'].median()
medianad=int(medianad)

data['ESTU_NACIMIENTO_ANNO'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_ANNO']=data['ESTU_NACIMIENTO_ANNO'].astype('int')

data['ESTU_NACIMIENTO_MES'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_MES']=data['ESTU_NACIMIENTO_MES'].astype('int')

data['ESTU_NACIMIENTO_DIA'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_DIA']=data['ESTU_NACIMIENTO_DIA'].astype('int')

data1=data[data['ESTU_TIPO_DOCUMENTO'].isna()] #sin tipo de documento
data.to_csv(ruta+"SB11 20121.csv",index=False)
print(data.isna().sum()/data.shape[0]*100)
data['LIMITA']=0

dataM=data[data['ESTU_LIMITA_MOTRIZ']=='M']
#data['ESTU_LIMITA_MOTRIZ'].fillna(0,inplace=True)
data.loc[data['ESTU_LIMITA_MOTRIZ']=='M','LIMITA']=data['LIMITA']|8


dataM['LIMITA']=dataM['LIMITA']|8

    

