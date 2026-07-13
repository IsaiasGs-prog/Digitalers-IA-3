class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El {self.marca} {self.modelo} esta en funcionamiento."
    
    def apagar(self):
        return f"El {self.marca} {self.modelo} se ha apagado."
    
    def frenar(self):
        return f"El {self.marca} {self.modelo} esta frenando."
