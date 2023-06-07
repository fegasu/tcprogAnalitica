# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
drop database covid19;

create database if not exists COVID19;
use covid19

CREATE TABLE DM_PAIS( ID_PAIS INT PRIMARY KEY AUTO_INCREMENT, NOMBRE VARCHAR(30) );

LOAD DATA INFILE 'c:/Borrar/DM_PAIS.csv' INTO TABLE DM_PAIS
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ID_PAIS,NOMBRE);

CREATE TABLE DM_ATENCION(
IDATENCION INTEGER PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(30)
);

LOAD DATA INFILE 'c:/Borrar/DM_ATENCION.csv' INTO TABLE DM_ATENCION
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDATENCION,NOMBRE);

CREATE TABLE DM_TIPO(
IDTIPO INTEGER PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(30)
);

LOAD DATA INFILE 'c:/Borrar/DM_TIPO.csv' INTO TABLE DM_TIPO
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDTIPO,NOMBRE);

CREATE TABLE DM_ESTADO(
IDESTADO INTEGER PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(30)
);

LOAD DATA INFILE 'c:/Borrar/DM_ESTADO.csv' INTO TABLE DM_ESTADO
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDESTADO,NOMBRE);

CREATE TABLE DM_FECHA(
IDFECHA INTEGER PRIMARY KEY AUTO_INCREMENT,
FECHA DATETIME
);

LOAD DATA INFILE 'c:/Borrar/DM_FECHA.csv' INTO TABLE DM_FECHA
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDFECHA,FECHA);

CREATE TABLE DM_DEPARTAMENTO(
IDDPTO INTEGER PRIMARY KEY,
NOMBRE TEXT
);

LOAD DATA INFILE 'c:/Borrar/DM_DEPARTAMENTO.csv' INTO TABLE DM_DEPARTAMENTO
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDDPTO,NOMBRE);

CREATE TABLE DM_CIUDAD(
IDCIUDAD INTEGER PRIMARY KEY,
NOMBRE TEXT
);

LOAD DATA INFILE 'c:/Borrar/DM_CIUDAD.csv' INTO TABLE DM_CIUDAD
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDCIUDAD,NOMBRE);

CREATE TABLE DM_SEXO(
IDSEXO INTEGER PRIMARY KEY,
NOMBRE TEXT
);

LOAD DATA INFILE 'c:/Borrar/DM_SEXO.csv' INTO TABLE DM_SEXO
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(IDSEXO,NOMBRE);

-- DROP TABLE TH_COVID19;
CREATE TABLE if not exists TH_COVID19(
ID INTEGER ,
IDFECHA INTEGER,
IDCIUDAD INTEGER,
IDDPTO INTEGER,
IDATENCION INTEGER,
EDAD INTEGER,
IDSEXO CHAR(1),
IDTIPO INTEGER,
IDESTADO INTEGER,
IDPAIS INTEGER,
GEDAD CHAR(1)
    
);

LOAD DATA INFILE 'c:/Borrar/TH_COVID19.csv' INTO TABLE TH_COVID19
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ID,IDFECHA,IDCIUDAD,IDDPTO,IDATENCION,EDAD,IDSEXO,IDTIPO,IDESTADO,IDPAIS,GEDAD);


# UPDATE TH_COVID19 SET IDESTADO=4 WHERE IDESTADO=0;
# ALTER TABLE TH_COVID19 ADD CONSTRAINT ESTADOFK FOREIGN KEY(IDESTADO) REFERENCES DM_ESTADO(IDESTADO);
# UPDATE TH_COVID19 SET IDATENCION=3 WHERE IDATENCION=0;
# ALTER TABLE TH_COVID19 ADD CONSTRAINT ATENCIONFK  FOREIGN KEY(IDATENCION) REFERENCES DM_ATENCION(IDATENCION);
# ALTER TABLE TH_COVID19 ADD CONSTRAINT CIUDADFK FOREIGN KEY(IDCIUDAD) REFERENCES DM_CIUDAD(IDCIUDAD);
# ALTER TABLE TH_COVID19 ADD CONSTRAINT DEPARTAMENTOFK FOREIGN KEY(IDDPTO) REFERENCES DM_DEPARTAMENTO(IDDPTO); 
# UPDATE TH_COVID19 SET IDTIPO=3 WHERE IDTIPO=0;
# ALTER TABLE TH_COVID19 ADD CONSTRAINT TIPOFK FOREIGN KEY(IDTIPO) REFERENCES DM_TIPO(IDTIPO);

SELECT IDPAIS,SEXO,COUNT(*) FROM TH_COVID19
WHERE IDPAIS=3
GROUP BY  IDPAIS,SEXO WITH ROLLUP;

SELECT IDSEXO,COUNT(*) FROM TH_COVID19
GROUP BY  IDSEXO;

SELECT IDSEXO,IDCIUDAD,COUNT(*) FROM TH_COVID19
WHERE IDSEXO='F' AND IDCIUDAD=11001
GROUP BY  IDSEXO,IDCIUDAD;

DROP TABLE IF EXISTS CUBO_COVID19;

CREATE TABLE CUBO_COVID19 AS
SELECT IDFECHA,IDCIUDAD,IDDPTO,IDATENCION,EDAD,IDSEXO,IDTIPO,IDESTADO,IDPAIS,GEDAD,COUNT(*) REGISTROS FROM TH_COVID19
GROUP BY  IDFECHA,IDCIUDAD,IDDPTO,IDATENCION,EDAD,IDSEXO,IDTIPO,IDESTADO,IDPAIS,GEDAD
WITH ROLLUP;

CREATE OR REPLACE VIEW VCUBOCOVID19 AS
SELECT  IDFECHA,(SELECT FECHA FROM DM_FECHA  WHERE IDFECHA=CO.IDFECHA) FECHA
,IDCIUDAD,(SELECT NOMBRE FROM DM_CIUDAD  WHERE IDCIUDAD=CO.IDCIUDAD) CIUDAD
,CO.IDDPTO,(SELECT NOMBRE FROM DM_DEPARTAMENTO  WHERE IDDPTO=CO.IDDPTO) DPTO
,IDATENCION,(SELECT NOMBRE FROM DM_ATENCION  WHERE IDATENCION=CO.IDATENCION) ATENCION
,EDAD,IDSEXO
,(SELECT NOMBRE FROM DM_TIPO  WHERE IDTIPO=CO.IDTIPO) TIPO
,(SELECT NOMBRE FROM DM_ESTADO WHERE IDESTADO=CO.IDESTADO) ESTADO
,(SELECT NOMBRE FROM DM_PAIS WHERE ID_PAIS=CO.IDPAIS) PAIS
,GEDAD,registros
FROM CUBO_COVID19 CO;