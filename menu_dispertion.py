import customtkinter
from tkinter import messagebox
from Cartografia import CartografiaCalculos
class App_Dispersao(customtkinter.CTk):

    def __init__(self, title, fg_color=None, **kwargs):
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
            text="DISPERSÃO\nMAGNÉTICA",
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
                "Calcule a variação média da dispersão magnética\n"
                "entre dois anos."
            ),
            font=("Arial", 13),
            text_color="#aaaaaa",
            justify="center"
        )

        self.description.pack(pady=(0, 20))

        # ==========================================
        # VALOR INICIAL
        # ==========================================

        self.frame_inicial = customtkinter.CTkFrame(
            self.frame_principal,
            corner_radius=15,
            fg_color="#222222"
        )

        self.frame_inicial.pack(
            fill="x",
            padx=25,
            pady=8
        )

        self.label_inicial = customtkinter.CTkLabel(
            self.frame_inicial,
            text="VALOR INICIAL",
            font=("Arial", 17, "bold"),
            text_color="#60a5fa"
        )

        self.label_inicial.pack(pady=(12, 8))

        # Ano inicial
        self.entry_ano_inicial = customtkinter.CTkEntry(
            self.frame_inicial,
            placeholder_text="Ano inicial — Ex: 1980",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.entry_ano_inicial.pack(pady=5)

        # Valor inicial
        self.entry_valor_inicial = customtkinter.CTkEntry(
            self.frame_inicial,
            placeholder_text="Valor inicial — Ex: 23",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.entry_valor_inicial.pack(pady=(5, 15))

        # ==========================================
        # VALOR FINAL
        # ==========================================

        self.frame_final = customtkinter.CTkFrame(
            self.frame_principal,
            corner_radius=15,
            fg_color="#222222"
        )

        self.frame_final.pack(
            fill="x",
            padx=25,
            pady=8
        )

        self.label_final = customtkinter.CTkLabel(
            self.frame_final,
            text="VALOR FINAL",
            font=("Arial", 17, "bold"),
            text_color="#34d399"
        )

        self.label_final.pack(pady=(12, 8))

        # Ano final
        self.entry_ano_final = customtkinter.CTkEntry(
            self.frame_final,
            placeholder_text="Ano final — Ex: 2025",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.entry_ano_final.pack(pady=5)

        # Valor final
        self.entry_valor_final = customtkinter.CTkEntry(
            self.frame_final,
            placeholder_text="Valor final — Ex: 28",
            width=350,
            height=38,
            corner_radius=10,
            font=("Arial", 13)
        )

        self.entry_valor_final.pack(pady=(5, 15))

        # ==========================================
        # BOTÃO
        # ==========================================

        self.button_calcular = customtkinter.CTkButton(
            self.frame_principal,
            text="CALCULAR DISPERSÃO",
            command=self.Calcular,
            width=350,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )

        self.button_calcular.pack(pady=(15, 5))

        # ==========================================
        # RODAPÉ
        # ==========================================

        self.label_rodape = customtkinter.CTkLabel(
            self.frame_principal,
            text="Calculadora Cartográfica • Dispersão Magnética",
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

        # ==========================================
        # VERIFICAR CAMPOS VAZIOS
        # ==========================================

        campos = [
            self.entry_ano_inicial.get(),
            self.entry_valor_inicial.get(),
            self.entry_ano_final.get(),
            self.entry_valor_final.get()
        ]

        if any(campo.strip() == "" for campo in campos):

            messagebox.showerror(
                "Erro",
                "Todos os campos devem ser preenchidos!"
            )

            return

        # ==========================================
        # CONVERTER VALORES
        # ==========================================

        try:

            ano_inicial = int(
                self.entry_ano_inicial.get()
            )

            valor_inicial = float(
                self.entry_valor_inicial.get().replace(",", ".")
            )

            ano_final = int(
                self.entry_ano_final.get()
            )

            valor_final = float(
                self.entry_valor_final.get().replace(",", ".")
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite apenas valores numéricos.\n\n"
                "Exemplo:\n"
                "Ano inicial: 1980\n"
                "Valor inicial: 23\n"
                "Ano final: 2025\n"
                "Valor final: 28"
            )

            return

        # ==========================================
        # VALIDAR ANOS
        # ==========================================

        if ano_final == ano_inicial:

            messagebox.showerror(
                "Erro",
                "O ano inicial e o ano final não podem ser iguais."
            )

            return

        # ==========================================
        # CALCULAR DISPERSÃO
        # ==========================================

        try:

            resultado = CartografiaCalculos.calcular_dispersao_magnetica(
                valor_inicial=valor_inicial,
                valor_final=valor_final,
                ano_inicial=ano_inicial,
                ano_final=ano_final
            )

            # ==========================================
            # MOSTRAR RESULTADO
            # ==========================================

            messagebox.showinfo(
                "Resultado",
                f"Dispersão magnética:\n\n"
                f"{resultado:.4f}° por ano"
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro no cálculo",
                f"Não foi possível realizar o cálculo.\n\n"
                f"Detalhes: {erro}"
            )
