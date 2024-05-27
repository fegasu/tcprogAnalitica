from rutinas.misrutinas import *

a=MongoExcel("mongodb://localhost:27018","Neptuno")
hojas=a.ExcelNumHojas("Neptuno.xlsx",1)
print(len(hojas),hojas)
a.Excel2MongogoDBTodo()