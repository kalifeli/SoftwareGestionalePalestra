from GestioneContabilita.daos.ContabilitaDaoFirebase import ContabilitaDaoFirebase
from GestioneContabilita.model.contabilita_model import ContabilitaModel
from GestioneContabilita.model.Entrata import Entrata, TipoEntrata
from GestioneContabilita.model.Uscita import Uscita, TipoUscita
from GestioneContabilita.view.ModificaUscitaPage import ModificaUscitaPage
from GestioneContabilita.view.ModificaEntrataPage import ModificaEntrataPage

class ContabilitaController:
    def __init__(self, view):
        self.view = view
        self.model = ContabilitaModel(ContabilitaDaoFirebase())

    # --- Entrate ---
    def aggiungi_entrata(self, descrizione, importo, data, tipo_str):
        try:
            tipo_enum = TipoEntrata(tipo_str)
        except ValueError:
            tipo_enum = TipoEntrata.ALTRO

        nuova_entrata = Entrata(
            descrizione=descrizione,
            importo=importo,
            data=data,
            tipo=tipo_enum
        )

        self.model.aggiungi_entrata(nuova_entrata)

        # Torna alla schermata precedente tramite il callback
        self.view.back_callback()

    def visualizza_entrate(self):
        dati = self.model.get_entrate()
        self.view.mostra_entrate(dati, self.apri_modifica_entrata)

    def modifica_entrata(self, entrata_id, descrizione, importo, data, tipo_str):
        tipo = TipoEntrata(tipo_str)
        nuovi_dati = {
            "descrizione": descrizione,
            "importo": importo,
            "data": data,
            "tipo": tipo.value
        }
        self.model.aggiorna_entrata(entrata_id, nuovi_dati)
        self.visualizza_entrate()
    
    def apri_modifica_entrata(self, entrata):
        

        if hasattr(self.view, 'pagina_corrente') and self.view.pagina_corrente:
            self.view.pagina_corrente.destroy()

        self.view.pagina_corrente = ModificaEntrataPage(
            self.view,
            entrata=entrata,
            back_callback=self.visualizza_entrate,
            controller=self
        )
        self.view.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.view.pagina_corrente.tkraise()
    
    def aggiorna_entrata(self, entrata_id, descrizione, importo, data, tipo):
        nuovi_dati = {
            "descrizione": descrizione,
            "importo": importo,
            "data": data,
            "tipo": tipo
        }
        self.model.aggiorna_entrata(entrata_id, nuovi_dati)
        self.visualizza_entrate()

    def elimina_entrata(self, entrata_id):
        self.model.elimina_entrata(entrata_id)
        self.visualizza_entrate()

    # --- Uscite ---
    
    def aggiungi_uscita(self, descrizione, importo, data, tipo_str):
        try:
            tipo_enum = TipoUscita(tipo_str)
        except ValueError:
            tipo_enum = TipoUscita.ALTRO  # fallback

        nuova_uscita = Uscita(
            descrizione=descrizione,
            importo=importo,
            data=data,
            tipo=tipo_enum
        )

        self.model.aggiungi_uscita(nuova_uscita)
        # Torna alla schermata precedente tramite il callback
        self.view.back_callback()

    def visualizza_uscite(self):
        dati = self.model.get_uscite()
        self.view.mostra_uscite(dati, self.apri_modifica_uscita)

    def apri_modifica_uscita(self, uscita):
        
        if hasattr(self.view, 'pagina_corrente') and self.view.pagina_corrente:
            self.view.pagina_corrente.destroy()

        self.view.pagina_corrente = ModificaUscitaPage(
            self.view, 
            uscita=uscita,
            back_callback=self.visualizza_uscite,
            controller=self
        )
        self.view.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.view.pagina_corrente.tkraise()

    def aggiorna_uscita(self, uscita_id, descrizione, importo, data, tipo):
        nuovi_dati = {
            "descrizione": descrizione,
            "importo": importo,
            "data": data,
            "tipo": tipo
        }
        self.model.aggiorna_uscita(uscita_id, nuovi_dati)
        self.visualizza_uscite()

    def modifica_uscita(self, uscita_id, descrizione, importo, data, tipo_str):
        tipo = TipoUscita(tipo_str)

    def elimina_uscita(self, uscita_id):
        self.model.elimina_uscita(uscita_id)
        self.visualizza_uscite()
