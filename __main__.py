import customtkinter
from menu_dist import *
from menu_passos import *
from menu_rumo import *
from menu_dispertion import * 


class App_Principal(customtkinter.CTk):

    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # =========================
        # CONFIGURAÇÕES DA JANELA
        # =========================

        self.geometry("420x600")
        self.title("Calculadora Cartográfica")
        self.resizable(False, False)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Centralizar janela
        #self.update_idletasks()

        largura = 420
        altura = 600

        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)

        self.geometry(f"{largura}x{altura}+{x}+{y}")

        # =========================
        # CONTAINER PRINCIPAL
        # =========================

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

        # =========================
        # TÍTULO
        # =========================

        self.lbl_titulo = customtkinter.CTkLabel(
            self.frame_principal,
            text="CALCULADORA\nCARTOGRÁFICA",
            font=("Arial", 27, "bold"),
            text_color="#f1f1f1"
        )

        self.lbl_titulo.pack(pady=(25, 5))

        # =========================
        # SUBTÍTULO
        # =========================

        self.lbl_subtitulo = customtkinter.CTkLabel(
            self.frame_principal,
            text="Ferramentas para cálculos cartográficos",
            font=("Arial", 13),
            text_color="#aaaaaa"
        )

        self.lbl_subtitulo.pack(pady=(0, 20))

        # =========================
        # BOTÃO DISTÂNCIA
        # =========================

        self.btn_dist = customtkinter.CTkButton(
            self.frame_principal,
            text="📍  Distância UTM",
            command=self.call_dist,
            width=300,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )

        self.btn_dist.pack(pady=6)

        # =========================
        # BOTÃO PASSOS
        # =========================

        self.btn_passos = customtkinter.CTkButton(
            self.frame_principal,
            text="👣  Calculadora de Passos",
            command=self.call_passos,
            width=300,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#059669",
            hover_color="#047857"
        )

        self.btn_passos.pack(pady=6)

        # =========================
        # BOTÃO DISPERÇÃO MAGNETICA
        # =========================

        self.btn_dispertion = customtkinter.CTkButton(
            self.frame_principal,
            text="🧭  Calculadora de Disperção magnética",
            command=self.call_dispertion,
            width=300,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#d97706",
            hover_color="#b45309"
        )

        self.btn_dispertion.pack(pady=6)

        # =========================
        # BOTÃO RUMO
        # =========================

        self.btn_rumo = customtkinter.CTkButton(
            self.frame_principal,
            text="🧭  Calculadora de Rumo",
            command=self.call_rumo,
            width=300,
            height=50,
            corner_radius=12,
            font=("Arial", 16, "bold"),
            fg_color="#9333ea",
            hover_color="#7e22ce"
        )

        self.btn_rumo.pack(pady=6)

        # =========================
        # RODAPÉ
        # =========================

        self.lbl_rodape = customtkinter.CTkLabel(
            self.frame_principal,
            text="Ferramentas Cartográficas • v1.0",
            font=("Arial", 11),
            text_color="#666666"
        )

        self.lbl_rodape.pack(
            side="bottom",
            pady=15
        )

    # =========================
    # ABRIR DISTÂNCIA
    # =========================

    def call_dist(self):

        self.destroy()

        dist = App_Dist(
            txt_b1="Ponto B",
            txt_a1="Ponto A",
            title="Calcular Distância UTM"
        )

        dist.mainloop()

    # =========================
    # ABRIR PASSOS
    # =========================

    def call_passos(self):

        self.destroy()

        passos = App_Passos(
            title="Calculadora de Passos"
        )

        passos.mainloop()

    # =========================
    # ABRIR DISPERÇÃO MAGNETICA
    # =========================

    def call_dispertion(self):
        self.destroy()
        dispertion = App_Dispersao(title="Calcular Disperção magnetica ")
        dispertion.mainloop()

    # =========================
    # ABRIR RUMO
    # =========================

    def call_rumo(self):
        self.destroy()
        app = App_Rumo(title="Calculadora Rumo")
        app.mainloop()



# =========================
# MAIN
# =========================

def main():

    main_app = App_Principal()
    main_app.mainloop()


if __name__ == "__main__":
    main()

