from BD import configuracion as connector

def getTypeUser():
    try:
        response = []
        typeUserList = [lista for lista in connector.callProcedure('spGetTypeUser')]
        for typeUser in typeUserList:
            response.append({'name':typeUser[1],'id': typeUser[0]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response