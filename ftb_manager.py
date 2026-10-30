class Partida:
    def __init__(self, casa, visitante):
        self.casa = casa
        self.visitante = visitante
        self.placar_casa = 0
        self.placar_visitante = 0
        self.status = "Não iniciada"

    def escalar_jogador(self, jogador):
        if jogador.time == self.casa or jogador.time == self.visitante:
            jogador.jogando = True
            if jogador.time == self.casa:
                print(f"{jogador.nome} escalado no time {self.casa.nome}")
            else:
                print(f"{jogador.nome} escalado em {self.visitante.nome}")
        else:
            print("O jogador não faz parte de nenhum dos 2 times da partida!")

    def inscrever_jogadores(self, time):
        for i in time.jogadores:
            self.escalar_jogador(i)
                 
                
class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.gols = 0

    def adicionar_jogadores(self, jogadores):
        for jogador in jogadores:
            if jogador.time is None:
                self.jogadores.append(jogador)
                jogador.time = self
            else:
                print(f"Esse jogador já pertence ao {jogador.time.nome}, tente transferi-lo!")

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

    def status_jogador(self):
        if self.jogando:
            return print("Está em jogo")
        else:
            return print("Não está em jogo")