

from dataclasses import dataclass


@dataclass
class Corso:
    id: int = None
    nome: str = None
    descrizione: str = None
    durata_mesi: int = None
    prezzo: float = None
    pt_assegnati: list = None  # Lista di ID dei Personal Trainer assegnati al corso

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "durata_mesi": self.durata_mesi,
            "prezzo": self.prezzo,
            "pt_assegnati": self.pt_assegnati or []
        }

    @classmethod
    def from_dict(cls,data):
        return cls(
            id=data.get("id"),
            nome=data.get("nome"),
            descrizione=data.get("descrizione"),
            durata_mesi=data.get("durata_mesi"),
            prezzo=data.get("prezzo"),
            pt_assegnati=data.get("pt_assegnati")
        )
