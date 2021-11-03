from BD import configuracion as connector

def getDepartments():
    try:
        response = []
        departmentsList = [lista for lista in connector.callProcedure('spGetDepartments')]
        for departments in departmentsList:
            response.append({'id':departments[0],'nombre': departments[1], 'direccion':departments[2],'cantHabitaciones':departments[3], 'cantEstacionamiento': departments[4],
                             'cantBanos': departments[5], 'internet':departments[6], 'cable': departments[7],'calefaccion':departments[8], 'amoblado': departments[9],
                             'precioDpto': departments[10], 'estadoDpto': departments[11],'descripcionDpto':departments[12]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response

def addDepartment(id, nombre, direccion,habitaciones,
                  estacionamientos, banos, internet, cable,
                  calefaccion, amoblado, precio, estado, descripcion):
    try:
     connector.callProcedureParameters('spAddDepartment', [id,nombre, direccion,habitaciones,estacionamientos, banos, internet, cable,
                                                           calefaccion, amoblado, precio, estado, descripcion])
     print('ok insert')
     return True
    except Exception as err:
        print('no se pudo agregar la Department')