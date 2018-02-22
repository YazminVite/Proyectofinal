import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_cliente):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_cliente) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                return self.GET_VIEW(id_cliente) # call GET_VIEW() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_cliente):
        id_cliente = config.check_secure_val(str(id_cliente)) # HMAC id_cliente validate
        result = config.model.get_clientes(id_cliente) # search for the id_cliente data
        return config.render.view(result) # render view.html with id_cliente data
