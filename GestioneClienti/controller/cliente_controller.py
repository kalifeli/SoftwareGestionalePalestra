from typing import List
from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.daos.ClienteDaoFirebase import ClienteDaoFirebase
from GestioneClienti.model.Abbonamento import Abbonamento



class ClienteController:
    def __init__(self, view):
        self.view = view
        self.dao = ClienteDaoFirebase()

        # Chiamo load_clienti solo se la view ha il metodo visualizzaClienti
        if hasattr(self.view, "visualizzaClienti"):
            self.load_clienti()

    def load_clienti(self):
        try:
            clienti = self.dao.get_all_clienti()
            print("Clienti caricati:", clienti) 
            self.view.visualizzaClienti(clienti)
        except Exception as e:
            print(f"Errore nel caricamento dei clienti: {str(e)}")

    def load_ricerca_clienti(self, clienti):
        """
        Carica i clienti dalla DAO e li visualizza nella view.
        """
        try:
            print("Caricamento clienti dalla DAO...")
            self.view.visualizzaClienti(clienti)
        except Exception as e:
            print(f"Errore nel caricamento dei clienti: {str(e)}")

    def aggiungi_cliente(self, cliente):
        """
        Aggiunge un nuovo cliente tramite la DAO e ricarica la lista dei clienti.
        """
        try:
            result = self.dao.aggiungi_cliente(cliente)
            if result:
                self.load_clienti()
                return True
            else:
                print("Cliente già esistente con la stessa email.")
                return False
        except Exception as e:
            print(f"Errore nell'aggiunta del cliente: {str(e)}")
            return False
        
    def elimina_cliente(self, cliente_id: str):
        """
        Elimina un cliente specifico tramite la DAO e ricarica la lista dei clienti.
        """
        try:
            success = self.dao.elimina_cliente(cliente_id)
            if success:
                self.load_clienti() 
            else:
                print(f"Errore nell'eliminazione del cliente {cliente_id}.")
            return success
        except Exception as e:
            print(f"Errore nell'eliminazione del cliente: {str(e)}")
            return False
        
    def trova_cliente_by_nome(self, nome: str):
        """
        Trova i clienti che corrispondono al nome specificato e li restituisce come lista di oggetti Cliente.
        """
        try:
            clienti = self.dao.trova_cliente_by_nome(nome)
            if clienti:
                print(f"Clienti trovati per nome '{nome}': {clienti}")
                return clienti
            else:
                print(f"Nessun cliente trovato con il nome '{nome}'.")
                return []
        except Exception as e:
            print(f"Errore nella ricerca del cliente: {str(e)}")
            return []
        
    def get_abbonamenti_by_cliente_id(self, cliente_id: str):
        """
        Recupera gli abbonamenti associati a un cliente specifico.
        """
        try:
            abbonamenti = self.dao.get_abbonamenti_by_cliente_id(cliente_id)
            return abbonamenti if abbonamenti else []
        except Exception as e:
            print(f"Errore nel recupero degli abbonamenti: {str(e)}")
            return None
        
    def elimina_abbonamento(self, abbonamento_id: str):
        """
        Elimina un abbonamento specifico.
        """
        try:
            success = self.dao.elimina_abbonamento(abbonamento_id)
            if success:
                print(f"Abbonamento {abbonamento_id} eliminato con successo.")
            else:
                print(f"Errore nell'eliminazione dell'abbonamento {abbonamento_id}.")
            return success
        except Exception as e:
            print(f"Errore nell'eliminazione dell'abbonamento: {str(e)}")
            return False
        
    def get_all_corsi(self):
        """
        Recupera tutti i corsi disponibili.
        """
        try:
            corsi = self.dao.get_all_corsi()
            return corsi if corsi else []
        except Exception as e:
            print(f"Errore nel recupero dei corsi: {str(e)}")
            return []
        
    def add_abbonamento_to_cliente(self, cliente_id: str, abbonamento: Abbonamento):
        """
        Aggiunge un abbonamento a un cliente specifico.
        """
        try:
            self.dao.add_abbonamento_to_cliente(cliente_id, abbonamento)
            print(f"Abbonamento aggiunto per il cliente {cliente_id}: {abbonamento}")
            return True
        except Exception as e:
            print(f"Errore nell'aggiunta dell'abbonamento: {str(e)}")
            return False
        
    def modifica_cliente(self, cliente: Cliente):
        """
        Aggiorna i dati di un cliente esistente.
        """
        try:
            result = self.dao.update_cliente(cliente)
            if result:
                print(f"Cliente {cliente.id} aggiornato con successo.")
                self.load_clienti()  # Ricarica la lista dei clienti dopo l'aggiornamento
                return True
            else:
                print(f"Errore nell'aggiornamento del cliente.")
                return False
        except Exception as e:
            print(f"Errore nell'aggiornamento del cliente: {str(e)}")
            return False
    
    def get_all_pacchetti(self):
        """
        Recupera tutti i pacchetti di abbonamento disponibili.
        """
        try:
            pacchetti = self.dao.get_all_pacchetti()
            return pacchetti if pacchetti else []
        except Exception as e:
            print(f"Errore nel recupero dei pacchetti: {str(e)}")
            return []

    def controlla_scadenze_abbonamenti(self, abbonamenti: List[Abbonamento]):
        """
        Controlla la scadenza degli abbonamenti di un cliente specifico.
        """
        try:
            self.dao.controlla_scadenze_abbonamenti(abbonamenti)
        except Exception as e:
            print(f"Errore nel controllo della scadenza degli abbonamenti: {str(e)}")

    def update_abbonamento_cliente(self, abbonamento) -> bool:
        return self.dao.update_abbonamento_cliente(abbonamento)
