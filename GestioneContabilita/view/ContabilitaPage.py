import customtkinter as ctk
from PIL import Image
from GestioneContabilita.controller.contabilita_controller import ContabilitaController
from datetime import datetime
from GestioneContabilita.view.ModificaUscitaPage import ModificaUscitaPage  
from .ModificaEntrataPage import ModificaEntrataPage
class ContabilitaPage(ctk.CTkFrame):
    def __init__(self, master, back_callback=None, show_aggiungi_entrata_callback=None, show_aggiungi_uscita_callback=None, show_grafico_contabilita_callback=None):
        super().__init__(master)

        self.sort_state_entrate = {
            "data": None,      # Può essere "asc" o "desc"
            "importo": None
        }
        self.sort_state_uscite = {
            "data": None,      # Può essere "asc" o "desc"
            "importo": None
        }
        self.tipo_ordine = ["Abbonamento", "Iscrizione", "Prodotti", "Altro"]
        self.ordinamento_tipo_asc = True  # toggle tra ascendente e discendente


        self.controller = ContabilitaController(self)
        self.back_callback = back_callback
        self.show_aggiungi_entrata_callback = show_aggiungi_entrata_callback
        self.show_aggiungi_uscita_callback = show_aggiungi_uscita_callback
        self.show_grafico_contabilita_callback = show_grafico_contabilita_callback
         # Scrollable frame per visualizzare le entrate/uscite
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=0,
            fg_color="#2c313a",
            width=1200,
            height=500
        )
        self.scrollable_frame.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Layout principale a griglia
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)  # Sidebar
        self.grid_columnconfigure(1, weight=0)  # Spazio
        self.grid_columnconfigure(2, weight=1)  # Contenuto principale

        # Sidebar a sinistra
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#1f1f2e")
        self.sidebar_frame.grid(row=1, column=0, sticky="nsew")

        # Pulsante Aggiungi Entrata con icona
        self.add_icon = ctk.CTkImage(Image.open("utils/assets/add_cliente.png"), size=(30, 30))
        self.aggiungi_entrata_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            text="Aggiungi Entrata",
            image=self.add_icon,
            command=self.show_aggiungi_entrata_callback,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16)
        )
        self.aggiungi_entrata_btn.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="ew")

        # Pulsante Aggiungi Uscita con icona
        self.add_icon = ctk.CTkImage(Image.open("utils/assets/add_cliente.png"), size=(30, 30))
        self.aggiungi_uscita_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            text="Aggiungi Uscita",
            image=self.add_icon,
            command=self.show_aggiungi_uscita_callback,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16)
        )
        self.aggiungi_uscita_btn.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        


        # Pulsante Visualizza Entrate
        self.visualizza_entrate_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            text="Visualizza Entrate",
            command=self.visualizza_entrate,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16)
        )
        self.visualizza_entrate_btn.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

          # Pulsante Visualizza Uscite
        self.visualizza_uscite_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            text="Visualizza Uscite",
            command=self.controller.visualizza_uscite,
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16)
        )
        self.visualizza_uscite_btn.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Pulsante Visualizza Grafico
        self.visualizza_grafico_btn = ctk.CTkButton(
            master=self.sidebar_frame,
            text="Visualizza Grafico Contabilità",
            command=self.show_grafico_contabilita_callback,  # Chiama la funzione della MainView
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=16)
        )
        self.visualizza_grafico_btn.grid(row=4, column=0, padx=10, pady=10, sticky="ew")


        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Titolo in alto
        title = ctk.CTkLabel(self, text="Sezione Contabilità", font=ctk.CTkFont(size=24, weight="bold"), text_color="#ffffff")
        title.grid(row=0, column=2, pady=(20, 10), sticky="n")

        # Bottone Indietro
        if self.back_callback:
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
            back_button.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")

       

    def visualizza_entrate(self):
        self.controller.visualizza_entrate()

    def mostra_entrate(self, dati_entrate, on_click_callback):
        self.dati_entrate_grezzi = dati_entrate

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.scrollable_frame.grid_columnconfigure(0, weight=1)  # Data
        self.scrollable_frame.grid_columnconfigure(1, weight=1)  # Importo
        self.scrollable_frame.grid_columnconfigure(2, weight=3)  # Descrizione
        self.scrollable_frame.grid_columnconfigure(3, weight=2)  # Tipo

        if not dati_entrate:
            ctk.CTkLabel(
                self.scrollable_frame,
                text="Nessuna entrata trovata",
                text_color="#ffffff"
            ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
            return

        headers = ["Data", "Importo", "Descrizione", "Tipo"]
        callbacks = [
            lambda: self.ordina_entrate_per("data"),
            lambda: self.ordina_entrate_per("importo"),
            None,
            lambda: self.ordina_entrate_per("tipo")
        ]

        for col, (header, cb) in enumerate(zip(headers, callbacks)):
            label = ctk.CTkLabel(
                self.scrollable_frame,
                text=header,
                font=ctk.CTkFont(weight="bold"),
                text_color="#ffffff",
                anchor="w",
                cursor="hand2" if cb else "arrow"
            )
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")
            if cb:
                label.bind("<Button-1>", lambda e, callback=cb: callback())

        def bind_entrata(label, item):
            label.bind("<Button-1>", lambda e, item=item: on_click_callback(item))
            label.configure(cursor="hand2")

        for row, entrata in enumerate(dati_entrate, start=1):
            label_data = ctk.CTkLabel(self.scrollable_frame, text=entrata.data, anchor="w", text_color="#ffffff")
            label_data.grid(row=row, column=0, sticky="w", padx=10, pady=2)
            bind_entrata(label_data, entrata)

            label_importo = ctk.CTkLabel(self.scrollable_frame, text=str(entrata.importo), anchor="w", text_color="#ffffff")
            label_importo.grid(row=row, column=1, sticky="w", padx=10, pady=2)
            bind_entrata(label_importo, entrata)

            label_descrizione = ctk.CTkLabel(self.scrollable_frame, text=entrata.descrizione, anchor="w", text_color="#ffffff")
            label_descrizione.grid(row=row, column=2, sticky="w", padx=10, pady=2)
            bind_entrata(label_descrizione, entrata)

            label_tipo = ctk.CTkLabel(self.scrollable_frame, text=entrata.tipo.value, anchor="w", text_color="#ffffff")
            label_tipo.grid(row=row, column=3, sticky="w", padx=10, pady=2)
            bind_entrata(label_tipo, entrata)
    
    def mostra_uscite(self, dati_uscite, on_click_callback):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_columnconfigure(2, weight=3)
        self.scrollable_frame.grid_columnconfigure(3, weight=2)

        if not dati_uscite:
            ctk.CTkLabel(
                self.scrollable_frame,
                text="Nessuna uscita trovata",
                text_color="#ffffff"
            ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
            return

        headers = ["Data", "Importo", "Descrizione", "Tipo"]
        for col, h in enumerate(headers):
            label = ctk.CTkLabel(
                self.scrollable_frame,
                text=h,
                font=ctk.CTkFont(weight="bold"),
                text_color="#ffffff",
                anchor="w",
                cursor="hand2"
            )
            label.grid(row=0, column=col, padx=10, pady=5, sticky="w")

            if h.lower() in ["data", "importo", "tipo"]:
                label.bind("<Button-1>", lambda e, key=h.lower(): self.ordina_uscite_per(key))

        def bind_uscita(label, item):
            label.bind("<Button-1>", lambda e, item=item: on_click_callback(item))
            label.configure(cursor="hand2")

        for row, uscita in enumerate(dati_uscite, start=1):
            label_data = ctk.CTkLabel(self.scrollable_frame, text=uscita.data, anchor="w", text_color="#ffffff")
            label_data.grid(row=row, column=0, padx=10, pady=2, sticky="w")
            bind_uscita(label_data, uscita)

            label_importo = ctk.CTkLabel(self.scrollable_frame, text=str(uscita.importo), anchor="w", text_color="#ffffff")
            label_importo.grid(row=row, column=1, padx=10, pady=2, sticky="w")
            bind_uscita(label_importo, uscita)

            label_descrizione = ctk.CTkLabel(self.scrollable_frame, text=uscita.descrizione, anchor="w", text_color="#ffffff")
            label_descrizione.grid(row=row, column=2, padx=10, pady=2, sticky="w")
            bind_uscita(label_descrizione, uscita)

            label_tipo = ctk.CTkLabel(self.scrollable_frame, text=uscita.tipo.value, anchor="w", text_color="#ffffff")
            label_tipo.grid(row=row, column=3, padx=10, pady=2, sticky="w")
            bind_uscita(label_tipo, uscita)

    def apri_modifica_entrata(self, entrata):
        from GestioneContabilita.view.ModificaEntrataPage import ModificaEntrataPage
        root = self.winfo_toplevel()  # ottiene MainView

        if hasattr(root, "pagina_corrente") and root.pagina_corrente:
            root.pagina_corrente.destroy()

        root.pagina_corrente = ModificaEntrataPage(
            root.container,  
            entrata=entrata,
            controller=self.controller,
            back_callback=root.torna_a_visualizza_entrate
        )
        root.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        root.pagina_corrente.tkraise()
        self.destroy()

    def apri_modifica_uscita(self, uscita):
        from GestioneContabilita.view.ModificaUscitaPage import ModificaUscitaPage
        root = self.winfo_toplevel()

        if hasattr(root, "pagina_corrente") and root.pagina_corrente:
            root.pagina_corrente.destroy()

        root.pagina_corrente = ModificaUscitaPage(
            root.container,
            uscita=uscita,
            controller=self.controller,
            back_callback=root.torna_a_visualizza_uscite
        )
        root.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        root.pagina_corrente.tkraise()
        self.destroy()
        
    def ordina_entrate_per(self, chiave):
        print(f"Ordinamento per: {chiave}")
        # Cicla stato
        stato = self.sort_state_entrate.get(chiave)
        if stato is None:
            nuovo_stato = "asc"
        elif stato == "asc":
            nuovo_stato = "desc"
        else:
            nuovo_stato = None

        # Aggiorna stato
        self.sort_state_entrate["data"] = None
        self.sort_state_entrate["importo"] = None
        self.sort_state_entrate[chiave] = nuovo_stato

        # Recupera dati
        dati = self.controller.model.get_entrate()

        # Applica ordinamento
        if nuovo_stato == "asc":
            dati.sort(key=lambda x: self._chiave_ordinamento(x, chiave))
        elif nuovo_stato == "desc":
            dati.sort(key=lambda x: self._chiave_ordinamento(x, chiave), reverse=True)

        self.mostra_entrate(dati, self.apri_modifica_entrata)

    def _chiave_ordinamento(self, voce, chiave):
        try:
            valore = getattr(voce, chiave)
        except AttributeError:
            return ""

        if chiave == "data":
            for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
                try:
                    return datetime.strptime(valore, fmt)
                except:
                    continue
            return datetime.min

        elif chiave == "importo":
            try:
                return float(valore)
            except:
                return 0.0

        elif chiave == "tipo":
            return valore.value if hasattr(valore, "value") else str(valore)

        return str(valore)

    def ordina_uscite_per(self, chiave):
        print(f"Ordinamento per: {chiave}")
        # Cicla stato
        stato = self.sort_state_uscite.get(chiave)
        if stato is None:
            nuovo_stato = "asc"
        elif stato == "asc":
            nuovo_stato = "desc"
        else:
            nuovo_stato = None

        # Aggiorna stato
        self.sort_state_uscite["data"] = None
        self.sort_state_uscite["importo"] = None
        self.sort_state_uscite[chiave] = nuovo_stato

        # Recupera dati
        dati = self.controller.model.get_uscite()

        # Applica ordinamento
        if nuovo_stato == "asc":
            dati.sort(key=lambda x: self._chiave_ordinamento(x, chiave))
        elif nuovo_stato == "desc":
            dati.sort(key=lambda x: self._chiave_ordinamento(x, chiave), reverse=True)

        self.mostra_uscite(dati, self.apri_modifica_uscita)