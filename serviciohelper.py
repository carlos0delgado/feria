#!/usr/bin/python
import bottle
import re, json
from bottle import route, request, response
from bottle import post, get, delete
import psycopg2
import psycopg2.extras
from psycopg2 import errorcodes


config = {
    'user':'odoo',
    'password':'odoo',
    'host':'181.198.202.181',
    'database':'feria2',
    'port':5432,
}


@route('/servicio')
@route('/servicio/<accion>')
def servicio(accion=None):
    response.headers['Content-Type'] = 'application/json'
    conn = psycopg2.connect(**config)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    tvfiltro = request.forms.get("tvfiltro")
    print(conn)
    if tvfiltro is None:
        #lista = {'nombre':'Jhon','edad':25}
        query = "select titulo as cantidad, autor as categoria from libro"
        cursor.execute(query)
        data=cursor.fetchall()
        print("aca")
        print(data)
        conn.close()
        return json.dumps(data)
        #return json.JSONEncoder.default(self, data)
    else:
        #lista = {'nombre':'carlos','apellido':'hernandez'}
        query = "select idcod as cantidad, titulo as categoria from libro where categoria = 'C'"
        cursor.execute(query, {'categoria':categoria})
        data=cursor.fetchall()
        conn.close()
        print(data)
        return json.dumps(data)

@route('/lectura', method=["POST"])
def servicio(accion=None):
    response.headers['Content-Type'] = 'application/json'
    conn = psycopg2.connect(**config)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    categoria = request.forms.get("categoria")
    print(categoria)
    print(conn)
    if categoria is None or categoria == "":
        #lista = {'nombre':'carlos','apellido':'hernandez'}
        query = "select titulo as texto, autor as subtexto,encode(imagen,'base64') AS imagen from libro where idcod=%(categoria)s"
        cursor.execute(query, {'categoria':categoria})
        data=cursor.fetchall()
        conn.close()
        print(data)
        return json.dumps(data)
    else:
        #lista = {'nombre':'carlos','apellido':'hernandez'}
        query = "select titulo as texto, autor as subtexto,encode(imagen,'base64') AS imagen from libro where idcod=%(categoria)s"
        cursor.execute(query, {'categoria':categoria})
        data=cursor.fetchall()
        conn.close()
        print(data)
        return json.dumps(data)

@route('/grabarProducto', method=["POST"])
def grabarProducto():
    try:
        msg = ""
        conn = psycopg2.connect(**config
        )

        cursor = conn.cursor()

        idcod = request.forms.get("idcod")
        titulo = request.forms.get("titulo")
        autor = request.forms.get("autor")
        categoria = request.forms.get("categoria")
        precio = request.forms.get("precio")

        query = "insert into libro values(%s, %s, %s, %s, %s)"
        cursor.execute(query, (idcod, titulo, autor, categoria, precio))
        conn.commit()

        conn.close()
        msg = "Dato Grabado Correctamente"
    except psycopg2.connect.error as err:
        msg = "ERR: " + format(err)
    return msg

"""@route('/eliminarProducto', method=["POST"])
def eliminarProducto():
    try:
        msg = ""
        conn = psycopg2.connect(**config
        )

        cursor = conn.cursor()

        idcod = request.forms.get("idcod")


        query = "delete from libro where libro.idcod=(%s)"
        cursor.execute(query, (idcod))
        conn.commit()

        conn.close()
        msg = "Dato Grabado Correctamente"
    except psycopg2.connect.error as err:
        msg = "ERR: " + format(err)
    return msg

@route('/servicio2')
def servicio2(accion=None):
    response.headers['Content-Type'] = 'application/json'
    conn = psycopg2.connect(**config)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    tvfiltro = request.forms.get("tvfiltro")
    print(conn)
    if tvfiltro is None:
        #lista = {'nombre':'Jhon','edad':25}
        query = "SELECT ROW_NUMBER() OVER( ORDER BY categoria) AS id, CASE categoria WHEN 'I' THEN 'INFANTIL' WHEN 'S' THEN 'ASTRONOMIA' WHEN 'C' THEN 'CIEN EXACT' WHEN 'L' THEN 'LITERATURA' WHEN 'A' THEN 'ARTE' END AS subject , count (categoria) as marks FROM libro GROUP BY categoria"
        cursor.execute(query)
        data=cursor.fetchall()
        print("aca")
        print(data)
        conn.close()
        return json.dumps(data)
        #return json.JSONEncoder.default(self, data)
    else:
        #lista = {'nombre':'carlos','apellido':'hernandez'}
        query = "select idcod as cantidad, titulo as categoria from libro where categoria = 'C'"
        cursor.execute(query, {'categoria':categoria})
        data=cursor.fetchall()
        conn.close()
        print(data)
        return json.dumps(data)"""


app = application = bottle.default_app()
if __name__ == "__main__":
    bottle.run(host='192.168.0.120', port=8073)
