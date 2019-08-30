class Auto:
    """ Esta clase nos muestra el precio, la patente, el kilometraje,
        el dueño y la marca de un auto. También es posible actualizar
        el kilometraje del vehículo mediante el método recorrer, como
        además determinar el uso del auto mediante el método uso.
    """
    
    def __init__(self, precio, patente, kilometraje, dueno, marca):
        self.pt = patente
        self.km = kilometraje
        self.dn = dueno
        self.marc = marca
        self.p = precio

    def __call__(self, km_recorridos):
        self.km += km_recorridos

    def __str__(self):
        return ('El auto cuesta ${}'.format(self.p))

    @property
    def uso(self):
        if self.km == 0:
            print("Nuevo")
        elif 0 < self.km <= 20000:
            print("Usado, pero como nuevo")
        else:
            print("Viejo")

mi_auto = Auto(10000000,123, 10000, "Franco", "daewoo")

mi_auto.uso
print(mi_auto)
mi_auto(10001)
print(mi_auto.km)
mi_auto.uso
