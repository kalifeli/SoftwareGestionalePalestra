import customtkinter as ctk

class UscitePage(ctk.CTkFrame):
    def __init__(self, parent, dati, on_click_callback):
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="Uscite", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=500, height=400)
        self.scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

        for uscita in dati:
            descrizione = uscita.get("descrizione", "N/A")
            importo = uscita.get("importo", "0")
            data = uscita.get("data", "N/A")
            tipo = uscita.get("tipo", "N/A") 

            item = ctk.CTkFrame(self.scroll_frame, fg_color="gray15", cursor="hand2")
            item.pack(fill="x", padx=10, pady=5)

            testo = f"{data} | {descrizione} - €{importo} ({tipo})"
            label = ctk.CTkLabel(item, text=testo, anchor="w", font=ctk.CTkFont(size=14))
            label.pack(padx=10, pady=5, fill="x")

            # Make the whole item clickable
            label.bind("<Button-1>", lambda e, u=uscita: on_click_callback(u))
            item.bind("<Button-1>", lambda e, u=uscita: on_click_callback(u))
