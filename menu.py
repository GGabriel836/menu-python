from time import sleep
from datetime import date

tempo = 0.5

while True:
    print("-=" * 25)
    print("                     MENU")
    print("-=" * 25)
    print("[ 1 ] Calculadora")
    print("[ 2 ] Calendario")
    print("-=" * 25)

    opcao = int(input("Escolha sua opção... "))

    if opcao == 1:
        print("-=" * 25)
        print(">>> CALCULADORA <<<")
        print("     [ 1 ] Soma")
        print("     [ 2 ] Subtração")
        print("     [ 3 ] Multiplicação")
        print("     [ 4 ] Divisão")
        print("-=" * 25)
        sleep(tempo)
        calculo = int(input("Escolha seu calculo... "))

        if calculo == 1:
            print("Voce escolheu a SOMA")
            print("-=" * 25)
            sleep(tempo)
            n1 = int(input("Escolha um valor... "))
            n2 = int(input("Escolha outro valor... "))
            print("Calculando...")
            sleep(tempo)
            print("-=" * 25)
            print(f"O resultado da soma entre {n1} + {n2} é igual a : {n1 + n2}")
        elif calculo == 2:
            print("Voce escolheu a SUBTRAÇÃO")
            print("-=" * 25)
            sleep(tempo)
            n1 = int(input("Escolha um valor... "))
            n2 = int(input("Escolha outro valor... "))
            print("Calculando...")
            sleep(tempo)
            print("-=" * 25)
            print(f"O resultado da subtração entre {n1} - {n2} é igual a : {n1 - n2}")
        elif calculo == 3:
            print("Voce escolheu a MULTIPLICAÇÃO")
            print("-=" * 25)
            sleep(tempo)
            n1 = int(input("Escolha um valor... "))
            n2 = int(input("Escolha outro valor... "))
            print("Calculando...")
            sleep(tempo)
            print("-=" * 25)
            print(f"O resultado da multiplicação entre {n1} x {n2} é igual a : {n1 * n2}")
        elif calculo == 4:
            print("Voce escolheu a DIVISÃO")
            print("-=" * 25)
            sleep(tempo)
            n1 = int(input("Escolha um valor... "))
            n2 = int(input("Escolha outro valor... "))
            print("Calculando...")
            sleep(tempo)
            print("-=" * 25)
            print(f"O resultado da divisão entre {n1} / {n2} é igual a : {n1 / n2}")
        else:
            print("Essa opção não existe! Tente novamente...")
            print()
            print()
            print()
            print()
            print()

    elif opcao == 2:
        print("-=" * 25)
        print(">>> CALENDARIO <<<")
        print("     [ 1 ] Data atual")
        print("-=" * 25)
        sleep(tempo)
        resposta_cal = int(input("Escolha sua opção... "))

        if resposta_cal == 1:
            print(f"A data atual é {date.today().day}/{date.today().month}/{date.today().year}")
            print("-=" * 25)
            break
        else:
            print("Essa opção não existe! Tente novamente...")
            print()
            print()
            print()
            print()


    else:
        print("Essa opção não existe! Tente novamente...")
        print()
        print()
        print()
        print()
        print()


