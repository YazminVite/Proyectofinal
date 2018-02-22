import web
import config

db = config.db


def get_all_empleados():
    try:
        return db.select('empleados')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_empleados(id_empleado):
    try:
        return db.select('empleados', where='id_empleado=$id_empleado', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_empleados(id_empleado):
    try:
        return db.delete('empleados', where='id_empleado=$id_empleado', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_empleados(nombre,apellidos,telefono,cargo):
    try:
        return db.insert('empleados',nombre=nombre,
apellidos=apellidos,
telefono=telefono,
cargo=cargo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_empleados(id_empleado,nombre,apellidos,telefono,cargo):
    try:
        return db.update('empleados',id_empleado=id_empleado,
nombre=nombre,
apellidos=apellidos,
telefono=telefono,
cargo=cargo,
                  where='id_empleado=$id_empleado',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
