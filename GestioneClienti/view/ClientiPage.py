import customtkinter as ctk
from PIL import Image


class ClientiPage(ctk.CTkFrame):
    def __init__(self, master, controller, back_callback, show_aggiungi_cliente_callback = None, show_info_cliente_callback = None):
        """
        master: riferimento al MainView
        back_callback: funzione da chiamare per tornare a HomePage
        """
        super().__init__(master)

        self.controller = controller
        self.back_callback = back_callback
        self.show_aggiungi_cliente_callback = show_aggiungi_cliente_callback
        self.show_info_cliente_callback = show_info_cliente_callback
    

        self.sidebar_frame = ctk.CTkFrame(
            master=self,
            width=200,
            corner_radius=0,
            fg_color="#1f1f2e"
        )
        self.sidebar_frame.grid(row=1, column=0, rowspan=2, sticky="nsew")

        # Layout a griglia (2 righe, 3 colonne)
        self.grid_rowconfigure(0, weight=0)  # riga titolo
        self.grid_rowconfigure(1, weight=1)  # riga contenuto
        # Colonna 0: sidebar (peso 0, larghezza fissa)
        self.grid_columnconfigure(0, weight=0)
        # Colonna 1: margine/separatore (peso 0, opzionale)
        self.grid_columnconfigure(1, weight=0, minsize=10)
        # Colonna 2: contenuto principale (peso 1, si espande)
        self.grid_columnconfigure(2, weight=1)


        # ── Bottone "← Indietro" in alto a sinistra ─────────────────
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

        # Campo di ricerca per trovare clienti
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            master=self.sidebar_frame,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            placeholder_text="Cerca Cliente",
            placeholder_text_color="#ffffff",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16),
            textvariable=self.search_var
        )
        self.search_entry.grid(row=1, column=0, padx=10, pady=(20, 10), sticky="ew")

        self.search_button = ctk.CTkButton(
            master=self.sidebar_frame,
            text="Cerca",
            width=40,
            height=40,
            corner_radius=8,
            fg_color="#4a90e2",
            hover_color="#357ab8",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16),
            command=lambda: self.on_search(self.search_var.get())  # collega la funzione di ricerca
        )
        self.search_button.grid(row=1, column=1, padx=(0, 10), pady=(20, 10), sticky="ew")


        # ── Titolo secondario centrato ──────────────────────────────
        subtitle = ctk.CTkLabel(
            self,
            text="Gestione Clienti",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        subtitle.grid(row=0, column=2, pady=(10, 5), sticky="n", padx=(0, 0))

        # Contenitore principale per la visualizzazione dei clienti 
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=0,
            fg_color="#2c313a",
            width=800,  
            height=500  
        )
        self.scrollable_frame.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="nsew")

        # Configuro il layout della scrollable_frame
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.add_cliente_icon = ctk.CTkImage(
            Image.open("utils/assets/add_cliente.png"),
            size=(40, 40)
        )

        aggiungiCliente_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            width=180,
            height=40,
            corner_radius=8,  
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16),
            command=show_aggiungi_cliente_callback,  # Callback per mostrare la pagina di aggiunta cliente
            text="Aggiungi Cliente",
            image=self.add_cliente_icon
        )
        aggiungiCliente_btn.grid(row=2, column=0, padx=10, pady=(20, 10), sticky="ew")

        self.sidebar_frame.grid_rowconfigure(3, weight=1)

    def visualizzaClienti(self, clienti):
        """
        Visualizza la lista dei clienti nella scrollable_frame.
        """
        self.all_clienti = clienti
        # Pulisce il contenuto precedente
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Aggiunge i clienti come Label nella scrollable_frame usando grid per migliore visualizzazione
        for idx, cliente in enumerate(clienti):
            cliente_label = ctk.CTkLabel(
                self.scrollable_frame,
                text=f"{cliente.nome} {cliente.cognome} - {cliente.email}",
                font=ctk.CTkFont(size=16),
                text_color="#ffffff",
                cursor="hand2",
            )
            cliente_label.grid(row=idx, column=0, sticky="ew", padx=10, pady=5)
            self.scrollable_frame.grid_rowconfigure(idx, weight=0)

            cliente_label.bind(
                "<Button-1>",
                lambda event, c=cliente: self.show_info_cliente_callback(c)
            )
    
    def on_search(self, nome:str):
        """
        Gestisce l'evento di ricerca quando l'utente preme Invio nella barra di ricerca.
        """
        if(nome == ""):
            self.controller.load_clienti()
        else:
            clienti_trovati = self.controller.trova_cliente_by_nome(nome)
            if clienti_trovati:
                self.controller.load_ricerca_clienti(clienti_trovati)
            else:
                self.show_error(f"Nessun cliente trovato con il nome '{nome}'.")

    def show_error(self, message):
        """
        Mostra un messaggio di errore in un popup.
        """
        error_popup = ctk.CTkToplevel(self)
        error_popup.title("Errore")
        error_popup.geometry("300x150")
        error_popup.resizable(False, False)

        error_label = ctk.CTkLabel(
            error_popup,
            text=message,
            font=ctk.CTkFont(size=14),
            text_color="#ff0000"
        )
        error_label.pack(pady=20, padx=20)

        close_button = ctk.CTkButton(
            error_popup,
            text="Chiudi",
            command=error_popup.destroy
        )
        close_button.pack(pady=(0, 20))

    
    



