import customtkinter
from Cartografia import  *
class App_Rumo(customtkinter.CTk):
    def __init__(self,title, fg_color = None, **kwargs):
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
            text="CALCULADORA\nDE RUMO",
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
                "Coloque o Azimute Para Descobrir o rumo\n"
                
            ),
            font=("Arial", 13),
            text_color="#aaaaaa",
            justify="center"
        )
        self.directions= customtkinter.CTkLabel(
            self.frame_principal,
            text=(
                "0-90 Graus = NE\n90-180 Graus = SE\n180-270 Graus = SW\n270-360 Graus  = NW "
        
            ),
            font=("Arial", 13),
            text_color="#0a6e34",
            justify="center"
        )
        self.directions.pack(pady=10)

       

        
        self.description.pack(pady=(0, 25))
        # ==========================================
        # CAMPO — AZIMUTE
        # ==========================================
        
        self.label_azimute= customtkinter.CTkLabel(
            self.frame_principal,
            text="📏  Azimute",
            font=("Arial", 16, "bold"),
            text_color="#ffffff"
        )
        
        
        
        self.entry_azimute = customtkinter.CTkEntry(
            self.frame_principal,
            placeholder_text="Ex.: 60 Graus",
            width=300,
            height=40,
            corner_radius=10,
            font=("Arial", 14)
        )
        self.option_dir = customtkinter.CTkOptionMenu(
            self.frame_principal,values=["NE","SE","SW","NW"]
        )
        self.dir_label= customtkinter.CTkLabel(
            self.frame_principal,
            text="📐 Informe os Parametros De Direção",
            font=("Arial", 16, "bold"),
            text_color="#ffffff"
        )

        # ==========================================
        # CAMPO — PACKS
        # ==========================================
        self.entry_azimute.pack(pady=10)
        self.dir_label.pack(pady=10)
        self.option_dir.pack(pady=10)
        self.button = customtkinter.CTkButton(
            self.frame_principal,
            text="Clica em mim",
            command=self.Calcular
        )

        self.button.pack(pady=10)
    def Calcular(self):

        # Verifica se o campo está vazio
        if self.entry_azimute.get().strip() == "":
            messagebox.showerror(
                "Erro",
                "Digite o valor do azimute!"
            )
            return

        # Tenta converter o azimute
        try:
            azimute = float(
                self.entry_azimute.get().replace(",", ".")
            )

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Digite apenas um valor numérico para o azimute!"
            )
            return

        # Verifica o intervalo do azimute
        if azimute < 0 or azimute > 360:
            messagebox.showerror(
                "Erro",
                "O azimute deve estar entre 0° e 360°!"
            )
            return

        # Pega a direção selecionada
        direction = self.option_dir.get()

        # Calcula o rumo
        CartografiaCalculos.calcular_rumo(
            azimute=azimute,
            direction=direction
    )
