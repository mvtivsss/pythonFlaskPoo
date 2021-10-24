import cx_Oracle
import configuracion as cfg

def getRegions():
    try:
        with cx_Oracle.connect(cfg.username,
                               cfg.password,
                               cfg.dsn,
                               encoding=cfg.encoding) as connection:
            with connection.cursor() as cursor:
                cursor.callproc('spGetRegions')
    except cx_Oracle.Error as error:
        print(error)