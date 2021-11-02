from BD import configuracion as connector

def getRegiones():
    response = []
    regions = connector.callProcedure('spGetRegion')
    for region in regions:
        response.append({'id':region[0], 'nombre':region[1]})
    return response