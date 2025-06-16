import customtkinter as ctk
from PIL import Image
from GestioneClienti.model.Abbonamento import Abbonamento, StatoAbbonamento

class AggiungiAbbonamentoPage(ctk.CTkFrame):
    def __init__(self, master, cliente, controller=None, back_callback=None):
        super().__init__(master)

        self.controller = controller
        self.back_callback = back_callback
        self.cliente = cliente  # Il cliente a cui aggiungere l'abbonamento
        self.corsi = self.controller.get_all_corsi() # Lista dei corsi disponibili
        self.pacchetti = self.controller.get_all_pacchetti() # Lista dei pacchetti disponibili
        print("Pacchetti caricati:", self.pacchetti)

        #Frame principale scorrevole
        self.content_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#2e2e3e"
        )
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configuro la colonna 0 di content_frame per espandersi
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Header (titolo + Indietro) su un'unica riga
        header_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=0,
            fg_color="transparent"
        )
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 20))
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=0)

        titolo = ctk.CTkLabel(
            master=header_frame,
            text="Aggiungi Abbonamento",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        titolo.grid(row=0, column=0, sticky="w")

        back_button = ctk.CTkButton(
            master=header_frame,
            text="« Indietro",
            height=36,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=self.back_callback
        )
        back_button.grid(row=0, column=1, sticky="e")

        # Form per l'inserimento dei dati dell'abbonamento 

        form_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=10,
            fg_color="#3a3a4d"
        )
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 20))
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # Etichette e campi di input per i dati dell'abbonamento

        ctk.CTkLabel(
            master=form_frame,
            text="Data Inizio:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))

        self.data_inizio_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="GG/MM/AAAA",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.data_inizio_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            master=form_frame,
            text="Data Fine:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=0, column=1, sticky="w", padx=10, pady=(10, 5))

        self.data_fine_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="GG/MM/AAAA",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.data_fine_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            master=form_frame,
            text="Tipo Abbonamento:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=(10, 5))

        selection_options = ["Pacchetto", "Corso"]

        self.tipo_var = ctk.StringVar(value=selection_options[0])
        self.tipo_menu = ctk.CTkOptionMenu(
            master=form_frame,
            variable=self.tipo_var,
            values=selection_options,
            command=self.on_selection_change,
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14)
        )
        self.tipo_menu.grid(row=3, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Secondo menu a tendina per mostrare corsi o pacchetti (inizialmente vuoto)
        self.sotto_opzioni_var = ctk.StringVar(value="Seleziona")
        self.sotto_opzioni_menu = ctk.CTkOptionMenu(
            master=form_frame,
            variable=self.sotto_opzioni_var,
            values=[],  # verrà aggiornato in on_selection_change
            font=ctk.CTkFont(size=14),
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.sotto_opzioni_menu.grid(row=3, column=1, sticky="ew", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            master=form_frame,
            text="Prezzo:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=4, column=0, sticky="w", padx=10, pady=(10, 5))

        self.prezzo_var = ctk.StringVar(value="€ 0")
        self.prezzo_label = ctk.CTkLabel(
            master=form_frame,
            textvariable=self.prezzo_var,
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.prezzo_label.grid(row=5, column=0, sticky="ew", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            master=form_frame,
            text="Saldato:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=4, column=1, sticky="w", padx=10, pady=(10, 5))

        selection_options_saldato = ["Sì", "No"]
        self.saldato_var = ctk.StringVar(value=selection_options_saldato[0])
        self.saldato_menu = ctk.CTkOptionMenu(
            master=form_frame,
            variable=self.saldato_var,
            values=selection_options_saldato,
            font=ctk.CTkFont(size=14),
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.saldato_menu.grid(row=5, column=1, sticky="ew", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            master=form_frame,
            text="Stato:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=6, column=0, sticky="w", padx=10, pady=(10, 5))

        # Ottengo le opzioni dalla Enum
        stato_options = [stato.value for stato in StatoAbbonamento]

        self.stato_var = ctk.StringVar(value=stato_options[0])
        self.stato_menu = ctk.CTkOptionMenu(
            master=form_frame,
            variable=self.stato_var,
            values=stato_options,
            font=ctk.CTkFont(size=14),
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.stato_menu.grid(row=7, column=0, sticky="ew", padx=10, pady=(10, 5))

        self.salva_button = ctk.CTkButton(
            master=form_frame,
            text="Salva Abbonamento",
            height=36,
            corner_radius=8,
            fg_color="#4a4a5d",
            hover_color="#5a5a6d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command= self.on_salva_abbonamento
        )
        self.salva_button.grid(row=8, column=0, sticky="ew", padx=10, pady=(10, 5))

        self.error_label = ctk.CTkLabel(
            master=form_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff5555"  # rosso per gli errori
            )
        self.error_label.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 0))

    def on_selection_change(self, scelta):
        if scelta == "Corso":
            self.sotto_opzioni_valori = [corso.nome for corso in self.corsi] if self.corsi else []
            self.sotto_opzioni_prezzi = [corso.prezzo for corso in self.corsi] if self.corsi else []
        elif scelta == "Pacchetto":
            self.sotto_opzioni_valori = [pacchetto.nome for pacchetto in self.pacchetti] if self.pacchetti else []
            self.sotto_opzioni_prezzi = [pacchetto.prezzo for pacchetto in self.pacchetti] if self.pacchetti else []
        else:
            self.sotto_opzioni_valori = []
            self.sotto_opzioni_prezzi = []

        self.sotto_opzioni_menu.configure(values=self.sotto_opzioni_valori, command=self.on_sotto_opzione_change)

        if self.sotto_opzioni_valori:
            self.sotto_opzioni_var.set(self.sotto_opzioni_valori[0])
            self.on_sotto_opzione_change(self.sotto_opzioni_valori[0])
        else:
            self.sotto_opzioni_var.set("Seleziona")
            self.prezzo_var.set("€ 0")

    def on_sotto_opzione_change(self, scelta):
        try:
            idx = self.sotto_opzioni_valori.index(scelta)
            prezzo = self.sotto_opzioni_prezzi[idx]
            self.prezzo_var.set(f"€ {prezzo}")
        except (ValueError, IndexError):
            self.prezzo_var.set("€ 0")

    def on_salva_abbonamento(self):
        data_inizio = self.data_inizio_entry.get()
        data_fine = self.data_fine_entry.get()
        tipo = self.tipo_var.get()
        sotto_opzione = self.sotto_opzioni_var.get()
        prezzo = float(self.prezzo_var.get().replace("€ ", ""))
        saldato = self.saldato_var.get()
        stato = self.stato_var.get()

        abbonamento = Abbonamento(
            id_cliente=self.cliente.id,
            corso=sotto_opzione if tipo == "Corso" else "",
            pacchetto=sotto_opzione if tipo == "Pacchetto" else "",
            data_inizio=data_inizio,
            data_fine=data_fine,
            prezzo=prezzo,
            saldato=saldato,
            stato=stato
        )

        if self.controller.add_abbonamento_to_cliente(self.cliente.id, abbonamento):
            self.error_label.configure(text="Abbonamento aggiunto con successo!", text_color="#00ff00", )
            self.back_callback()
        else:
            self.error_label.configure(text="Errore nell'aggiunta dell'abbonamento.", text_color="#ff5555")
            print(f"Errore nell'aggiunta dell'abbonamento per il cliente")
