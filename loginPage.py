import customtkinter as ctk
from PIL import Image

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, login_gestore_callback=None, login_pt_callback=None):
        """
        master: riferimento al MainView
        login_callback: funzione da chiamare quando si clicca "Login"
        """
        super().__init__(master)
        self.login_gestore_callback = login_gestore_callback
        self.login_pt_callback = login_pt_callback

        # Imposto layout a griglia per questa pagina (1 colonna, 3 righe)
        self.grid_rowconfigure(0, weight=1)  # spazio sopra il titolo
        self.grid_rowconfigure(1, weight=0)  # titolo
        self.grid_rowconfigure(2, weight=1)  # spazio fra titolo e bottoni
        self.grid_rowconfigure(3, weight=0)  # bottoni
        self.grid_rowconfigure(4, weight=1)  # spazio sotto i bottoni
        self.grid_columnconfigure(0, weight=1)

        # Titolo 
        title_label = ctk.CTkLabel(
            self,
            text="Login",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=1, column=0, pady=(20, 10), sticky="n")

        # Carico le icone (ridimensiono a 40×40)
        self.login_gestore_icon = ctk.CTkImage(
            Image.open("utils/assets/icon_gestore.png").resize((40, 40)),
            size=(40, 40)
        )
        self.login_pt_icon = ctk.CTkImage(
            Image.open("utils/assets/icon_pt.png").resize((40, 40)),
            size=(40, 40)
        )

        # Frame orizzontale per i due bottoni
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=3, column=0, pady=(10, 10))

        # Imposto griglia interna per disporre i due bottoni fianco a fianco
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        # Bottone "Gestore"
        gestore_login_button = ctk.CTkButton(
            master=button_frame,
            text="Gestore",
            image=self.login_gestore_icon,
            compound="top",
            width=140,
            height=140,
            corner_radius=16,
            fg_color="#3a7ff6",
            hover_color="#5596ff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.login_gestore_callback  # callback per navigare
        )
        gestore_login_button.grid(row=0, column=0, padx=20, sticky="nsew")

        # Bottone "Personal Trainer"
        pt_login_button = ctk.CTkButton(
            master=button_frame,
            text="Personal Trainer",
            image=self.login_pt_icon,
            compound="top",
            width=140,
            height=140,
            corner_radius=16,
            fg_color="#3a7ff6",
            hover_color="#5596ff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.login_pt_callback
        )
        pt_login_button.grid(row=0, column=1, padx=20, sticky="nsew")


