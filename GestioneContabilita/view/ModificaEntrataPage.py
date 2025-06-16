import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox

class ModificaEntrataPage(ctk.CTkFrame):
    def __init__(self, parent, entrata, back_callback, controller):
        super().__init__(parent)
        self.controller = controller
        self.entrata = entrata
        self.back_callback = back_callback
        self.id_doc = entrata.id

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        contenuto = ctk.CTkFrame(self)
        contenuto.grid(row=0, column=0, sticky="nsew")
        contenuto.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(contenuto, text="Modifica Entrata", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, pady=(30, 10), padx=20, sticky="n")

        self.tipo_options = ["Abbonamento", "Iscrizione", "Prodotti", "Altro"]
        ctk.CTkLabel(contenuto, text="Tipo:").grid(row=1, column=0, padx=20, sticky="w")
        self.tipo_var = ctk.StringVar(value=entrata.tipo.value)
        self.tipo_menu = ctk.CTkOptionMenu(contenuto, values=self.tipo_options, variable=self.tipo_var)
        self.tipo_menu.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(contenuto, text="Descrizione:").grid(row=3, column=0, padx=20, sticky="w")
        self.descrizione_entry = ctk.CTkEntry(contenuto)
        self.descrizione_entry.insert(0, entrata.descrizione)
        self.descrizione_entry.grid(row=4, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(contenuto, text="Importo:").grid(row=5, column=0, padx=20, sticky="w")
        self.importo_entry = ctk.CTkEntry(contenuto)
        self.importo_entry.insert(0, str(entrata.importo))
        self.importo_entry.grid(row=6, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(contenuto, text="Data (aaaa-mm-gg):").grid(row=7, column=0, padx=20, sticky="w")
        self.data_entry = ctk.CTkEntry(contenuto)
        self.data_entry.insert(0, entrata.data)
        self.data_entry.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="ew")

        ctk.CTkButton(contenuto, text="Salva", command=self.salva_modifiche).grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ew")
        ctk.CTkButton(contenuto, text="Indietro", command=self.torna_indietro, fg_color="gray").grid(row=10, column=0, padx=20, pady=(0, 10), sticky="ew")
        ctk.CTkButton(contenuto, text="Elimina", command=self.elimina_entrata, fg_color="red", hover_color="#b30000").grid(row=11, column=0, padx=20, pady=(0, 30), sticky="ew")

    def salva_modifiche(self):
        descrizione = self.descrizione_entry.get()
        importo = self.importo_entry.get()
        data = self.data_entry.get()
        tipo = self.tipo_var.get()

        if not descrizione or not importo or not data:
            self.show_error("Tutti i campi sono obbligatori.")
            return

        try:
            importo_float = float(importo)
        except ValueError:
            self.show_error("Importo non valido.")
            return

        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            self.show_error("Formato data non valido. Usa AAAA-MM-GG.")
            return

        if (
            descrizione == self.entrata.descrizione and
            importo_float == self.entrata.importo and
            data == self.entrata.data and
            tipo == self.entrata.tipo.value
        ):
            self.back_callback()
            self.destroy()
            return

        try:
            self.controller.aggiorna_entrata(self.id_doc, descrizione, importo_float, data, tipo)
            self.back_callback()
            self.destroy()
        except Exception as e:
            self.show_error(f"Errore durante il salvataggio: {e}")

    def elimina_entrata(self):
        conferma = messagebox.askyesno("Conferma", "Sei sicuro di voler eliminare questa entrata?")
        if conferma:
            try:
                self.controller.elimina_entrata(self.id_doc)
                self.back_callback()
                self.destroy()
            except Exception as e:
                self.show_error(f"Errore durante l'eliminazione: {e}")

    def torna_indietro(self):
        self.back_callback()
        self.destroy()

    def show_error(self, message):
        popup = ctk.CTkToplevel(self)
        popup.title("Errore")
        popup.geometry("300x150")

        label = ctk.CTkLabel(popup, text=message, text_color="red", font=ctk.CTkFont(size=14))
        label.grid(row=0, column=0, pady=20, padx=20)

        btn = ctk.CTkButton(popup, text="Chiudi", command=popup.destroy)
        btn.grid(row=1, column=0, pady=10)
