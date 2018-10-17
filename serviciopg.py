import yaml
from pgsql import *
import bottle
import re, json
from bottle import route, request, response
from bottle import post, get, put, delete
conn=None

def conectar():
    try:
        with open('C:/ws/config.yaml','r') as ymlfile:
            cfg = yaml.load(ymlfile)
			   
        host = cfg['database']['host']
        base = cfg['database']['base']
        port = cfg['database']['port']
        user = cfg['database']['user']
        pswd = cfg['database']['passwd']
		
        conn = pgsql(host, base, port, user, pswd)
        return conn		
    except yaml.YAMLError as e:
        print("error")
        return None

		
@route('/lectura')
def lectura():
    response.headers['Content-Type'] = 'application/json'
    conn=conectar()
		
    query = "SELECT texto AS texto,encode(imagen,'base64') AS imagen FROM prueba"
    data = conn.getData(query)
                
    platos = []
    
    for valor in data:
        platos.append({'imagen': valor.imagen, 'texto': valor.texto})
		
    conn.cerrar()
    return json.dumps(platos)
    

app = application = bottle.default_app()
if __name__ == "__main__":
    bottle.run(host='192.168.1.20', port=8095)
