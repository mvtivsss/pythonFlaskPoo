from types import MethodType
from flask import Flask, json, jsonify, request
# from regions import regions
# from clients import clientes
# from BD import configuracion
from controller import regionController as region, servicioExtraController as servicioExtra
from controller import actaController, departmentController

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'PÁGINA DE INICIO'

@app.route('/regions')
def getRegions():
    regiones = [regionList for regionList in region.getRegiones()]
    # listRegiones = json.dumps(regiones)
    print(regiones)
    if (len(regiones) > 0):
        return jsonify({"Regiones":regiones})

@app.route('/departments', methods=['POST'])
def addDepartment():
    newDepartment = {
        "amoblado": request.json["amoblado"], 
        "cable": request.json["cable"], 
        "calefaccion": request.json["calefaccion"], 
        "cantBanos": request.json["cantBanos"], 
        "cantEstacionamiento": request.json["cantEstacionamiento"], 
        "cantHabitaciones": request.json["cantHabitaciones"], 
        "descripcionDepto": request.json["descripcionDepto"], 
        "direccion": request.json["direccion"], 
        "estadoDpto": request.json["estadoDpto"], 
        "id": request.json["id"], 
        "internet": request.json["internet"], 
        "nombre": request.json["nombre"], 
        "precioDpto": request.json["precioDpto"]
    }
    lista = region.getRegiones().append(newDepartment)
    return jsonify({"message": "Departamento agregado !", "Departamentos" : lista})


@app.route('/serviciosExtra')
def getServExtra():
    servicios = [serviciosList for serviciosList in servicioExtra.getServExtra()]
    # print(servicios)
    if servicios:
        return jsonify({'Servicios': servicios})
    else: 
        return 'Datos'

@app.route('/acta')
def getActa():
    actas=[]
    actas = [listaActa for listaActa in actaController.getActa()]
    if (len(actas) > 0 ):
        return jsonify({'Actas': actas})
    else:
        return 'Acta Else'

@app.route('/departments')
def getDepartments():
    departamentos = [departmentList for departmentList in departmentController.getDepartments()]
    if (len(departamentos)> 0):
        return jsonify({'Departamentos':departamentos })

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