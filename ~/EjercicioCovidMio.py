# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:59:07 2023

@author: Jose Fernando Galindo Suarez
@email: jgalindos@sena.edu.co
"""

import pandas as pd


ruta="c:/Borrar/"
data=pd.read_csv(ruta+'COVID19-JULIO2020.csv',low_memory=False)
print(data.shape)

data['Estado']=data['Estado'].str.replace('leve','Leve',regex=False)
DM_ESTADO=pd.DataFrame(data['Estado'])
DM_ESTADO.drop_duplicates(inplace=True)
DM_ESTADO['IDESTADO']=range(1, len(DM_ESTADO) + 1)
DM_ESTADO.set_index('IDESTADO', inplace=True)
DM_ESTADO=DM_ESTADO.fillna('NA')
DM_ESTADO.to_csv(ruta+'DM_ESTADO.csv')

data['Tipo']=data['Tipo'].str.replace('relacionado','Relacionado',regex=False)
data['Tipo']=data['Tipo'].str.replace('RELACIONADO','Relacionado',regex=False)
data['Tipo']=data['Tipo'].str.replace('En Estudio','En estudio',regex=False)
DM_TIPO=pd.DataFrame(data['Tipo'])
DM_TIPO.drop_duplicates(inplace=True)
DM_TIPO['IDTIPO']= range(1, len(DM_TIPO) + 1)
DM_TIPO.set_index('IDTIPO', inplace=True)
DM_TIPO.to_csv(ruta+'DM_TIPO.csv')

DM_FECHA=pd.DataFrame(data['Fecha'])
DM_FECHA.drop_duplicates(inplace=True)
DM_FECHA['IDFECHA']=range(1,len(DM_FECHA)+1)
DM_FECHA.set_index('IDFECHA',inplace=True)
DM_FECHA.to_csv(ruta+'DM_FECHA.csv')

DM_DEPARTAMENTO=pd.DataFrame(data['Departamento o Distrito '])
DM_DEPARTAMENTO.drop_duplicates(inplace=True)

DM_DEPARTAMENTO.columns=DM_DEPARTAMENTO.columns.str.replace('Departamento o Distrito ','NOMBRE')
DM_DEPARTAMENTO['IDDPTO']=data['Código DIVIPOLA']//1000
DM_DEPARTAMENTO.loc[DM_DEPARTAMENTO['NOMBRE']=='Barranquilla D.E.','IDDPTO']=8001
DM_DEPARTAMENTO.loc[DM_DEPARTAMENTO['NOMBRE']=='Cartagena D.T. y C.','IDDPTO']=13001
DM_DEPARTAMENTO.loc[DM_DEPARTAMENTO['NOMBRE']=='Santa Marta D.T. y C.','IDDPTO']=47001
DM_DEPARTAMENTO.loc[DM_DEPARTAMENTO['NOMBRE']=='Buenaventura D.E.','IDDPTO']=76109
DM_DEPARTAMENTO.set_index('IDDPTO',inplace=True)
DM_DEPARTAMENTO.to_csv(ruta+'DM_DEPARTAMENTO.csv')

DM_CIUDAD=pd.DataFrame(data['Ciudad de ubicación'])
DM_CIUDAD.drop_duplicates(inplace=True)
DM_CIUDAD['IDCIUDAD']=data['Código DIVIPOLA']
DM_CIUDAD.set_index('IDCIUDAD',inplace=True)
DM_CIUDAD.to_csv(ruta+'DM_CIUDAD.csv')

DM_ATENCION=pd.DataFrame(data['atención'])
DM_ATENCION=DM_ATENCION.fillna('NA')
DM_ATENCION.drop_duplicates(inplace=True)
DM_ATENCION['IDATENCION']=range(1,len(DM_ATENCION)+1)
DM_ATENCION.set_index('IDATENCION',inplace=True)
DM_ATENCION.to_csv(ruta+'DM_ATENCION.csv')

DM_PAIS=pd.DataFrame(data['País de procedencia'])
DM_PAIS=DM_PAIS.fillna('COLOMBIA')
data['País de procedencia'].fillna('COLOMBIA',inplace=True)
DM_PAIS.columns=DM_PAIS.columns.str.replace('País de procedencia','NOMBRE')
DM_PAIS['NOMBRE']=DM_PAIS.NOMBRE.str.replace('ESTADOS UNIDOS DE AMÉRICA','ESTADOS UNIDOS',regex=False)
DM_PAIS['NOMBRE']=DM_PAIS.NOMBRE.str.replace('ESTADOS UNIDOS DE AMERICA','ESTADOS UNIDOS',regex=False)
DM_PAIS['NOMBRE']=DM_PAIS.NOMBRE.str.replace('ARABIA SAUDÍ','ARABIA SAUDITA',regex=False)
DM_PAIS['NOMBRE']=DM_PAIS.NOMBRE.str.replace('MÉXICO','MEXICO',regex=False)
DM_PAIS['NOMBRE']=DM_PAIS.NOMBRE.str.replace('PANAMÁ','PANAMA',regex=False)
DM_PAIS['NOMBRE']=DM_PAIS.NOMBRE.str.replace('PERÚ','PERU',regex=False)
DM_PAIS.drop_duplicates(inplace=True)
DM_PAIS['IDPAIS']=range(1,len(DM_PAIS)+1)
DM_PAIS.set_index('IDPAIS',inplace=True)
DM_PAIS=DM_PAIS.sort_values('NOMBRE')
DM_PAIS.to_csv(ruta+'DM_PAIS.csv')

data['Sexo']=data.Sexo.str.replace('m','M',regex=False)
data['Sexo']=data.Sexo.str.replace('f','F',regex=False)
DM_SEXO=pd.DataFrame(data['Sexo'])
DM_SEXO.columns=DM_SEXO.columns.str.replace('SEXO','NOMBRE')
DM_SEXO.drop_duplicates(inplace=True)
DM_SEXO['IDSEXO']=range(1,len(DM_SEXO)+1)
DM_SEXO.set_index('IDSEXO',inplace=True)
DM_SEXO.to_csv(ruta+'DM_SEXO.csv')

data.columns=data.columns.str.replace('Tipo','IDTIPO')
data.columns=data.columns.str.replace('Estado','IDESTADO')
data.columns=data.columns.str.replace('Código DIVIPOLA','IDCIUDAD')
data.columns=data.columns.str.replace('atención','IDATENCION')
data.columns=data.columns.str.replace('País de procedencia','IDPAIS')
data.columns=data.columns.str.replace('Sexo','IDSEXO')
data.columns=data.columns.str.replace('Departamento o Distrito ','IDDPTO')

data['IDDPTO']=data['IDCIUDAD']//1000

data.drop('Ciudad de ubicación',axis=1,inplace=True)

data['IDTIPO']=data.IDTIPO.str.replace('Importado','1',regex=False)
data['IDTIPO']=data.IDTIPO.str.replace('Relacionado','2',regex=False)
data['IDESTADO']=data.IDESTADO.str.replace('Leve','1',regex=False)
data['IDESTADO']=data.IDESTADO.str.replace('Asintomático','2',regex=False)
data['IDATENCION']=data.IDATENCION.str.replace('Recuperado','1',regex=False)
data['IDATENCION']=data.IDATENCION.str.replace('Fallecido','2',regex=False)
data['IDATENCION']=data.IDATENCION.str.replace('NA','3',regex=False)
data['IDATENCION']=data.IDATENCION.str.replace('Casa','4',regex=False)
data['IDATENCION']=data.IDATENCION.str.replace('UCI','5',regex=False)
data['IDATENCION']=data.IDATENCION.str.replace('Hospital','6',regex=False)
data['IDESTADO']=data.IDESTADO.str.replace('Fallecido','3',regex=False)
data['IDTIPO']=data.IDTIPO.str.replace('En estudio','3',regex=False)

pais=pd.read_csv(ruta+'DM_PAIS.csv')

z1=pais['IDPAIS']
z2=pais['NOMBRE']

for idpais,nombre in zip(z1,z2):
    data['IDPAIS']=data.IDPAIS.str.replace(nombre,str(idpais),regex=False)

mfecha=pd.read_csv(ruta+'DM_FECHA.csv')
z1=mfecha['IDFECHA']
z2=mfecha['Fecha']

for idfecha,fecha in zip(z1,z2):
    data['Fecha']=data.Fecha.str.replace(fecha,str(idfecha),regex=False)

data.columns=data.columns.str.replace('Fecha','IDFECHA')
#data.drop('Fecha',axis=1,inplace=True)
rangos=[0,5,10,18,50,100,110]
nombrer=['A','B','C','D','E','F']
data['GEDAD']=pd.cut(data['Edad'],rangos,labels=nombrer)

data['ID']=range(1,len(data)+1)    
data.set_index("ID",inplace=True)
data.to_csv(ruta+'TH_COVID19.csv',index=False)



