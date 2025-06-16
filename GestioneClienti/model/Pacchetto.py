
from dataclasses import dataclass


@dataclass
class Pacchetto:
    id: int = None
    nome: str = None
    descrizione: str = None
    prezzo: float = None

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "prezzo": self.prezzo
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            id=data.get("id"),
            nome=data.get("nome"),
            descrizione=data.get("descrizione"),
            prezzo=data.get("prezzo")
        )
