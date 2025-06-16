
from datetime import datetime
from typing import List, Optional
from GestioneClienti.daos.IClienteDao import IClienteDAO
from GestioneClienti.model.Abbonamento import Abbonamento, StatoAbbonamento
from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.model.Corso import Corso
from GestioneClienti.model.Pacchetto import Pacchetto
from utils.firebase_client import get_firestore_client

class ClienteDaoFirebase(IClienteDAO):

    def __init__(self):
        self.client = get_firestore_client()
        self.collection_clienti = self.client.collection("clienti")
        self.collection_abbonamenti = self.client.collection("abbonamenti")
        self.collection_corsi = self.client.collection("corsi")
        self.collection_pacchetti = self.client.collection("pacchetti")
        self.collection_pt = self.client.collection("pt")


    def aggiungi_cliente(self, cliente: Cliente):
        try:

            # Controllo se esiste già un cliente con la stessa email
            query = self.collection_clienti.where("email", "==", cliente.email).stream()
            for doc in query:
                print(f"Cliente già presente con email: {cliente.email}")
                return False  # Cliente già esistente, non lo aggiunge
            
            doc_ref = self.collection_clienti.document()
            cliente.id = doc_ref.id
            dati = cliente.to_dict()
            dati['id'] = cliente.id  # Associa l'ID del cliente al dizionario
            doc_ref.set(dati)  # Aggiungi il documento con i dati del cliente
            print(f"Cliente aggiunto: {cliente.id}")
            return True
        except Exception as e:
            print(f"Errore aggiungendo cliente: {e}")
            return False


    def elimina_cliente(self, cliente_id: int) -> bool:
        try:
            self.collection_clienti.document(cliente_id).delete()
            return True
        except Exception as e:
            print(f"Errore eliminando cliente: {e}")
            return False

    def get_cliente_by_id(self, cliente_id: int) -> Optional[Cliente]:
        doc = self.collection_clienti.document(cliente_id).get()
        if doc.exists:
            return Cliente.from_dict(doc.to_dict())
        return None

    def get_all_clienti(self) -> List[Cliente]:
        docs = self.collection_clienti.stream()
        clienti = []
        for doc in docs:
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                clienti.append(Cliente(**data))
        return clienti
    
    def get_abbonamenti_by_cliente_id(self, cliente_id) -> Optional[List[Abbonamento]]:
        print(f"Query abbonamenti per id_cliente={cliente_id}")  # DEBUG
        docs = self.collection_abbonamenti.where("id_cliente", "==", cliente_id).stream()
        abbonamenti = []
        for doc in docs:
            print("Abbonamento trovato:", doc.id, doc.to_dict())  # DEBUG
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                # Conversione delle date in stringa
                if 'data_inizio' in data and hasattr(data['data_inizio'], 'isoformat'):
                    data['data_inizio'] = data['data_inizio'].isoformat()
                if 'data_fine' in data and hasattr(data['data_fine'], 'isoformat'):
                    data['data_fine'] = data['data_fine'].isoformat()
                abbonamenti.append(Abbonamento.from_dict(data))
        return abbonamenti if abbonamenti else None
    
    def add_abbonamento_to_cliente(self, cliente_id: str, abbonamento: Abbonamento):
        """
        Aggiunge un nuovo documento nella collezione "abbonamenti". Dopo il 'add',
        assegniamo all'oggetto 'abbonamento.id' e l'id del cliente.
        """
        try:
            doc_ref = self.collection_abbonamenti.document()
            abbonamento.id = doc_ref.id  # Imposta l'ID dell'abbonamento
            dati = abbonamento.to_dict()
            dati['id'] = abbonamento.id
            dati['id_cliente'] = cliente_id  # Associa l'abbonamento al cliente
            doc_ref.set(dati)  # Aggiungi il documento con i dati dell'abbonamento
            print(f"Abbonamento aggiunto: {abbonamento.id} per cliente {cliente_id}")

            return True
        except Exception as e:
            print(f"Errore nell'aggiunta dell'abbonamento abbonamento: {e}")
            return False 

    def elimina_abbonamento(self, abbonamento_id: str) -> bool:
        try:
            self.collection_abbonamenti.document(abbonamento_id).delete()
            return True
        except Exception as e:
            print(f"Error deleting abbonamento: {e}")
            return False
    
    def get_all_corsi(self) -> List[Corso]:
        """
        Recupera tutti i corsi disponibili.
        """
        docs = self.collection_corsi.stream()
        corsi = []
        for doc in docs:
            data = doc.to_dict()
            corsi.append(Corso.from_dict(data))
        return corsi
    
    def trova_cliente_by_nome(self, nome: str) -> List[Cliente]:
        """
        Trova i clienti che corrispondono al nome specificato e li restituisce come lista di oggetti Cliente.
        """
        query = self.collection_clienti.where("nome", "==", nome).stream()
        clienti = []
        for doc in query:
            data = doc.to_dict()
            data['id'] = doc.id
            clienti.append(Cliente.from_dict(data))
        return clienti
    
    def update_cliente(self, cliente: Cliente) -> bool:
        """
        Aggiorna in Firestore il documento del cliente con i campi
        della nuova istanza `cliente`.
        """
        try:
            # Controllo se esiste già un cliente con la stessa email
            query = self.collection_clienti.where("email", "==", cliente.email).stream()
            for doc in query:
                if doc.id != cliente.id:
                    print(f"Cliente già presente con email: {cliente.email}")
                    return False  # Cliente già esistente, non lo aggiorna
            # prendo il documento del cliente
            doc_ref = self.collection_clienti.document(cliente.id)
            # converto l'istanza del clienti in un dizionario
            dati = cliente.to_dict()
            # aggiorno il documento con i nuovi dati
            doc_ref.update(dati)
            return True
        except Exception as e:
            print(f"Errore nell'aggiornamento del cliente: {e}")
            return False
    
    def get_all_pacchetti(self) -> List[Pacchetto]:
        """
        Recupera tutti i pacchetti di abbonamento disponibili.
        """
        docs = self.collection_pacchetti.stream()
        pacchetti = []
        for doc in docs:
            data = doc.to_dict()
            pacchetti.append(Pacchetto.from_dict(data))
        return pacchetti
    
    def controlla_scadenze_abbonamenti(self, abbonamenti: List[Abbonamento]):
        """
        Controlla se l'abbonamento di un cliente è scaduto.
        """
        try:
            formato = "%d/%m/%Y"
            for abbonamento in abbonamenti:
                data_fine = datetime.strptime(abbonamento.data_fine, formato)
                oggi = datetime.today()

                if data_fine < oggi:
                    abbonamento.stato = StatoAbbonamento.SCADUTO.value
                    doc_ref = self.collection_abbonamenti.document(abbonamento.id)
                    doc_ref.update({"stato": abbonamento.stato})  # Aggiorna lo stato dell'abbonamento
        except Exception as e:
            print(f"Errore nel controllo della scadenza dell'abbonamento: {e}")
    
    def get_corso_by_nome(self, nome_corso: str):
        query = self.collection_corsi.where("nome", "==", nome_corso).stream()
        corsi = []
        for doc in query:
            data = doc.to_dict()
            data['id'] = doc.id
            corsi.append(Corso.from_dict(data))
        return corsi[0] if corsi else None
    def update_abbonamento_cliente(self, abbonamento):
        try:
            doc_ref = self.collection_abbonamenti.document(abbonamento.id)
            data = abbonamento.to_dict()
            doc_ref.update(data)
            return True
        except Exception as e:
            print(f"Errore durante l'aggiornamento dei dati dell'abbonamento: {e}")
            return False
    