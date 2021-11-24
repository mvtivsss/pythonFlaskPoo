from BD import configuracion as connector

def getUsuarios():
    try:
        response = []
        usersList = [lista for lista in connector.callProcedure('spGetUsers')]
        for users in usersList:
            response.append({'id':users[0], 'rut': users[1],'firstName': users[2], 'lastNameP':users[3],'lastNameM': users[4],'dateOfBirth':users[5],
            'mail':users[6],'phone':users[7],'pass':users[8],'idCommune':users[9],
            'nameCommune': users[10],'idType':users[11],'nameType':users[12]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response

def usuarioInit(nombre, rut, apPaterno, apMaterno, fNacimiento, mail, telefono, contraseña, idComuna,tipo):
    try:
     connector.callProcedureParameters('spAddUser', [nombre, rut, apPaterno, apMaterno, fNacimiento, mail, telefono, contraseña, idComuna,tipo])
    #  connector.callExecute('COMMIT')
     print('ok insert')
     return True
    except Exception as err:
        print('no se pudo agregar el/la usuario/a')

def updateUser(id,rut,nombre, apPaterno, apMaterno, fNacimiento, mail, telefono, contraseña, idComuna,tipo):
    try:
     connector.callProcedureParameters('spUpdateUser', [id,rut,nombre,apPaterno, apMaterno, fNacimiento, mail, telefono, contraseña, idComuna,tipo])
    #  connector.callExecute('COMMIT')
     print('ok update')
     return True
    except Exception as err:
        print('no se pudo actualizar el/la usuario/a')

def deleteUser(id):
    try:
     connector.callProcedureParameters('spDeleteUser', [id])
    #  connector.callExecute('COMMIT')
     print('ok delete')
     return True
    except Exception as err:
        print('no se pudo eliminar el/la usuario/a')