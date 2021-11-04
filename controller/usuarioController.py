from BD import configuracion as connector

def getUsuarios():
    try:
        response = []
        usersList = [lista for lista in connector.callProcedure('spGetUsers')]
        for users in usersList:
            response.append({'id':users[0],'firstName': users[1], 'lastNameP':users[2],'lastNameP': users[3],'dateOfBirth':users[4],
            'mail':users[5],'phone':users[6],'pass':users[7],'idCommune':users[8],
            'nameCommune': users[9],'idType':users[10],'nameType':users[11]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response