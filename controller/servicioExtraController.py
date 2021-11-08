from BD import configuracion as connector

def getServExtra():
    try:
        serviciosExtra = connector.callProcedure('spGetServExtra')
        print(serviciosExtra)
        response = []
        for servicio in serviciosExtra:
            response.append({'id':servicio[0],'description':servicio[1], 'price': servicio[2]})
            # print(servicio)
        return response
    except Exception as ex:
        print('Excepcion con el controlador.',ex)
    finally:
        return response

def addServExtra(descripcion,precio):
    try:
     connector.callProcedureParameters('spAddServExtra', [descripcion,precio])
     print('ok insert')
     return True
    except Exception as err:
        print('no se pudo agregar el servicio extra' , err)

def updateServExtra(id,descripcion,precio):
    try:
     connector.callProcedureParameters('spUpdateServExtra', [id,descripcion,precio])
     print('ok update')
     return True
    except Exception as err:
        print('no se pudo actualizar el servicio extra' , err)


def deleteServExtra(id):
    try:
     connector.callProcedureParameters('spDeleteServExtra', [id])
     print('ok delete')
     return True
    except Exception as err:
        print('no se pudo eliminar el servicio extra' , err)