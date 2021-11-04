from BD import configuracion as connector

def addMaintainsDepartments(initDate,finishDate,userId,departmentId):
    try:
     connector.callProcedureParameters('spAddMaintainsDepartments', [initDate,finishDate,userId,departmentId])
     print('ok insert')
     return True
    except Exception as err:
        print('error insert', err)


def getMaintainsDepartments():
    try:
        response = []
        maintainsDepartmentList = [lista for lista in connector.callProcedure('spGetMaintainsDepartment')]
        for maintainsDepartment in maintainsDepartmentList:
            response.append({'id':maintainsDepartment[0],'initDate': maintainsDepartment[1],
                             'finishDate':maintainsDepartment[2],'userId': maintainsDepartment[3],'userName':maintainsDepartment[4],
                             'departmentId':maintainsDepartment[5]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response