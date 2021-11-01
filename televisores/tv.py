class TV(object):
    NumTV = 0

    def __init__(self, marca, estado):
        self.canal = 1
        self.precio = 500
        estado = False
        self.volumen = 1
        self.marca = marca
        self.estado = estado
        TV.NumTV += 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.canal >= 1 and self.canal <120 and self.estado == True:
            self.canal += 1

    def canalDown(self):
        if self.canal > 1 and self.canal <=120 and self.estado == True:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen >= 0 and self.volumen <7 and self.estado == True:
            self.volumen += 1

    def volumenDown(self):
        if self.volumen >= 0 and self.volumen <=7 and self.estado == True:
            self.volumen -= 1

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if canal >= 1 and canal <=120 and self.estado == True:
            self.canal = canal

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if volumen >= 0 and volumen <=7 and self.estado == True:
            self.volumen = volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    @staticmethod
    def getNumTV():
        return TV.NumTV

    @staticmethod
    def setNumTV(numTV):
        TV.NumTV = numTV

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado






