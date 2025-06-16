from abc import ABC, abstractmethod
from typing import List, Optional

from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.model.SchedaCliente import SchedaCliente
from GestioneClienti.model.pt import PersonalTrainer


class IPtDAO(ABC):
    @abstractmethod
    def get_pt_by_id(self, pt_id: str) -> Optional[PersonalTrainer]:
        """
        Recupera un Personal Trainer specifico in base all'ID.
        """
        pass

    @abstractmethod
    def get_clienti_by_corso(self, nomeCorso: str) -> List[str]:
        """
        Recupera tutti gli id dei clienti iscritti a un corso specifico che presentano un abbonamento ATTIVO.
        """
        pass

    @abstractmethod
    def aggiorna_clienti_pt(self, pt_id) -> bool:
        """
        Aggiorna la lista dei clienti associati a un PT in base ai corsi che tiene.
        """
        pass

    @abstractmethod
    def get_clienti_associati_by_pt(self, pt_id: str) -> List[Cliente]:
        """
        Recupera tutti i clienti associati a un PT specifico.
        """
        pass

    @abstractmethod
    def get_orario_pt(self, pt_id:str) -> dict:
        """
        Recupera l'orario di lavoro di un PT specifico.
        """
        pass

    @abstractmethod
    def get_scheda_cliente(self, cliente_id: str) -> Optional[SchedaCliente]:
        """
        Recupera la scheda di un cliente specifico
        """
        pass

    @abstractmethod
    def add_scheda_cliente(self, scheda: SchedaCliente, cliente_id: str) -> bool:
        """
        Aggiunge una scheda con dati e misure ad un cliente
        """
        pass
    @abstractmethod
    def elimina_scheda_cliente(self, scheda_id: str) -> bool:
        """
        Elimina una scheda cliente dal database
        """
        pass
    def update_scheda_cliente(self, scheda: SchedaCliente) -> bool:
        """
        Aggiorna i dati della scheda di un cliente a seguito di una modifica
        """


