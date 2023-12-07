class FerramentaComunicacao:
    def enviar_mensagem(self, destinatario, mensagem):
        # Lógica para enviar mensagens de confirmação aos pacientes
        # pass
        # Suponhamos que estamos simulando e a mensagem sempre é enviada com sucesso
        mensagem_enviada = True if destinatario != "" and mensagem != "" else False
        return mensagem_enviada