class covtemp:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def calFahtoCel(self):
        operacion = ((self.fahrenheit - 32) / 1.8)
        return round(operacion, 1)

    def calCeltoFah(self):
        operacion = ((self.celsius * 1.8) + 32)
        return round(operacion, 1)

    def guardar_resultado(self, resultado):
        with open("resultadosConvertidor.txt", "a") as archivo:
            archivo.write(f"{resultado}\n")
