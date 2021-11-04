CREATE OR REPLACE PROCEDURE TURISMO.spDeleteDepartments (
  ID IN TURISMO.DEPARTAMENTO.ID_DEPTO%TYPE
) 
AS
BEGIN
  DELETE DEPARTAMENTO WHERE ID_DEPTO = ID;
  COMMIT;
  EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END;
/
CREATE OR REPLACE PROCEDURE TURISMO.spDeleteInventory (
ID IN TURISMO.INVENTARIO.ID_OBJ%TYPE
)
AS
BEGIN
  DELETE INVENTARIO WHERE ID_OBJ = ID;
  COMMIT;
  EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END;
/