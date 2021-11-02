from BD import configuracion as connector

def getRegiones():
    try:
        response = []
        regions = connector.callProcedure('spGetRegion')
        for region in regions:
            response.append({'id':region[0], 'nombre':region[1]})
        return response
    except Exception as err:
        print('Error en controller')
    finally:
        return response
