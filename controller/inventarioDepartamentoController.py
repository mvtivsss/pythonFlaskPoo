from BD import configuracion as connector


def getInventoryDepartment():
    try:
        response = []
        inventoriesList = [lista for lista in connector.callProcedure('SPGETINVENTORYDEPARTMENT')]
        for inventories in inventoriesList:
            response.append({'id':inventories[0],'quantity': inventories[1], 'departmentId':inventories[2],'inventoryId': inventories[3],'inventoryName':inventories[4]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response


def addInventoryDepartment(cantidad,id_dpto,id_inventario):
    try:
     connector.callProcedureParameters('spAddInventoryDepartment', [cantidad,id_dpto,id_inventario])
     print('ok insert')
     return True
    except Exception as err:
        print('error insert')

def deleteInventoryDepartment(id):
    try:
     connector.callProcedureParameters('spDeleteInventoryDepartment', [id])
     print('ok delete')
     return True
    except Exception as err:
        print('error delete')


def getInventoryDepartmentById(id):
    try:
        response = []
        inventoriesList = [lista for lista in connector.callProcedureIdRefCursor('SPGETINVENTORYDEPARTMENTBYID',[id])]
        for inventories in inventoriesList:
            response.append({'id':inventories[0],'quantity': inventories[1], 'departmentId':inventories[2],'inventoryId': inventories[3],'objName':inventories[4]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response