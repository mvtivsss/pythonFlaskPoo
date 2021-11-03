from BD import configuracion as connector

def getComuna():
    try:
        response = []
        comunaList = [lista for lista in connector.callProcedure('spGetComuna')]
        for comuna in comunaList:
            response.append({'id':comuna[0],'nombre': comuna[1]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response