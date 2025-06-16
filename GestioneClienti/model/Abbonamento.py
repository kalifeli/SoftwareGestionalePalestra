
from dataclasses import dataclass
from datetime import date
from enum import Enum


class StatoAbbonamento(Enum):
    ATTIVO = "Attivo"
    SCADUTO = "Scaduto"
    SOSPESO = "Sospeso"


@dataclass
class Abbonamento:
    id: str = None
    id_cliente: str = None
    corso: str = ""
    pacchetto: str = ""
    data_inizio: str = date.today().strftime("dd-mm-yyyy")
    data_fine: str = date.today().strftime("dd-mm-yyyy")
    prezzo: float = 0.0
    saldato: bool = False
    stato: str = StatoAbbonamento.ATTIVO.value

    def to_dict(self):
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "corso": self.corso,
            "pacchetto": self.pacchetto,
            "data_inizio": self.data_inizio,
            "data_fine": self.data_fine,
            "prezzo": self.prezzo,
            "saldato": self.saldato,
            "stato": self.stato
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            id_cliente=data.get("id_cliente"),
            corso=data.get("corso"),
            pacchetto=data.get("pacchetto"),
            data_inizio=data.get("data_inizio"),
            data_fine=data.get("data_fine"),
            prezzo=data.get("prezzo"),
            saldato=data.get("saldato"),
            stato=data.get("stato")
        )
    
