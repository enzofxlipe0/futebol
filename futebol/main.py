
import random
import time
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def esperar():
    time.sleep(1)

def jogar():
    limpar()

    print("⚽ TERMINAL FOOTBALL ⚽")
    print("======================")
    time = input("Nome do seu time: ")

    adversarios = [
        "Real Python",
        "FC Terminal",
        "Manchester Code",
        "Barcelona.exe"
    ]

    adversario = random.choice(adversarios)

    seu_time = 0
    gols_ia = 0

    print("\nSeu time:", time)
    print("Adversário:", adversario)

    input("\nPressione ENTER para começar!")

    for minuto in range(1, 91, 5):
        limpar()

        print("⚽ TERMINAL FOOTBALL")
        print("======================")
        print(time, seu_time, "x", gols_ia, adversario)
        print("Minuto:", minuto)
        print("======================")

        print("\n1 - Chutar")
        print("2 - Passar")
        print("3 - Driblar")
        print("4 - Roubar a bola")

        escolha = input("\nO que deseja fazer? ")

        if escolha == "1":
            chance = random.randint(1, 100)

            print("\nVocê chutou!")

            if chance <= 30:
                seu_time += 1
                print("⚽ GOOOOOL!")
            elif chance <= 65:
                print("O goleiro defendeu!")
            else:
                print("A bola foi para fora!")

        elif escolha == "2":
            print("\nVocê fez um passe!")

            if random.randint(1, 100) <= 75:
                print("Passe completado!")
            else:
                print("Passe interceptado!")

        elif escolha == "3":
            print("\nVocê tentou um drible!")

            if random.randint(1, 100) <= 60:
                print("Drible bem sucedido!")
            else:
                print("Você perdeu a bola!")

        elif escolha == "4":
            print("\nVocê tentou roubar a bola!")

            if random.randint(1, 100) <= 50:
                print("Bola recuperada!")
            else:
                print("O adversário escapou!")

        else:
            print("\nComando inválido!")

        # Ataque adversário
        if random.randint(1, 100) <= 25:
            print("\nO adversário está atacando!")

            if random.randint(1, 100) <= 20:
                gols_ia += 1
                print("⚽ Gol do adversário!")

        input("\nENTER para continuar...")

    limpar()

    print("======================")
    print("       FIM DE JOGO")
    print("======================")
    print(time, seu_time, "x", gols_ia, adversario)

    if seu_time > gols_ia:
        print("\n🏆 VOCÊ VENCEU!")
    elif seu_time < gols_ia:
        print("\n😢 VOCÊ PERDEU!")
    else:
        print("\n🤝 EMPATE!")

    input("\nPressione ENTER para sair.")


jogar()
