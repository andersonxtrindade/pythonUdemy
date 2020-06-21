from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_completo(self):
        return f"Eu sou {self.nome} {self.sobrenome}"