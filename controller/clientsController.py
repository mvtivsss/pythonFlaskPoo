from BD import configuracion as connector

def getClients():
    try:
        response = []
        clientsList = [lista for lista in connector.callProcedure('spGetclients')]
        for clients in clientsList:
            response.append({'id':clients[0],'name': clients[1], 'apPaterno':clients[2],
                             'apMaterno':clients[3],'fNacimiento':clients[4], 'mail': clients[5],
                             'celular': clients[6], 'pass':clients[7], 'worker' : ''})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response