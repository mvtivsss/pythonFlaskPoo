from BD import configuracion

def validateLogin(mail,password):
    response = []
    try:
        data = configuracion.callProcedureIdRefCursor('spValidateLogin',[mail, password])
        for row in data:
            response.append({'id':row[0],'mail':row[1],'firstName': row[2], 'lastNameP': row[3], 'lastNameM':row[4], 'dob': row[5],
                            'phone': row[6], 'idCommune':row[7], 'typeUser': row[10] })
        print('ok validate true')
    except Exception as err:
        print('validate false', err)
    finally:
        return response