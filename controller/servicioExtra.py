from BD import configuracion as connector

def getServExtra():
    response = []
    serviciosExtra = connector.callProcedure('spGetServExtra')
    for servicio in serviciosExtra:
        response.append({'id':servicio[0],'nombre':servicio[1], 'valor': servicio[2]})
        print(response)
    return response