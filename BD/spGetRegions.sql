CREATE OR REPLACE PROCEDURE spGetRegions IS
BEGIN
  SELECT * FROM REGION "r";
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END