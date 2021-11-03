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
        return jsonify({"regions":regiones})
    else:
        return jsonify({"regions": []})

@app.route('/api/regions', methods=['POST'])
def addRegion():
    try:
        data = request.get_json()
        print(data['id'], data['nombre'])
        region.addRegion(data['id'], data['nombre'])
        return jsonify({'ok': True})
    except Exception as err:
        return 

@app.route('/api/communes')
def getComuna():
    comuna = [comunaList for comunaList in comunaController.getComuna()]
    print(comuna)
    if (len(comuna) > 0):
        return jsonify({"communes":comuna})
    else:
        return jsonify({"communes":[]})


@app.route('/api/cities')
def getCiudad():
    ciudad = [ciudadList for ciudadList in ciudadController.getCiudad()]
    print(ciudad)
    if (len(ciudad) > 0):
        return jsonify({"cities":ciudad})
    else:
        return jsonify({"cities":[]})


@app.route('/api/departments', methods=['POST'])
def addDepartment():
    try:
        data = request.get_json()
        departmentController.addDepartment(data['name'], data['address'],data['totalRooms'], data['totalParking'],data['totalBaths'],
              data['internet'],data['tv'],data['heating'],data['furnished'],data['departmentPrice'],
              data['departmentStatus'],data['departmentDesc'],data["idCommune"])
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
        return jsonify({"message":'no existen servicios extra'})



@app.route('/api/acta')
def getActa():
    actas=[]
    actas = [listaActa for listaActa in actaController.getActa()]
    if (len(actas) > 0 ):
        return jsonify({'Actas': actas})
    else:
        return jsonify({"message":'no existen actas'})


@app.route('/api/departments', methods=['GET'])
def getDepartments():
    departamentos = [departmentList for departmentList in departmentController.getDepartments()]
    if (len(departamentos)> 0):
        return jsonify({'departments':departamentos })
    else:
        return jsonify({'departments':[] })


@app.route('/api/clients')
def getClients():
    clients = [clientList for clientList in clientsController.getClients()]
    if(len(clients) > 0 ):
        return jsonify({'Clientes' : clients})
    else:
        return jsonify({"message":'no existen clientes'})



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