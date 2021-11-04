from BD import configuracion as connector

def getDepartments():
    try:
        response = []
        departmentsList = [lista for lista in connector.callProcedure('spGetDepartments')]
        for departments in departmentsList:
            response.append({'id':departments[0],'name': departments[1], 'address':departments[2],'totalRooms':departments[3], 'totalParking': departments[4],
                             'totalBaths': departments[5], 'internet':departments[6], 'tv': departments[7],'heating':departments[8], 'furnished': departments[9],
                             'departmentPrice': departments[10], 'departmentStatus': departments[11],'departmentDesc':departments[12], 'idCommune':departments[13],
                             'nameCommune': departments[14]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response

def addDepartment(nombre, direccion,habitaciones,
                  estacionamientos, banos, internet, cable,
                  calefaccion, amoblado, precio, estado, descripcion,comuna):
    try:
     connector.callProcedureParameters('spAddDepartment', [nombre, direccion,habitaciones,estacionamientos, banos, internet, cable,
                                                           calefaccion, amoblado, precio, estado, descripcion,comuna])
     print('ok insert')
     return True
    except Exception as err:
        print('no se pudo agregar la Department')

def updateDepartment(id,nombre, direccion,habitaciones,
                  estacionamientos, banos, internet, cable,
                  calefaccion, amoblado, precio, estado, descripcion,comuna):
    try:
     connector.callProcedureParameters('spUpdateDepartments', [id,nombre, direccion,habitaciones,estacionamientos, banos, internet, cable,
                                                           calefaccion, amoblado, precio, estado, descripcion,comuna])
     print('ok update')
     return True
    except Exception as err:
        print('no se pudo agregar department')

def deleteDepartment(id):
    try:
     connector.callProcedureParameters('spDeleteDepartments', [id])
     print('ok delete')
     return True
    except Exception as err:
        print('no se pudo agregar department')