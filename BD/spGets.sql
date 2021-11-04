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
CREATE OR REPLACE PROCEDURE TURISMO.spGetDepartments
  (pDepartments out sys_refcursor)
 AS
BEGIN
  OPEN pDepartments FOR
      SELECT ID_DEPTO, NOM_DEPTO, DIRECCION_DEPTO, CANT_HABITACIONES, CANT_ESTACIONAMIENTOS,
             CANT_BANOS, INTERNET, CABLE, CALEFACCION, AMOBLADO, FOTO_DEPTO, PRECIO_DEPTO,
             ESTADO_DEPTO, DESCRIPCION_DEPTO, COMUNA_ID_COMUNA FROM DEPARTAMENTO;
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetDepartments;
/
-- CREATE OR REPLACE PROCEDURE TURISMO.spGetUsers
--   (pUsers out sys_refcursor)
--  AS
-- BEGIN
--   OPEN pUsers FOR
--       SELECT "u".ID_USU, "u".NOM_USU, "u".APP_USU, "u".APM_USU, "u".FNACIMIENTO_USU, "u".EMAIL_USU, "u".CELULAR_USU, "u".CONTRASENA_USU FROM USUARIO "u";
--     EXCEPTION
--     WHEN OTHERS THEN
--         dbms_output.put_line(sqlerrm);
-- END spGetClients;
-- /
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
CREATE OR REPLACE PROCEDURE TURISMO.spGetActa
  (pActa out sys_refcursor)
 AS
BEGIN
  OPEN pActa FOR
      SELECT ID_ACTA, NOMBRE_MULTA, DESCRIPCION_MULTA, VALOR_MULTA, SUBTOTAL_MULTA FROM ACTA "a";
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetActa;
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