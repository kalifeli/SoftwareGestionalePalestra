import firebase_admin
from firebase_admin import firestore

from utils.firebase_client import get_firestore_client
from .IContabilitaDao import IContabilitaDao
from GestioneContabilita.model.Entrata import Entrata
from GestioneContabilita.model.Uscita import Uscita

class ContabilitaDaoFirebase(IContabilitaDao):

    def __init__(self):
        self.client = get_firestore_client()
        self.collection_entrate = self.client.collection('entrate')
        self.collection_uscite = self.client.collection('uscite')


    def aggiungi_entrata(self, entrata: Entrata):
        doc_ref = self.collection_entrate.document()
        doc_ref.set(entrata.to_dict())

    def get_entrate(self):
        docs = self.collection_entrate.stream()
        return [Entrata.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def aggiorna_entrata(self, entrata_id, nuovi_dati):
        self.collection_entrate.document(entrata_id).update(nuovi_dati)

    def elimina_entrata(self, entrata_id):
        self.collection_entrate.document(entrata_id).delete()

    def aggiungi_uscita(self, uscita: Uscita):
        doc_ref = self.collection_uscite.document()
        doc_ref.set(uscita.to_dict())

    def get_uscite(self):
        docs = self.collection_uscite.stream()
        return [Uscita.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def aggiorna_uscita(self, uscita_id, nuovi_dati):
        self.collection_uscite.document(uscita_id).update(nuovi_dati)

    def elimina_uscita(self, uscita_id):
        self.collection_uscite.document(uscita_id).delete()
