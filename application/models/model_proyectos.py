import web
import config

db = config.db


def get_all_proyectos():
    try:
        return db.select('proyectos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_proyectos(id_proyecto):
    try:
        return db.select('proyectos', where='id_proyecto=$id_proyecto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_proyectos(id_proyecto):
    try:
        return db.delete('proyectos', where='id_proyecto=$id_proyecto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_proyectos(proyecto,estatus,empleado_elabora,titular):
    try:
        return db.insert('proyectos',proyecto=proyecto,
estatus=estatus,
empleado_elabora=empleado_elabora,
titular=titular)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_proyectos(id_proyecto,proyecto,estatus,empleado_elabora,titular):
    try:
        return db.update('proyectos',id_proyecto=id_proyecto,
proyecto=proyecto,
estatus=estatus,
empleado_elabora=empleado_elabora,
titular=titular,
                  where='id_proyecto=$id_proyecto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
