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

CREATE OR REPLACE PROCEDURE TURISMO.SPGETDEPARTMENTBYDISPONIBILITY(DISPONIBILITY  IN  TURISMO.DEPARTAMENTO.ESTADO_DEPTO % TYPE,
                                                                   CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "d".ID_DEPTO,--0
           "d".NOM_DEPTO,--1
           "d".DIRECCION_DEPTO,--2
           "d".CANT_HABITACIONES,--3
           "d".CANT_ESTACIONAMIENTOS,--4
           "d".CANT_BANOS,--5
           "d".INTERNET,--6
           "d".CABLE,--7
           "d".CALEFACCION,--8
           "d".AMOBLADO,--9
           "d".PRECIO_DEPTO,--10
           "d".ESTADO_DEPTO,--11
           "r".NOMBRE_REGION || ', ' || "c1".NOMBRE_CIUDAD || ', ' || "c".NOMBRE_COMUNA AS UBICACION, --12
           "d".DESCRIPCION_DEPTO, --13
           "d".IMG_PATH
      FROM DEPARTAMENTO "d"
        JOIN COMUNA "c"
          ON "d".COMUNA_ID_COMUNA = "c".ID_COMUNA
        JOIN CIUDAD "c1"
          ON "c".CIUDAD_ID_CIUDAD = "c1".ID_CIUDAD
        JOIN REGION "r"
          ON "c1".REGION_ID_REGION = "r".ID_REGION
      WHERE  1=1
      and "d".ESTADO_DEPTO = 1
      and ROWNUM <= 15;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETDEPARTMENTBYID(ID  IN  TURISMO.DEPARTAMENTO.ID_DEPTO % TYPE,
                                                        CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "d".ID_DEPTO,
           "d".NOM_DEPTO,
           "d".DIRECCION_DEPTO,
           "d".CANT_HABITACIONES,
           "d".CANT_ESTACIONAMIENTOS,
           "d".CANT_BANOS,
           "d".INTERNET,
           "d".CABLE,
           "d".CALEFACCION,
           "d".AMOBLADO,
           "d".PRECIO_DEPTO,
           "d".ESTADO_DEPTO,
           "r".NOMBRE_REGION || ', ' || "c1".NOMBRE_CIUDAD || ', ' || "c".NOMBRE_COMUNA AS UBICACION,
           "d".DESCRIPCION_DEPTO,
           "d".IMG_PATH
      FROM DEPARTAMENTO "d"
        JOIN COMUNA "c"
          ON "d".COMUNA_ID_COMUNA = "c".ID_COMUNA
        JOIN CIUDAD "c1"
          ON "c".CIUDAD_ID_CIUDAD = "c1".ID_CIUDAD
        JOIN REGION "r"
          ON "c1".REGION_ID_REGION = "r".ID_REGION
      WHERE "d".ID_DEPTO = ID;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
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

CREATE OR REPLACE PROCEDURE TURISMO.SPGETMAINTAINDEPARTMENTBYID(id IN  NUMBER,
                                                                CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "m".ID_MANTENCION,
           TO_CHAR("m".FECHA_INICIO, 'DD/MM/YYYY'),
           TO_CHAR("m".FECHA_TERMINO, 'DD/MM/YYYY'),
           "u".ID_USU,
           "u".NOM_USU || '-' || "u".APP_USU || '-' || "u".APM_USU AS NAMEUSER,
           "m".DEPARTAMENTO_ID_DEPTO
      FROM MANTENCION "m" 
        JOIN USUARIO "u"
          ON "m".ID_FUNCIONARIO = "u".ID_USU
        JOIN DEPARTAMENTO "d"
          ON "m".DEPARTAMENTO_ID_DEPTO = "d".ID_DEPTO
      WHERE "m".DEPARTAMENTO_ID_DEPTO = id;
      EXCEPTION WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
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

CREATE OR REPLACE PROCEDURE TURISMO.SPGETMULTA(IDRESERVA IN  TURISMO.RESERVA_ACTA.ID % TYPE,
                                               CUR       OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "ra".ID,
           "ra".CANTIDAD_ACTA,
           "ra".SUBTOTAL_ACTA,
           "ra".ACTA_ID_ACTA,
           "ra".RESERVA_ID_RESERVA
      FROM RESERVA_ACTA "ra"
      WHERE "ra".RESERVA_ID_RESERVA = IDRESERVA;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
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

CREATE OR REPLACE PROCEDURE TURISMO.SPGETRESERVA(CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "r".ID_RESERVA,
           TO_CHAR("r".CHECK_IN_PLANIFICADO, 'DD/MM/YYYY'),
           TO_CHAR("r".CHECK_IN, 'DD/MM/YYYY'),
           TO_CHAR("r".CHECK_OUT, 'DD/MM/YYYY'),
           "r".CANT_DIAS,
           "r".CANT_ADULTOS,
           "r".CANT_NINOS,
           "r".TOTAL_RESERVA,
           "r".ESTADO_RESERVA,
           "r".DEPARTAMENTO_ID_DEPTO,
           "r".ID_CLIENTE,
           "r".ID_FUNCIONARIO,
           "d".NOM_DEPTO,
           "d".DIRECCION_DEPTO,
           "d".CANT_HABITACIONES,
           "d".CANT_ESTACIONAMIENTOS,
           "d".CANT_BANOS,
           "d".INTERNET,
           "d".CABLE,
           "d".CALEFACCION,
           "d".AMOBLADO,
           "d".PRECIO_DEPTO,
           "d".ESTADO_DEPTO,
           "d".DESCRIPCION_DEPTO,
           "d".COMUNA_ID_COMUNA
      FROM RESERVA "r"
        JOIN DEPARTAMENTO "d"
          ON "r".DEPARTAMENTO_ID_DEPTO = "d".ID_DEPTO
        JOIN COMUNA "c"
          ON "d".COMUNA_ID_COMUNA = "c".ID_COMUNA;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETRESERVASERVEX(IDRESERVA IN  TURISMO.RESERVA_ACTA.ID % TYPE,
                                                       CUR       OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "rs".ID,
           "rs".CANTIDAD_SERVEX,
           "rs".SUBTOTAL_SERVEX,
           "rs".SERVICIO_EXTRA_ID_SERV,
           "rs".RESERVA_ID_RESERVA,
           "se".DESC_SERV
      FROM RESERVA_SERVEX "rs"
      INNER JOIN SERVICIO_EXTRA "se" 
        ON "rs".SERVICIO_EXTRA_ID_SERV = "se".ID_SERV
      WHERE "rs".RESERVA_ID_RESERVA = IDRESERVA;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
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

CREATE OR REPLACE PROCEDURE TURISMO.spGetTypeUser (pTypeUsers OUT SYS_REFCURSOR)
 AS
 BEGIN
 OPEN pTypeUsers FOR                
  SELECT "tu".ID_TIPO, "tu".NOMBRE_TIPO FROM TIPO_USUARIO "tu";
  EXCEPTION WHEN 
  OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETUSERS(PUSER OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN PUSER FOR
    SELECT "u".ID_USU,
           "u".RUT_USU,
           "u".NOM_USU,
           "u".APP_USU,
           "u".APM_USU,
           TO_CHAR("u".FNACIMIENTO_USU,'DD/MM/YYYY'),
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

CREATE OR REPLACE PROCEDURE TURISMO.SPGETINVENTORYDEPARTMENTBYID(ID  IN  NUMBER,
                                                                 CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "di".ID,
           "di".CANTIDAD,
           "di".DEPARTAMENTO_ID_DEPTO,
           "di".INVENTARIO_ID_OBJ,
           "i".NOMBRE_OBJ
      FROM DEPARTAMENTO_INVENTARIO "di"
      JOIN INVENTARIO "i" ON "di".INVENTARIO_ID_OBJ = "i".ID_OBJ WHERE "di".DEPARTAMENTO_ID_DEPTO = ID;
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetTransports(CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT tt.ID_TRANS
        , tt.RESERVA_ID_RESERVA
        , (cli.NOM_USU||' '||cli.APP_USU) as clientName
        , (wk.NOM_USU||' '||wk.APP_USU) as  workerName
        , tt.VEHICULO_TRANS 
        , tt.LUGAR_TRANS AS tripStart
        , (dep.DIRECCION_DEPTO||', '||com.NOMBRE_COMUNA) as tripEnd
        , tt.HORARIO_TRANS 
        , tt.ID_FUNCIONARIO
    FROM TRANSPORTE tt
    INNER JOIN RESERVA re on tt.RESERVA_ID_RESERVA = re.ID_RESERVA
    INNER JOIN USUARIO cli on re.ID_CLIENTE = cli.ID_USU
    INNER JOIN  DEPARTAMENTO dep on re.DEPARTAMENTO_ID_DEPTO = dep.ID_DEPTO
    INNER JOIN  COMUNA com on dep.COMUNA_ID_COMUNA = com.ID_COMUNA
    INNER JOIN USUARIO wk on tt.ID_FUNCIONARIO = wk.ID_USU;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETRESERVABYUSER(ID TURISMO.USUARIO.ID_USU % TYPE,
                                               CUR OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "r".ID_RESERVA,
           "d".NOM_DEPTO,
           "c".NOMBRE_COMUNA,
           "d".DIRECCION_DEPTO
      FROM RESERVA "r"
        JOIN DEPARTAMENTO "d"
          ON "r".DEPARTAMENTO_ID_DEPTO = "d".ID_DEPTO
        JOIN COMUNA "c"
          ON "d".COMUNA_ID_COMUNA = "c".ID_COMUNA
        JOIN USUARIO "u"
          ON "r".ID_CLIENTE = "u".ID_USU
      WHERE "u".ID_USU = ID;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETRESERVABYID(ID_AUX     TURISMO.RESERVA.ID_RESERVA % TYPE,
                                                     CUR    OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "r".ID_RESERVA,
           "r".TOTAL_RESERVA,
           TO_CHAR("r".CHECK_IN, 'DD/MM/YYYY'),
           TO_CHAR("r".CHECK_OUT, 'DD/MM/YYYY')
      FROM RESERVA "r"
      WHERE "r".ID_RESERVA = ID_AUX;
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.SPGETORDERPAY(ID TURISMO.USUARIO.ID_USU % TYPE,
cur OUT SYS_REFCURSOR)
  AS
  BEGIN
  OPEN cur FOR
    SELECT "o".ID,
           "o".TOTAL_PAGO,
           "o".ESTADO,
           "o".FECHA_REGISTRO,
           "o".ID_RESERVA
      FROM ORDENPAGO "o"
        JOIN RESERVA "r"
          ON "o".ID_RESERVA = "r".ID_RESERVA
      WHERE "r".ID_CLIENTE = ID;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM);
  END;
/

CREATE OR REPLACE PROCEDURE TURISMO.spGetOrderPayById(ID_AUX     TURISMO.ORDENPAGO.ID % TYPE,
                                               CUR    OUT SYS_REFCURSOR)
  AS
  BEGIN
  OPEN CUR FOR
    SELECT "o".ID, "o".TOTAL_PAGO, "o".ESTADO, "o".FECHA_REGISTRO, "o".ID_RESERVA
      FROM ORDENPAGO "o" WHERE "o".ID = ID_AUX;
      EXCEPTION WHEN OTHERS THEN 
      DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/
CREATE OR REPLACE PROCEDURE TURISMO.spGetOrderPayById(ID_AUX     TURISMO.ORDENPAGO.ID % TYPE,
                                               CUR    OUT SYS_REFCURSOR)
  AS
  BEGIN
  OPEN CUR FOR
    SELECT "o".ID, "o".TOTAL_PAGO, "o".ESTADO, "o".FECHA_REGISTRO, "o".ID_RESERVA
      FROM ORDENPAGO "o" WHERE "o".ID = ID_AUX;
      EXCEPTION WHEN OTHERS THEN 
      DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/