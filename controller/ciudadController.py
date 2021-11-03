from BD import configuracion as connector

def getCiudad():
    try:
        response = []
        ciudadList = [lista for lista in connector.callProcedure('spGetCiudad')]
        for ciudad in ciudadList:
            response.append({'id':ciudad[0],'name': ciudad[1]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response