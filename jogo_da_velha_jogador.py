#Jogo da velha -  versão jogador vs jogador
#Em processo de implementação de versão Jogador vs Computador (IA) - versão 1.0

def mostrar_tabuleiro(tab):
    for i in range(0, 9, 3):  # pula de 3 em 3: início de cada linha (0, 3, 6)
        print(f"{tab[i]} / {tab[i+1]} / {tab[i+2]}") # imprime as 3 posições daquela linha
        if i < 6: # não imprime divi´soria depois da ùltima linha
            print("---+---+---")


def verificar_vencedor(tab, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # linhas 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # colunas 
        [0, 4, 8], [2, 4, 6],            # diagonais 
    ]
    for combo in combinacoes: #all e combo vão operar em conjunto sobre as operações de verificação de vitória, retornando True se todas as posições da combinação forem ocupadas pelo mesmo jogador.
        if all(tab[i] == jogador for i in combo): # so retorna true se as 3 forem do mesmo jogador, caso contrário retorna false
            return True 
    return False #nenhuma combinação bateu, por isso retornou false


def tabuleiro_cheio(tab):
    return " " not in tab # se não houver espaços vazios, o tabuleiro está cheio, retornando True. Caso contrário, retorna False.


def jogador_humano(tab, jogador):
    while True: #repete até que o jogador escolha uma posição válida
        pos = int(input(f"Jogador {jogador}, escolha uma posição (0-8): "))
        if tab[pos] == " ": #posição está vazia, então o jogador pode ocupar
            tab[pos] = jogador
            break # sai do loop. jogada feita
        else:
            print("Posição ocupada, tente outra.") #volta para o início do loop/while, para que o jogador escolha outra posição.


def jogar():
    tab = [" " for _ in range(9)] #tabuleiro startando vazio, com 9 posições 0-8
    jogador_atual = "X" # O jogador X é sempre o primeiro a jogar. A cada jogada o jogador atual alterna entre X e O

    while True: #loop principal do jogo, até que haja um vencedor ou empate
        mostrar_tabuleiro(tab)
        jogador_humano(tab, jogador_atual)

        if verificar_vencedor(tab, jogador_atual):
            mostrar_tabuleiro(tab)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if tabuleiro_cheio(tab):
            mostrar_tabuleiro(tab)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"
# os espaços do tabuleiro são representados por uma lista de 9 elementos, onde cada elemento pode ser "X", "O" ou " "

# A orientação do tabuleiro é a seguinte:
# 0 / 1 / 2
# ---+---+---
# 3 / 4 / 5
# ---+---+---
# 6 / 7 / 8 

jogar()
