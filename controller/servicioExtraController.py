from BD import configuracion as connector

def getServExtra():
    try:
        serviciosExtra = connector.callProcedure('spGetServExtra')
        print(serviciosExtra)
        response = []
        for servicio in serviciosExtra:
            response.append({'id':servicio[0],'descripcion':servicio[1], 'valor': servicio[2]})
            # print(servicio)
        return response
    except Exception as ex:
        print('Excepcion con el controlador.',ex)
    finally:
        return response