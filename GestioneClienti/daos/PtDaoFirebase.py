from typing import List, Optional
from GestioneClienti.daos.IPtDao import IPtDAO
from GestioneClienti.model.Abbonamento import StatoAbbonamento
from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.model.SchedaCliente import SchedaCliente
from GestioneClienti.model.pt import PersonalTrainer
from utils.firebase_client import get_firestore_client


class PtDaoFirebase(IPtDAO):
    def __init__(self):
        self.client = get_firestore_client()
        self.collection_pt = self.client.collection("pt")
        self.collection_abbonamenti = self.client.collection("abbonamenti")
        self.collection_schedaCliente = self.client.collection("schedaCliente")

    def get_pt_by_id(self, pt_id: str) -> Optional[PersonalTrainer]:
        """
        Recupera un Personal Trainer specifico in base all'ID.
        """
        doc = self.collection_pt.document(pt_id).get()
        if doc.exists:
            return PersonalTrainer.from_dict(doc.to_dict())
        return None

    def get_clienti_by_corso(self, nomeCorso: str) -> List[str]:
        query = self.collection_abbonamenti.where("corso", "==", nomeCorso).where("stato", "==", StatoAbbonamento.ATTIVO.value).stream()
        clientiId = []
        for doc in query:
            data = doc.to_dict()
            clientiId.append(data['id_cliente'])
        return clientiId

    def aggiorna_clienti_pt(self, pt_id):
        # recupera il Pt dal database
        pt_doc = self.collection_pt.document(pt_id).get()
        if not pt_doc.exists:
            print(f"PT con id {pt_id} non trovato.")
            return False
        pt_data = pt_doc.to_dict()
        corsi_pt = pt_data.get("corsi", [])
        # creo una collezione di elementi disordinati ma unici che rappresentano gli id dei clienti
        clienti_set = set()

        # Per ogni corso (nome), trova i clienti con abbonamento attivo a quel corso
        for nome_corso in corsi_pt:
            clienti_ids = self.get_clienti_by_corso(nome_corso)
            clienti_set.update(clienti_ids)

        # Aggiorna la lista dei clienti nel documento del PT
        self.collection_pt.document(pt_id).update({"clienti": list(clienti_set)})
        print(f"Clienti aggiornati per PT {pt_id}: {list(clienti_set)}")
        return True
    def get_clienti_associati_by_pt(self, pt_id: str) -> List[Cliente]:
        """
        Recupera tutti i clienti associati a un PT specifico.
        """
        pt_doc = self.collection_pt.document(pt_id).get()
        if not pt_doc.exists:
            print(f"PT con id {pt_id} non trovato.")
            return []

        pt_data = pt_doc.to_dict()
        clienti_ids = pt_data.get("clienti", [])
        
        clienti = []
        for cliente_id in clienti_ids:
            cliente_doc = self.client.collection("clienti").document(cliente_id).get()
            if cliente_doc.exists:
                cliente_data = cliente_doc.to_dict()
                clienti.append(Cliente.from_dict(cliente_data))
        
        return clienti
    
    def get_orario_pt(self, pt_id: str) -> dict:
        """
        Recupera l'orario di lavoro di un PT specifico.
        """
        pt_doc = self.collection_pt.document(pt_id).get()
        if pt_doc.exists:
            pt_data = pt_doc.to_dict()
            return pt_data.get("orario", {})
        return {}
    
    def get_scheda_cliente(self, cliente_id: str) -> Optional[SchedaCliente]:
        """
        Recupera la scheda di un cliente specifico.
        """
        query = self.collection_schedaCliente.where("id_cliente", "==", cliente_id).get()
        if query:
            scheda_data = query[0].to_dict()
            return SchedaCliente.from_dict(scheda_data)
        return None
    def add_scheda_cliente(self, scheda, cliente_id):
        """
        Aggiunge una nuova scheda ad un cliente che non la possiede.
        """
        try:
            doc_ref = self.collection_schedaCliente.document()
            scheda_id = doc_ref.id
            dati = scheda.to_dict()
            dati['id'] = scheda_id
            dati['id_cliente'] = cliente_id
            doc_ref.set(dati)
            print(f"Scheda aggiunta: {scheda.id} per il cliente {cliente_id}")

            return True
        except Exception as e:
            print(f"Errore nell'aggiunta della scheda: {e}")
            return False
        
    def elimina_scheda_cliente(self, scheda_id:str):
        try:
            self.collection_schedaCliente.document(scheda_id).delete()
            print("scheda cliente eliminata correttamente")
            return True
        except Exception as e:
            print(f"Errore durante l'eliminazione della scheda cliente {e}")
            return False
        
    def update_scheda_cliente(self, scheda):
        try:
            doc_ref = self.collection_schedaCliente.document(scheda.id)
            # conveeto l'istanza della scheda in un dizionario
            dati = scheda.to_dict()
            # aggiorno il documento con i nuovi dati
            doc_ref.update(dati)
            return True
        except Exception as e:
            print(f"Errore durante la modifica della scheda: {e}")
            return False


    

            


    