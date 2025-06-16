from dataclasses import dataclass, field
from typing import List

from GestioneClienti.model.Cliente import Sesso


@dataclass
class PersonalTrainer:
    id: str = None
    nome: str = ""
    cognome: str = ""
    username: str = ""
    password: str = ""
    sesso: str = Sesso.MASCHIO.value
    stipendio: float = 0.0
    orario: dict[str, str] = field(default_factory=dict)
    clienti: List[str] = field(default_factory=list)
    corsi: List[str] = field(default_factory=list)

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "username": self.username,
            "password": self.password,
            "sesso": self.sesso,
            "stipendio": self.stipendio,
            "orario": self.orario,
            "clienti": self.clienti,
            "corsi": self.corsi
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
        id=data.get("id"),
        nome=data.get("nome", ""),
        cognome=data.get("cognome", ""),
        username=data.get("username", ""),
        password=data.get("password", ""),
        sesso=data.get("sesso", Sesso.MASCHIO.value),
        stipendio=data.get("stipendio", 0.0),
        orario=data.get("orario", {}),
        clienti=data.get("clienti", []),
        corsi=data.get("corsi", [])
    )


        
        




