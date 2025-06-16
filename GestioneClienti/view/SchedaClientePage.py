import customtkinter as ctk

class SchedaClientePage(ctk.CTkFrame):
    def __init__(self, master, pt_controller, cliente_id, pt, back_callback, aggiungi_scheda_callback, modifica_scheda_callback):
        """
        master: riferimento al MainView
        scheda: oggetto SchedaCliente da visualizzare
        back_callback: funzione da chiamare per tornare alla pagina precedente
        """
        super().__init__(master)

        self.back_callback = back_callback
        self.pt = pt
        self.pt_controller = pt_controller
        self.scheda = pt_controller.get_scheda_cliente(cliente_id)
        self.aggiungi_scheda_callback = aggiungi_scheda_callback
        self.modifica_scheda_callback = modifica_scheda_callback

        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#2e2e3e"
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=(0,20))

        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid_rowconfigure(0, weight=0)
        self.scroll_frame.grid_rowconfigure(1, weight=1)

        # Header (titolo + Indietro) su un'unica riga
        self.header_frame = ctk.CTkFrame(
            master=self.scroll_frame,
            corner_radius=0,
            fg_color="transparent"
        )
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 20))
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=0)

        # Titolo della pagina
        title_label = ctk.CTkLabel(
            self.header_frame,
            text=f"Scheda Cliente:",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 0))

        # Bottone "Indietro"
        back_button = ctk.CTkButton(
            master=self.header_frame,
            text="Indietro",
            width=100,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=lambda: self.back_callback(self.pt)
        )
        back_button.grid(row=0, column=1, padx=(20, 0), sticky="e")

        # Contenuto delle informazioni della scheda
        self.content_frame = ctk.CTkFrame(
            master=self.scroll_frame,
            corner_radius=10,
            fg_color="#3a3a4d"
        )

        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(5, 20))
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        # Controllo se il cliente ha già una scheda

        if self.scheda:
            self.build_ui(self.content_frame, self.scheda)
        else:
            self.build_ui_no_scheda(self.content_frame, cliente_id, aggiungi_scheda_callback)
            

    
    def build_ui(self, frame,scheda):
        # Etichette per le informazioni della scheda
        labels = [
            ("Peso (kg):", scheda.peso),
            ("Altezza (cm):", scheda.altezza),
            ("Massa muscolare (kg):", scheda.massa_muscolare),
            ("Massa grassa (kg):", scheda.massa_grassa),
            ("BMI:", scheda.bmi),
            ("Note:", scheda.note),
            ("Data rilevazione:", scheda.data_rilevazione),
            ("Data creazione:", scheda.data_creazione),
        ]

        for idx, (label_text, value) in enumerate(labels):
            label = ctk.CTkLabel(
                frame,
                text=label_text,
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="#cccccc"
            )
            label.grid(row=idx, column=0, sticky="w", padx=(10, 5), pady=5)

            value_label = ctk.CTkLabel(
                frame,
                text=str(value),
                font=ctk.CTkFont(size=16),
                text_color="#ffffff"
            )
            value_label.grid(row=idx, column=1, sticky="w", padx=(0, 10), pady=5)
        
        # Calcola la riga finale
        last_row = len(labels)

        # Sezione misure (se presenti)
        if scheda.misure:
            misure_title = ctk.CTkLabel(
                frame,
                text="Misure (cm):",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="#cccccc"
            )
            misure_title.grid(row=last_row, column=0, sticky="w", padx=(10, 5), pady=(10, 5))

            for i, (misura, valore) in enumerate(scheda.misure.items()):
                misura_label = ctk.CTkLabel(
                    frame,
                    text=f"{misura}:",
                    font=ctk.CTkFont(size=15),
                    text_color="#cccccc"
                )
                misura_label.grid(row=last_row+i+1, column=0, sticky="w", padx=(20, 5), pady=2)

                valore_label = ctk.CTkLabel(
                    frame,
                    text=str(valore),
                    font=ctk.CTkFont(size=15),
                    text_color="#ffffff"
                )
                valore_label.grid(row=last_row+i+1, column=1, sticky="w", padx=(0, 10), pady=2)
            last_row = last_row + len(scheda.misure) + 1
        
        self.elimina_scheda_btn = ctk.CTkButton(
            master=self.content_frame,
            text="Elimina Scheda",
            width=150,
            height=40,
            corner_radius=8,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=lambda: self.on_delete_scheda()
        )
        self.elimina_scheda_btn.grid(row=last_row, column=0, sticky="e", padx=(0, 10), pady=2)

        self.modifica_scheda_btn = ctk.CTkButton(
            master=self.content_frame,
            text="Modifica Cliente",
            width=150,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=lambda: self.modifica_scheda_callback(scheda)
        )
        self.modifica_scheda_btn.grid(row=last_row, column=1, sticky="w", padx=(0, 10), pady=2)

        self.error_label = ctk.CTkLabel(
            master=self.content_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff5555"  # rosso per gli errori
            )
        self.error_label.grid(row=last_row + 1, column=0, columnspan=2, sticky="ew", padx=10, pady=(5, 0))


    def build_ui_no_scheda(self, frame, cliente_id, aggiungi_scheda_callback):


        no_scheda_label = ctk.CTkLabel(
            frame,
            text="Il cliente non possiede ancora una scheda.\nInizia creandone una!",
            text_color="#ffffff",
            font=ctk.CTkFont(size=20, weight="bold"),
            justify="center"
        )
        
        no_scheda_label.grid(row=1, column=0, columnspan=2, sticky="")

        aggiungi_scheda_btn = ctk.CTkButton(
            master=frame,
            text="Aggiungi Scheda",
            width=160,
            height=40,
            corner_radius=8,
            fg_color="#3a7ff6",
            hover_color="#5596ff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16, weight="bold"),
            command= lambda: aggiungi_scheda_callback(cliente_id)
        )
        aggiungi_scheda_btn.grid(row=2, column=0, columnspan=2, sticky="")

    def on_delete_scheda(self):
            self.error_label.configure(text = "")
            if not self.pt_controller.elimina_scheda_cliente(self.scheda.id):
                self.error_label.configure(text = "Si è verificato un errore durante l'eliminazione della scheda")
            else:
                self.back_callback(self.pt)

        

