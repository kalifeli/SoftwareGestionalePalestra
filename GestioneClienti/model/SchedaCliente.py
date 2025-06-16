from dataclasses import dataclass, field


@dataclass
class SchedaCliente:
    id:str = None
    id_cliente: str = ""
    peso: float = 0.0
    altezza: float = 0.0
    massa_muscolare: float = 0.0
    massa_grassa: float = 0.0
    bmi: float = 0.0
    misure: dict[str, float] = field(default_factory=dict)
    note : str = ""
    data_rilevazione : str = ""
    data_creazione: str = ""

    def to_dict(self):
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "peso": self.peso,
            "altezza": self.altezza,
            "massa_muscolare": self.massa_muscolare,
            "massa_grassa": self.massa_grassa,
            "bmi": self.bmi,
            "misure": self.misure,
            "note": self.note,
            "data_rilevazione": self.data_rilevazione,
            "data_creazione": self.data_creazione
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            id_cliente=data.get("id_cliente", ""),
            peso=data.get("peso", 0.0),
            altezza=data.get("altezza", 0.0),
            massa_muscolare=data.get("massa_muscolare", 0.0),
            massa_grassa=data.get("massa_grassa", 0.0),
            bmi=data.get("bmi", 0.0),
            misure=data.get("misure", {}),
            note=data.get("note", ""),
            data_rilevazione=data.get("data_rilevazione", ""),
            data_creazione=data.get("data_creazione", "")
        )