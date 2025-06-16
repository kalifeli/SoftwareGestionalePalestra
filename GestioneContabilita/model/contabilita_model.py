from GestioneContabilita.daos.IContabilitaDao import IContabilitaDao
from GestioneContabilita.model.Entrata import Entrata
from GestioneContabilita.model.Uscita import Uscita

class ContabilitaModel:
    def __init__(self, dao: IContabilitaDao):
        self.dao = dao

    # --- Entrate ---
    def aggiungi_entrata(self, entrata: Entrata):
        self.dao.aggiungi_entrata(entrata)

    def get_entrate(self):
        return self.dao.get_entrate()

    def aggiorna_entrata(self, entrata_id: str, nuovi_dati: dict):
        self.dao.aggiorna_entrata(entrata_id, nuovi_dati)

    def elimina_entrata(self, entrata_id: str):
        self.dao.elimina_entrata(entrata_id)

    # --- Uscite ---
    def aggiungi_uscita(self, uscita: Uscita):
        self.dao.aggiungi_uscita(uscita)

    def get_uscite(self):
        return self.dao.get_uscite()

    def aggiorna_uscita(self, uscita_id: str, nuovi_dati: dict):
        self.dao.aggiorna_uscita(uscita_id, nuovi_dati)

    def elimina_uscita(self, uscita_id: str):
        self.dao.elimina_uscita(uscita_id)
