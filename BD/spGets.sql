CREATE OR REPLACE PROCEDURE TURISMO.spGetActa
  (pActa out sys_refcursor)
 AS
  BEGIN
  OPEN pActa FOR
      SELECT "a".ID_ACTA, "a".NOMBRE_MULTA, "a".DESCRIPCION_MULTA, "a".VALOR_MULTA FROM ACTA "a";
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetActa;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetCiudad
  (pCiudad out sys_refcursor)
 AS
 BEGIN
  OPEN pCiudad FOR
      SELECT "c".ID_CIUDAD, "c".NOMBRE_CIUDAD FROM CIUDAD "c";
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetCiudad;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetComuna
    (pComuna out sys_refcursor)
  AS
  BEGIN
    OPEN pComuna FOR
        SELECT ID_COMUNA, NOMBRE_COMUNA FROM COMUNA "c";
      EXCEPTION
      WHEN OTHERS THEN
          dbms_output.put_line(sqlerrm);
END spGetComuna;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETDEPARTMENTS(PDEPARTMENTS OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN PDEPARTMENTS FOR
    SELECT ID_DEPTO,
           NOM_DEPTO,
           DIRECCION_DEPTO,
           CANT_HABITACIONES,
           CANT_ESTACIONAMIENTOS,
           CANT_BANOS,
           INTERNET,
           CABLE,
           CALEFACCION,
           AMOBLADO,
           PRECIO_DEPTO,
           ESTADO_DEPTO,
           DESCRIPCION_DEPTO,
           "c".ID_COMUNA,
           "c".NOMBRE_COMUNA
      FROM DEPARTAMENTO
        JOIN COMUNA "c"
          ON DEPARTAMENTO.COMUNA_ID_COMUNA = "c".ID_COMUNA;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM);
  END SPGETDEPARTMENTS;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetInventory 
  (pInventario out sys_refcursor)
  AS
  BEGIN
  OPEN pInventario FOR
  SELECT "i".NOMBRE_OBJ, "i".ID_OBJ, "i".DESC_OBJ FROM INVENTARIO "i";
  EXCEPTION
      WHEN OTHERS THEN
          dbms_output.put_line(sqlerrm);
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETINVENTORYDEPARTMENT(PINVENTORYDEPARTMENT OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN PINVENTORYDEPARTMENT FOR
    SELECT "di".ID,
           "di".CANTIDAD,
           "di".DEPARTAMENTO_ID_DEPTO,
           "i".ID_OBJ,"i".NOMBRE_OBJ
      FROM DEPARTAMENTO_INVENTARIO "di"
        JOIN INVENTARIO "i"
          ON "di".INVENTARIO_ID_OBJ = "i".ID_OBJ;
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETMAINTAINSDEPARTMENT(PMAINTAINS OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN PMAINTAINS FOR
    SELECT "m".ID_MANTENCION,
           TO_CHAR("m".FECHA_INICIO,'DD/MM/YYYY'),
           TO_CHAR("m".FECHA_TERMINO,'DD/MM/YYYY'),
           "u".ID_USU,
           "u".NOM_USU ||'-'||"u".APP_USU||'-'|| "u".APM_USU  AS nameUser,
           "m".DEPARTAMENTO_ID_DEPTO
      FROM MANTENCION "m"
        JOIN USUARIO "u"
          ON "m".ID_FUNCIONARIO = "u".ID_USU;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM);
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetRegion
  (pRegion out sys_refcursor)
 AS
 BEGIN
  OPEN pRegion FOR
    SELECT ID_REGION, NOMBRE_REGION FROM REGION "r";
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetRegion;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetServExtra
  (pServicio out sys_refcursor)
 AS
 BEGIN
  OPEN pServicio FOR
      SELECT ID_SERV, DESC_SERV, VALOR_SERV FROM SERVICIO_EXTRA;
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetServExtra;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETUSERS(PUSER OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN PUSER FOR
    SELECT "u".ID_USU,
           "u".NOM_USU,
           "u".APP_USU,
           "u".APM_USU,
           "u".FNACIMIENTO_USU,
           "u".EMAIL_USU,
           "u".CELULAR_USU,
           "u".CONTRASENA_USU,
           "c".ID_COMUNA,
           "c".NOMBRE_COMUNA,
           "tu".ID_TIPO,
           "tu".NOMBRE_TIPO
      FROM USUARIO "u"
        JOIN COMUNA "c"
          ON "u".COMUNA_ID_COMUNA = "c".ID_COMUNA
        JOIN TIPO_USUARIO "tu"
          ON "u".TIPO_USUARIO_ID_TIPO = "tu".ID_TIPO;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM);
  END;
/