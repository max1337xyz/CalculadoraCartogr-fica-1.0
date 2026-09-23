from tkinter import messagebox
import math
class CartografiaCalculos:

    def Calcular_utm(longeA=0,latiA=0,longeB=0,latiB=0):

        dist = math.sqrt((longeA-longeB)**2+(latiA-latiB)**2)
     
        math.sin
        messagebox.showinfo("Sucesso",f"{dist:0.2f}METROS")

    def calcular_passos(n1,metros):
        passos = float(metros/n1)
        messagebox.showinfo("Sucesso",f"Para Percorrer {metros:0.0f} Metros Precisamos de Andar  {passos:0.0f} Passos")
        
    def calcular_rumo(azimute, direction):

        if direction == "NE":
            rumo = azimute

        elif direction == "SE":
            rumo = 180 - azimute

        elif direction == "SW":
            rumo = azimute - 180

        elif direction == "NW":
            rumo = 360 - azimute

        else:
            messagebox.showerror(
                "Erro",
                "Direção inválida!"
            )
            return None

        messagebox.showinfo(
            "Sucesso!",
            f"Rumo: {rumo:.2f}°"
        )

        return rumo
    def calcular_dispersao_magnetica(valor_inicial, valor_final,
                                      ano_inicial, ano_final):

        diferenca_valor = valor_final - valor_inicial
        diferenca_anos = ano_final - ano_inicial

        if diferenca_anos == 0:
            raise ValueError("Os anos não podem ser iguais.")

        dispersao = diferenca_valor / diferenca_anos

        return dispersao