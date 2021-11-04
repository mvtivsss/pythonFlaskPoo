from BD import configuracion as connector

def getInventories():
    try:
        response = []
        inventoriesList = [lista for lista in connector.callProcedure('spGetInventory')]
        for inventories in inventoriesList:
            response.append({'name':inventories[0],'id': inventories[1], 'description':inventories[2]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response


def addInventoryDepartment(id,cantidad,id_dpto,id_inventario):
    try:
     connector.callProcedureParameters('spAddInventoryDepartment', [id,cantidad,id_dpto,id_inventario])
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