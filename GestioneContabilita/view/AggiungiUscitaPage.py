import customtkinter as ctk
from datetime import datetime

class AggiungiUscitaPage(ctk.CTkFrame):
    def __init__(self, parent, controller, back_callback):
        super().__init__(parent)

        self.controller = controller
        self.back_callback = back_callback

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text="Aggiungi Uscita", font=ctk.CTkFont(size=24, weight="bold"))
        title.grid(row=0, column=0, pady=(30, 10), padx=20, sticky="n")

        ctk.CTkLabel(self, text="Tipo:").grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")
        self.tipo_options = ["Affitto", "Manutenzione", "Acquisti", "Stipendi", "Altro"]
        self.tipo_var = ctk.StringVar(value=self.tipo_options[0])
        self.tipo_menu = ctk.CTkOptionMenu(self, values=self.tipo_options, variable=self.tipo_var)
        self.tipo_menu.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        self.descrizione_entry = ctk.CTkEntry(self, placeholder_text="Descrizione")
        self.descrizione_entry.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.importo_entry = ctk.CTkEntry(self, placeholder_text="Importo (es. 50.00)")
        self.importo_entry.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.data_entry = ctk.CTkEntry(self, placeholder_text="Data (aaaa-mm-gg)")
        self.data_entry.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        salva_btn = ctk.CTkButton(self, text="Salva Uscita", command=self.aggiungi_uscita)
        salva_btn.grid(row=6, column=0, pady=20)

        back_btn = ctk.CTkButton(self, text="Torna alla Contabilità", command=self.back_callback, fg_color="gray")
        back_btn.grid(row=7, column=0, pady=(0, 20))

    def aggiungi_uscita(self):
        descrizione = self.descrizione_entry.get().strip()
        importo = self.importo_entry.get().strip()
        data = self.data_entry.get().strip()

        if not descrizione or not importo or not data:
            self.show_error("Compila tutti i campi.")
            return

        try:
            importo_float = float(importo)
        except ValueError:
            self.show_error("Importo non valido.")
            return

        try:
            data_formattata = datetime.strptime(data, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            self.show_error("Formato data non valido. Usa AAAA-MM-GG.")
            return

        try:
            tipo = self.tipo_var.get()
            self.controller.aggiungi_uscita(descrizione, importo_float, data_formattata, tipo)
            self.back_callback()
        except Exception as e:
            self.show_error(f"Errore durante il salvataggio: {e}")

    def show_error(self, message):
        popup = ctk.CTkToplevel(self)
        popup.title("Errore")
        popup.geometry("300x150")

        label = ctk.CTkLabel(popup, text=message, text_color="red", font=ctk.CTkFont(size=14))
        label.grid(row=0, column=0, pady=20, padx=20)

        btn = ctk.CTkButton(popup, text="Chiudi", command=popup.destroy)
        btn.grid(row=1, column=0, pady=10)
