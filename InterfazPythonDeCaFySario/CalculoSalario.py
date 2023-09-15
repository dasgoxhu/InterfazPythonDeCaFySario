class Salario():

    def __init__(self, Salario, Aumento, Dias):
        self.Subsidio = 800000
        self.tranporte = 140606
        self.sal = Salario
        self.aum = Aumento
        self.dia = Dias
        self.nombres = ""
        self.apellidos = ""

    def ingresar_nombres(self, nombres):
        self.nombres = nombres

    def ingresar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def aumento(self):
        sub=self.sal
        if self.sal < self.Subsidio:
            sub = self.sal + self.tranporte

        self.sal = (self.sal * self.aum) + self.sal
        return round((self.sal)),round((sub))

    def Prima(self):
        cal = ((self.sal*self.dia)/360)
        return round((cal))

    def Cesantias(self):
        cal = ((self.sal*self.dia)/360)
        return round((cal))

    def Vacaciones(self):
        cal = ((self.sal*self.dia)/720)
        return round((cal))

    def Intereses(self):
        cal = ((self.Cesantias()*self.dia*0.12)/360)
        return round((cal))

    def SumaTodo(self):
        Salario,Subsidiado = self.aumento()
        Prima = self.Prima()
        Censantias = self.Cesantias()
        Interes = self.Intereses()
        Vacaciones = self.Vacaciones()
        return round((Subsidiado + Prima + Censantias + Interes + Vacaciones))

    def exportar_resultado(self, resultado):
        with open("resultadosSalario.txt", "a") as archivo:
            archivo.write(f"{resultado}\n")



