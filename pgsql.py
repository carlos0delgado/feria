from logger import *

import psycopg2
import psycopg2.extras


class pgsql:
    conn = ''
    conectado = False

    #lg = logger()

    def __setCriticalLogger(self, msg):
        self.lg.setCritical('DB-Error: %s' % msg)
    
    def __setInfoLogger(self, msg):
        self.lg.setInfo('DB-Info: %s' % msg)

    def __init__(self, servidor, base, puerto, usuario, clave):
        try:
            self.conn = psycopg2.connect(host=servidor,
                                         database=base,
                                         port=puerto,
                                         user=usuario,
                                         password=clave)

            self.conectado=True
            #self.__setInfoLogger('Conexion a base de datos OK')
        except psycopg2.Error as e:
            print((e.pgerror))
            #self.__setCriticalLogger(e.pgerror)

    def closeDB(self):
        self.__setInfoLogger('conexion a base de datos cerrada')

    def getData(self, query, valores="", likeArray=False, onlyOne=False):
        try:
            if likeArray is True:
                cur = self.conn.cursor(
                          cursor_factory=psycopg2.extras.RealDictCursor)
            else:
                cur = self.conn.cursor(
                          cursor_factory=psycopg2.extras.NamedTupleCursor)

            if valores=="":
                cur.execute(query)
            else:
                cur.execute(query,valores)

            if onlyOne:
                return cur.fetchone()
            else:
                return cur.fetchall()

        except psycopg2.Error as e:
            #self.__setCriticalLogger(e.pgerror)
            print((e.pgerror))
            return None

    def updateData(self, query, valores="", withCommit=True):
        try:
            cur = self.conn.cursor()
            if valores=="":
                cur.execute(query)
            else:
                cur.execute(query,valores)

            if withCommit:
                self.conn.commit()
        except psycopg2.Error as e:
            #self.__setCriticalLogger(e.pgerror)
            print((e.pgerror))

    def toBinary(self, valor):
        return psycopg2.Binary(valor)

    def stringToBoolean(self, valor):
        if valor == '1':
            return True
        else:
            return False

    def commitUpdate(self):
        self.conn.commit()

    def cerrar(self):
        self.conn.close()