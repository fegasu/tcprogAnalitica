# -- coding: utf-8 --
"""
Created on Sun Apr 16 18:36:03 2023

@author: JOSE F GALINDO
"""

import csv 
import json
import pandas as pd
import sys
import os
import platform
sistema = platform.system()
if sistema=="Linux":
    os.system("clear")
else:
    os.system ("cls")
print("\n\n** INICIO DEL CONVERTIDOR DE FORMATO **\nAUTOR: JOSE FERNANDO GALINDO SUAREZ\n")
def json2csv(archi1):
    archi=archi1
    print("Convirtiendo JSON a CSV")
    df = pd.read_json(archi1)
    df.to_csv(archi1+'.csv', index = None)   
def csv2json(archi1):
    df = pd.read_csv(archi1)
    df.to_json(archi1+".json",orient='records')
argu= len(sys.argv)   
if argu==1:
    print("Use: python convierta.py csv2json archivo_csv\npython convierta.py json2csv archivo_json ") 
    sys.exit(1)
else:
    modulo=sys.argv[1]    
if modulo=="csv2json":
    print("Convirtiendo CSV a JSON")
    archi=sys.argv[2]    
    csv2json(archi)
elif modulo=="json2csv":
    archi=sys.argv[2]  
    json2csv(archi)
print("\nFinalizo la conversion")