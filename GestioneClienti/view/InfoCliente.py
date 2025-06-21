import customtkinter as ctk
from PIL import Image

class InfoClientePage(ctk.CTkFrame):
    def __init__(self, master, cliente, controller, back_callback, aggiungi_abbonamento_callback=None, modifica_abbonamento_callback=None, modifica_cliente_callback=None):
        """
        master: riferimento al MainView
        cliente: oggetto cliente da visualizzare
        back_callback: funzione da chiamare per tornare alla pagina precedente
        """
        super().__init__(master)

        self.cliente = cliente
        self.controller = controller
        self.back_callback = back_callback
        self.aggiungi_abbonamento_callback = aggiungi_abbonamento_callback
        self.modifica_abbonamento_callback = modifica_abbonamento_callback
        self.modifica_cliente_callback = modifica_cliente_callback

        self.abbonamenti = self.controller.get_abbonamenti_by_cliente_id(cliente.id) if cliente else []

        self.grid_rowconfigure(0, weight=0)  # riga titolo
        self.grid_rowconfigure(1, weight=1)  # riga contenuto
        self.grid_columnconfigure(0, weight=1)

        # Titolo della pagina
        title_label = ctk.CTkLabel(
            self,
            text=f"Informazioni Cliente: {cliente.nome}",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=0, column=0, pady=(10, 5), sticky="n")

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
            command=self.back_callback
        )
        back_button.grid(row=0, column=0, pady=(10, 5), padx=(10, 0), sticky="w")

        # Contenuto delle informazioni del cliente
        self.content_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#3a3a4d",
            width=600,
            height=400
        )
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=0)
        self.content_frame.grid_rowconfigure(1, weight=0)
        self.content_frame.grid_rowconfigure(2, weight=1)
        self.content_frame.grid(row=1, column=0, padx=20, pady=(5, 20), sticky="nsew")

        # Frame per le informazioni del cliente
        info_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=10,
            fg_color="#44445a"
        )
        info_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        info_frame.grid_columnconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)

        # Etichette per le informazioni del cliente

        labels = [
            ("Nome:", cliente.nome),
            ("Cognome:", cliente.cognome),
            ("Email:", cliente.email),
            ("Telefono:", cliente.telefono),
            ("Data di Nascita:", cliente.data_nascita.strftime('%d/%m/%Y') if hasattr(cliente.data_nascita, 'strftime') else str(cliente.data_nascita)),
            ("Sesso:", cliente.sesso.value if hasattr(cliente.sesso, 'value') else str(cliente.sesso)),
            ("Certificato Medico:", "Sì" if cliente.certificatoMedico else "No"),
        ]

        for idx, (label_text, value) in enumerate(labels):
            label = ctk.CTkLabel(
            info_frame,
            text=label_text,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#cccccc"
            )
            label.grid(row=idx, column=0, sticky="w", padx=(10, 5), pady=5)

            value_label = ctk.CTkLabel(
            info_frame,
            text=value,
            font=ctk.CTkFont(size=16),
            text_color="#ffffff"
            )
            value_label.grid(row=idx, column=1, sticky="w", padx=(0, 10), pady=5)

        # Sezione per gli abbonamenti
        self.sezione_abbonamenti = SezioneAbbonamento(
            master=self.content_frame,
            abbonamenti=self.abbonamenti,
            cliente=self.cliente,
            controller=self.controller,
            aggiungi_abbonamento_callback=self.aggiungi_abbonamento_callback,
            modifica_abbonamento_callback = self.modifica_abbonamento_callback
        )
        self.sezione_abbonamenti.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 20))


        self.elimina_cliente_button = ctk.CTkButton(
            master=self.content_frame,
            text="Elimina Cliente",
            width=150,
            height=40,
            corner_radius=8,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=lambda: self.on_elimina_cliente()
        )

        self.modifica_cliente_button = ctk.CTkButton(
            master=self.content_frame,
            text="Modifica Cliente",
            width=150,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=self.modifica_cliente_callback
        )
        self.modifica_cliente_button.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=(10, 0))
        self.elimina_cliente_button.grid(row=3, column=1, sticky="w", padx=(10, 0), pady=(10, 0))

        self.error_label = ctk.CTkLabel(
            master=self.content_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff5555" 
            )
        self.error_label.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 0))

    def on_elimina_cliente(self):
        """
        Logica per eliminare il cliente.
        """
        # Svuota la label degli errori all'inizio
        self.error_label.configure(text="")

        if self.controller.elimina_cliente(self.cliente.id):
            self.error_label.configure(text="")
            self.back_callback()
        else:
            self.error_label.configure(text="Errore nell'eliminazione del cliente. Riprova.")

class AbbonamentoCard(ctk.CTkFrame):
    def __init__(self, master, abbonamento, cliente, elimina_abbonamento=None, modifica_abbonamento=None):
        super().__init__(master)
        self.abbonamento = abbonamento
        self.elimina_callback = elimina_abbonamento
        self.modifica_callback = modifica_abbonamento

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Mostra le specifiche dell'abbonamento in un frame orizzontale
        specifiche_frame = ctk.CTkFrame(
            master=self,
            corner_radius=8,
            fg_color="#44445a"
        )
        specifiche_frame.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        specifiche_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        specifiche_frame.grid_rowconfigure(0, weight=1)


        self.id_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"ID: {self.abbonamento.id}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff"
        )
        self.id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.corso_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Corso: {self.abbonamento.corso}" if self.abbonamento.corso else f"Pacchetto: {self.abbonamento.pacchetto}",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.corso_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.data_inizio_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Inizio: {self.abbonamento.data_inizio}",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.data_inizio_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.data_fine_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Fine: {self.abbonamento.data_fine}",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.data_fine_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        self.prezzo_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Prezzo: {self.abbonamento.prezzo} €",
            font=ctk.CTkFont(size=14),
            text_color="#ffffff"
        )
        self.prezzo_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")

        self.saldato_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Pagato: {self.abbonamento.saldato}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff"
        )
        self.saldato_label.grid(row=0, column=5, padx=10, pady=(5, 0), sticky="w")

        self.stato_label = ctk.CTkLabel(
            master=specifiche_frame,
            text=f"Stato: {self.abbonamento.stato}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff"
        )
        self.stato_label.grid(row=0, column=6, padx=10, pady=(5, 0), sticky="w")

        self.bottone_elimina = ctk.CTkButton(
            master=self,
            text="Elimina",
            width=70,
            height=30,
            corner_radius=8,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=lambda:self.elimina_callback(self.abbonamento.id)
        )
        self.bottone_elimina.grid(row=0, column=7, padx=10, pady=(5, 10), sticky="e")

        self.bottone_modifica = ctk.CTkButton(
            master=self,
            text="Modifica",
            width=70,
            height=30,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=lambda:self.modifica_callback(cliente ,self.abbonamento)
        )
        self.bottone_modifica.grid(row=0, column=6, padx=10, pady=(5, 10), sticky="e")

class SezioneAbbonamento(ctk.CTkFrame):
    def __init__(self, master, abbonamenti=None, cliente=None, controller=None, aggiungi_abbonamento_callback=None, modifica_abbonamento_callback=None):
        super().__init__(master, corner_radius=10)
        self.abbonamenti = abbonamenti if abbonamenti else []
        self.cliente = cliente
        self.controller = controller
        self.aggiungi_abbonamento_callback = aggiungi_abbonamento_callback
        self.modifica_abbonamento_callback= modifica_abbonamento_callback

        self.controller.controlla_scadenze_abbonamenti(self.abbonamenti)

        self.build_ui()

    def build_ui(self):
            
            for widget in self.winfo_children():
                widget.destroy()

            # Titolo e bottone in una riga orizzontale
            header_frame = ctk.CTkFrame(self, fg_color="transparent")
            header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
            header_frame.grid_columnconfigure(0, weight=1)
            header_frame.grid_columnconfigure(1, weight=0)  # il bottone non si espande

            titolo = ctk.CTkLabel(
                master=header_frame,
                text="Abbonamenti",
                font=ctk.CTkFont(size=20, weight="bold"),
                text_color="#ffffff"
            )
            titolo.grid(row=0, column=0, sticky="w")

            aggiungi_abbonamento_button = ctk.CTkButton(
                master=header_frame,
                text="Aggiungi Abbonamento",
                width=200,
                height=40,
                corner_radius=8,
                fg_color="#3a3a4d",
                hover_color="#4a4a5d",
                text_color="#ffffff",
                font=ctk.CTkFont(size=14),
                command=self.aggiungi_abbonamento_callback
            )
            aggiungi_abbonamento_button.grid(row=0, column=1, sticky="e", padx=(10, 0))

            # Area abbonamenti/cards
            cards_frame = ctk.CTkFrame(self, fg_color="transparent")
            cards_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
            cards_frame.grid_columnconfigure(0, weight=1)

            if not self.abbonamenti:
                no_abbonamenti_label = ctk.CTkLabel(
                    master=cards_frame,
                    text="Nessun abbonamento disponibile.",
                    font=ctk.CTkFont(size=16),
                    text_color="#ffffff"
                )
                no_abbonamenti_label.grid(row=0, column=0, padx=10, pady=5, sticky="n")
            else:
                for idx, abbonamento in enumerate(self.abbonamenti):
                    elimina_callback = lambda ab_id=abbonamento.id: self.elimina_e_aggiorna(ab_id)
                    card = AbbonamentoCard(
                        master=cards_frame,
                        abbonamento=abbonamento,
                        cliente= self.cliente,
                        elimina_abbonamento=elimina_callback,
                        modifica_abbonamento=self.modifica_abbonamento_callback
                    )
                    card.grid(row=idx, column=0, padx=0, pady=5, sticky="ew")

    def refresh_abbonamenti(self):
        # Aggiorna la lista abbonamenti dal controller
        self.abbonamenti = self.controller.get_abbonamenti_by_cliente_id(self.cliente.id)
        self.build_ui()

    def elimina_e_aggiorna(self, abbonamento_id):
        success = self.controller.elimina_abbonamento(abbonamento_id)
        if success:
            self.refresh_abbonamenti()

