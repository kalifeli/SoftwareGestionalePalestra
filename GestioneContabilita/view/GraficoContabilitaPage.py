import customtkinter as ctk
from tkinter import ttk
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraficoContabilitaPage(ctk.CTkFrame):
    def __init__(self, parent, controller, back_callback):
        super().__init__(parent)
        self.controller = controller
        self.back_callback = back_callback

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Titolo
        ctk.CTkLabel(self, text="Grafico Contabilità", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, pady=(20, 10))

        # Frame per controlli
        controllo_frame = ctk.CTkFrame(self)
        controllo_frame.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
        controllo_frame.grid_columnconfigure(0, weight=1)
        controllo_frame.grid_columnconfigure(1, weight=1)
        controllo_frame.grid_columnconfigure(2, weight=1)

        # Selettore tipo dati (entrate o uscite)
        self.tipo_dati = ctk.StringVar(value="Entrate")
        tipo_menu = ctk.CTkOptionMenu(controllo_frame, variable=self.tipo_dati, values=["Entrate", "Uscite"])
        tipo_menu.grid(row=0, column=0, padx=10, pady=10)

        # Selettore tipo grafico
        self.tipo_grafico = ctk.StringVar(value="Torta")
        grafico_menu = ctk.CTkOptionMenu(controllo_frame, variable=self.tipo_grafico, values=["Torta", "Barre"])
        grafico_menu.grid(row=0, column=1, padx=10, pady=10)

        # Bottone per generare il grafico
        genera_btn = ctk.CTkButton(controllo_frame, text="Mostra Grafico", command=self.mostra_grafico)
        genera_btn.grid(row=0, column=2, padx=10, pady=10)

        # Canvas per il grafico
        self.canvas_frame = ctk.CTkFrame(self)
        self.canvas_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # Bottone indietro
        back_btn = ctk.CTkButton(self, text="Indietro", command=self.back_callback, fg_color="gray")
        back_btn.grid(row=3, column=0, pady=(0, 20))

    def mostra_grafico(self):
        # Pulisci il frame
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        tipo = self.tipo_dati.get()
        grafico = self.tipo_grafico.get()

        if tipo == "Entrate":
            dati = self.controller.get_entrate()
        else:
            dati = self.controller.get_uscite()

        aggregati = defaultdict(float)
        for voce in dati:
            tipo_voce = voce.tipo.value if hasattr(voce.tipo, 'value') else str(voce.tipo)
            aggregati[tipo_voce] += float(voce.importo)

        tipi = list(aggregati.keys())
        importi = list(aggregati.values())

        fig, ax = plt.subplots(figsize=(6, 4))

        if grafico == "Torta":
            ax.pie(importi, labels=tipi, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
        else:
            ax.bar(tipi, importi, color=plt.cm.tab20.colors[:len(tipi)])
            ax.set_ylabel("Importo (€)")
            ax.set_title(f"{tipo} per Tipo")

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
