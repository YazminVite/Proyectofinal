import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_empleado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_empleado) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_empleado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_empleado) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
        
    

    @staticmethod
    def GET_EDIT(id_empleado, **k):
        message = None # Error message
        id_empleado = config.check_secure_val(str(id_empleado)) # HMAC id_empleado validate
        result = config.model.get_empleados(int(id_empleado)) # search for the id_empleado
        result.id_empleado = config.make_secure_val(str(result.id_empleado)) # apply HMAC for id_empleado
        return config.render.edit(result, message) # render empleados edit.html

    @staticmethod
    def POST_EDIT(id_empleado, **k):
        form = config.web.input()  # get form data
        form['id_empleado'] = config.check_secure_val(str(form['id_empleado'])) # HMAC id_empleado validate
        # edit user with new data
        result = config.model.edit_empleados(
            form['id_empleado'],form['nombre'],form['apellidos'],form['telefono'],form['cargo'],
        )
        if result == None: # Error on udpate data
            id_empleado = config.check_secure_val(str(id_empleado)) # validate HMAC id_empleado
            result = config.model.get_empleados(int(id_empleado)) # search for id_empleado data
            result.id_empleado = config.make_secure_val(str(result.id_empleado)) # apply HMAC to id_empleado
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/empleados') # render empleados index.html
