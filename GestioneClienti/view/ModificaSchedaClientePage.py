from copy import deepcopy
import customtkinter as ctk
from datetime import date
from GestioneClienti.model.SchedaCliente import SchedaCliente

class ModificaSchedaClientePage(ctk.CTkFrame):
    def __init__(self, master, pt_controller, scheda_cliente: SchedaCliente, back_callback=None):
        super().__init__(master)

        self.back_callback = back_callback
        self.pt_controller = pt_controller
        self.scheda = scheda_cliente

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
            text= self.scheda.data_creazione,
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
            text= self.scheda.data_rilevazione,
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
            placeholder_text= f"{self.scheda.peso} Kg",
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
            placeholder_text= f"{self.scheda.altezza} cm",
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
            placeholder_text=f"{self.scheda.massa_muscolare} Kg",
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
            placeholder_text=f"{self.scheda.massa_grassa} Kg",
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
            placeholder_text=self.scheda.bmi,
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
            placeholder_text= self.scheda.note,
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
            placeholder_text=str(self.scheda.misure.get("bicipite")),
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
            placeholder_text=str(self.scheda.misure.get("coscia")),
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
            placeholder_text=str(self.scheda.misure.get("fianchi")),
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
            placeholder_text=str(self.scheda.misure.get("petto")),
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
            placeholder_text= str(self.scheda.misure.get("polpaccio")),
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
            placeholder_text= str(self.scheda.misure.get("vita")),
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

        #recupero i dati dalle entry
        peso = self.safe_float(self.peso_entry.get()) or self.scheda.peso
        altezza = self.safe_float(self.altezza_entry.get()) or self.scheda.altezza
        massa_muscolare = self.safe_float(self.massa_muscolare_entry.get()) or self.scheda.massa_muscolare
        massa_grassa = self.safe_float(self.massa_grassa_entry.get()) or self.scheda.massa_grassa
        note = self.note_entry.get().strip() or self.scheda.note
        data_rilevazione = date.today().strftime("%d-%m-%Y")

        # Calcolo BMI solo se peso e altezza sono validi
        if peso is not None and altezza is not None and peso > 0 and altezza > 0:
            h_m = altezza / 100
            bmi = round(peso / (h_m * 2), 1)
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
            testo = entry.get().strip()
            if testo == "":
                # Se il campo è vuoto, mantiene il valore precedente (se esiste)
                if self.scheda.misure and key in self.scheda.misure:
                    misure[key] = self.scheda.misure[key]
            else:
                val = self.safe_float(testo)
                if val is not None:
                    misure[key] = val

        try:
            # Creo una copia temporanea della scheda
            scheda_modificata = deepcopy(self.scheda)
            scheda_modificata.peso = peso
            scheda_modificata.altezza = altezza
            scheda_modificata.data_rilevazione = data_rilevazione
            scheda_modificata.bmi = bmi
            scheda_modificata.massa_muscolare = massa_muscolare
            scheda_modificata.massa_grassa = massa_grassa
            scheda_modificata.note = note
            scheda_modificata.misure = misure

            # Provo a salvare
            result = self.pt_controller.update_scheda_cliente(scheda_modificata)

            if result:
                # aggiorno ora l'oggetto in memoria
                self.scheda.peso = peso
                self.scheda.altezza = altezza
                self.scheda.data_rilevazione = data_rilevazione
                self.scheda.bmi = bmi
                self.scheda.massa_muscolare = massa_muscolare
                self.scheda.massa_grassa = massa_grassa
                self.scheda.note = note
                self.scheda.misure

                self.back_callback()
            else:
                self.error_label.configure(text="Errore durante l'aggiornamento della scheda del cliente.", text_color="#ff5555")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")
            self.error_label.configure(text=f"Errore: {str(e)}", text_color="#ff5555")





           


















