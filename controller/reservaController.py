from BD import configuracion as connector

def getReservas():
    try:
        response = []
        reservaList = [lista for lista in connector.callProcedure('spGetReserva')]
        for reserva in reservaList:
            response.append({'id':reserva[0],'planifiedCheckIn': reserva[1], 'checkIn':reserva[2],'checkOut':reserva[3], 'totalDays': reserva[4],
                             'totalAdults': reserva[5],'totalKids': reserva[6], 'totalReserve':reserva[7], 'statusReserve': reserva[8],'departmentId':reserva[9], 'clientId': reserva[10],
                             'workerId': reserva[11], 'departmentName': reserva[12],'departmentAdress':reserva[13],'totalRooms':reserva[14], 'totalParking': reserva[15],
                             'totalBaths': reserva[16], 'internet':reserva[17], 'tv': reserva[18],'heating':reserva[19], 'furnished': reserva[20],
                             'departmentPrice': reserva[21], 'departmentStatus': reserva[22],'departmentDesc':reserva[23], 'idCommune':reserva[24]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response
    
def addMulta(cant, subtotal, idActa, idReserva):
    try:
        connector.callProcedureParameters('SPADDMULTA',[cant, subtotal, idActa, idReserva])
        print('ok insert')
        return True
    except Exception as err:
        print('Error en controller ', err)

def deleteMulta(id):
    try:
        connector.callProcedureParameters('SPDELETEMULTA', [id])
        print('ok Delete')
        return True
    except Exception as err:
        print(err)

def getMulta(id):
    try:
        response = []
        multaList = [lista for lista in connector.callProcedureIdRefCursor('spGetMulta',[id])]
        for multa in multaList:
            response.append({'id': multa[0], 'quantity': multa[1], 'subTotal' : multa[2], 'idActa': multa[3], 'idReserve': multa[4]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller', err)
    finally:
        return response  

def getReservaServex(id):
    try:
        response = []
        reservaServexList = [lista for lista in connector.callProcedureIdRefCursor('spGetReservaServex',[id])]
        for reservaServex in reservaServexList:
            response.append({'id': reservaServex[0], 'quantity': reservaServex[1], 'subTotal' : reservaServex[2], 'idServEx': reservaServex[3], 'idReserve': reservaServex[4]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller', err)
    finally:
        return response  