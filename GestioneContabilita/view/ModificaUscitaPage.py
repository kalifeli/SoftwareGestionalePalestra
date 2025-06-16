import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox

class ModificaUscitaPage(ctk.CTkFrame):
    def __init__(self, master, uscita, back_callback, controller):
        super().__init__(master)
        self.uscita = uscita
        self.back_callback = back_callback
        self.controller = controller
        self.id_doc = uscita.id

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        contenuto = ctk.CTkFrame(self)
        contenuto.grid(row=0, column=0, sticky="nsew")
        contenuto.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(contenuto, text="Modifica Uscita", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, pady=(30, 10), padx=20, sticky="n")

        self.tipo_options = ["Affitto", "Manutenzione", "Acquisti", "Stipendi", "Altro"]
        ctk.CTkLabel(contenuto, text="Tipo:").grid(row=1, column=0, padx=20, sticky="w")
        self.tipo_var = ctk.StringVar(value=uscita.tipo.value)
        self.tipo_menu = ctk.CTkOptionMenu(contenuto, values=self.tipo_options, variable=self.tipo_var)
        self.tipo_menu.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(contenuto, text="Descrizione:").grid(row=3, column=0, padx=20, sticky="w")
        self.descrizione_entry = ctk.CTkEntry(contenuto)
        self.descrizione_entry.insert(0, uscita.descrizione)
        self.descrizione_entry.grid(row=4, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(contenuto, text="Importo:").grid(row=5, column=0, padx=20, sticky="w")
        self.importo_entry = ctk.CTkEntry(contenuto)
        self.importo_entry.insert(0, str(uscita.importo))
        self.importo_entry.grid(row=6, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(contenuto, text="Data (aaaa-mm-gg):").grid(row=7, column=0, padx=20, sticky="w")
        self.data_entry = ctk.CTkEntry(contenuto)
        self.data_entry.insert(0, uscita.data)
        self.data_entry.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="ew")

        ctk.CTkButton(contenuto, text="Salva", command=self.salva_modifiche).grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ew")
        ctk.CTkButton(contenuto, text="Indietro", command=self.torna_indietro, fg_color="gray").grid(row=10, column=0, padx=20, pady=(0, 10), sticky="ew")
        ctk.CTkButton(contenuto, text="Elimina", command=self.elimina_uscita, fg_color="red", hover_color="#b30000").grid(row=11, column=0, padx=20, pady=(0, 30), sticky="ew")

    def salva_modifiche(self):
        descrizione = self.descrizione_entry.get().strip()
        importo = self.importo_entry.get().strip()
        data = self.data_entry.get().strip()
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
            descrizione == self.uscita.descrizione and
            importo_float == self.uscita.importo and
            data == self.uscita.data and
            tipo == self.uscita.tipo.value
        ):
            self.back_callback()
            self.destroy()
            return

        try:
            self.controller.aggiorna_uscita(self.id_doc, descrizione, importo_float, data, tipo)
            self.back_callback()
            self.destroy()
        except Exception as e:
            self.show_error(f"Errore durante il salvataggio: {e}")

    def elimina_uscita(self):
        conferma = messagebox.askyesno("Conferma", "Sei sicuro di voler eliminare questa uscita?")
        if conferma:
            try:
                self.controller.elimina_uscita(self.id_doc)
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
