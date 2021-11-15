CREATE OR REPLACE PROCEDURE TURISMO.spUpdateDepartments (
  ID IN TURISMO.DEPARTAMENTO.ID_DEPTO%TYPE,
  nombre IN TURISMO.DEPARTAMENTO.NOM_DEPTO%TYPE,
  direccion IN TURISMO.DEPARTAMENTO.DIRECCION_DEPTO%TYPE,
  habitaciones IN TURISMO.DEPARTAMENTO.CANT_HABITACIONES%TYPE,
  estacionamientos IN TURISMO.DEPARTAMENTO.CANT_ESTACIONAMIENTOS%TYPE,
  banos IN TURISMO.DEPARTAMENTO.CANT_BANOS%TYPE,
  internet IN TURISMO.DEPARTAMENTO.INTERNET%TYPE,
  cable IN TURISMO.DEPARTAMENTO.CABLE%TYPE,
  calefaccion IN TURISMO.DEPARTAMENTO.CALEFACCION%TYPE,
  amoblado IN TURISMO.DEPARTAMENTO.AMOBLADO%TYPE,
  precio IN TURISMO.DEPARTAMENTO.PRECIO_DEPTO%TYPE,
  estado IN TURISMO.DEPARTAMENTO.ESTADO_DEPTO%TYPE,
  descripcion IN TURISMO.DEPARTAMENTO.DESCRIPCION_DEPTO%TYPE,
  comuna IN TURISMO.DEPARTAMENTO.COMUNA_ID_COMUNA%TYPE
 ) 
 AS
 BEGIN
  UPDATE DEPARTAMENTO SET NOM_DEPTO = NOMBRE,
                          DIRECCION_DEPTO = DIRECCION,
                          CANT_HABITACIONES = HABITACIONES,
                          CANT_ESTACIONAMIENTOS = ESTACIONAMIENTOS,
                          CANT_BANOS = BANOS,
                          INTERNET = INTERNET,
                          CABLE = CABLE,
                          CALEFACCION = CALEFACCION,
                          AMOBLADO = AMOBLADO,
                          PRECIO_DEPTO = PRECIO,
                          ESTADO_DEPTO = ESTADO,
                          DESCRIPCION_DEPTO = DESCRIPCION WHERE ID_DEPTO = ID; 
 COMMIT;
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spUpdateServExtra (
  id TURISMO.SERVICIO_EXTRA.ID_SERV%TYPE,
  descripcion TURISMO.SERVICIO_EXTRA.DESC_SERV%TYPE,
  precio TURISMO.SERVICIO_EXTRA.VALOR_SERV%TYPE
 )
 AS
 BEGIN
  UPDATE SERVICIO_EXTRA SET DESC_SERV = DESCRIPCION, VALOR_SERV = PRECIO WHERE ID_SERV = ID;
  COMMIT;
  EXCEPTION WHEN
  OTHERS THEN
  DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spUpdateUser (
  ID TURISMO.USUARIO.ID_USU%TYPE,
  NOM IN TURISMO.USUARIO.NOM_USU%TYPE,
  APP TURISMO.USUARIO.APP_USU%TYPE,
  APM TURISMO.USUARIO.APM_USU%TYPE,
  FNACIMIENTO VARCHAR2,
  EMAIL TURISMO.USUARIO.EMAIL_USU%TYPE,
  CELULAR TURISMO.USUARIO.CELULAR_USU%TYPE,
  CONTRASENA TURISMO.USUARIO.CONTRASENA_USU%TYPE,
  IDCOMUNA TURISMO.USUARIO.COMUNA_ID_COMUNA%TYPE,
  TIPOUSUARIO TURISMO.USUARIO.TIPO_USUARIO_ID_TIPO%TYPE
 )
 AS
 BEGIN
  UPDATE USUARIO SET NOM_USU = NOM,
                     APP_USU = APP,
                     APM_USU = APM,
                     FNACIMIENTO_USU = TO_DATE(FNACIMIENTO, 'DD/MM/YYYY'),
                     EMAIL_USU = EMAIL,
                     CELULAR_USU = CELULAR,
                     CONTRASENA_USU = CONTRASENA,
                     COMUNA_ID_COMUNA = IDCOMUNA,
                     TIPO_USUARIO_ID_TIPO = TIPOUSUARIO WHERE ID_USU = ID;
                     COMMIT;
 EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spUpdateDisponibility (
  id IN TURISMO.DEPARTAMENTO.ID_DEPTO%TYPE
 )
 AS
 disponibility TURISMO.DEPARTAMENTO.ESTADO_DEPTO%TYPE;
 BEGIN
  SELECT "d".ESTADO_DEPTO INTO DISPONIBILITY FROM DEPARTAMENTO "d" WHERE "d".ID_DEPTO = ID;
  
  IF DISPONIBILITY = '0'
  THEN
  UPDATE DEPARTAMENTO SET ESTADO_DEPTO = '1' WHERE ID_DEPTO = ID;
  COMMIT;
  ELSE
  UPDATE DEPARTAMENTO
  SET ESTADO_DEPTO = '0' WHERE ID_DEPTO = ID;
  COMMIT;
  END IF;
END;
/