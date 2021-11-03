from types import MethodType
from flask import Flask, json, jsonify, request
# from regions import regions
# from clients import clientes
# from BD import configuracion
from controller import regionController as region, servicioExtraController as servicioExtra
from controller import actaController, departmentController, clientsController, comunaController, ciudadController

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'PÁGINA DE INICIO'

@app.route('/api/regions', methods=['GET'])
def getRegions():
    regiones = [regionList for regionList in region.getRegiones()]
    # listRegiones = json.dumps(regiones)
    print(regiones)
    if (len(regiones) > 0):
        return jsonify({"regiones":regiones})

@app.route('/api/regions', methods=['POST'])
def addRegion():
    try:
        data = request.get_json()
        print(data['id'], data['nombre'])
        region.addRegion(data['id'], data['nombre'])
        return jsonify({'ok': True})
    except Exception as err:
        return 

@app.route('/api/comuna')
def getComuna():
    comuna = [comunaList for comunaList in comunaController.getComuna()]
    print(comuna)
    if (len(comuna) > 0):
        return jsonify({"comunas":comuna})

@app.route('/api/ciudad')
def getCiudad():
    ciudad = [ciudadList for ciudadList in ciudadController.getCiudad()]
    print(ciudad)
    if (len(ciudad) > 0):
        return jsonify({"ciudades":ciudad})

@app.route('/api/departments', methods=['POST'])
def addDepartment():
    try:
        data = request.get_json()
        print(data['id'], data['nombre'])
        departmentController.addDepartment(data['id'], data['nombre'], data['direccion'],data['cantHabitaciones'], data['cantEstacionamiento'],data['cantBanos'],
              data['internet'],data['cable'],data['calefaccion'],data['amoblado'],data['precioDpto'],
              data['estadoDpto'],data['descripcionDpto'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/serviciosExtra')
def getServExtra():
    servicios = [serviciosList for serviciosList in servicioExtra.getServExtra()]
    # print(servicios)
    if servicios:
        return jsonify({'servicios': servicios})
    else: 
        return jsonify({'message': 'ups'} )

@app.route('/api/acta')
def getActa():
    actas=[]
    actas = [listaActa for listaActa in actaController.getActa()]
    if (len(actas) > 0 ):
        return jsonify({'Actas': actas})
    else:
        return 'Acta Else'

@app.route('/api/departments', methods=['GET'])
def getDepartments():
    departamentos = [departmentList for departmentList in departmentController.getDepartments()]
    if (len(departamentos)> 0):
        return jsonify({'Departamentos':departamentos })

@app.route('/api/clients')
def getClients():
    clients = [clientList for clientList in clientsController.getClients()]
    if(len(clients) > 0 ):
        return jsonify({'Clientes' : clients})


# @app.route('/regions/<string:region_name>')
# def getRegion(region_name):
#     regionFound = [region for region in regions if region['nombre']==region_name]
#     if(len(regionFound)>0):
#         return jsonify({"Regiones":regionFound[0]})
#     return jsonify({"message": "region no encontrada !"})

# @app.route('/regions/<int:region_id>', methods=["PUT"])
# def editRegion(region_id):
#     regionFound = [region for region in regions if region['id'] == region_id]
#     if (len(regionFound) > 0):
#         regionFound[0]['id'] = request.json['id']
#         regionFound[0]['nombre'] = request.json['nombre']
#         return jsonify({
#             "Regiones": regionFound[0]
#         })
#     return jsonify({
#         "message" : "Region no encontrada !"
#     })

# @app.route('/regions/<string:name>', methods=['DELETE'])
# def deleteRegion(name):
#     regionFound = [region for region in regions if region['nombre'] == name]
#     regions.remove(regionFound[0])
#     return jsonify({
#         "message": "Region eliminada !",
#         "Regiones": regionFound
#     })

# @app.route('/clients')
# def getClients():
#     return jsonify({'clientes': clientes})

if __name__ == '__main__':
    app.run(debug = True, port = 4000)