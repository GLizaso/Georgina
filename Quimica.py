class Elemento:
    def __init__(self, simbolo, numeroAtomico, cantNeutrones, valencia):
        self.simbolo = simbolo
        self.numeroAtomico = numeroAtomico
        self.cantNeutrones = cantNeutrones
        self.valencia = valencia


    def cantProtones(self):
        return self.numeroAtomico

    def cantNeutrones(self):
        return self.cantNeutrones

    def cantElectrones(self):
        return self.numeroAtomico

    def numeroAtomico(self):
        return self.numeroAtomico

    def pesoAtomico(self):
        peso = self.numeroAtomico+ self.cantNeutrones
        return peso

    def valencia(self):
        return self.valencia

    def simbolo(self):
        return self.simbolo


class TablaPeriodica:
    def _init_(self):
        self.elementos = []

    def elementos(self):
        return self.elementos

    def agregarElemento(self,elemento):
        if self.elementoS(elemento.simbolo()) is None:
              self.elementos.__add__(self, elemento) #o elementos.append(elemento)

    def elementoS(self,simbolo):
        return self.findElemento(simbolo, lambda elemento: elemento.simbolo()) #como digo que elemento pertenece a la clase Elemento

    def elementoN(self,numero):
        return self.findElemento(numero, lambda elemento: elemento.numeroAtomico())

    def findElemento(self,atributo,mensaje):
        return next ((elemento for elemento in self.elementos if mensaje(elemento) == atributo))

#   27/6/18
""""
class Compuesto: # ver que onda con esta clase
    def __init__(self, formula):
        self.formula = formula

    def agregarAtomo(self, elemento, cantAtomos ):
     return self.agregarAtomo()

class CompuestoAux:
    def __init__(self,compuesto,moles):
        self.compuesto=compuesto
        self.moles=moles
    def getmoles(self):
        return self.moles
    def getcompuesto(self):
        return self.compuesto
    def aniadirmoles(self, cantidadMoles):
        self.moles = self.moles+ cantidadMoles

class Medio:
    def __init__(self):
        self.listacompuestos=[]

    def agregarComponente(self,compuesto, cantMoles):
        if self.findcompuesto(compuesto) is None:
            self.listacompuestos.append(CompuestoAux(compuesto,cantMoles))
        else:
           self.findcompuesto(compuesto).aniadirmoles(cantMoles)

     def findcompuesto(self,compuesto):
         return next ((compuesto for compuesto in self.listacompuestos if compuesto.getcompuesto == compuesto))

     def masaTotal(self):
        return self.
    def elementosPresentes(self):
        return self.listacompuestos
    #def cantMolesElemento(self):
     #   return
    def masaDeCompuesto(self):
    def masaDeElemento(self):
    def proporcionElementoSobreMasa(self):
    def proporcionCompuestoSobreMasa(self):
        

"""
#estas variables las uso para los test
#oxigeno = Elemento(simbolo, numeroAtomico, cantNeutrones, valencia)

oxigeno = Elemento('O', 8, 8, 4)
hidrogeno = Elemento('H', 1, 1, 1)
carbono= Elemento('C',6, 7, 2)
nitrogeno= Elemento('N', 7, 6, 4)


tabla = TablaPeriodica()