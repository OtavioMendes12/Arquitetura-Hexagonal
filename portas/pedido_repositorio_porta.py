from abc import ABC, abstractmethod
from dominio.pedido import Pedido

class PedidoRepositorioPorta(ABC):
    @abstractmethod
    def adicionar(self, pedido: Pedido):
        pass

    @abstractmethod
    def buscar_por_id(self, id_pedido: int) -> Pedido:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Pedido]:
        pass
