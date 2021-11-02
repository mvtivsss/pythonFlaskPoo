CREATE OR REPLACE PROCEDURE spGetRegions,
  (region_id IN REGION.ID_REGION%TYPE,
   region_nom IN REGION.NOMBRE_REGION%TYPE,
   pRegions out sys_refcursor)
 AS
BEGIN
  OPEN pRegions FOR
    SELECT ID_REGION, NOMBRE_REGION FROM REGION "r";
    EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line(sqlerrm);
END spGetRegions;
/