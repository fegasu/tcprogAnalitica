from peewee import *
from pymongo import MongoClient
import pandas as pd
class MongoExcel:
    def __init__(self,host,basecita):
        self.__bd=basecita
        self.__host=host
        self.__cnx=MongoClient(self.__host)
        
        
    def ExcelNumHojas(self,Libro,saltehoja):
        self.__Libro=Libro
        self.__libro=pd.ExcelFile(self.__Libro)
        self.__hojitas=self.__libro.sheet_names[saltehoja:]
        return self.__hojitas

    def Excel2MongoDB(self,cole,hoja):
        
        bd=self.__cnx[self.__bd]
        self.__coleccion=bd[cole]

        x=pd.read_excel(self.__libro,sheet_name=hoja)
        
            
        j=len(x)
        i=0 
        while i<j:
            zz=x.loc[i]  #tRAE UNA FILA
            self.__coleccion.insert_one(zz.to_dict()) 
            i=i+1
    def Excel2MongogoDBTodo(self):
        i=1
        for h in self.__hojitas:
            i=self.__hojitas.index(h)+1
            self.Excel2MongoDB(h,i)
            i=i+1