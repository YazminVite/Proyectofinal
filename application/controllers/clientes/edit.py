import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_cliente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_cliente) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                return self.GET_EDIT(id_cliente) # call GET_EDIT function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_cliente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_cliente) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                return self.POST_EDIT(id_cliente) # call POST_EDIT function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
        
    

    @staticmethod
    def GET_EDIT(id_cliente, **k):
        message = None # Error message
        id_cliente = config.check_secure_val(str(id_cliente)) # HMAC id_cliente validate
        result = config.model.get_clientes(int(id_cliente)) # search for the id_cliente
        result.id_cliente = config.make_secure_val(str(result.id_cliente)) # apply HMAC for id_cliente
        return config.render.edit(result, message) # render clientes edit.html

    @staticmethod
    def POST_EDIT(id_cliente, **k):
        form = config.web.input()  # get form data
        form['id_cliente'] = config.check_secure_val(str(form['id_cliente'])) # HMAC id_cliente validate
        # edit user with new data
        result = config.model.edit_clientes(
            form['id_cliente'],form['nombre'],form['apellidos'],form['telefono'],form['proyecto'],
        )
        if result == None: # Error on udpate data
            id_cliente = config.check_secure_val(str(id_cliente)) # validate HMAC id_cliente
            result = config.model.get_clientes(int(id_cliente)) # search for id_cliente data
            result.id_cliente = config.make_secure_val(str(result.id_cliente)) # apply HMAC to id_cliente
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/clientes') # render clientes index.html
