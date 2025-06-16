
from dataclasses import dataclass
from enum import Enum

class Sesso(Enum):
    MASCHIO = "Maschio"
    FEMMINA = "Femmina"
    ALTRO = "Altro"

@dataclass
class Cliente:
    id: str = None
    nome: str = ""
    cognome: str = ""
    sesso: str = Sesso.MASCHIO.value
    data_nascita: str = ""
    email: str = ""
    telefono: str = ""
    certificatoMedico: bool = False  # Indica se il cliente ha un certificato medico valido

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cognome": self.cognome,
            "sesso": self.sesso,
            "data_nascita": self.data_nascita,
            "email": self.email,
            "telefono": self.telefono,
            "certificatoMedico": self.certificatoMedico,
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            id=data.get("id"),
            nome=data.get("nome", ""),
            cognome=data.get("cognome", ""),
            sesso=data.get("sesso", Sesso.MASCHIO.value),
            data_nascita=data.get("data_nascita", ""),
            email=data.get("email", ""),
            telefono=data.get("telefono", ""),
            certificatoMedico=data.get("certificatoMedico", ""),
        )

