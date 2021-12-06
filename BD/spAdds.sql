CREATE OR REPLACE PROCEDURE TURISMO.spAddDepartment (
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
  comuna IN TURISMO.DEPARTAMENTO.COMUNA_ID_COMUNA%TYPE,
  imgPath IN TURISMO.DEPARTAMENTO.IMG_PATH%TYPE
 ) 
 IS
    ID NUMBER;
 BEGIN
    SELECT SEQ_DEPARTAMENTO.NEXTVAL INTO ID FROM DUAL "d";
    INSERT INTO DEPARTAMENTO (ID_DEPTO, NOM_DEPTO, DIRECCION_DEPTO, CANT_HABITACIONES, CANT_ESTACIONAMIENTOS, CANT_BANOS, INTERNET, CABLE,
                CALEFACCION, AMOBLADO, PRECIO_DEPTO, ESTADO_DEPTO, DESCRIPCION_DEPTO,COMUNA_ID_COMUNA, IMG_PATH) 
                VALUES (ID,NOMBRE,DIRECCION,HABITACIONES,ESTACIONAMIENTOS,BANOS,INTERNET,CABLE,CALEFACCION,AMOBLADO,PRECIO,ESTADO,DESCRIPCION,COMUNA,imgPath);
    COMMIT;
    EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
 END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spAddInventoryDepartment (
 --  id_inventarioDepartamento IN TURISMO.DEPARTAMENTO_INVENTARIO.ID%TYPE,
  cantidad IN TURISMO.DEPARTAMENTO_INVENTARIO.CANTIDAD%TYPE,
  id_depto IN TURISMO.DEPARTAMENTO_INVENTARIO.DEPARTAMENTO_ID_DEPTO%TYPE,
  id_inventario IN TURISMO.DEPARTAMENTO_INVENTARIO.INVENTARIO_ID_OBJ%TYPE
 ) 
 AS
  ID_aux NUMBER;
 BEGIN
  SELECT SEQ_INVENTARIO.NEXTVAL INTO ID_aux FROM DUAL "d";
      INSERT INTO DEPARTAMENTO_INVENTARIO (ID, CANTIDAD, DEPARTAMENTO_ID_DEPTO, INVENTARIO_ID_OBJ) VALUES (ID_aux,CANTIDAD,ID_DEPTO,ID_INVENTARIO);
      COMMIT;
      EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPADDMAINTAINSDEPARTMENTS
 (FECHAINICIO VARCHAR2,
 FECHATERMINO VARCHAR2,
 IDFUNCIONARIO IN TURISMO.MANTENCION.ID_FUNCIONARIO % TYPE,
 IDDEPARTAMENTO IN TURISMO.MANTENCION.DEPARTAMENTO_ID_DEPTO % TYPE)
  AS
    ID NUMBER;
  BEGIN
  SELECT SEQ_MANTENCION.NEXTVAL INTO ID FROM DUAL "d";
    INSERT INTO MANTENCION (
      ID_MANTENCION, FECHA_INICIO, FECHA_TERMINO, ID_FUNCIONARIO, DEPARTAMENTO_ID_DEPTO)
    VALUES (ID,TO_DATE(FECHAINICIO,'DD/MM/YYYY'), TO_DATE(FECHATERMINO,'DD/MM/YYYY'),IDFUNCIONARIO,IDDEPARTAMENTO);
    COMMIT;
    EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPADDMULTA(CANTIDAD  IN NUMBER,
                                               SUBTOTAL IN TURISMO.RESERVA_ACTA.SUBTOTAL_ACTA%TYPE,
                                               ACTAID    IN TURISMO.ACTA.ID_ACTA % TYPE,
                                               RESERVAID IN TURISMO.RESERVA.ID_RESERVA % TYPE
                                               )
  AS
    ID_AUX NUMBER;
  BEGIN
    SELECT SEQ_INGRESOMULTA.nextval INTO ID_AUX FROM DUAL;

    INSERT INTO RESERVA_ACTA (
      ID, CANTIDAD_ACTA ,SUBTOTAL_ACTA, ACTA_ID_ACTA, RESERVA_ID_RESERVA
    )
    VALUES (ID_AUX, CANTIDAD, SUBTOTAL, ACTAID, RESERVAID);
    COMMIT;
    EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/


CREATE OR REPLACE PROCEDURE TURISMO.SPADDRESERVA(CHECKIN_PLANIFICADO IN VARCHAR2,
                                                 CHECKOUT            IN VARCHAR2,
                                                 CANTDIAS            IN TURISMO.RESERVA.CANT_DIAS % TYPE,
                                                 CANTADULTOS         IN TURISMO.RESERVA.CANT_ADULTOS % TYPE,
                                                 CANTNINOS           IN TURISMO.RESERVA.CANT_NINOS % TYPE,
                                                 CANTBEBES           IN TURISMO.RESERVA.CANT_BEBES % TYPE,
                                                 TOTALRESERVA        IN TURISMO.RESERVA.TOTAL_RESERVA % TYPE,
                                                 ESTADORESERVA       IN TURISMO.RESERVA.ESTADO_RESERVA % TYPE,
                                                 DEPTOID             IN TURISMO.RESERVA.DEPARTAMENTO_ID_DEPTO % TYPE,
                                                 CLIENTEID           IN TURISMO.RESERVA.ID_CLIENTE % TYPE)
  AS
    ID_AUX NUMBER;
    ID_WORKERRAN NUMBER;
  BEGIN

    SELECT SEQ_RESERVA.nextval
      INTO ID_AUX
      FROM DUAL "d";
      
    SELECT ID_USU 
        into ID_WORKERRAN
    from USUARIO
    where TIPO_USUARIO_ID_TIPO = 2
    and ROWNUM=1 ORDER BY DBMS_RANDOM.RANDOM;
    
    INSERT INTO RESERVA (
      ID_RESERVA, CHECK_IN_PLANIFICADO, CHECK_IN, CHECK_OUT, CANT_DIAS, CANT_ADULTOS, CANT_NINOS, CANT_BEBES, TOTAL_RESERVA, ESTADO_RESERVA, DEPARTAMENTO_ID_DEPTO, ID_CLIENTE, ID_FUNCIONARIO
    )
    VALUES (ID_AUX, TO_DATE(CHECKIN_PLANIFICADO, 'DD/MM/YYYY'), NULL,TO_DATE(CHECKOUT, 'DD/MM/YYYY'), CANTDIAS, CANTADULTOS, CANTNINOS, CANTBEBES, TOTALRESERVA, ESTADORESERVA, DEPTOID, CLIENTEID, ID_WORKERRAN);

    spUpdateDisponibility(DEPTOID);
    COMMIT;
    EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spAddServExtra (
  --  id TURISMO.SERVICIO_EXTRA.ID_SERV%TYPE,
  descripcion TURISMO.SERVICIO_EXTRA.DESC_SERV%TYPE,
  precio TURISMO.SERVICIO_EXTRA.VALOR_SERV%TYPE
 )
 AS
  ID NUMBER;
 BEGIN
  SELECT SEQ_SERV_EXTRA.NEXTVAL INTO ID FROM DUAL "d";
  INSERT INTO SERVICIO_EXTRA (ID_SERV, DESC_SERV, VALOR_SERV) VALUES (ID,DESCRIPCION,PRECIO);
  COMMIT;
  EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spAddUser (
 --  ID_USU               NUMBER(10, 0)      NOT NULL,
  NOM IN TURISMO.USUARIO.NOM_USU%TYPE,
  RUT IN TURISMO.USUARIO.RUT_USU%TYPE,
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
 ID NUMBER;
 BEGIN
  SELECT SEQ_USERS.NEXTVAL INTO ID FROM DUAL "d";
  INSERT INTO USUARIO (ID_USU, RUT_USU, NOM_USU, APP_USU, APM_USU, FNACIMIENTO_USU, EMAIL_USU, CELULAR_USU,CONTRASENA_USU, COMUNA_ID_COMUNA, TIPO_USUARIO_ID_TIPO)
  VALUES (ID,RUT ,NOM,APP,APM,TO_DATE(FNACIMIENTO,'DD/MM/YYYY'),EMAIL,CELULAR,CONTRASENA,IDCOMUNA,TIPOUSUARIO);
  COMMIT;
 EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/
CREATE OR REPLACE PROCEDURE TURISMO.spAddReservaServex (
  CANTIDAD TURISMO.RESERVA_SERVEX.CANTIDAD_SERVEX%TYPE,
  SUBTOTAL TURISMO.RESERVA_SERVEX.SUBTOTAL_SERVEX%TYPE,
  ID_SERVEX TURISMO.RESERVA_SERVEX.SERVICIO_EXTRA_ID_SERV%TYPE,
  IDRESERVA TURISMO.RESERVA_SERVEX.RESERVA_ID_RESERVA%TYPE
)
AS
ID_AUX NUMBER;
BEGIN
  SELECT SEQ_RESERVASERVEX.nextval INTO ID_AUX FROM DUAL "d";
  INSERT INTO RESERVA_SERVEX (ID, CANTIDAD_SERVEX, SUBTOTAL_SERVEX, SERVICIO_EXTRA_ID_SERV, RESERVA_ID_RESERVA) VALUES (ID_AUX,CANTIDAD,SUBTOTAL,ID_SERVEX,IDRESERVA);
  COMMIT;
  EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spAddTransport (
  LUGAR TURISMO.TRANSPORTE.LUGAR_TRANS%TYPE,
  HORARIO TURISMO.TRANSPORTE.HORARIO_TRANS%TYPE,
  VEHICULO TURISMO.TRANSPORTE.VEHICULO_TRANS%TYPE,
  IDRESERVA TURISMO.TRANSPORTE.RESERVA_ID_RESERVA%TYPE,
  IDFUNCIONARIO TURISMO.TRANSPORTE.ID_FUNCIONARIO%TYPE
) 
AS
ID_AUX NUMBER;
BEGIN
  SELECT SEQ_TRANSPORT.nextval INTO ID_AUX FROM DUAL "d";
  INSERT INTO TRANSPORTE (ID_TRANS, LUGAR_TRANS, HORARIO_TRANS, VEHICULO_TRANS, RESERVA_ID_RESERVA, ID_FUNCIONARIO) VALUES (ID_AUX,LUGAR,HORARIO,VEHICULO,IDRESERVA,IDFUNCIONARIO);
  COMMIT;
  EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/
