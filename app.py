from types import MethodType
from flask import Flask, json, jsonify, request
from regions import regions
from clients import clientes
from BD import configuracion

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'PÁGINA DE INICIO'

@app.route('/regions')
def getRegions():
    regiones = [region for region in configuracion.row]
    return jsonify({'Regiones': regiones})

@app.route('/regions/<string:region_name>')
def getRegion(region_name):
    regionFound = [region for region in regions if region['nombre']==region_name]
    if(len(regionFound)>0):
        return jsonify({"Regiones":regionFound[0]})
    return jsonify({"message": "region no encontrada !"})

@app.route('/regions', methods=['POST'])
def addRegion():
    newRegion = {
        "id" : request.json["id"],
        "nombre" : request.json["nombre"]
    }
    regions.append(newRegion)
    return jsonify({"message": "Region agregada !", "Regiones" : regions})

@app.route('/regions/<int:region_id>', methods=["PUT"])
def editRegion(region_id):
    regionFound = [region for region in regions if region['id'] == region_id]
    if (len(regionFound) > 0):
        regionFound[0]['id'] = request.json['id']
        regionFound[0]['nombre'] = request.json['nombre']
        return jsonify({
            "Regiones": regionFound[0]
        })
    return jsonify({
        "message" : "Region no encontrada !"
    })

@app.route('/regions/<string:name>', methods=['DELETE'])
def deleteRegion(name):
    regionFound = [region for region in regions if region['nombre'] == name]
    regions.remove(regionFound[0])
    return jsonify({
        "message": "Region eliminada !",
        "Regiones": regionFound
    })

@app.route('/clients')
def getClients():
    return jsonify({'clientes': clientes})

if __name__ == '__main__':
    app.run(debug = True, port = 4000)