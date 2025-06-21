import customtkinter as ctk
from PIL import Image


class EntratePage(ctk.CTkFrame):
    def __init__(self, master, controller, back_callback, show_aggiungi_entrata_callback=None):
        super().__init__(master)

        self.controller = controller
        self.back_callback = back_callback
        self.show_aggiungi_entrata_callback = show_aggiungi_entrata_callback

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(
            master=self,
            width=200,
            corner_radius=0,
            fg_color="#1f1f2e"
        )
        self.sidebar_frame.grid(row=1, column=0, rowspan=2, sticky="nsew")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0, minsize=10)
        self.grid_columnconfigure(2, weight=1)

        # Bottone "Indietro"
        back_button = ctk.CTkButton(
            master=self,
            text="Indietro",
            width=100,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=back_callback
        )
        back_button.grid(row=0, column=0, pady=(10, 5), padx=10, sticky="")

        # Titolo centrale
        subtitle = ctk.CTkLabel(
            self,
            text="Gestione Entrate",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        subtitle.grid(row=0, column=2, pady=(10, 5), sticky="n", padx=(0, 0))

        # Scrollable Frame centrale per visualizzare entrate
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=0,
            fg_color="#2c313a",
            width=800,
            height=500
        )
        self.scrollable_frame.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Campo di ricerca (placeholder per futuro filtro)
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            master=self.sidebar_frame,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            placeholder_text="Cerca Entrata",
            placeholder_text_color="#ffffff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16),
            textvariable=self.search_var
        )
        self.search_entry.grid(row=1, column=0, padx=10, pady=(20, 10), sticky="ew")

        # Icona per bottone "Aggiungi"
        self.add_icon = ctk.CTkImage(
            Image.open("utils/assets/add_cliente.png"),
            size=(40, 40)
        )

        aggiungiEntrata_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16),
            command=show_aggiungi_entrata_callback,
            text="Aggiungi Entrata",
            image=self.add_icon
        )
        aggiungiEntrata_btn.grid(row=2, column=0, padx=10, pady=(20, 10), sticky="ew")

        self.sidebar_frame.grid_rowconfigure(3, weight=1)

    def visualizzaEntrate(self, entrate):
        """
        Visualizza la lista delle entrate nella scrollable_frame.
        """
        self.all_entrate = entrate

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for idx, e in enumerate(entrate):
            tipo = e.get("tipo", "N/A")  # fallback nel caso manchi
            label = ctk.CTkLabel(
                self.scrollable_frame,
                text=f"{e['data']} - €{e['importo']} - {e['descrizione']} - {tipo}",
                font=ctk.CTkFont(size=16),
                text_color="#ffffff",
                anchor="w"
            )
            label.grid(row=idx, column=0, sticky="ew", padx=10, pady=5)
            self.scrollable_frame.grid_rowconfigure(idx, weight=0)
