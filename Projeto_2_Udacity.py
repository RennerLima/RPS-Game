import random

moves = ['pedra', 'papel', 'tesoura']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):

        player_move = input(', '.join(moves) + '?' + ' > ')

        while player_move not in moves:
            player_move = input(', '.join(moves) + '?' + ' > ')

        return player_move


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return Player.move(self)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.last_play = None

    def move(self):
        play = None
        if self.last_play is None:
            play = Player.move(self)
        else:
            index = moves.index(self.last_play) + 1
            play = moves[index % len(moves)]
        self.last_play = play
        return play


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = game.check_result(move1, move2)

        print(f"Jogador A: {move1}  Jogador B: {move2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # Vitoria do jogador A
        if result == "jogadorAvitoria":
            self.p1.score += 1
            print("Jogador A ganhou!\n")

        # Vitoria do jogador B
        elif result == "jogadorBvitoria":
            self.p2.score += 1
            print("Jogador B ganhou!\n")

        # Empate
        else:
            print("Empate!\n")

        print("O placar ficou: Jogador A %s x %s Jogador B\n" %
              (str(self.p1.score), str(self.p2.score)))

    def beats(draw, one, two):

        if (one == 'pedra' and two == 'tesoura'):
            return True

        elif (one == 'tesoura' and two == 'papel'):
            return True

        elif (one == 'papel' and two == 'pedra'):
            return True

        return False

    def check_result(draw, one, two):
        if game.beats(one, two):
            return "jogadorAvitoria"

        if game.beats(two, one):
            return "jogadorBvitoria"

        else:
            return "empate"

    def play_game(self):
        print("O jogo vai começar!\n")

        partidas = int(input("Quantos rounds você quer jogar? "))

        for partidas in range(partidas):

            print(f"Round {partidas}:")

            self.play_round()

        print("Bom jogo!")


if __name__ == '__main__':
    player_pool_text = """Você pode escolher entre os seguintes jogadores:
      Humano: Você controla os movimentos
      Rocker: PC sempre escolhe pedra
      Random: PC esolhe movimentos randomicamente
      Cycler: PC alterna entre pedra, papel e tesoura
      Reflect: PC utiliza o seu ultimo movimento"""

    player_pool = {
        'humano': HumanPlayer(),
        'rocker': Player(),
        'random': RandomPlayer(),
        'cycler': CyclePlayer(),
        'reflect': ReflectPlayer()
        }

    print(player_pool_text)
    player1 = input("Quem e o jogador 1?").lower()
    player2 = input("Quem e o jogador 2?").lower()

    while player1 not in player_pool or player2 not in player_pool:
        player1 = input("Quem e o jogador 1?").lower()
        player2 = input("Quem e o jogador 2?").lower()

    game = Game(player_pool[player1], player_pool[player2])
    game.play_game()
