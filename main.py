import customtkinter as ctk
from main_view import MainView

def main():
    # Configurazione tema
    ctk.set_appearance_mode("dark")  # Modalità scura
    ctk.set_default_color_theme("blue")  # Tema blu
    # Creazione della finestra principale
    app = MainView()
    app.mainloop()  # Avvio del loop principale dell'applicazione

if __name__ == "__main__":
    main()
