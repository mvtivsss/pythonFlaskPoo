# Para la conexión a base de datos, es necesario descargar "Instant Client" de oracle.
# Luego los archivos .dll copiarlos y pegarlos en la carpeta donde tenemos almacenado python
# C:\Python39 en mi caso.
import cx_Oracle as conn



def callProcedure(procedureName):
    lista = []
    try:
        con = conn.connect('turismo/turismo@localhost:1521')
    except Exception as err:
        print('Excepcion ocurrio en la creacion de la conexion a base de datos.')
    else:
        try:
            cursor = con.cursor()
            refCursor = con.cursor()
            cursor.callproc(procedureName,[refCursor])
            # myvar = cursor.var(conn.NUMBER)
            for row in refCursor:           
                # print(row)
                lista.append(row)
        except Exception as err:
            print('Error ocasionado en el procedimiento almacenado.', err)
        finally:
            cursor.close()
            refCursor.close()
    finally:
        con.close()
        return lista

def callProcedureParameters(procedureName,parameters):
    lista = []
    try:
        con = conn.connect('turismo/turismo@localhost:1521')
    except Exception as err:
        print('Excepcion ocurrio en la creacion de la conexion a base de datos.')
    else:
        try:
            cursor = con.cursor()
            cursor.callproc(procedureName,parameters)
            # myvar = cursor.var(conn.NUMBER)
        except Exception as err:
            print('Error ocasionado en el procedimiento almacenado.', err)
        finally:
            cursor.close()
    finally:
        con.close()
        return lista

def callExecute(query,parameters):
    lista = []
    try:
        con = conn.connect('turismo/turismo@localhost:1521')
    except Exception as err:
        print('Excepcion ocurrio en la creacion de la conexion a base de datos.')
    else:
        try:
            cursor = con.cursor()
            refCursor = con.cursor()
            # cursor.execute(query,parameters)
            cursor.executemany(query, parameters)
            # myvar = cursor.var(conn.NUMBER)
            # for row in refCursor:           
            #     # print(row)
            #     lista.append(row)
            print('ok insert')
            return True
        except Exception as err:
            print('Error ocasionado en el procedimiento almacenado.', err)
        finally:
            cursor.close()
            refCursor.close()
    finally:
        con.close()
        return lista
# def callProcedureINSERT():


# Comando para corroborar la conexión y la version a base de datos.
# con = conn.connect('turismo/turismo@localhost:1521')
# print("Database version:", con.version)