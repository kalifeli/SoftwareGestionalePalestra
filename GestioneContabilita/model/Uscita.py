from enum import Enum
from dataclasses import dataclass

class TipoUscita(Enum):
    AFFITTO = "Affitto"
    MANUTENZIONE = "Manutenzione"
    ACQUISTI = "Acquisti"
    STIPENDI = "Stipendi"
    ALTRO = "Altro"

@dataclass
class Uscita:
    id: str = None
    descrizione: str = ""
    importo: float = 0.0
    data: str = ""
    tipo: TipoUscita = TipoUscita.ALTRO

    def to_dict(self):
        return {
            "descrizione": self.descrizione,
            "importo": self.importo,
            "data": self.data,
            "tipo": self.tipo.value
        }

    @staticmethod
    def from_dict(id: str, data: dict):
        return Uscita(
            id=id,
            descrizione=data.get("descrizione", ""),
            importo=data.get("importo", 0.0),
            data=data.get("data", ""),
            tipo=TipoUscita(data.get("tipo", "Altro"))
        )
