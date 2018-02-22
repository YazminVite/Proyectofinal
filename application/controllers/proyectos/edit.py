import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_proyecto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_proyecto) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_proyecto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_proyecto) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
        
    

    @staticmethod
    def GET_EDIT(id_proyecto, **k):
        message = None # Error message
        id_proyecto = config.check_secure_val(str(id_proyecto)) # HMAC id_proyecto validate
        result = config.model.get_proyectos(int(id_proyecto)) # search for the id_proyecto
        result.id_proyecto = config.make_secure_val(str(result.id_proyecto)) # apply HMAC for id_proyecto
        return config.render.edit(result, message) # render proyectos edit.html

    @staticmethod
    def POST_EDIT(id_proyecto, **k):
        form = config.web.input()  # get form data
        form['id_proyecto'] = config.check_secure_val(str(form['id_proyecto'])) # HMAC id_proyecto validate
        # edit user with new data
        result = config.model.edit_proyectos(
            form['id_proyecto'],form['proyecto'],form['estatus'],form['empleado_elabora'],form['titular'],
        )
        if result == None: # Error on udpate data
            id_proyecto = config.check_secure_val(str(id_proyecto)) # validate HMAC id_proyecto
            result = config.model.get_proyectos(int(id_proyecto)) # search for id_proyecto data
            result.id_proyecto = config.make_secure_val(str(result.id_proyecto)) # apply HMAC to id_proyecto
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/proyectos') # render proyectos index.html
