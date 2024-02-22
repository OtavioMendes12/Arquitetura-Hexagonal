from portas.pedido_repositorio_porta import PedidoRepositorioPorta
from dominio.pedido import Pedido

class PedidoServico:
    def __init__(self, repositorio: PedidoRepositorioPorta):
        self._repositorio = repositorio

    def criar_pedido(self, id_pedido: int, detalhes: str):
        pedido = Pedido(id_pedido, detalhes)
        self._repositorio.adicionar(pedido)
        return pedido

    def processar_pedido(self, id_pedido: int):
        pedido = self._repositorio.buscar_por_id(id_pedido)
        if pedido:
            pedido.processar()
            return pedido
        return None

    def listar_pedidos(self):
        return self._repositorio.listar_todos()
