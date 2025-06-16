import customtkinter as ctk
from datetime import date

from GestioneClienti.model.SchedaCliente import SchedaCliente
class AggiungiSchedaClientePage(ctk.CTkFrame):
    def __init__(self, master, pt_controller, cliente_id, back_callback=None):
        super().__init__(master)

        self.cliente_id = cliente_id
        self.back_callback = back_callback
        self.pt_controller = pt_controller

        #Frame principale scorrevole
        self.content_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#2e2e3e"
        )
        self.content_frame.pack(fill="both", expand=True)

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
            text="Aggiungi Scheda Cliente",
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

        # Form per l'inserimento dei dati della scheda di un cliente 

        form_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=10,
            fg_color="#3a3a4d"
        )
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 20))
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # Etichette e campi di input per i dati della scheda

        # Data Creazione
        ctk.CTkLabel(
            master=form_frame,
            text="Data Creazione: ",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            master=form_frame,
            text= date.today().strftime("%d-%m-%Y"),
            font=ctk.CTkFont(size=16),
            text_color="#ffffff"
        ).grid(row=1, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Data Rilevazione
        ctk. CTkLabel(
            master=form_frame,
            text="Data Rilevazione: ",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=0, column=1, sticky="ew", padx=10, pady=(10, 5))


        ctk. CTkLabel(
            master=form_frame,
            text= date.today().strftime("%d-%m-%Y"),
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=1, column=1, sticky="ew", padx=10, pady=(10, 5))

        # Peso

        ctk.CTkLabel(
            master=form_frame,
            text="Peso:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=(10, 5))

        self.peso_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Kg",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.peso_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Altezza

        ctk.CTkLabel(
            master=form_frame,
            text="Altezza:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=2, column=1, sticky="w", padx=10, pady=(10, 5))

        self.altezza_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.altezza_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=(10, 5))

        # Massa Muscolare

        ctk.CTkLabel(
            master=form_frame,
            text="Massa Muscolare:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=4, column=0, sticky="w", padx=10, pady=(10, 5))

        self.massa_muscolare_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Kg",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.massa_muscolare_entry.grid(row=5, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Massa grassa

        ctk.CTkLabel(
            master=form_frame,
            text="Massa Grassa:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=4, column=1, sticky="w", padx=10, pady=(10, 5))

        self.massa_grassa_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Kg",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.massa_grassa_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=(10, 5))

        # bmi

        ctk.CTkLabel(
            master=form_frame,
            text="bmi:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=6, column=0, sticky="w", padx=10, pady=(10, 5))

        self.bmi_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="peso / (altezza * 2)",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.bmi_entry.grid(row=7, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Note

        ctk.CTkLabel(
            master=form_frame,
            text="Note",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=8, column=0, columnspan = 2,sticky="w", padx=10, pady=(10, 5))

        self.note_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Cosa devi ricordare?",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.note_entry.grid(row=9, column=0, columnspan = 2, sticky="ew", padx=10, pady=(10, 5))

        # Misure

        ctk.CTkLabel(
            master=form_frame,
            text="Misure",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        ).grid(row=10, column=0, columnspan = 2, sticky="n", padx=10, pady=(10, 5))

        # bicipite

        ctk.CTkLabel(
            master=form_frame,
            text="Bicipite",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=11, column=0,sticky="w", padx=10, pady=(10, 5))

        self.misura_bicipite_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.misura_bicipite_entry.grid(row=12, column=0, sticky="ew", padx=10, pady=(10, 5))

        # coscia

        ctk.CTkLabel(
            master=form_frame,
            text="coscia",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=11, column=1,sticky="w", padx=10, pady=(10, 5))

        self.misura_coscia_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.misura_coscia_entry.grid(row=12, column=1, sticky="ew", padx=10, pady=(10, 5))

        # fianchi

        ctk.CTkLabel(
            master=form_frame,
            text="fianchi",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=13, column=0,sticky="w", padx=10, pady=(10, 5))

        self.misura_fianchi_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.misura_fianchi_entry.grid(row=14, column=0, sticky="ew", padx=10, pady=(10, 5))
        # petto

        ctk.CTkLabel(
            master=form_frame,
            text="petto",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=13, column=1,sticky="w", padx=10, pady=(10, 5))

        self.misura_petto_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.misura_petto_entry.grid(row=14, column=1, sticky="ew", padx=10, pady=(10, 5))

        # polpaccio

        ctk.CTkLabel(
            master=form_frame,
            text="polpaccio",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=15, column=0,sticky="w", padx=10, pady=(10, 5))

        self.misura_polpaccio_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.misura_polpaccio_entry.grid(row=16, column=0, sticky="ew", padx=10, pady=(10, 5))

        # vita

        ctk.CTkLabel(
            master=form_frame,
            text="vita",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=15, column=1,sticky="w", padx=10, pady=(10, 5))

        self.misura_vita_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.misura_vita_entry.grid(row=16, column=1, sticky="ew", padx=10, pady=(10, 5))


        self.salva_button = ctk.CTkButton(
            master=form_frame,
            text="Salva scheda",
            height=36,
            corner_radius=8,
            fg_color="#4a4a5d",
            hover_color="#5a5a6d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command= self.on_salva_scheda
        )
        self.salva_button.grid(row=17, column=0, columnspan = 2, sticky="ew", padx=10, pady=(10, 5))

        self.error_label = ctk.CTkLabel(
            master=form_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff5555"  # rosso per gli errori
            )
        self.error_label.grid(row=18, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 0))

    def safe_float(self, s: str, default: float = None) -> float:
        """
        Prova a convertire s in float,
        se s è vuota o non è un numero ritorna default (None di default)
        """
        s = s.replace(",", ".").strip()
        try:
            return float(s) if s != "" else default
        except (ValueError, TypeError):
            return default

    def on_salva_scheda(self):
        peso = self.safe_float(self.peso_entry.get())
        altezza = self.safe_float(self.altezza_entry.get())
        massa_muscolare = self.safe_float(self.massa_muscolare_entry.get())
        massa_grassa = self.safe_float(self.massa_grassa_entry.get())
        note = self.note_entry.get().strip()

        # Calcolo BMI solo se peso e altezza sono validi
        if peso is not None and altezza is not None and peso > 0 and altezza > 0:
            h_m = altezza / 100
            bmi = round(peso / (h_m * h_m), 1)
        else:
            bmi = None

        # dict per le misure includendo solo i campi compilati
        misure = {}
        for key, entry in [
            ("bicipite", self.misura_bicipite_entry),
            ("coscia", self.misura_coscia_entry),
            ("fianchi", self.misura_fianchi_entry),
            ("petto", self.misura_petto_entry),
            ("polpaccio", self.misura_polpaccio_entry),
            ("vita", self.misura_vita_entry),
        ]:
            val = self.safe_float(entry.get())
            if val is not None:
                misure[key] = val

        scheda = SchedaCliente(
            id_cliente=self.cliente_id,
            peso=peso,
            altezza=altezza,
            massa_muscolare=massa_muscolare,
            massa_grassa=massa_grassa,
            bmi=bmi,
            note=note,
            data_rilevazione=date.today().strftime("%d-%m-%Y"),
            data_creazione=date.today().strftime("%d-%m-%Y"),
            misure=misure
        )

        if self.pt_controller.add_scheda_cliente(self.cliente_id, scheda):
            if self.back_callback:
                self.back_callback()
        else:
            self.error_label.configure(text="Errore durante il salvataggio della scheda.")


















