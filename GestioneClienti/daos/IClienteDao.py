from abc import ABC, abstractmethod
from typing import List, Optional
from GestioneClienti.model.Abbonamento import Abbonamento
from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.model.Corso import Corso
from GestioneClienti.model.Pacchetto import Pacchetto
from GestioneClienti.model.pt import PersonalTrainer

class IClienteDAO(ABC):
    @abstractmethod
    def aggiungi_cliente(self, cliente: Cliente):
        pass

    @abstractmethod
    def elimina_cliente(self, cliente_id: int) -> bool:
        pass

    @abstractmethod
    def get_cliente_by_id(self, cliente_id: int) -> Optional[Cliente]:
        pass

    @abstractmethod
    def get_all_clienti(self) -> List[Cliente]:
        pass

    @abstractmethod
    def trova_cliente_by_nome(self, nome: str) -> List[Cliente]:
        """
        Trova i clienti che corrispondono al nome specificato e li restituisce come lista di oggetti Cliente.
        """
        pass

    @abstractmethod
    def get_abbonamenti_by_cliente_id(self, cliente_id: str) -> Optional[List[Abbonamento]]:
        pass

    @abstractmethod
    def add_abbonamento_to_cliente(self, cliente_id: str, abbonamento: Abbonamento):
        """
        Aggiunge un abbonamento a un cliente specifico.
        """
        pass

    @abstractmethod
    def elimina_abbonamento(self, abbonamento_id: str) -> bool:
        """
        Elimina un abbonamento specifico.
        """
        pass

    @abstractmethod
    def get_all_corsi(self) -> List[Corso]:
        """
        Recupera tutti i corsi disponibili.
        """

    @abstractmethod
    def update_cliente(self, cliente: Cliente) -> bool:
        """
        Aggiorna i dati di un cliente esistente.
        """
        pass

    @abstractmethod
    def get_all_pacchetti(self) -> List[Pacchetto]:
        """
        Recupera tutti i pacchetti di abbonamento disponibili.
        """
        pass

    @abstractmethod
    def controlla_scadenze_abbonamenti(self, abbonamenti: List[Abbonamento]):
        """
        Controlla se l'abbonamento di un cliente è scaduto.
        """
        pass

    @abstractmethod
    def get_corso_by_nome(self, nomeCorso: str) -> Optional[Corso]:
        """
        Recupera un corso specifico in base al nome.
        """
        pass

    @abstractmethod
    def update_abbonamento_cliente(self, abbonamento: Abbonamento) -> bool:
        """
        Modifica i dati di un abbonamento esistente
        """



