from .autos import Auto


def probar_auto(marca, modelo):
    auto = Auto(marca, modelo)
    return auto.arrancar()
