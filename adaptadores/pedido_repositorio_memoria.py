from portas.pedido_repositorio_porta import PedidoRepositorioPorta
from dominio.pedido import Pedido

class PedidoRepositorioMemoria(PedidoRepositorioPorta):
    def __init__(self):
        self._pedidos = {}

    def adicionar(self, pedido: Pedido):
        self._pedidos[pedido.id_pedido] = pedido

    def buscar_por_id(self, id_pedido: int) -> Pedido:
        return self._pedidos.get(id_pedido)

    def listar_todos(self) -> list[Pedido]:
        return list(self._pedidos.values())
