# CONSTANTES dos Limites (nomes iguais ao do código de Edge)
TEMP_ATENCAO = 28
TEMP_PERIGO = 32
UMID_ATENCAO_BAIXA = 30
UMID_PERIGO_BAIXA = 20
UMID_ALTA = 85
HORAS_ATENCAO = 12   # no Wokwi: 24 s (1 h = 2 s)
HORAS_PERIGO = 13    # no Wokwi: 26 s

DATA = "15/11/2026"

# registros=[hora, temperatura (°C), umidade (%), horas desde o último check-in]
registros = [
    ["06:00", 27.5, 80, 10],
    ["07:00", 28.9, 82, 11],
    ["08:00", 30.1, 88, 0],    # check-in da manhã feito às 8h
    ["09:00", 31.1, 78, 1],
    ["10:00", 32.0, 70, 2],
    ["15:00", 34.0, 58, 7],    # pico de calor
    ["19:00", 32.7, 65, 11],
    ["20:00", 32.0, 70, 12],   # horário do check-in da noite
    ["21:00", 31.1, 75, 13],   # check-in não feito: alerta ao porteiro
    ["22:00", 30.1, 80, 1],    # porteiro verificou, idosa fez o check-in às 21h
    ["23:00", 28.9, 84, 2],
    ["24:00", 27.5, 88, 3],
]

# ---------------- Classificação dos Sensores ----------------
# Segui a ordem de Edge: a primeira condição verdadeira ganha.
def classificar(temperatura, umidade, horas_checkin):
    if horas_checkin >= HORAS_PERIGO:
        estado = "PERIGO"
        mensagem = "SEM CHECK-IN 13h"
    elif temperatura >= TEMP_PERIGO:
        estado = "PERIGO"
        mensagem = "CALOR PERIGOSO!"
    elif umidade < UMID_PERIGO_BAIXA:
        estado = "PERIGO"
        mensagem = "AR MUITO SECO!"
    elif umidade > UMID_ALTA and temperatura >= TEMP_ATENCAO:
        estado = "PERIGO"
        mensagem = "CALOR + UMIDADE!"
    elif horas_checkin >= HORAS_ATENCAO:
        estado = "ATENÇÃO"
        mensagem = "Faca check-in"
    elif temperatura >= TEMP_ATENCAO:
        estado = "ATENÇÃO"
        mensagem = "Calor: beba agua"
    elif umidade < UMID_ATENCAO_BAIXA:
        estado = "ATENÇÃO"
        mensagem = "Ar seco"
    elif umidade > UMID_ALTA:
        estado = "ATENÇÃO"
        mensagem = "Ar muito umido"
    else:
        estado = "OK"
        mensagem = "Tudo bem"

    return [estado, mensagem]


# ---------------- Opções do menu ----------------
def mostrar_leituras():
    print()
    print("Leituras do dia", DATA)
    print("Hora | Temp. | Umid. | Sem check-in | Estado | Aviso")

    for registro in registros:
        hora = registro[0]
        temperatura = registro[1]
        umidade = registro[2]
        horas_checkin = registro[3]

        resultado = classificar(temperatura, umidade, horas_checkin)
        estado = resultado[0]
        mensagem = resultado[1]

        print(hora, "|", temperatura, "°C |", umidade, "% |", horas_checkin, "h |", estado, "|", mensagem)


# ---------------- Resumo ----------------
def calcular_resumo(lista):
    ''' Devolve [média da temperatura, maior temperatura, hora da maior, 
    qtd em alerta, qtd em perigo]'''
    soma = 0
    maior = lista[0][1]
    hora_maior = lista[0][0]
    qtd_alerta = 0
    qtd_perigo = 0

    for registro in lista:
        temperatura = registro[1]
        soma = soma + temperatura

        if temperatura > maior:
            maior = temperatura
            hora_maior = registro[0]

        resultado = classificar(registro[1], registro[2], registro[3])
        if resultado[0] != "OK":
            qtd_alerta += 1
        if resultado[0] == "PERIGO":
            qtd_perigo += 1

    media = soma / len(lista)
    return [media, maior, hora_maior, qtd_alerta, qtd_perigo]


    lista_teste = [
        ["10:00", 20, 50, 0],   # OK
        ["11:00", 30, 50, 0],   # ATENÇÃO (calor)
        ["12:00", 34, 50, 0],   # PERIGO (calor perigoso)
        ["13:00", 24, 50, 0],   # OK
    ]
    # Esperado: média 27.0, maior 34 às 12:00, 2 em alerta, 1 em perigo
    resumo = calcular_resumo(lista_teste)

    if resumo == [27.0, 34, "12:00", 2, 1]:
        print("Teste do resumo: PASSOU")
    else:
        print("Teste do resumo: FALHOU -> obtido:", resumo)


def mostrar_resumo():
    resumo = calcular_resumo(registros)
    media = resumo[0]
    maior = resumo[1]
    hora_maior = resumo[2]
    qtd_alerta = resumo[3]
    qtd_perigo = resumo[4]
    total = len(registros)
    percentual = qtd_alerta / total * 100

    print()
    print("Resumo do dia", DATA)
    print("Média da temperatura:", round(media, 1), "°C")
    print("Maior temperatura:", maior, "°C às", hora_maior)
    print("Leituras em alerta (ATENÇÃO ou PERIGO):", qtd_alerta, "de", total, "-", round(percentual, 1), "%")
    print("Leituras em PERIGO:", qtd_perigo, "de", total)

    if qtd_perigo > 0:
        print("AVISO: houve leituras em PERIGO. Beba água e mantenha a casa ventilada.")


# ---------------- Menu do nosso Programa ----------------
def main():
    opcao = ""

    while opcao != "0":
        print()
        print("=== TôBem · Copacabana ===")
        print("1 - Fazer check-in agora")
        print("2 - Ver leituras do dia")
        print("3 - Resumo do dia")
        print("4 - Testar uma leitura")
        print("5 - Ver regras e limites")
        print("0 - Sair")
        opcao = input("> ").strip()

        if opcao == "1":
            print("fazer check-in")
        elif opcao == "2":
            mostrar_leituras()
        elif opcao == "3":
            mostrar_resumo()
        elif opcao == "4":
            print("testar uma leitura")
        elif opcao == "5":
            print("regras e limites")
        elif opcao == "0":
            print("Até logo! Cuide-se.")
        else:
            print("Opção inválida. Digite um número de 0 a 5.")


main()