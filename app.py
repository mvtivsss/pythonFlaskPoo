from types import MethodType
from flask import Flask, json, jsonify, request
from base64 import b64encode, b64decode
import base64
from controller import regionController as region, servicioExtraController as servicioExtra
from controller import actaController, departmentController, clientsController, comunaController, ciudadController, inventarioController, inventarioDepartamentoController
from controller import usuarioController, maintainsDepartmentController, typeUserController, loginController, reservaController, transportController
import random
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
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
    print('test////////////////////////////')
    departamentos = [departmentList for departmentList in departmentController.getDepartments()]
    if (len(departamentos)> 0):
        return jsonify({'departments':departamentos })
    else:
        return jsonify({'departments':[] })

@app.route('/api/departments', methods=['POST'])
def addDepartment():
    try:
        print('I work?')
        data = request.get_json()
        departmentController.addDepartment(data['name']
        ,data['address']
        ,data['totalRooms']
        ,data['totalParking']
        ,data['totalBaths']
        ,data['internet']
        ,data['tv']
        ,data['heating']
        ,data['furnished']
        ,data['departmentPrice']
        ,data['departmentStatus']
        ,data['departmentDesc']
        ,data['idCommune']
        ,data['imgB64'])
        
        return jsonify({'ok': True})
    except Exception as err:
        print(err)
        return jsonify({'ok': False})

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
        inventarioDepartamentoController.addInventoryDepartment(data['quantity'],data["departmentId"],data["inventoryId"])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/inventoriesDepartmentById', methods=['GET'])
def getInventoryDepartmentsById():
    data = request.args['id']
    inventario = [inventarioList for inventarioList in inventarioDepartamentoController.getInventoryDepartmentById(data)]
    if (len(inventario)> 0):
        return jsonify({'inventoriesDepartments':inventario })
    else:
        return jsonify({'inventoriesDepartments':[] })

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
        usuarioController.usuarioInit(data['firstName'],data['rut'],data['lastNameP'],data['lastNameM'], data['dateOfBirth'], data['mail'],
        data['phone'], data['pass'], data['idCommune'], data['idType'])
        print(data)
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/users', methods=['PUT'])
def updateUser():
    try:
        data = request.get_json()
        usuarioController.updateUser(data['id'],data['rut'],data['firstName'],data['lastNameP'],data['lastNameM'], data['dateOfBirth'], data['mail'],
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

@app.route('/api/maintainsDepartmentsById',methods=['GET'])
def getMaintainsDepartmentsById():
    data = request.args['id']
    print(data)
    maintains = [maintainsList for maintainsList in maintainsDepartmentController.getMaintainDepartmentById(data)]
    # print(data)
    if (len(maintains)> 0):
        return jsonify({'maintainsDepartments':maintains })
    else:
        return jsonify({'maintainsDepartments':[] })

@app.route('/api/typeUser', methods=['GET'])
def getTypeUser():
    typeUser = [typeUserList for typeUserList in typeUserController.getTypeUser()]
    if(len(typeUser) > 0):
        return jsonify({'typeUsers': typeUser})
    else:
        return jsonify({'typeUsers': []})

@app.route('/api/validateLogin', methods=['POST'])
def validateLogin():
    try:
        json = request.get_json()
        datos = loginController.validateLogin(json['mail'],json['password'])
        # print(datos)
        if(len(datos)> 0):
            return jsonify({'user': datos})
        else:
            return jsonify({'user': []})
    except Exception as err:
        return print(err)

@app.route('/api/departmentById', methods=['GET'])
def getDepartmentById():
    data = request.args['id']
    department = [departmentList for departmentList in departmentController.getDepartmentById(data)]
    print(department)
    if (len(department) > 0):
        return jsonify({'department': department})
    else:
        return jsonify({'department': []})

@app.route('/api/departmentByDisponibility', methods=['GET'])
def getDepartmentByDisponibility():
    department = [departmentList for departmentList in departmentController.getDepartmentByDisponibility(1)]#request.args['disponibility']
    print(department)
    if(len(department) > 0):
        return jsonify({'departments': department})
    else:
        return jsonify({'department': []})

@app.route('/api/updateDisponibility', methods=['PUT'])
def updateDisponibility():
    try:
        data = request.get_json()
        departmentController.updateDisponibility(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)
    
@app.route('/api/reserve', methods=['GET'])
def getReserve():
    reserva = [reservaList for reservaList in reservaController.getReservas()]
    print(reserva)
    if(len(reserva) > 0):
        return jsonify({'reserves': reserva})
    else:
        return jsonify({'reserves': []})

@app.route('/api/reserve', methods=['POST'])
def addReserve():
    try:
        data = request.get_json()
        reservaController.addReserva(data['checkInPlanning'],data['checkOut'],data['totalDays'],
                                     data['totalAdults'], data['totalKids'], data['totalBabies'],data['totalReserve'],
                                     data['statusReserve'], data['departmentId'],data['clientId'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/reserve', methods=['DELETE'])
def deleteReserve():
    try:
        data = request.get_json()
        reservaController.deleteReserve(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/checkInReserve', methods=['PUT'])
def updateCheckIn():
    try:
        data = request.get_json()
        reservaController.updateCheckIn(data['checkIn'], data['reserveId'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/multa', methods=['POST'])
def addMulta():
    try:
        data = request.get_json()
        print(data)
        reservaController.addMulta(data['quantity'], data['subTotal'], data['idActa'], data['idReserve'] )
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/multa', methods=['DELETE'])
def deleteMulta():
    try:
        data = request.get_json()
        print(data)
        reservaController.deleteMulta(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return print(err)

@app.route('/api/multa', methods=['GET'])
def getMulta():
    try:
        data = request.args["id"]
        multa = [multaList for multaList in reservaController.getMulta(data)]
        print(multa)
        if(len(multa)> 0):
            return jsonify({'fines': multa})
        else:
            return jsonify({'fines': []})
    except Exception as err:
        print(err)

@app.route('/api/reserveServex', methods=['GET'])
def getReservaServex():
    try:
        reservaServex = [reservaServexList for reservaServexList in reservaController.getReservaServex(request.args['id'])]
        print(reservaServex)
        if(len(reservaServex)> 0):
            return jsonify({'services': reservaServex})
        else:
            return jsonify({'services': []})
    except Exception as err:
        print(err)

@app.route('/api/reserveServex', methods=['POST'])
def addReservaServex():
    try:
        data = request.get_json()
        reservaController.addReservaServex(data['cantidad'],data['subtotal'],data['serv_id'],data['reserv_id'])
        return jsonify({'ok': True})
    except Exception as err:
        return jsonify({'ok': err})

@app.route('/api/reserveServex', methods=['DELETE'])
def deleteReservaServex():
    try:
        data = request.get_json()
        reservaController.deleteReservaServex(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return jsonify({'message':'no se pudo eliminar la reserva'})


@app.route('/api/extraServices', methods=['GET'])
def getServExtra():
    servicios = [serviciosList for serviciosList in servicioExtra.getServExtra()]
    # print(servicios)
    if servicios:
        return jsonify({'servicios': servicios})
    else:
        return jsonify({"servicios":[]})
        
# @app.route('/api/reserveByUser')
# def getReservaByUser():
#     try:
#         data = request.args['id']
#         reserveByUser = [lista for lista in reservaController.getReservaByUser(data)]
#         if len(reserveByUser) > 0:
#             return jsonify({'reserve': reserveByUser})
#         else: 
#             return jsonify

@app.route('/api/transport', methods=['GET'])
def getTransports():
    transport = [transports for transports in transportController.getTransports()]
    print(transport)
    if(len(transport) > 0):
        return jsonify({'transports': transport})
    else:
        return jsonify({'transports': []})


@app.route('/api/transport', methods=['POST'])
def addTransports():
    try:
        data = request.get_json()
        transportController.addTransport(data['place'],data['time'], 
        data['vehicle'],data['idReserve'],data['idWorker'])
        return jsonify({'ok': True})
    except Exception as err:
        return jsonify({'ok': err})

@app.route('/api/transport', methods=['PUT'])
def updateTransport():
    try:
        data = request.get_json()
        transportController.updateTransport(data['id'],data['place']
        ,data['time'],data['vehicle'],data['idReserve'],data['idWorker'])
        return jsonify({'ok': True})
    except Exception as err:
        return

@app.route('/api/transport', methods=['DELETE'])
def deleteTransport():
    try:
        data = request.get_json()
        transportController.deleteTransport(data['id'])
        return jsonify({'ok': True})
    except Exception as err:
        return jsonify({'message':'no se pudo eliminar el transporte'})

@app.route('/api/getReservaByUser')
def getReservaByUser():
    data = request.args['id']
    reserva = [lista for lista in reservaController.getReservaByUser(data)]
    print(reserva)
    if(len(reserva) > 0):
        return jsonify({"reserve" : reserva})
    else:
        return jsonify({"reserve" : []})

@app.route('/api/getCheckout')
def getCheckout():
    try:
        data = request.args["id"]
        reserva = [reservaList for reservaList in reservaController.getReservaById(data)]
        acta = [actalist for actalist in reservaController.getMulta(data)]
        servex = [servexList for servexList in reservaController.getReservaServex(data)]
        print(acta)

        return jsonify({'reserve': reserva, 'fines' : acta, 'servex' : servex})
    except Exception as err:
        print(err)

@app.route('/api/putCheckout', methods=['PUT'])
def putCheckout():
    try:
        data = request.get_json()
        reservaController.putCheckout(data["id"])
        reservaController.createOrderPay(data["id"])
        return jsonify({'ok': True})
    except Exception as err:
        print(err)

@app.route('/api/pagoInfo', methods=['POST'])
def pagoInfo():
    try:

        data = request.get_json()["token"]
        print(data)
        response = Transaction.commit(data)
        print(str(response))
        return jsonify({"response": str(response)})
    except Exception as err:
        print(err)
        return str(err)

@app.route('/api/pago', methods=["GET"])
def pago():
    try:
     # El SDK apunta por defecto al ambiente de pruebas, no es necesario configurar lo siguiente
        # Transaction.webpay.webpay_plus.webpay_plus_default_commerce_code = 597055555532
        # Transaction.webpay.webpay_plus.default_api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
        # Transaction.webpay.webpay_plus.default_integration_type = IntegrationType.TEST
        # response = Transaction.webpay.webpay_plus.create("PRUEBABUY_ORDER", "123", 1000, "https://www.google.cl")
        data = request.args['id']
        response = reservaController.getOrderPayById(data) #Deberia ser get order pay y agregar un update

        print("Webpay Plus Transaction.create")
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        amount = random.randrange(10000, 1000000)
        return_url = request.url_root + 'webpay-plus/commit'

        create_request = {
            "buy_order": buy_order,
            "session_id": session_id,
            "amount": amount,
            "return_url": "http://localhost:4000/"
        }

        responseTrans = Transaction.create(buy_order, session_id, response[0]["totalReserve"], "http://localhost:4000/client/pago")
        # print(responseTrans.token, responseTrans.url)
        # response = Transaction.commit(token = responseTrans.token)
        reservaController.updateOrderPay(data)
        return jsonify({"url" : str(responseTrans.url), "token" : str(responseTrans.token)})
    except Exception as err:
        print(err)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug = True, port = 4000)