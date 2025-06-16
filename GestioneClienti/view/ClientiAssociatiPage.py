import customtkinter as ctk
from PIL import Image


class ClientiAssociatiPage(ctk.CTkFrame):
    def __init__(self, master, pt, pt_controller, back_callback, show_scheda_cliente_callback = None):
        """
        master: riferimento al MainView
        back_callback: funzione da chiamare per tornare a HomePage
        """
        super().__init__(master)

        self.pt = pt
        self.pt_controller = pt_controller
        self.back_callback = back_callback
        self.show_scheda_cliente_callback = show_scheda_cliente_callback

        self.clienti_associati = self.pt_controller.get_clienti_associati_by_pt(self.pt.id)  # Lista per memorizzare i clienti associati al PT

        self.pt_controller.aggiorna_clienti_pt(self.pt.id)  # Aggiorno i clienti associati al PT quando inizializzo la view
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

        # ── Titolo secondario centrato ──────────────────────────────
        subtitle = ctk.CTkLabel(
            self,
            text="Gestione Clienti Associati",
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

    def visualizzaClientiAssociati(self, clienti_associati):
        """
        Visualizza la lista dei clienti associati al personal trainer nella scrollable_frame.
        """
        self.all_clienti = clienti_associati
        # Pulisce il contenuto precedente
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Aggiunge i clienti come Label nella scrollable_frame usando grid per migliore visualizzazione
        for idx, cliente in enumerate(clienti_associati):
            cliente_label = ctk.CTkLabel(
                self.scrollable_frame,
                text=f"{cliente.nome} {cliente.cognome} - {cliente.sesso} - {cliente.telefono}",
                font=ctk.CTkFont(size=16),
                text_color="#ffffff",
                cursor="hand2",
            )
            cliente_label.grid(row=idx, column=0, sticky="ew", padx=10, pady=5)

            cliente_label.bind(
                "<Button-1>",
                lambda event, c=cliente.id, pt=self.pt: self.show_scheda_cliente_callback(c, pt)
            )

            self.scrollable_frame.grid_rowconfigure(len(clienti_associati), weight=1)
    
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

    
    



