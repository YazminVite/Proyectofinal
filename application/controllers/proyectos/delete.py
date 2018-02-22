import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_proyecto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_proyecto) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_proyecto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_proyecto) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_proyecto, **k):
        message = None # Error message
        id_proyecto = config.check_secure_val(str(id_proyecto)) # HMAC id_proyecto validate
        result = config.model.get_proyectos(int(id_proyecto)) # search  id_proyecto
        result.id_proyecto = config.make_secure_val(str(result.id_proyecto)) # apply HMAC for id_proyecto
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_proyecto, **k):
        form = config.web.input() # get form data
        form['id_proyecto'] = config.check_secure_val(str(form['id_proyecto'])) # HMAC id_proyecto validate
        result = config.model.delete_proyectos(form['id_proyecto']) # get proyectos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_proyecto = config.check_secure_val(str(id_proyecto))  # HMAC user validate
            id_proyecto = config.check_secure_val(str(id_proyecto))  # HMAC user validate
            result = config.model.get_proyectos(int(id_proyecto)) # get id_proyecto data
            result.id_proyecto = config.make_secure_val(str(result.id_proyecto)) # apply HMAC to id_proyecto
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/proyectos') # render proyectos delete.html 
