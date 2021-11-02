from BD import configuracion as connector

def getActa():
    try:
        response = []
        actasList = connector.callProcedure('spGetActa')
        for acta in actasList:
            response.append({'id':acta[0],'multaNom': acta[1], 'multaDesc':acta[2],'valor':acta[3], 'subTotal': acta[4]})
            # print(response)
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response