import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    
    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_privilege = app.session.privilege  # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_INSERT():
        return config.render.insert() # render insert.html

    @staticmethod
    def POST_INSERT():
        form = config.web.input() # get form data

        # call model insert_empleados and try to insert new data
        config.model.insert_empleados(
            form['nombre'],form['apellidos'],form['telefono'],form['cargo'],
        )
        raise config.web.seeother('/empleados') # render empleados index.html
