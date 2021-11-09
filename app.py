from types import MethodType
from flask import Flask, json, jsonify, request
from controller import regionController as region, servicioExtraController as servicioExtra
from controller import actaController, departmentController, clientsController, comunaController, ciudadController, inventarioController, inventarioDepartamentoController
from controller import usuarioController, maintainsDepartmentController
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

@app.route('/api/serviciosExtra', methods=['GET'])
def getServExtra():
    servicios = [serviciosList for serviciosList in servicioExtra.getServExtra()]
    # print(servicios)
    if servicios:
        return jsonify({'servicios': servicios})
    else:
        return jsonify({"servicios":[]})

@app.route('/api/serviciosExtra', methods=['POST'])
def addServExtra():
    try:
        data = request.get_json()
        servicioExtra.addServExtra(data['description'], data['price'])
        return jsonify({'ok': True})
    except Exception as err:
        return jsonify({'ok': err})

@app.route('/api/serviciosExtra', methods=['PUT'])
def updateServExtra():
    try:
        data = request.get_json()
        servicioExtra.updateServExtra(data['id'], data['description'], data['price'])
        return jsonify({'ok': True})
    except Exception as err:
        return

@app.route('/api/serviciosExtra', methods=['DELETE'])
def deleteServExtra():
    try:
        data = request.get_json()
        servicioExtra.deleteServExtra(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return jsonify({'message':'no se pudo eliminar el servicio extra'})

@app.route('/api/acta')
def getActa():
    actas = [listaActa for listaActa in actaController.getActa()]
    print(actas)
    if (len(actas) > 0 ):
        return jsonify({'actas': actas})
    else:
        return jsonify({"message":'no existen actas'})

@app.route('/api/departments', methods=['GET'])
def getDepartments():
    departamentos = [departmentList for departmentList in departmentController.getDepartments()]
    if (len(departamentos)> 0):
        return jsonify({'departments':departamentos })
    else:
        return jsonify({'departments':[] })

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

@app.route('/api/departments', methods=['PUT'])
def updateDepartment():
    try:
        data = request.get_json()
        departmentController.updateDepartment(data['id'],data['name'], data['address'],data['totalRooms'], data['totalParking'],data['totalBaths'],
              data['internet'],data['tv'],data['heating'],data['furnished'],data['departmentPrice'],
              data['departmentStatus'],data['departmentDesc'],data["idCommune"])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/departments', methods=['DELETE'])
def deleteDepartment():
    try:
        data = request.get_json()
        departmentController.deleteDepartment(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/inventories', methods=['GET'])
def getInventory():
    inventario = [inventarioList for inventarioList in inventarioController.getInventories()]
    if (len(inventario)> 0):
        return jsonify({'inventories':inventario })
    else:
        return jsonify({'inventories':[] })

@app.route('/api/inventoriesDepartment', methods=['GET'])
def getInventoryDepartments():
    inventario = [inventarioList for inventarioList in inventarioDepartamentoController.getInventoryDepartment()]
    if (len(inventario)> 0):
        return jsonify({'inventoriesDepartments':inventario })
    else:
        return jsonify({'inventoriesDepartments':[] })

@app.route('/api/inventoriesDepartment', methods=['POST'])
def addInventoryDepartment():
    try:
        data = request.get_json()
        inventarioDepartamentoController.addInventoryDepartment(data['id'],data['quantity'],data["departmentId"],data["inventoryId"])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/inventoriesDepartment', methods=['DELETE'])
def deleteInventoryDepartment():
    try:
        data = request.get_json()
        inventarioDepartamentoController.deleteInventoryDepartment(data["id"])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/users', methods=['GET'])
def getUsers():
    user = [userList for userList in usuarioController.getUsuarios()]
    if (len(user)> 0):
        return jsonify({'users':user })
    else:
        return jsonify({'users':[] })

@app.route('/api/users', methods=['POST'])
def userInit():
    try:
        data = request.get_json()
        usuarioController.usuarioInit(data['firstName'],data['lastNameP'],data['lastNameM'], data['dateOfBirth'], data['mail'],
        data['phone'], data['pass'], data['idCommune'], data['idType'])
        print(data)
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/users', methods=['PUT'])
def updateUser():
    try:
        data = request.get_json()
        usuarioController.updateUser(data['id'],data['firstName'],data['lastNameP'],data['lastNameM'], data['dateOfBirth'], data['mail'],
        data['phone'], data['pass'], data['idCommune'], data['idType'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/users', methods=['DELETE'])
def deleteUser():
    try:
        data = request.get_json()
        usuarioController.deleteUser(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/maintainsDepartments', methods=['POST'])
def addMaintainDepartment():
    try:
        data = request.get_json()
        maintainsDepartmentController.addMaintainsDepartments(data['initDate'],data["finishDate"],data["userId"],data["departmentId"])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/maintainsDepartments',methods=['GET'])
def getMaintainsDepartments():
    maintains = [maintainsList for maintainsList in maintainsDepartmentController.getMaintainsDepartments()]
    if (len(maintains)> 0):
        return jsonify({'maintainsDepartments':maintains })
    else:
        return jsonify({'maintainsDepartments':[] })



# @app.route('/api/maintainerDepartment', methods=['GET'])

# @app.route('/api/clients')
# def getClients():
#     clients = [clientList for clientList in clientsController.getClients()]
#     if(len(clients) > 0 ):
#         return jsonify({'Clientes' : clients})
#     else:
#         return jsonify({"message":'no existen clientes'})

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