import tkinter as tk
import random

numero_gerado = str(random.randint(1000, 9999))

def menu():
    mensagem = "Vamos Jogar Mastermind!\nSerá gerado um número aleatório de 4 dígitos.\nTente adivinhar o número gerado. Boa sorte!"
    nota.config(text=mensagem)

def jogo():
    global numero_gerado
    parabens = "Parabéns, você é o mestre do jogo e adivinhou todos os 4 números!"
    try:
        entrada_jogador = entrada.get()
        if len(entrada_jogador) != 4:
            raise ValueError("Entrada inválida")
        palpite = int(entrada_jogador)
    except ValueError:
        resultado.config(text="Entrada inválida. Por favor, digite um número inteiro de 4 dígitos.")
        return
    
    if 1000 <= palpite <= 9999:
        numeros_corretos = 0
        numeros_errados = 0
        posicoes_corretas = []
        posicoes_erradas = []
        for i in range(4):
            if str(palpite)[i] == numero_gerado[i]:
                numeros_corretos += 1
                posicoes_corretas.append(i)
            elif str(palpite)[i] in numero_gerado:
                numeros_errados += 1
                posicoes_erradas.append(i)
                
        if numeros_corretos == 4:
            resultado.config(text=parabens)
        else:
            mensagem = f"Você acertou {numeros_corretos} número(s) na posição correta"
            if numeros_corretos > 0:
                posicoes = ""
                for pos in posicoes_corretas:
                    posicoes += str(pos+1) + ", "
                posicoes = posicoes[:-2]
                mensagem += f" nas posições {posicoes}."
            if numeros_errados > 0:
                posicoes = ""
                for pos in posicoes_erradas:
                    posicoes += str(pos+1) + ", "
                posicoes = posicoes[:-2]
                mensagem += f"\nVocê acertou {numeros_errados} número(s) na posição errada."
            resultado.config(text=mensagem)
    else:
        resultado.config(text="Número inserido não está entre 1.000 e 9.999. Tente novamente.")




janela = tk.Tk()
janela.title("Mastermind")
janela.configure(bg="#add8e6")

nota = tk.Label(janela, text="", bg ="#add8e6", font=("Display", 15))
nota.grid(row=0, column=0)
menu()

palpite_jogador = tk.Label(janela, text="Digite um número de 4 dígitos entre 1000 e 9999 para tentar adivinhar:", bg ="#add8e6", font=("Arial", 15))
palpite_jogador.grid(row=1, column=0)

entrada = tk.Entry(janela)
entrada.grid(row=2, column=0)

botao_gerar = tk.Button(janela, text="Confirmar", command=jogo)
botao_gerar.grid(row=3, column=0)

resultado = tk.Label(janela, text="", bg="#add8e6", font=("Arial", 15))
resultado.grid(row=4, column=0)

janela.mainloop()






