
import customtkinter as ctk
from PIL import Image

class HomePage(ctk.CTkFrame):
    def __init__(self, master, show_clienti_callback = None, show_contabilità_callback = None, logout_callback=None):
        """
        master: riferimento al MainView
        show_clienti_callback: funzione da chiamare quando si clicca "Clienti"
        show_contabilità_callback: funzione da chiamare quando si clicca "Contabilità"
        """
        super().__init__(master)

         # Header frame per il bottone Esci
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ne", padx=20, pady=10)
        header_frame.grid_columnconfigure(0, weight=1)

        esci_button = ctk.CTkButton(
            master=header_frame,
            text="Esci",
            width=80,
            height=36,
            corner_radius=8,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=logout_callback
        )
        esci_button.grid(row=0, column=1, sticky="e")

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
            text="Millennum Club",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=1, column=0, pady=(20, 10), sticky="n")

        # Carico le icone 
        self.clienti_icon = ctk.CTkImage(
            Image.open("utils/assets/clienti.png").resize((40, 40)),
            size=(40, 40)
        )
        self.contabilita_icon = ctk.CTkImage(
            Image.open("utils/assets/contabilità.png").resize((40, 40)),
            size=(40, 40)
        )

        # Frame orizzontale per i due bottoni
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=3, column=0, pady=(10, 10))

        # Imposto griglia interna per disporre i due bottoni fianco a fianco
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        # Bottone "Clienti"
        clienti_button = ctk.CTkButton(
            master=button_frame,
            text="Clienti",
            image=self.clienti_icon,
            compound="top",
            width=140,
            height=140,
            corner_radius=16,
            fg_color="#3a7ff6",
            hover_color="#5596ff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=show_clienti_callback  # callback per navigare
        )
        clienti_button.grid(row=0, column=0, padx=20, sticky="nsew")

        # Bottone "Contabilità"
        contabilità_button = ctk.CTkButton(
            master=button_frame,
            text="Contabilità",
            image=self.contabilita_icon,
            compound="top",
            width=140,
            height=140,
            corner_radius=16,
            fg_color="#3a7ff6",
            hover_color="#5596ff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=show_contabilità_callback
        )
        contabilità_button.grid(row=0, column=1, padx=20, sticky="nsew")