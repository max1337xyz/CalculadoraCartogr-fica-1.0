import customtkinter
from tkinter import messagebox

from Cartografia import CartografiaCalculos


class App_Passos(customtkinter.CTk):

    def __init__(self, title, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # ==========================================
        # CONFIGURAÇÕES DA JANELA
        # ==========================================

        self.geometry("450x500")
        self.title(title)
        self.resizable(False, False)

        # Tema
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Centralizar janela
        self.update_idletasks()

        largura = 450
        altura = 500

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
            text="CALCULADORA\nDE PASSOS",
            font=("Arial", 28, "bold"),
            text_color="#ffffff"
        )

        self.label_title.pack(pady=(30, 5))

        # ==========================================
        # DESCRIÇÃO
        # ==========================================

        self.description = customtkinter.CTkLabel(
            self.frame_principal,
            text=(
                "Descubra quantos passos são necessários\n"
                "para percorrer determinada distância."
            ),
            font=("Arial", 13),
            text_color="#aaaaaa",
            justify="center"
        )

        self.description.pack(pady=(0, 25))

        # ==========================================
        # CAMPO — TAMANHO DO PASSO
        # ==========================================

        self.label_Passo1 = customtkinter.CTkLabel(
            self.frame_principal,
            text="📏  Tamanho do passo",
            font=("Arial", 16, "bold"),
            text_color="#ffffff"
        )

        self.label_Passo1.pack(pady=(5, 5))

        self.entry_passo1 = customtkinter.CTkEntry(
            self.frame_principal,
            placeholder_text="Ex.: 0.75 metros",
            width=300,
            height=40,
            corner_radius=10,
            font=("Arial", 14)
        )

        self.entry_passo1.pack(pady=(0, 15))

        # ==========================================
        # CAMPO — DISTÂNCIA
        # ==========================================

        self.label_metros = customtkinter.CTkLabel(
            self.frame_principal,
            text="📐  Distância em metros",
            font=("Arial", 16, "bold"),
            text_color="#ffffff"
        )

        self.label_metros.pack(pady=(5, 5))

        self.entry_metros = customtkinter.CTkEntry(
            self.frame_principal,
            placeholder_text="Ex.: 100 metros",
            width=300,
            height=40,
            corner_radius=10,
            font=("Arial", 14)
        )

        self.entry_metros.pack(pady=(0, 25))

        # ==========================================
        # BOTÃO CALCULAR
        # ==========================================

        self.button_utm = customtkinter.CTkButton(
            self.frame_principal,
            text="CALCULAR",
            command=self.Calcular,
            width=300,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )
        self.button_passo = customtkinter.CTkButton(
            self.frame_principal,
            text="SABER TAMANHO DO PASSO",
            command=self.Comp_passo,
            width=300,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )

        self.button_utm.pack(pady=5)
        self.button_passo.pack(pady=5)
        # ==========================================
        # RODAPÉ
        # ==========================================

        self.label_rodape = customtkinter.CTkLabel(
            self.frame_principal,
            text="Calculadora Cartográfica • Passos",
            font=("Arial", 10),
            text_color="#666666"
        )

        self.label_rodape.pack(
            side="bottom",
            pady=12
        )
    # ==========================================
    # CÁLCULO PARA SABER O TAMANHO DO PASSO
    # ==========================================
    def Comp_passo(self):
        messagebox.showinfo("Informação","Para saber o tamanho do passo caminhe 100 metros contando quantos passos você fez \n e depois divida 100 Metros Pela Quantidade De Passsos")
    # ==========================================
    # CÁLCULO
    # ==========================================

    def Calcular(self):

        # Verifica se os campos estão vazios
        if (
            self.entry_metros.get().strip() == ""
            or self.entry_passo1.get().strip() == ""
        ):
            messagebox.showerror(
                "Erro",
                "Todos os campos devem ser preenchidos!"
            )
            return

        try:

            passo1 = float(
                self.entry_passo1.get().replace(",", ".")
            )

            metros = float(
                self.entry_metros.get().replace(",", ".")
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite apenas valores numéricos.\n"
                "Exemplo: 0.75"
            )

            return

        # Verifica valores inválidos
        if passo1 <= 0:
            messagebox.showerror(
                "Erro",
                "O tamanho do passo deve ser maior que zero."
            )
            return

        if metros <= 0:
            messagebox.showerror(
                "Erro",
                "A distância deve ser maior que zero."
            )
            return

        # Realiza cálculo
        resultado = CartografiaCalculos.calcular_passos(
            n1=passo1,
            metros=metros
        )

        # Caso a função retorne um resultado
        if resultado is not None:

            messagebox.showinfo(
                "Resultado",
                f"Você precisa de aproximadamente:\n\n"
                f"{resultado:.2f} passos"
            )
    

