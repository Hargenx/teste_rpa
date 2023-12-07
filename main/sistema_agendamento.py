class SistemaAgendamento:
    def verificar_disponibilidade(self, data, especialidade):
        # Lógica para verificar a disponibilidade de horários na base de dados
        # Retorna True se houver horários disponíveis para a especialidade na data especificada
        # Caso contrário, retorna False
        # pass
    # Suponhamos que estamos simulando e sempre há disponibilidade
        disponibilidade = True if especialidade != "Indisponível" else False
        return disponibilidade
    
    def agendar_consulta(self, paciente, data, especialidade):
        # Lógica para agendar a consulta na base de dados
        # Retorna True se a consulta foi agendada com sucesso
        # Caso contrário, retorna False
        # pass
        # Suponhamos que estamos simulando e a consulta sempre é agendada com sucesso
        consulta_agendada = True if paciente != "" and especialidade != "" else False
        return consulta_agendada