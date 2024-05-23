from peewee import *
from pymongo import MongoClient
import pandas as pd

cnx=MongoClient("mongodb://localhost:27017")
bd=cnx["Neptuno"]
coleccion=bd["PRODUCTOS"]

x=pd.read_excel("Neptuno.xlsx",sheet_name=4)
    
j=len(x)
i=0 
while i<j:
    zz=""
    zz=x.loc[i]  
    coleccion.insert_one(zz.to_dict()) 
    i=i+1
