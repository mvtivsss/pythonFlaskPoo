# Para la conexión a base de datos, es necesario descargar "Instant Client" de oracle.
# Luego los archivos .dll copiarlos y pegarlos en la carpeta donde tenemos almacenado python
# C:\Python39 en mi caso.
import cx_Oracle as conn

try:
    con = conn.connect('turismo/turismo@localhost:1521')
except Exception as err:
    print('Excepcion ocurrio en la creacion de la conexion a base de datos.')
else:
    try:
        cur = con.cursor()
        for row in cur.execute('SELECT * FROM REGION'):
            print(row)
        # cursor.callproc('sp_get_regions')
    except Exception as err:
        print('Error ocasionado en el procedimiento almacenado.', err)
    finally:
        cur.close()
finally:
    con.close()

# Comando para corroborar la conexión y la version a base de datos.
# con = conn.connect('turismo/turismo@localhost:1521')
# print("Database version:", con.version)