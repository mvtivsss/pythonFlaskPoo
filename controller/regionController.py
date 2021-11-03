from types import ClassMethodDescriptorType
from flask import json
from flask.json import jsonify
from BD import configuracion as connector

def getRegiones():
    try:
        response = []
        regions = connector.callProcedure('spGetRegion')
        for region in regions:
            response.append({'id':region[0], 'name':region[1]})
        return response
    except Exception as err:
        print('Error en controller')
    finally:
        return response

def addRegion(id, nombre):
    try:
     connector.callProcedureParameters('spAddRegion', [id,nombre])
    #  connector.callExecute('COMMIT')
     print('ok insert')
     return True
    except Exception as err:
        print('no se pudo agregar la region')
