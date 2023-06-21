import random

def jogar_pedra_papel_tesoura():
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")

    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_usuario = int(input("Digite o número da sua escolha: "))
    escolha_computador = random.randint(1, 3)

    print("Você escolheu:", opcoes[escolha_usuario - 1])
    print("O computador escolheu:", opcoes[escolha_computador - 1]) #Para corresponder ao "-1" do opções, o de baixo também necessita de um "-1", assim, fazendo o código funcionar.   

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 1 and escolha_computador == 3) or (escolha_usuario == 2 and escolha_computador == 1) or (escolha_usuario == 3 and escolha_computador == 2):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogar_pedra_papel_tesoura()
    else:
        print("Obrigado por jogar!")

jogar_pedra_papel_tesoura()
