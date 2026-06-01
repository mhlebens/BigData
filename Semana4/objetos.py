# El nombre del objeto
class Objeto:
    def __init__(self, primerParametro, segundoParametro):
        self.primerParametro = primerParametro
        self.segundoParametro = segundoParametro

    def saludo(self):
        print("Bienvenido al sistema de BigData 2026")

nuevo = Objeto("1", "2")

print (nuevo.primerParametro)
print(nuevo.segundoParametro)
nuevo.saludo()