from abc import ABC, abstractmethod

class IContabilitaDao(ABC):

    @abstractmethod
    def aggiungi_entrata(self, entrata):
        pass

    @abstractmethod
    def get_entrate(self):
        pass

    @abstractmethod
    def aggiorna_entrata(self, entrata_id, nuovi_dati):
        pass

    @abstractmethod
    def elimina_entrata(self, entrata_id):
        pass

    @abstractmethod
    def aggiungi_uscita(self, uscita):
        pass

    @abstractmethod
    def get_uscite(self):
        pass

    @abstractmethod
    def aggiorna_uscita(self, uscita_id, nuovi_dati):
        pass

    @abstractmethod
    def elimina_uscita(self, uscita_id):
        pass
