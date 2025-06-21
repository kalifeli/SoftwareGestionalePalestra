import customtkinter as ctk
from copy import deepcopy

from GestioneClienti.model.Cliente import Sesso

class ModificaClientePage(ctk.CTkFrame):
    def __init__(self, master, controller, cliente, back_callback):
        super().__init__(master)

        self.controller = controller
        self.cliente = cliente
        self.back_callback = back_callback

        self.content_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#2e2e3e"
        )
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configuro la colonna 0 di content_frame per espandersi
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.cert_var = ctk.BooleanVar(value=self.cliente.certificatoMedico if self.cliente else False)

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
            text="Modifica Dati Cliente",
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

        # Campi per modificare i dati del cliente

        # Nome 
        nome_label = ctk.CTkLabel(
            master=dati_frame,
            text="Nome:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        nome_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

        self.nome_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text= self.cliente.nome if self.cliente else "Inserisci nome",
            corner_radius=8
        )

        self.nome_entry.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        # Cognome
        cognome_label = ctk.CTkLabel(
            master=dati_frame,
            text="Cognome:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        cognome_label.grid(row=1, column=1, padx=20, pady=(10, 5), sticky="w")
        self.cognome_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text= self.cliente.cognome if self.cliente else "Inserisci cognome",
            corner_radius=8
        )
        self.cognome_entry.grid(row=2, column=1, padx=20, pady=5, sticky="ew")

        # Email

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

        # Telefono

        telefono_label = ctk.CTkLabel(
            master=dati_frame,
            text="Telefono:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        telefono_label.grid(row=3, column=1, padx=20, pady=(10, 5), sticky="w")

        self.telefono_entry = ctk.CTkEntry(
            master=dati_frame,
            placeholder_text= self.cliente.telefono if self.cliente else "Inserisci telefono",
            corner_radius=8
        )
        self.telefono_entry.grid(row=4, column=1, padx=20, pady=5, sticky="ew")

        # Data Nascita

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

        # Sesso

        sesso_label = ctk.CTkLabel(
            master=dati_frame,
            text="Sesso:",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        sesso_label.grid(row=5, column=1, padx=20, pady=(10, 5), sticky="w")
        self.sesso_var = ctk.StringVar(value=cliente.sesso)
        self.sesso_menu = ctk.CTkOptionMenu(
            master=dati_frame,
            variable=self.sesso_var,
            values=[s.value for s in Sesso],
            corner_radius=8
        )
        self.sesso_menu.grid(row=6, column=1, padx=20, pady=5, sticky="ew")

        # Checkbox per il certificato medico
        self.cert_checkbox = ctk.CTkCheckBox(
            master=dati_frame,
            text="Certificato Medico",
            variable=self.cert_var,
            font=ctk.CTkFont(size=14),
        )
        self.cert_checkbox.grid(row=7, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="w")
        dati_frame.grid_rowconfigure(7, weight=1)

        # Pulsante per salvare le modifiche
        salva_button = ctk.CTkButton(
            master=self.content_frame,
            text="Salva Modifiche",
            height=40,
            corner_radius=8,
            fg_color="#4a90e2",
            hover_color="#357ab8",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self._on_salva
        )
        salva_button.grid(row=8, column=0, sticky="ew", padx=10, pady=(10, 20))

        # Etichetta per errori
        self.error_label = ctk.CTkLabel(
            master=self.content_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff5555" 
        )
        self.error_label.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 0))

    def _on_salva(self):
        """
        Gestisce il salvataggio delle modifiche al cliente.
        """

        self.error_label.configure(text="") 

         # Recupero i dati dalle entry
        nome = self.nome_entry.get() or self.cliente.nome
        cognome = self.cognome_entry.get() or self.cliente.cognome
        email = self.email_entry.get() or self.cliente.email
        telefono = self.telefono_entry.get() or self.cliente.telefono
        data_nascita = self.data_nascita_entry.get() or self.cliente.data_nascita
        sesso = self.sesso_var.get()
        certificatoMedico = self.cert_var.get()

        try:
            # Creo una copia temporanea del cliente
            cliente_modificato = deepcopy(self.cliente)
            cliente_modificato.nome = nome
            cliente_modificato.cognome = cognome
            cliente_modificato.telefono = telefono
            cliente_modificato.email = email
            cliente_modificato.data_nascita = data_nascita
            cliente_modificato.sesso = sesso
            cliente_modificato.certificatoMedico = certificatoMedico

            # Prova a salvare la copia
            result = self.controller.modifica_cliente(cliente_modificato)

            if result:
            # Solo ora aggiorna l'oggetto in memoria
                self.cliente.nome = nome
                self.cliente.cognome = cognome
                self.cliente.telefono = telefono
                self.cliente.email = email
                self.cliente.data_nascita = data_nascita
                self.cliente.sesso = sesso
                self.cliente.certificatoMedico = certificatoMedico

                self.error_label.configure(text="Cliente aggiornato con successo.", text_color="#00ff00")
                self.back_callback()
            else:
                self.error_label.configure(text="Errore durante l'aggiornamento del cliente.")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")
            self.error_label.configure(text=f"Errore: {str(e)}")






        









