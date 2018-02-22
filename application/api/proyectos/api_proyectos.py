import web
import config
import json


class Api_proyectos:
    def get(self, id_proyecto):
        try:
            # http://0.0.0.0:8080/api_proyectos?user_hash=12345&action=get
            if id_proyecto is None:
                result = config.model.get_all_proyectos()
                proyectos_json = []
                for row in result:
                    tmp = dict(row)
                    proyectos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(proyectos_json)
            else:
                # http://0.0.0.0:8080/api_proyectos?user_hash=12345&action=get&id_proyecto=1
                result = config.model.get_proyectos(int(id_proyecto))
                proyectos_json = []
                proyectos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(proyectos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            proyectos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proyectos_json)

# http://0.0.0.0:8080/api_proyectos?user_hash=12345&action=put&id_proyecto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, proyecto,estatus,empleado_elabora,titular):
        try:
            config.model.insert_proyectos(proyecto,estatus,empleado_elabora,titular)
            proyectos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proyectos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_proyectos?user_hash=12345&action=delete&id_proyecto=1
    def delete(self, id_proyecto):
        try:
            config.model.delete_proyectos(id_proyecto)
            proyectos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proyectos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_proyectos?user_hash=12345&action=update&id_proyecto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_proyecto, proyecto,estatus,empleado_elabora,titular):
        try:
            config.model.edit_proyectos(id_proyecto,proyecto,estatus,empleado_elabora,titular)
            proyectos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proyectos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            proyectos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proyectos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_proyecto=None,
            proyecto=None,
            estatus=None,
            empleado_elabora=None,
            titular=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_proyecto=user_data.id_proyecto
            proyecto=user_data.proyecto
            estatus=user_data.estatus
            empleado_elabora=user_data.empleado_elabora
            titular=user_data.titular
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_proyecto)
                elif action == 'put':
                    return self.put(proyecto,estatus,empleado_elabora,titular)
                elif action == 'delete':
                    return self.delete(id_proyecto)
                elif action == 'update':
                    return self.update(id_proyecto, proyecto,estatus,empleado_elabora,titular)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
