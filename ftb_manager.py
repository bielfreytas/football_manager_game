class Partida:
    def __init__(self, casa, visitante):
        self.casa = casa
        self.visitante = visitante
        self.placar_casa = 0
        self.placar_visitante = 0
        self.status = "Não iniciada"

    def escalar_jogador(self, jogador):
        if jogador.time == self.casa or jogador.time == self.visitante:
            if jogador.time == self.casa:
                print(f"Jogador escalado no time {self.casa.nome}")
                self.jogando = True 
            else:
                print(f"Jogador escalado em {self.visitante.nome}")
                self.jogando = True


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.gols = 0

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        jogador.time = self
      
class Jogador:
    def __init__(self, nome, idade, posicao):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.energia = 100
        self.gols = 0
        self.time = None
        self.jogando = False

    def mostrar_info(self): 
        print(f"""
    ==== INFORMAÇÕES ====
    Nome: {self.nome}
    Idade: {self.idade}
    Posição: {self.posicao}
    Energia: {self.energia}
    Número de gols: {self.gols}
    """)

    def marcar_gol(self):
        if self.jogando:
            print(f"{self.nome} marcou um gol!")
            self.gols += 1
            self.gastar_energia()
        else:
            print("Jogador não está em jogo!")

    def gastar_energia(self):
        if self.energia <= 20:
            self.energia = 0
            self.jogando = False
        else:
            self.energia -= 20

    def recuperar_energia(self, dias):
        if not self.jogando and self.energia < 100:
            for _ in range(dias):
                if (100 - self.energia) >= 15:
                    self.energia += 15
                else:
                    self.energia = 100
                    print("Jogador recuperado!")
                    break