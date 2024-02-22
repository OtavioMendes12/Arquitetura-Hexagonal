from adaptadores.pedido_repositorio_memoria import PedidoRepositorioMemoria
from servicos.pedido_servico import PedidoServico

def main():
    repositorio = PedidoRepositorioMemoria()
    servico = PedidoServico(repositorio)

    pedido1 = servico.criar_pedido(1, "Pedido 1")
    pedido2 = servico.criar_pedido(2, "Pedido 2")

    servico.processar_pedido(1)

    for pedido in servico.listar_pedidos():
        print(f"Pedido ID: {pedido.id_pedido}, Status: {pedido.status}")

if __name__ == "__main__":
    main()
