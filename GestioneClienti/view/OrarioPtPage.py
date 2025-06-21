import customtkinter as ctk


class OrarioPtPage(ctk.CTkFrame):

    orario_dict_prova = {
    "Lunedì": "09:00 - 12:00",
    "Martedì": "10:00 - 13:00",
    "Mercoledì": "15:00 - 18:00",
    "Giovedì": "09:00 - 12:00",
    "Venerdì": "14:00 - 17:00",
    "Sabato": "10:00 - 13:00",
    "Domenica": "Chiuso"
    }

    def __init__(self, master, pt, pt_controller, back_callback):
        """
        :param master: parent widget
        :param pt: oggetto del personal trainer
        :param pt_controller: controller per la logica del PT
        :param back_callback: funzione da chiamare per tornare indietro
        """
        super().__init__(master)
        self.pt = pt
        self.back_callback = back_callback
        self.pt_controller = pt_controller

        self.orario_dict = self.pt_controller.get_orario_pt(self.pt.id)
        self.init_ui()

    def init_ui(self):
            
        # Layout a griglia (2 righe, 3 colonne)
        self.grid_rowconfigure(0, weight=0)  # riga titolo
        self.grid_rowconfigure(1, weight=1)  # riga contenuto
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)


        # Bottone "Indietro" in alto a sinistra 
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
        back_button.grid(row=0, column=0, pady=(10, 5), padx=10, sticky="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Orario Personal Trainer",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        subtitle.grid(row=0, column=1, pady=(10, 5), sticky="n", padx=(0, 0))

        table_frame = ctk.CTkFrame(self, fg_color="#4a4a5d", corner_radius=8)
        table_frame.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="ew")

        # Header
        header_giorno = ctk.CTkLabel(table_frame, text="Giorno", font=ctk.CTkFont(weight="bold"), width=120)
        header_orario = ctk.CTkLabel(table_frame, text="Orario", font=ctk.CTkFont(weight="bold"), width=120)
        header_giorno.grid(row=0, column=0, padx=10, pady=8)            
        header_orario.grid(row=0, column=1, padx=10, pady=8)

        GIORNI_ORDINATI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

        idx = 1
        for giorno in GIORNI_ORDINATI:
            orario = self.orario_dict.get(giorno)
            if orario is not None:
                giorno_lbl = ctk.CTkLabel(table_frame, text=giorno, width=120)
                orario_lbl = ctk.CTkLabel(table_frame, text=orario, width=120)
                giorno_lbl.grid(row=idx, column=0, padx=10, pady=4)
                orario_lbl.grid(row=idx, column=1, padx=10, pady=4)
                idx += 1

        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)

