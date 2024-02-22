class Pedido:
    def __init__(self, id_pedido, detalhes, status='Pendente'):
        self.id_pedido = id_pedido
        self.detalhes = detalhes
        self.status = status

    def processar(self):
        self.status = 'Processado'
