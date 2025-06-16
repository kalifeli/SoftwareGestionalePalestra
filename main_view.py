import customtkinter as ctk
from PIL import Image
from GestioneClienti.controller.cliente_controller import ClienteController

from GestioneClienti.controller.pt_controller import PtController
from GestioneClienti.view.AggiungiSchedaClientePage import AggiungiSchedaClientePage
from GestioneClienti.view.ClientiAssociatiPage import ClientiAssociatiPage
from GestioneClienti.view.ModificaAbbonamentoPage import ModificaAbbonamentoPage
from GestioneClienti.view.ModificaSchedaClientePage import ModificaSchedaClientePage
from GestioneClienti.view.OrarioPtPage import OrarioPtPage
from GestioneClienti.view.PtPage import PtHomePage
from GestioneClienti.view.AggiungiAbbonamentoPage import AggiungiAbbonamentoPage
from GestioneClienti.view.AggiungiClientePage import AggiungiClientePage
from GestioneClienti.view.ClientiPage import ClientiPage
from GestioneClienti.view.InfoCliente import InfoClientePage
from GestioneClienti.view.ModificaClientePage import ModificaClientePage
from GestioneClienti.view.SchedaClientePage import SchedaClientePage
from GestioneContabilita.controller.contabilita_controller import ContabilitaController
from GestioneContabilita.view.AggiungiEntrataPage import AggiungiEntrataPage
from GestioneContabilita.view.AggiungiUscitaPage import AggiungiUscitaPage
from GestioneContabilita.view.ContabilitaPage import ContabilitaPage
from GestioneContabilita.view.EntratePage import EntratePage
from GestioneContabilita.view.GraficoContabilitaPage import GraficoContabilitaPage
from HomePage import HomePage
from loginPage import LoginPage

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gym Management Software")
        self.geometry("1024x768")

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pagina_corrente = None

        self.login_page = LoginPage(
            self.container,
            login_gestore_callback=self.show_home_page,
            login_pt_callback=self.show_pt_page
        )
        self.login_page.grid(row=0, column=0, sticky="nsew")

        self.show_login_page()


    def show_login_page(self):
        self.login_page.tkraise()

    def show_home_page(self):
        self.home_page.tkraise()

    def show_pt_page(self):
        controller = PtController(self)
        self.pt_page = PtHomePage(
            self.container,
            pt_controller =controller,
            show_clienti_associati_callback= self.show_clienti_associati_page,
            show_orario_callback=self.show_orario_pt_page,
            logout_callback=self.show_login_page
        )
        self.pt_page.controller = PtController(self.pt_page)
        self.pt_page.grid(row=0, column=0, sticky="nsew")
        self.pt_page.tkraise()

    def show_home_page(self):
        self.home_page = HomePage(self.container, show_clienti_callback=self.show_clienti_page, show_contabilità_callback= self.show_contabilita_page, logout_callback=self.show_login_page)
        self.home_page.grid(row=0, column=0, sticky="nsew")
        self.home_page.tkraise()

    def show_clienti_page(self):
        self.clienti_page = ClientiPage(
            self.container,
            controller=None,  # Il controller sarà impostato dopo
            back_callback=self.show_home_page,
            show_aggiungi_cliente_callback= self.show_aggiungi_cliente_page,
            show_info_cliente_callback=self.show_info_cliente_page
        )
        self.clienti_page.controller = ClienteController(self.clienti_page)
        self.clienti_page.grid(row=0, column=0, sticky="nsew")
        self.clienti_page.tkraise()

    def show_aggiungi_cliente_page(self):
        self.aggiungi_cliente_page = AggiungiClientePage(
            self.container,
            controller= None,
            back_callback=self.show_clienti_page
        )
        self.aggiungi_cliente_page.controller = ClienteController(self.aggiungi_cliente_page)
        self.aggiungi_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.aggiungi_cliente_page.tkraise()

    def show_info_cliente_page(self, cliente):
        controller = ClienteController(self)
        self.info_cliente_page = InfoClientePage(
            self.container,
            cliente=cliente,
            controller=controller, 
            back_callback=self.show_clienti_page,
            aggiungi_abbonamento_callback=lambda: self.show_aggiungi_abbonamento_page(cliente),
            modifica_abbonamento_callback=self.show_modifica_abbonamento_cliente_page,
            modifica_cliente_callback=lambda: self.show_modifica_cliente_page(cliente)
        )
        self.info_cliente_page.controller = ClienteController(self.info_cliente_page)
        self.info_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.info_cliente_page.tkraise()

    def show_aggiungi_abbonamento_page(self, cliente):
        self.aggiungi_abbonamento_page = AggiungiAbbonamentoPage(
            self.container,
            cliente=cliente,
            controller=ClienteController(self),  
            back_callback=lambda: self.show_info_cliente_page(cliente),
        )
        self.aggiungi_abbonamento_page.controller = ClienteController(self.aggiungi_abbonamento_page)
        self.aggiungi_abbonamento_page.grid(row=0, column=0, sticky="nsew")
        self.aggiungi_abbonamento_page.tkraise()
    
    def show_modifica_cliente_page(self, cliente):
        self.modifica_cliente_page = ModificaClientePage(
            self.container,
            controller=ClienteController(self),
            cliente=cliente,
            back_callback=lambda: self.show_info_cliente_page(cliente)
        )
        self.modifica_cliente_page.controller = ClienteController(self.modifica_cliente_page)
        self.modifica_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.modifica_cliente_page.tkraise()

    def show_clienti_associati_page(self, pt):
        controller = PtController(self)
        self.clienti_associati_page = ClientiAssociatiPage(
            self.container,
            pt=pt,
            pt_controller=controller,
            back_callback=self.show_pt_page,
            show_scheda_cliente_callback=self.show_scheda_cliente_page
        )
        self.clienti_associati_page.controller = PtController(self.clienti_associati_page)
        self.clienti_associati_page.grid(row=0, column=0, sticky="nsew")
        self.clienti_associati_page.tkraise()
    
    def show_orario_pt_page(self, pt):
        controller = PtController(self)
        self.orario_pt_page = OrarioPtPage(
            self.container,
            pt=pt,
            pt_controller=controller,
            back_callback=self.show_pt_page,
        )
        self.orario_pt_page.controller = PtController(self.orario_pt_page)
        self.orario_pt_page.grid(row=0, column=0, sticky="nsew")
        self.orario_pt_page.tkraise()

    def show_scheda_cliente_page(self, cliente_id, pt):
        controller = PtController(self)
        self.scheda_cliente_page = SchedaClientePage(
            self.container,
            pt_controller= controller,
            cliente_id = cliente_id,
            pt = pt,
            back_callback= self.show_clienti_associati_page,
            aggiungi_scheda_callback= lambda cid=cliente_id, pt_=pt: self.show_aggiungi_scheda_cliente_page(cid, pt_),
            modifica_scheda_callback=lambda scheda: self.show_modifica_scheda_cliente_page(cliente_id, scheda, pt)
        )
        self.scheda_cliente_page.pt_controller = PtController(self.scheda_cliente_page)
        self.scheda_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.scheda_cliente_page.tkraise()

    def show_aggiungi_scheda_cliente_page(self, cliente_id, pt):
        controller = PtController(self)
        self.aggiungi_scheda_cliente_page = AggiungiSchedaClientePage(
            self.container,
            cliente_id=cliente_id,
            pt_controller= controller,
            back_callback= lambda: self.show_scheda_cliente_page(cliente_id, pt)
        )
        self.aggiungi_scheda_cliente_page.pt_controller = PtController(self.aggiungi_scheda_cliente_page)
        self.aggiungi_scheda_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.aggiungi_scheda_cliente_page.tkraise()
    
    def show_modifica_scheda_cliente_page(self, cliente_id, scheda_cliente, pt):
        controller = PtController(self)
        self.modifica_scheda_cliente_page = ModificaSchedaClientePage(
            self.container,
            pt_controller= controller,
            scheda_cliente=scheda_cliente,
            back_callback= lambda: self.show_scheda_cliente_page(cliente_id, pt)
        )

        self.modifica_scheda_cliente_page.pt_controller = PtController(self.modifica_scheda_cliente_page)
        self.modifica_scheda_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.modifica_scheda_cliente_page.tkraise()

    def show_modifica_abbonamento_cliente_page(self, cliente, abbonamento):
        controller = ClienteController(self)
        self.modifica_abbonamento_page = ModificaAbbonamentoPage(
            self.container,
            abbonamento= abbonamento,
            cliente_controller=controller,
            back_callback= lambda: self.show_info_cliente_page(cliente)
        )
        self.modifica_abbonamento_page.cliente_controller = ClienteController(self.modifica_abbonamento_page)
        self.modifica_abbonamento_page.grid(row=0, column=0, sticky="nsew")
        self.modifica_abbonamento_page.tkraise()
    
    def show_contabilita_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = ContabilitaPage(
            self.container,
            back_callback=self.show_home_page,
            show_aggiungi_entrata_callback=self.show_aggiungi_entrata_page,
            show_aggiungi_uscita_callback=self.show_aggiungi_uscita_page,
            show_grafico_contabilita_callback=self.show_grafico_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_entrate_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = EntratePage(
            self.container,
            controller=ContabilitaController(),
            back_callback=self.show_home_page
        )
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_aggiungi_entrata_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = AggiungiEntrataPage(
            self.container,
            controller=None,
            back_callback=self.show_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_aggiungi_uscita_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = AggiungiUscitaPage(
            self.container,
            controller=None,
            back_callback=self.show_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def torna_a_visualizza_entrate(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()
        self.show_contabilita_page()
        self.contabilita_page.visualizza_entrate()

    def torna_a_visualizza_uscite(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()
        self.show_contabilita_page()
        self.contabilita_page.visualizza_uscite()

    def show_grafico_contabilita_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = GraficoContabilitaPage(
            self.container,
            controller=None,
            back_callback=self.show_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()




