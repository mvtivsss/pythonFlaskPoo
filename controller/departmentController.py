from BD import configuracion as connector
import base64

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

def getDepartmentById(id):
    try:
        response = []
        departmentByIdList = connector.callProcedureIdRefCursor('SPGETDEPARTMENTBYID',[id])
        for department in departmentByIdList:
            response.append({'id':department [0],'name': department [1], 'address':department [2],'totalRooms':department [3], 'totalParking': department [4],
                             'totalBaths': department [5], 'internet':department [6], 'tv': department [7],'heating':department [8], 'furnished': department [9],
                             'departmentPrice': department [10], 'departmentStatus': department [11],'ubication':department [12]})
            print(response)
        return response
    except Exception as err:
        print('error en controller', err)
    finally: 
        return response

def getDepartmentByDisponibility(disponibility):
    try:
        response = []
        departmentByIdList = connector.callProcedureIdRefCursor('SPGETDEPARTMENTBYDISPONIBILITY',[disponibility])
        for department in departmentByIdList:
            response.append({'id':department [0],'name': department [1], 'address':department [2],'totalRooms':department [3], 'totalParking': department [4],
                             'totalBaths': department [5], 'internet':department [6], 'tv': department [7],'heating':department [8], 'furnished': department [9],
                             'departmentPrice': department [10], 'departmentStatus': department [11],'ubication':department [12], 'description' : department[13]})
            print(response)
        return response
    except Exception as err:
        print('error en controller', err)
    finally: 
        return response



def addDepartment(nombre, direccion,habitaciones,
                  estacionamientos, banos, internet, cable,
                  calefaccion, amoblado, precio, estado, descripcion,comuna):
    try:
    #  foto = Image.open('C:\\Users\\matim\\Desktop\\TurismoPy\\images\\python.jpg')
     
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

def updateDisponibility(id):
    try:
        connector.callProcedureParameters('spUpdateDisponibility',[id])
        print('ok update disponibility')
        return True
    except Exception as err:
        print('no se pudo actualizar la disponibilidad', err)

def deleteDepartment(id):
    try:
     connector.callProcedureParameters('spDeleteDepartments', [id])
     print('ok delete')
     return True
    except Exception as err:
        print('no se pudo agregar department')