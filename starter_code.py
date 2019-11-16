#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    """这个 Player 的类是所有 Player 类别的父类。你将编写多个与 Player 有关的类。
    """
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    """继承 Player 类 随机输出
    """
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """继承 Player 类 并接受人类输入结果.
    """
    def __init__(self):
        print('you need to chose "paper" or "rock" or "scissors" each time')

    def move(self):
        move = input('paper, rock, scissors or quit >').lower()
        while move not in ['paper', 'rock', 'scissors', 'quit']:
            print("无效输入，请再试一次!")
            move = input('Please choose rock, paper, scissors, or quit >').lower()
        if move != 'quit':
            print(f"You played {move}.")
        return move


class ReflectPlayer(RandomPlayer):
    """继承 RandomPlayer 输出对手上一次的选择.
    """
    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.their_move == "":
            return super().move()
        else:
            return self.
        return self.next_move

    





class CyclePlayer(Player):

    def __init__(self):
        self.index = 0

    def move(self):
        return moves[self.index % 3]

    def learn(self, my_move, their_move):
        self.index += 1


def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        return 1
    elif ((one == 'rock' and two == 'paper') or
            (one == 'scissors' and two == 'rock') or
            (one == 'paper' and two == 'scissors')):
        return 2
    else:
        return 0


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = beats(move1, move2)
        if result == 1:
            self.p1.score += 1
        elif result == 2:
            self.p2.score += 1
        else:
            print(f'Player 1 and Player 2 have same move {move1},{move2}')
        print(f"P 1: {move1} {self.p1.score}  P 2: {move2} {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()