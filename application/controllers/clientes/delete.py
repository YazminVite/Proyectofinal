import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_cliente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_cliente) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_cliente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_cliente) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_cliente, **k):
        message = None # Error message
        id_cliente = config.check_secure_val(str(id_cliente)) # HMAC id_cliente validate
        result = config.model.get_clientes(int(id_cliente)) # search  id_cliente
        result.id_cliente = config.make_secure_val(str(result.id_cliente)) # apply HMAC for id_cliente
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_cliente, **k):
        form = config.web.input() # get form data
        form['id_cliente'] = config.check_secure_val(str(form['id_cliente'])) # HMAC id_cliente validate
        result = config.model.delete_clientes(form['id_cliente']) # get clientes data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_cliente = config.check_secure_val(str(id_cliente))  # HMAC user validate
            id_cliente = config.check_secure_val(str(id_cliente))  # HMAC user validate
            result = config.model.get_clientes(int(id_cliente)) # get id_cliente data
            result.id_cliente = config.make_secure_val(str(result.id_cliente)) # apply HMAC to id_cliente
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/clientes') # render clientes delete.html 
