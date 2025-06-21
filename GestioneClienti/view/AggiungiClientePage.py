from datetime import datetime
import customtkinter as ctk
from PIL import Image
from GestioneClienti.controller.cliente_controller import ClienteController
from GestioneClienti.model.Cliente import Cliente, Sesso

class AggiungiClientePage(ctk.CTkFrame):
    def __init__(self, master, controller, back_callback):
        super().__init__(master)
        self.cliente = None  # Inizializzo cliente come None, sarà creato al salvataggio
        self.back_callback = back_callback
        self.controller = controller

        self.cert_var = ctk.BooleanVar()  # Variabile per il certificato medico

        # Frame principale scorrevole
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
            text="Aggiungi Cliente",
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

        # Frame dei dati cliente
        dati_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=10,
            fg_color="#3a3a4d"
        )
        dati_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        # Permetto alla colonna 0 e 1 di dati_frame di espandersi
        dati_frame.grid_columnconfigure(0, weight=1, uniform="col")
        dati_frame.grid_columnconfigure(1, weight=1, uniform="col")

        # Sezione "Dati del Cliente"
        dati_cliente_label = ctk.CTkLabel(
            master=dati_frame,
            text="Dati del Cliente",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#ffffff"
        )
        dati_cliente_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="n")

        # -------------------------
        # 1) Nome e Cognome (due colonne)
        # -------------------------
        nome_label = ctk.CTkLabel(
            master=dati_frame,
            text="Nome:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        nome_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")
        self.nome_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text="Inserisci nome",
            corner_radius=8
        )
        # Si estende in orizzontale
        self.nome_entry.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        cognome_label = ctk.CTkLabel(
            master=dati_frame,
            text="Cognome:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        cognome_label.grid(row=1, column=1, padx=20, pady=(10, 5), sticky="w")
        self.cognome_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text="Inserisci cognome",
            corner_radius=8
        )
        self.cognome_entry.grid(row=2, column=1, padx=20, pady=5, sticky="ew")

        # -------------------------
        # 2) Email e Telefono (due colonne)
        # -------------------------
        email_label = ctk.CTkLabel(
            master=dati_frame,
            text="Email:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        email_label.grid(row=3, column=0, padx=20, pady=(10, 5), sticky="w")
        self.email_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text="esempio@dominio.com",
            corner_radius=8
        )
        self.email_entry.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        telefono_label = ctk.CTkLabel(
            master=dati_frame,
            text="Telefono:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        telefono_label.grid(row=3, column=1, padx=20, pady=(10, 5), sticky="w")
        self.telefono_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text="+39 123 4567890",
            corner_radius=8
        )
        self.telefono_entry.grid(row=4, column=1, padx=20, pady=5, sticky="ew")

        # -------------------------
        # 3) Data di Nascita e Sesso (due colonne)
        # -------------------------
        data_nascita_label = ctk.CTkLabel(
            master=dati_frame,
            text="Data di Nascita:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        data_nascita_label.grid(row=5, column=0, padx=20, pady=(10, 5), sticky="w")
        self.data_nascita_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text="DD/MM/YYYY",
            corner_radius=8
        )
        self.data_nascita_entry.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

        sesso_label = ctk.CTkLabel(
            master=dati_frame,
            text="Sesso:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        sesso_label.grid(row=5, column=1, padx=20, pady=(10, 5), sticky="w")
        self.sesso_var = ctk.StringVar(value=Sesso.MASCHIO.value)
        self.sesso_menu = ctk.CTkOptionMenu(
            master=dati_frame,
            variable=self.sesso_var,
            values=[s.value for s in Sesso],
            corner_radius=8
        )
        self.sesso_menu.grid(row=6, column=1, padx=20, pady=5, sticky="ew")

        # Riservo la riga 7 per spaziatura flessibile
        dati_frame.grid_rowconfigure(7, weight=1)

        # Checkbox per il certificato medico
        self.cert_checkbox = ctk.CTkCheckBox(
            master=dati_frame,
            text="Certificato Medico",
            variable=self.cert_var,
            font=ctk.CTkFont(size=14),
        )
        self.cert_checkbox.grid(row=7, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="w")

        
        salva_button = ctk.CTkButton(
            master=self.content_frame,
            text="Salva Cliente",
            height=40,
            corner_radius=8,
            fg_color="#4a90e2",
            hover_color="#357ab8",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._on_salva
        )
        salva_button.grid(row=8, column=0, sticky="ew", padx=10, pady=(10, 20))

        self.content_frame.grid_rowconfigure(4, weight=0)

        self.error_label = ctk.CTkLabel(
            master=self.content_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff5555" 
            )
        self.error_label.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 0))



    def _on_salva(self):
        """
        Logica per salvare il cliente.
        Qui dovresti implementare la logica per validare i dati e salvarli nel database.
        """
        # Svuota la label degli errori all'inizio
        self.error_label.configure(text="")

        nome = self.nome_entry.get()
        cognome = self.cognome_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()
        data_nascita = self.data_nascita_entry.get()
        sesso = Sesso(self.sesso_var.get())
        certificatoMedico = self.cert_var.get()

        # Validazione e salvataggio del cliente
        if not nome or not cognome or not email:
            self.error_label.configure(text="Nome, Cognome ed Email sono obbligatori.")
            return

        cliente = Cliente(
            id=None,  # L'ID sarà generato automaticamente
            nome=nome,
            cognome=cognome,
            email=email,
            telefono=telefono,
            data_nascita=data_nascita,
            sesso=sesso.value,
            certificatoMedico=certificatoMedico
        )

        if self.controller.aggiungi_cliente(cliente):
            self.error_label.configure(text="")
            self.back_callback()
        else:
            self.error_label.configure(text="Errore durante il salvataggio del cliente. Riprova.")
            print("Errore durante il salvataggio del cliente.")
            return


