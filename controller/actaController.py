from BD import configuracion as connector

def getActa():
    try:
        response = []
        actasList = connector.callProcedure('spGetActa')
        for acta in actasList:
            response.append({'id':acta[0],'fineName': acta[1], 'fineDesc':acta[2],'price':acta[3], 'subPrice': acta[4]})
            # print(response)
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response