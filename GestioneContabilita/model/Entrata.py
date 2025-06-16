from enum import Enum
from dataclasses import dataclass

class TipoEntrata(Enum):
    ABBONAMENTO = "Abbonamento"
    ISCRIZIONE = "Iscrizione"
    PRODOTTI = "Prodotti"
    ALTRO = "Altro"

@dataclass
class Entrata:
    id: str = None
    descrizione: str = ""
    importo: float = 0.0
    data: str = ""
    tipo: TipoEntrata = TipoEntrata.ALTRO

    def to_dict(self):
        return {
            "descrizione": self.descrizione,
            "importo": self.importo,
            "data": self.data,
            "tipo": self.tipo.value
        }

    @staticmethod
    def from_dict(id: str, data: dict):
        return Entrata(
            id=id,
            descrizione=data.get("descrizione", ""),
            importo=data.get("importo", 0.0),
            data=data.get("data", ""),
            tipo=TipoEntrata(data.get("tipo", "Altro"))
        )
