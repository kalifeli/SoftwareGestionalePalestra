import firebase_admin
from firebase_admin import firestore

from utils.firebase_client import get_firestore_client
from .IContabilitaDao import IContabilitaDao
from GestioneContabilita.model.Entrata import Entrata
from GestioneContabilita.model.Uscita import Uscita

class ContabilitaDaoFirebase(IContabilitaDao):

    def __init__(self):
        self.client = get_firestore_client()

    def aggiungi_entrata(self, entrata: Entrata):
        doc_ref = self.client.collection('entrate').document()
        doc_ref.set(entrata.to_dict())

    def get_entrate(self):
        docs = self.client.collection('entrate').stream()
        return [Entrata.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def aggiorna_entrata(self, entrata_id, nuovi_dati):
        self.client.collection('entrate').document(entrata_id).update(nuovi_dati)

    def elimina_entrata(self, entrata_id):
        self.client.collection('entrate').document(entrata_id).delete()

    def aggiungi_uscita(self, uscita: Uscita):
        doc_ref = self.client.collection('uscite').document()
        doc_ref.set(uscita.to_dict())

    def get_uscite(self):
        docs = self.client.collection('uscite').stream()
        return [Uscita.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def aggiorna_uscita(self, uscita_id, nuovi_dati):
        self.client.collection('uscite').document(uscita_id).update(nuovi_dati)

    def elimina_uscita(self, uscita_id):
        self.client.collection('uscite').document(uscita_id).delete()
