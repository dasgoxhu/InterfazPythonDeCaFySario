import tkinter as tk
import tkinter as ttk
from ConvertidorTempo import covtemp
from CalculoSalario import Salario

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')


color_fondo = "#1E1E1E"
color_texto = "white"
color_botones = "#333333"

ventana1 = tk.Tk()
center_window(ventana1, 410, 300)
ventana1.geometry('330x30')
ventana1.title('Taller 1')
ventana1.configure(bg=color_fondo)

Temp = 0
msg = 0


def Punto1():
    def caltemp1():
        msg = float(entrada1.get())
        Temp = covtemp(0,msg)
        resultado_celsius = Temp.calFahtoCel()
        etiqueta_resultado_celsius.config(text=f"Resultado Celsius: {resultado_celsius} °C")
        Temp.guardar_resultado(f"Convertir {msg} Fahrenheit a Celsius: {resultado_celsius} °C")

    def caltemp2():
        msg = float(entrada1.get())
        Temp = covtemp(msg,0 )
        resultado_fahrenheit = Temp.calCeltoFah()
        etiqueta_resultado_fahrenheit.config(text=f"Resultado Fahrenheit: {resultado_fahrenheit} °F")
        Temp.guardar_resultado(f"Convertir {msg} Celsius a Fahrenheit: {resultado_fahrenheit} °F")

    def exportar_resultados():
        etiqueta4.config(text="Exportado con Éxito")

    def volver_a_ventana1():
        ventana2.destroy()
        ventana1.deiconify()

    ventana1.withdraw()
    ventana2 = tk.Tk()
    ventana2.geometry('410x300')
    ventana2.overrideredirect(True)
    ventana2.title('Convertidor de F a C')
    ventana2.configure(bg=color_fondo)
    center_window(ventana2, 410, 300)
    etiqueta1 = tk.Label(ventana2, text="Convertidor de grados 15%", foreground=color_texto, background=color_fondo)
    etiqueta1.grid(row=0)
    entrada1 = ttk.Entry(ventana2, width=35, foreground=color_texto, background=color_fondo)
    entrada1.grid(row=1, column=0, padx=100, pady=10)
    boton1 = ttk.Button(ventana2, text="Convertir a Fahrenheit", command=caltemp1, foreground=color_texto,
                        background=color_botones)
    boton1.grid(row=2, column=0, padx=100, pady=10)

    boton2 = ttk.Button(ventana2, text="Convertir a Celsius", command=caltemp2, foreground=color_texto,
                        background=color_botones)
    boton2.grid(row=4, column=0, padx=100, pady=10)

    boton3 = ttk.Button(ventana2, text="Exportar", command=exportar_resultados, foreground=color_texto,
                        background=color_botones)
    boton3.grid(row=6, column=0, padx=100, pady=10)

    etiqueta4 = tk.Label(ventana2, text="", foreground=color_texto, background=color_fondo)
    etiqueta4.grid(row=7)

    etiqueta_resultado_fahrenheit = tk.Label(ventana2, text="", foreground=color_texto, background=color_fondo)
    etiqueta_resultado_fahrenheit.grid(row=5, columnspan=2)

    etiqueta_resultado_celsius = tk.Label(ventana2, text="", foreground=color_texto, background=color_fondo)
    etiqueta_resultado_celsius.grid(row=3, columnspan=2)

    boton_volver = ttk.Button(ventana2, text="Volver", command=volver_a_ventana1, foreground=color_texto,
                              background=color_botones)
    boton_volver.grid(row=8, column=0)

    ventana2.mainloop()


def Punto2():
    ventana1.withdraw()
    ventana3 = tk.Tk()
    ventana3.overrideredirect(True)
    ventana3.configure(bg=color_fondo)
    center_window(ventana3, 410, 300)
    ventana3.geometry('500x500')
    ventana3.title('Calcular Salarios')

    def volver_a_ventana1():
        ventana3.destroy()
        ventana1.deiconify()

    def calcular_salario():
        salario = float(entrada_salario.get())
        aumento = float(entrada_aumento.get())
        dias = float(entrada_dias.get())
        nombres = entrada_nombres.get()
        apellidos = entrada_apellidos.get()

        salario_obj = Salario(salario, aumento, dias)

        salario_final, subsidio = salario_obj.aumento()
        prima = salario_obj.Prima()
        cesantias = salario_obj.Cesantias()
        intereses = salario_obj.Intereses()
        vacaciones = salario_obj.Vacaciones()
        suma_total = salario_obj.SumaTodo()

        etiqueta_resultados.config(text=f"Nombres: {nombres}\n"
                                        f"Apellidos: {apellidos}\n"
                                        f"Salario Final: {salario_final}\n"
                                        f"Subsidio: {subsidio}\n"
                                        f"Prima: {prima}\n"
                                        f"Cesantías: {cesantias}\n"
                                        f"Intereses: {intereses}\n"
                                        f"Vacaciones: {vacaciones}\n"
                                        f"Suma Total: {suma_total}")



    def exportarSalario():
        salario = float(entrada_salario.get())
        aumento = float(entrada_aumento.get())
        dias = float(entrada_dias.get())
        nombres = entrada_nombres.get()
        apellidos = entrada_apellidos.get()

        salario_obj = Salario(salario, aumento, dias)
        salario_final, subsidio = salario_obj.aumento()
        prima = salario_obj.Prima()
        cesantias = salario_obj.Cesantias()
        intereses = salario_obj.Intereses()
        vacaciones = salario_obj.Vacaciones()
        suma_total = salario_obj.SumaTodo()

        salario_obj.exportar_resultado(f"Nombres: {nombres}\n"
                                       f"Apellidos: {apellidos}\n"
                                       f"Salario Final: {salario_final}\n"
                                       f"Subsidio: {subsidio}\n"
                                       f"Prima: {prima}\n"
                                       f"Cesantías: {cesantias}\n"
                                       f"Intereses: {intereses}\n"
                                       f"Vacaciones: {vacaciones}\n"
                                       f"Suma Total: {suma_total}")

    etiqueta_nombres = ttk.Label(ventana3, text="Nombres:", foreground=color_texto, background=color_fondo)
    etiqueta_nombres.grid(row=0, column=0)
    entrada_nombres = ttk.Entry(ventana3, width=35, foreground=color_texto, background=color_fondo)
    entrada_nombres.grid(row=0, column=1, padx=10, pady=10)

    etiqueta_apellidos = ttk.Label(ventana3, text="Apellidos:", foreground=color_texto, background=color_fondo)
    etiqueta_apellidos.grid(row=1, column=0)
    entrada_apellidos = ttk.Entry(ventana3, width=35, foreground=color_texto, background=color_fondo)
    entrada_apellidos.grid(row=1, column=1, padx=10, pady=10)
    etiqueta_salario = ttk.Label(ventana3, text="Salario:", foreground=color_texto, background=color_fondo)
    etiqueta_salario.grid(row=2, column=0)
    entrada_salario = ttk.Entry(ventana3, width=35, foreground=color_texto, background=color_fondo)
    entrada_salario.grid(row=2, column=1, padx=10, pady=10)

    etiqueta_aumento = ttk.Label(ventana3, text="Aumento (%):", foreground=color_texto, background=color_fondo)
    etiqueta_aumento.grid(row=3, column=0)
    entrada_aumento = ttk.Entry(ventana3, width=35, foreground=color_texto, background=color_fondo)
    entrada_aumento.grid(row=3, column=1, padx=10, pady=10)

    etiqueta_dias = ttk.Label(ventana3, text="Días trabajados:", foreground=color_texto, background=color_fondo)
    etiqueta_dias.grid(row=4, column=0)
    entrada_dias = ttk.Entry(ventana3, width=35, foreground=color_texto, background=color_fondo)
    entrada_dias.grid(row=4, column=1, padx=10, pady=10)

    boton_calcular = ttk.Button(ventana3, text="Calcular Salario", command=calcular_salario,
                                foreground=color_texto, background=color_botones)
    boton_calcular.grid(row=5, columnspan=2, padx=10, pady=10)

    etiqueta_resultados = ttk.Label(ventana3, text="", foreground=color_texto, background=color_fondo)
    etiqueta_resultados.grid(row=6, columnspan=2)

    boton_Exportar = ttk.Button(ventana3, text="Exportar", command=exportarSalario,
                                foreground=color_texto, background=color_botones)
    boton_Exportar.grid(row=7, columnspan=2, padx=10, pady=10)

    boton_volver = ttk.Button(ventana3, text="Volver", command=volver_a_ventana1, foreground=color_texto,
                              background=color_botones)
    boton_volver.grid(row=8, column=0)

    ventana3.mainloop()


boton1 = ttk.Button(ventana1, text="Convertidor de F a C", command=Punto1, foreground=color_texto,
                    background=color_botones)
boton1.grid(row=1, column=1, padx=35)

boton2 = ttk.Button(ventana1, text="Calcular Salarios", command=Punto2, foreground=color_texto,
                    background=color_botones)
boton2.grid(row=1, column=2)

ventana1.mainloop()
