# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:14:05 2023

@author: Jose Fernando Galindo Suarez
@email: jgalindos@sena.edu.co
"""


import pandas as pd

ruta="c:/Borrar/"
data=pd.read_csv(ruta+'SB11-20121-RGSTRO-CLFCCN-V1-0-txt-csv.csv',low_memory=False)
print(data.shape)

# df = px.data.tips()
# fig = px.bar(df, x='ESTU_GENERO', y='ESTU_GENERO')
# fig.show()


dataX=data[data['ESTU_GENERO']=='X'] #creamos el dataset que tienen X en su genero
dataX['aux']=0 #creamos la columna aux en el dataset que tiene los X
hayX=len(dataX.index) #cantidad de registros que tienen X=423
hay=len(data.index)-hayX #total de registros menos lo que tienen X en el genero = 44967

dataF=data[data['ESTU_GENERO']=='F'] #creamos el dataset que su genero es F
hayF=len(dataF.index) #contamos cuantas mujeres hay=21711
dataM=data[data['ESTU_GENERO']=='M'] #creamos el dataset que su genero es M
hayM=len(dataM.index) #contamos cuantos hombres hay=23256

pmujeres=hayF/hay #que porcentaje hay de mujeres=0.4828207352058176
phombres=hayM/hay #que porcentaje hay de hommbres=0.5171792647941824
mujeres=hayX*pmujeres #sacamos la cantidad de mujeres que tienen X=204
hombres=hayX*phombres ##sacamos la cantidad de hombres que tienen X=219

#convirtiendo columna a valores enteros
data['ESTU_NACIMIENTO_ANNO'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_ANNO']=data['ESTU_NACIMIENTO_ANNO'].astype('int')

data['ESTU_NACIMIENTO_MES'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_MES']=data['ESTU_NACIMIENTO_MES'].astype('int')

data['ESTU_NACIMIENTO_DIA'].fillna(0,inplace=True)
data['ESTU_NACIMIENTO_DIA']=data['ESTU_NACIMIENTO_DIA'].astype('int')


dataX['aux']=range(1,hayX+1) # colocamos en la columna aux una secuencia de numero

for i in range(1,int(mujeres)+1):
    dataX.loc[dataX['aux']==i,'ESTU_GENERO']='F' #asignamos el genero F
   
for i in range(int(mujeres) ,hayX+1):
    dataX.loc[dataX['aux']==i,'ESTU_GENERO']='M' #asignamos el genero M
   
   
data=data.drop(data[data['ESTU_GENERO']=="X"].index) #borramos las fila que su genero tenga X

data=pd.concat([data,dataX]) # unimos el dataset data con el dataset dataX

print(data[data['ESTU_GENERO']=="X"]) 

data.to_csv(ruta+'SB11-20121.csv',index=False)