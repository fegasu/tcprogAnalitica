CREATE TABLE DM_PAIS(
    IDPAIS NUMBER        GENERATED BY DEFAULT ON NULL AS IDENTITY,
    NOMBRE VARCHAR2(255)
)

INSERT INTO DM_PAIS(NOMBRE) VALUES('SUTAPON');

SELECT * FROM DM_PAIS;