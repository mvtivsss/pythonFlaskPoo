from logging import error
from BD import configuracion as connector

def getTransports():
    try:
        response = []
        trasporteList = [lista for lista in connector.callProcedure('spGetTransports')]
        for transport in trasporteList:
            response.append({'id':transport[0],'idReserve': transport[1], 'clientName':transport[2],'workerName':transport[3],
             'vehicle': transport[4],'tripStart': transport[5],'tripEnd': transport[6], 'time':transport[7]})
            print(response)
        return response
    except Exception as err:
        print('Error en controller ', err)
    finally:
        return response

def addTransport(place,time,vehicle,idReserve,idWorker):
    try:
     connector.callProcedureParameters('spAddTransport', [place,time,vehicle,idReserve,idWorker])
     print('ok insert')
     return True
    except Exception as err:
        print('no se pudo agregar el transporte ' , err)

def updateTransport(id,idReserve,vehicle,tripStart,tripEnd,time):
    try:
        connector.callProcedureParameters('spUpdateTransport', [id,idReserve,vehicle,tripStart,tripEnd,time])
        print('ok insert')
        return True
    except Exception as err:
        print('no se pudo modificar el transporte ' , err)

def deleteTransport(id):
    try:
     connector.callProcedureParameters('spDeleteTransport', [id])
     print('ok delete')
     return True
    except Exception as err:
        print('no se pudo eliminar el transporte ' , err)

