CREATE OR REPLACE PROCEDURE TURISMO.SPVALIDATELOGIN(CORREO   IN  TURISMO.USUARIO.EMAIL_USU % TYPE,
                                                    PASSWORD IN  TURISMO.USUARIO.CONTRASENA_USU % TYPE,
                                                    CUR      OUT SYS_REFCURSOR)
  AS
  BEGIN
    OPEN CUR FOR
    SELECT "u1".ID_USU,
           "u1".EMAIL_USU,
           "u1".NOM_USU,
           "u1".APP_USU,
           "u1".APM_USU,
           TO_CHAR("u1".FNACIMIENTO_USU,'DD/MM/YYYY'),
           "u1".CELULAR_USU,
           "u1".COMUNA_ID_COMUNA,
           "u1".TIPO_USUARIO_ID_TIPO,
           "tu".ID_TIPO,
           "tu".NOMBRE_TIPO
      FROM USUARIO "u1"
        JOIN TIPO_USUARIO "tu"
          ON "u1".TIPO_USUARIO_ID_TIPO = "tu".ID_TIPO
      WHERE "u1".EMAIL_USU = CORREO
        AND "u1".CONTRASENA_USU = PASSWORD;
  EXCEPTION
    WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(SQLERRM());
  END;
/