from zope.interface import Interface
from zope.interface import implementer

class Ielemento(Interface):
    def insertarElemento(self, posicion, objeto):
        pass
    def agregarElemento(self, objeto):
        pass
    def mostrarElemento(self, posicion):
        pass

