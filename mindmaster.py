def menu ():
    mensagem = ("Vamos Jogar Mastermind! \nserá gerado um número aleatorio de 4 digitos \nTente advinhar o numero gerado. Boa Sorte!")
    print("*" * 45)
    print(mensagem)
    print("*" * 45)
    
def jogo ():
    palpite = 0
    parabens = ("Parabéns, você é o mestre do jogo advinhou todos os 4 numeros!")
    import random
    numero_gerado = str (random.randint(1000,9999))
    while True:
        palpite = input("Informe um numero entre 1000 e 9999:")
        
        numeros_corretos = 0
        for i in range(4):
            if palpite[i] == numero_gerado[i]:
                numeros_corretos += 1
            
        for i in range(4):
            if palpite[i] in numero_gerado[i]:
                print("O numero", palpite[i], "está no campo", numero_gerado.index(palpite[i]) + 1, "-", numero_gerado.rindex(palpite[i])+1)
            
        if numeros_corretos == 4:
            print(parabens)
            break
            
        else:
            numeros_errados = 0
            for i in range(4):
                if palpite[i] in numero_gerado and palpite[i] != numero_gerado[i]:
                    numeros_errados += 1
                    
            print("Voce acertou", numeros_corretos, "na posição certa")
            print("Voce acertou", numeros_errados, "na posição errada")

menu()

jogo()