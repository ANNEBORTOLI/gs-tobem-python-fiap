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

# ---------------- Programa principal ----------------
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
            print("leituras do dia")
        elif opcao == "3":
            print("resumo do dia")
        elif opcao == "4":
            print("testar uma leitura")
        elif opcao == "5":
            print("regras e limites")
        elif opcao == "0":
            print("Até logo! Cuide-se.")
        else:
            print("Opção inválida. Digite um número de 0 a 5.")


main()