import logging
import logging.handlers


class logger:
    lg = logging.getLogger('techind')
    hdlr = logging.handlers.RotatingFileHandler('techind.log',maxBytes=1048576, backupCount=5)

    formato = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

    def __init__(self):
        self.hdlr.setFormatter(self.formato)
        self.lg.addHandler(self.hdlr)
        self.lg.setLevel(logging.DEBUG)

    def getHandler(self):
	    return self.hdlr

    def setWarning(self, message):
        self.lg.warn(message)

    def setError(self, message):
        self.lg.error(message)

    def setInfo(self, message):
        self.lg.info(message)

    def setCritical(self, message):
        self.lg.critical(message)

    def setDebug(self, message):
        self.lg.debug(message)
