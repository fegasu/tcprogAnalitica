#*************************************************************************************************
#* TECNICO PROGRAMACION PARA ANALITICA DE DATOS -228117-
#* PROYECTO DE FORMACION: APLICAR BUENAS PRACTICAS PARA PREPARAR, LIMPIAR,
#* REFINAR Y EXPLORAR GRANDES VOLÚMENES DE DATOS EN EL SECTOR PRODUCTIVO.  
#* CENTRO DE GESTION DE MERCADOS, LOGISTICA Y TECNOLOGIAS DE LA INFORMACION
#* PROPOSITO: LIMPIEZA DE DATOS DEL DATASET COVID19 CON R
#* ACTIVIDAD DE APRENDIZAJE: VALIDACION DEL PROYECTO DE ACUERDO AL PROYECTO
#* AUTOR: JOSE FERNANDO GALINDO SUAREZ
#* EMAIL: jgalindos@sena.edu.co
#*************************************************************************************************

COVID19<-read.csv("https://siomi.datasena.com/analitica/data/COVID19.csv", sep=",", header = TRUE, encoding = "UTF-8")
COVID=COVID19
COVID19<-COVID
#CAMBIA EL NOMBRE DE LA COLUMNA 11
colnames(COVID19)[11]<-'PAIS'
#REPLAZA LOS VALORES VACION POR COLOMBIA
COVID19$PAIS[COVID19$PAIS==""] <-"COLOMBIA"

if(!require(stringr)) {
  install.packages("stringr")
}
library(stringr)
# ARREGLO ERRORES TIPOGRAFICOS
COVID19$PAIS<-str_replace(COVID19$PAIS, "ESTADOS UNIDOS DE AMÉRICA", "ESTADOS UNIDOS")
COVID19$PAIS<-str_replace(COVID19$PAIS, "ESTADOS UNIDOS DE AMERICA", "ESTADOS UNIDOS")
COVID19$PAIS<-str_replace(COVID19$PAIS, "MÉXICO", "MEXICO")
COVID19$PAIS<-str_replace(COVID19$PAIS, "CANADÁ", "CANADA")
COVID19$PAIS<-str_replace(COVID19$PAIS, "ARABIA SAUDÍ","ARABIA SAUDITA")
COVID19$PAIS<-str_replace(COVID19$PAIS, "PERÚ","PERU")
COVID19$PAIS<-str_replace(COVID19$PAIS, "PERÚ","PERU")
COVID19$PAIS<-str_replace(COVID19$PAIS, "PANAMÁ","PANAMA")
COVID19$Estado<-str_replace(COVID19$Estado, "leve","Leve")
COVID19$Tipo<-str_replace(COVID19$Tipo, "En Estudio","En estudio")
COVID19$Tipo<-str_replace(COVID19$Tipo, "relacionado","Relacionado")
COVID19$Tipo<-str_replace(COVID19$Tipo, "RELACIONADO","Relacionado")
COVID19$Tipo<-str_replace(COVID19$Tipo, "En Estudio","En estudio")
COVID19$atención<-str_replace(COVID19$atención, "Hospital UCI","UCI")

#CREA EL DATAFRAME DM_PAIS CON LA COLUMNA 11
DM_PAIS<-COVID19[,c(11,11)]
#ELIMINA DUPLICADOS
DM_PAIS<-DM_PAIS[!duplicated(DM_PAIS), ]
#CAMBIA EL NOMBRE DE LAS COLUMNAS
colnames(DM_PAIS)[1]<-'IDPAIS'
colnames(DM_PAIS)[2]<-'NOMBRE'
#CUENTA EL NUMERO DE FILAS DEL DATAFRAME
x=nrow(DM_PAIS)
#CREA UN CONSECUTIVO EN LA COLUMNA IDPAIS
DM_PAIS$IDPAIS<-1:x
#ESCRIBE EL DATFRAME A UN ARCHIVO CSV
write.csv(DM_PAIS,'c:/Borrar/DM_PAIS.csv', fileEncoding = "UTF-8",row.names = FALSE)
#EMPAREJA LA TABLA DE HECHO CON LA DIMENSION
COVID19<-merge(COVID19,DM_PAIS,by.x = "PAIS",by.y = "NOMBRE",all.x = TRUE)
#ORDENA LAS COLUMNAS
COVID19 <- COVID19 [, c (2:12)]

#****CREACION DE LA DIMENSION ESTADO ************
DM_ESTADO<-COVID19[,c(10,10)]
DM_ESTADO<-DM_ESTADO[!duplicated(DM_ESTADO), ]
colnames(DM_ESTADO)[1]<-'IDESTADO'
colnames(DM_ESTADO)[2]<-'NOMBRE'

x=nrow(DM_ESTADO)
DM_ESTADO$IDESTADO<-1:x
write.csv(DM_ESTADO,'c:/Borrar/DM_ESTADO.csv', fileEncoding = "UTF-8",row.names = FALSE)
COVID19<-merge(COVID19,DM_ESTADO,by.x = "Estado",by.y = "NOMBRE",all.x = TRUE)
COVID19 <- COVID19 [, c (2:12)]

#****CREACION DE LA DIMENSION TIPO ************
DM_TIPO<-COVID19[,c(9,9)]
DM_TIPO<-DM_TIPO[!duplicated(DM_TIPO), ]
colnames(DM_TIPO)[1]<-'IDTIPO'
colnames(DM_TIPO)[2]<-'NOMBRE'
x=nrow(DM_TIPO)
DM_TIPO$IDTIPO<-1:x
write.csv(DM_ESTADO,'c:/Borrar/DM_ESTADO.csv', fileEncoding = "UTF-8",row.names = FALSE)
COVID19<-merge(COVID19,DM_TIPO,by.x = "Tipo",by.y = "NOMBRE",all.x = TRUE)
COVID19 <- COVID19 [, c (2:12)]

#****CREACION DE LA DIMENSION ATENCION ************
DM_ATENCION<-COVID19[,c(6,6)]
DM_ATENCION<-DM_ATENCION[!duplicated(DM_ATENCION), ]
colnames(DM_ATENCION)[1]<-'IDATENCION'
colnames(DM_ATENCION)[2]<-'NOMBRE'
x=nrow(DM_ATENCION)
DM_ATENCION$IDATENCION<-1:x
write.csv(DM_ATENCION,'c:/Borrar/DM_ATENCION.csv', fileEncoding = "UTF-8",row.names = FALSE)
COVID19<-merge(COVID19,DM_ATENCION,by.x = "atención",by.y = "NOMBRE",all.x = TRUE)
COVID19 <- COVID19 [, c (2:12)]

colnames(COVID19)[1]<-'ID'
colnames(COVID19)[3]<-'IDCIUDAD'
colnames(COVID19)[2]<-'FECHA'
COVID19$IDDPTO<-as.integer(COVID19$IDCIUDAD/1000)

#****CREACION DE LA DIMENSION CIUDAD ************
DM_CIUDAD<-COVID19[,c(3,4)]
DM_CIUDAD<-DM_CIUDAD[!duplicated(DM_CIUDAD), ]
colnames(DM_CIUDAD)[1]<-'IDCIUDAD'
colnames(DM_CIUDAD)[2]<-'NOMBRE'
write.csv(DM_CIUDAD,'c:/Borrar/DM_CIUDAD.csv', fileEncoding = "UTF-8",row.names = FALSE)
COVID19<-COVID19[,-c(4)]
COVID19 <- COVID19 [, c (2:11,1)]

#****CREACION DE LA DIMENSION DEPARTAMENTO ************
DM_DEPARTAMENTO<-COVID19[,c(10,3)]
DM_DEPARTAMENTO<-DM_DEPARTAMENTO[!duplicated(DM_DEPARTAMENTO), ]
colnames(DM_DEPARTAMENTO)[1]<-'IDDPTO'
colnames(DM_DEPARTAMENTO)[2]<-'NOMBRE'
COVID19<-COVID19[,-c(3)]
write.csv(DM_DEPARTAMENTO,'c:/Borrar/DM_DEPARTAMENTO.csv', fileEncoding = "UTF-8",row.names = FALSE)

DM_FECHA<-COVID19[,c(1,1)]
DM_FECHA<-DM_FECHA[!duplicated(DM_FECHA), ]
colnames(DM_FECHA)[1]<-'IDFECHA'
colnames(DM_FECHA)[2]<-'NOMBRE'
x=nrow(DM_FECHA)
DM_FECHA$IDFECHA<-1:x
write.csv(DM_FECHA,'c:/Borrar/DM_FECHA.csv', fileEncoding = "UTF-8",row.names = FALSE)
COVID19<-merge(COVID19,DM_FECHA,by.x = "FECHA",by.y = "NOMBRE",all.x = TRUE)
COVID19 <- COVID19 [, c (10:11,2:9)]
COVID19 <- COVID19 [, c (1:3,10,4:9)]

write.csv(COVID19,'c:/Borrar/THCOVID19.csv', fileEncoding = "UTF-8",row.names = FALSE)

