import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_empleado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_empleado) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_empleado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_empleado) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

   

    
    

     @staticmethod
    def GET_DELETE(id_empleado, **k):
        message = None # Error message
        id_empleado = config.check_secure_val(str(id_empleado)) # HMAC id_empleado validate
        result = config.model.get_empleados(int(id_empleado)) # search  id_empleado
        result.id_empleado = config.make_secure_val(str(result.id_empleado)) # apply HMAC for id_empleado
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_empleado, **k):
        form = config.web.input() # get form data
        form['id_empleado'] = config.check_secure_val(str(form['id_empleado'])) # HMAC id_empleado validate
        result = config.model.delete_empleados(form['id_empleado']) # get empleados data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_empleado = config.check_secure_val(str(id_empleado))  # HMAC user validate
            id_empleado = config.check_secure_val(str(id_empleado))  # HMAC user validate
            result = config.model.get_empleados(int(id_empleado)) # get id_empleado data
            result.id_empleado = config.make_secure_val(str(result.id_empleado)) # apply HMAC to id_empleado
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/empleados') # render empleados delete.html 
