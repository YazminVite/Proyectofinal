# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/api_clientes/?', 'application.api.clientes.api_clientes.Api_clientes',
    '/clientes', 'application.controllers.clientes.index.Index',
'/clientes/view/(.+)', 'application.controllers.clientes.view.View',
'/clientes/edit/(.+)', 'application.controllers.clientes.edit.Edit',
'/clientes/delete/(.+)', 'application.controllers.clientes.delete.Delete',
'/clientes/insert', 'application.controllers.clientes.insert.Insert',
    '/api_empleados/?', 'application.api.empleados.api_empleados.Api_empleados',
    '/empleados', 'application.controllers.empleados.index.Index',
'/empleados/view/(.+)', 'application.controllers.empleados.view.View',
'/empleados/edit/(.+)', 'application.controllers.empleados.edit.Edit',
'/empleados/delete/(.+)', 'application.controllers.empleados.delete.Delete',
'/empleados/insert', 'application.controllers.empleados.insert.Insert',
    '/api_proyectos/?', 'application.api.proyectos.api_proyectos.Api_proyectos',
    '/proyectos', 'application.controllers.proyectos.index.Index',
'/proyectos/view/(.+)', 'application.controllers.proyectos.view.View',
'/proyectos/edit/(.+)', 'application.controllers.proyectos.edit.Edit',
'/proyectos/delete/(.+)', 'application.controllers.proyectos.delete.Delete',
'/proyectos/insert', 'application.controllers.proyectos.insert.Insert',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
