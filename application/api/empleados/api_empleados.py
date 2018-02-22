import web
import config
import json


class Api_empleados:
    def get(self, id_empleado):
        try:
            # http://0.0.0.0:8080/api_empleados?user_hash=12345&action=get
            if id_empleado is None:
                result = config.model.get_all_empleados()
                empleados_json = []
                for row in result:
                    tmp = dict(row)
                    empleados_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(empleados_json)
            else:
                # http://0.0.0.0:8080/api_empleados?user_hash=12345&action=get&id_empleado=1
                result = config.model.get_empleados(int(id_empleado))
                empleados_json = []
                empleados_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(empleados_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            empleados_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(empleados_json)

# http://0.0.0.0:8080/api_empleados?user_hash=12345&action=put&id_empleado=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,apellidos,telefono,cargo):
        try:
            config.model.insert_empleados(nombre,apellidos,telefono,cargo)
            empleados_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(empleados_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_empleados?user_hash=12345&action=delete&id_empleado=1
    def delete(self, id_empleado):
        try:
            config.model.delete_empleados(id_empleado)
            empleados_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(empleados_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_empleados?user_hash=12345&action=update&id_empleado=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_empleado, nombre,apellidos,telefono,cargo):
        try:
            config.model.edit_empleados(id_empleado,nombre,apellidos,telefono,cargo)
            empleados_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(empleados_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            empleados_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(empleados_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_empleado=None,
            nombre=None,
            apellidos=None,
            telefono=None,
            cargo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_empleado=user_data.id_empleado
            nombre=user_data.nombre
            apellidos=user_data.apellidos
            telefono=user_data.telefono
            cargo=user_data.cargo
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_empleado)
                elif action == 'put':
                    return self.put(nombre,apellidos,telefono,cargo)
                elif action == 'delete':
                    return self.delete(id_empleado)
                elif action == 'update':
                    return self.update(id_empleado, nombre,apellidos,telefono,cargo)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
