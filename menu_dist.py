import customtkinter
from tkinter import messagebox

from Cartografia import CartografiaCalculos


class App_Dist(customtkinter.CTk):

    def __init__(self, title, txt_a1, txt_b1, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # ==========================================
        # CONFIGURAÇÕES DA JANELA
        # ==========================================

        self.geometry("500x650")
        self.title(title)
        self.resizable(False, False)

        # Tema
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Centralizar janela
        self.update_idletasks()

        largura = 500
        altura = 650

        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)

        self.geometry(f"{largura}x{altura}+{x}+{y}")

        # ==========================================
        # FRAME PRINCIPAL
        # ==========================================

        self.frame_principal = customtkinter.CTkFrame(
            self,
            corner_radius=20,
            fg_color="#1a1a1a"
        )

        self.frame_principal.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # ==========================================
        # TÍTULO
        # ==========================================

        self.label_title = customtkinter.CTkLabel(
            self.frame_principal,
            text="DISTÂNCIA\nUTM",
            font=("Arial", 28, "bold"),
            text_color="#ffffff"
        )

        self.label_title.pack(pady=(25, 5))

        # ==========================================
        # DESCRIÇÃO
        # ==========================================

        self.description = customtkinter.CTkLabel(
            self.frame_principal,
            text=(
                "Calcule a distância entre dois pontos\n"
                "utilizando suas coordenadas UTM."
            ),
            font=("Arial", 13),
            text_color="#aaaaaa",
            justify="center"
        )

        self.description.pack(pady=(0, 20))

        # ==========================================
        # PONTO A
        # ==========================================

        self.frame_pointA = customtkinter.CTkFrame(
            self.frame_principal,
            corner_radius=15,
            fg_color="#222222"
        )

        self.frame_pointA.pack(
            fill="x",
            padx=25,
            pady=8
        )

        self.label_pointA = customtkinter.CTkLabel(
            self.frame_pointA,
            text=txt_a1,
            font=("Arial", 17, "bold"),
            text_color="#60a5fa"
        )

        self.label_pointA.pack(pady=(12, 8))

        # Longitude / E
        self.longe_pointA = customtkinter.CTkEntry(
            self.frame_pointA,
            placeholder_text="Longitude (E) — Ponto A",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.longe_pointA.pack(pady=5)

        # Latitude / N
        self.lati_pointA = customtkinter.CTkEntry(
            self.frame_pointA,
            placeholder_text="Latitude (N) — Ponto A",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.lati_pointA.pack(pady=(5, 15))

        # ==========================================
        # PONTO B
        # ==========================================

        self.frame_pointB = customtkinter.CTkFrame(
            self.frame_principal,
            corner_radius=15,
            fg_color="#222222"
        )

        self.frame_pointB.pack(
            fill="x",
            padx=25,
            pady=8
        )

        self.label_pointB = customtkinter.CTkLabel(
            self.frame_pointB,
            text=txt_b1,
            font=("Arial", 17, "bold"),
            text_color="#34d399"
        )

        self.label_pointB.pack(pady=(12, 8))

        # Longitude / E
        self.longe_pointB = customtkinter.CTkEntry(
            self.frame_pointB,
            placeholder_text="Longitude (E) — Ponto B",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.longe_pointB.pack(pady=5)

        # Latitude / N
        self.lati_pointB = customtkinter.CTkEntry(
            self.frame_pointB,
            placeholder_text="Latitude (N) — Ponto B",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.lati_pointB.pack(pady=(5, 15))

        # ==========================================
        # BOTÃO
        # ==========================================

        self.button_utm = customtkinter.CTkButton(
            self.frame_principal,
            text="CALCULAR DISTÂNCIA",
            command=self.Calcular,
            width=350,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )

        self.button_utm.pack(pady=(15, 5))

        # ==========================================
        # RODAPÉ
        # ==========================================

        self.label_rodape = customtkinter.CTkLabel(
            self.frame_principal,
            text="Calculadora Cartográfica • UTM",
            font=("Arial", 10),
            text_color="#666666"
        )

        self.label_rodape.pack(
            side="bottom",
            pady=10
        )

    # ==========================================
    # CÁLCULO
    # ==========================================

    def Calcular(self):

        # Verificar campos vazios
        campos = [
            self.lati_pointA.get(),
            self.longe_pointA.get(),
            self.lati_pointB.get(),
            self.longe_pointB.get()
        ]

        if any(campo.strip() == "" for campo in campos):

            messagebox.showerror(
                "Erro",
                "Todos os campos devem ser preenchidos!"
            )

            return

        # Converter valores
        try:

            lati_a = float(
                self.lati_pointA.get().replace(",", ".")
            )

            longe_a = float(
                self.longe_pointA.get().replace(",", ".")
            )

            lati_b = float(
                self.lati_pointB.get().replace(",", ".")
            )

            longe_b = float(
                self.longe_pointB.get().replace(",", ".")
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite apenas valores numéricos.\n\n"
                "Exemplo:\n"
                "Latitude: 9584321.45\n"
                "Longitude: 543210.78"
            )

            return

        # ==========================================
        # CALCULAR DISTÂNCIA
        # ==========================================

        try:

            resultado = CartografiaCalculos.Calcular_utm(
                longeA=longe_a,
                latiA=lati_a,
                longeB=longe_b,
                latiB=lati_b
            )

            # Mostrar resultado caso a função retorne um valor
            if resultado is not None:

                messagebox.showinfo(
                    "Resultado",
                    f"Distância entre os pontos:\n\n"
                    f"{resultado:.2f} metros"
                )

        except Exception as erro:

            messagebox.showerror(
                "Erro no cálculo",
                f"Não foi possível realizar o cálculo.\n\n"
                f"Detalhes: {erro}"
            )
