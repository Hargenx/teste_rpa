from sistema_agendamento import SistemaAgendamento
from ferramenta_comunicacao import FerramentaComunicacao

def agendar_consulta(paciente, data, especialidade):
    sistema = SistemaAgendamento()
    comunicacao = FerramentaComunicacao()

    horario_disponivel = sistema.verificar_disponibilidade(data, especialidade)
    
    if horario_disponivel:
        consulta_agendada = sistema.agendar_consulta(paciente, data, especialidade)
        if consulta_agendada == True:
            mensagem = f"Olá {paciente}, sua consulta foi agendada para {data} na especialidade {especialidade}."
        
        comunicacao.enviar_mensagem(paciente, mensagem)
        
        return mensagem
    else:
        return "Desculpe, não há horários disponíveis para esta especialidade na data selecionada."

# Exemplo de uso da função para agendar uma consulta
paciente1 = "Raphael"
data_consulta = "2023-12-07"
especialidade_desejada = "Clinica Geral"

resultado_agendamento = agendar_consulta(paciente1, data_consulta, especialidade_desejada)
print(resultado_agendamento)
