from typing import Optional

from GestioneClienti.daos.PtDaoFirebase import PtDaoFirebase
from GestioneClienti.model.SchedaCliente import SchedaCliente
from GestioneClienti.model.pt import PersonalTrainer


class PtController:
    def __init__(self, view):
        self.pt_dao = PtDaoFirebase()
        self.view = view

        if hasattr(self.view, "visualizzaClientiAssociati"):
            self.load_clienti_associati(view.pt.id)

    def get_pt_by_id(self, pt_id: str) -> Optional[PersonalTrainer]:
        """
        Recupera il PersonalTrainer attraverso il suo id
        """
        return self.pt_dao.get_pt_by_id(pt_id)

    def aggiorna_clienti_pt(self, pt_id: str) -> bool:
        return self.pt_dao.aggiorna_clienti_pt(pt_id)
    
    def get_clienti_associati_by_pt(self, pt_id: str):
        """
        Recupera tutti i clienti associati a un PT specifico.
        """
        return self.pt_dao.get_clienti_associati_by_pt(pt_id)
    
    def load_clienti_associati(self, pt_id: str):
        """
        Carica i clienti associati a un PT specifico e li visualizza nella view.
        """
        clienti = self.get_clienti_associati_by_pt(pt_id)
        if clienti:
            self.view.visualizzaClientiAssociati(clienti)

    def get_orario_pt(self, pt_id: str) -> dict:
        """
        Recupera l'orario di lavoro di un PT specifico.
        """
        return self.pt_dao.get_orario_pt(pt_id)
    
    def get_scheda_cliente(self, cliente_id:str) -> Optional[SchedaCliente]:
        """
        Recupera una scheda associata al cliente_id specificato
        """
        try:
            return self.pt_dao.get_scheda_cliente(cliente_id)
        except:
            print("Si è verificato un errore durante il recupero della scheda del cliente " + cliente_id )
            return None
        
    def add_scheda_cliente(self, scheda, cliente_id) -> bool:
            """
            Aggiunge una scheda al cliente specificato tramite il suo id
            """
            return self.pt_dao.add_scheda_cliente(cliente_id, scheda)
    
    def elimina_scheda_cliente(self, scheda_id:str) -> bool:
        """
        elimina una scheda di un cliente utilizzando la scheda_id
        """
        return self.pt_dao.elimina_scheda_cliente(scheda_id)
    
    def update_scheda_cliente(self, scheda: SchedaCliente) -> bool:
        """
        aggiorna le informazioni di una scheda cliente
        """
        return self.pt_dao.update_scheda_cliente(scheda)


        
