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
    def move(self):
        move = input('rock, paper, scissors or quit >').lower()
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
            return self.their_move


class CyclePlayer(RandomPlayer):
    """
    继承 RadnomPlayer 类，循环采用不同的选择
    """
    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.my_move == "":
            return super().move()
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.result = {"p1": 0, "p2": 0}
        self.end = False

    def update_result(self, one, two):
        if one == two:
            print("It's is a tie!")
        elif beats(one, two):
            print("Player 1 won !")
            self.result['p1'] += 1
        else:
            print("Player 2 won!")
            self.result["p2"] += 1

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 != 'quit':
            print(f'Player 1: {move1}, Player 2: {move2}.')
            self.update_result(move1, move2)
            print(f"Score: Player one: {self.result['p1']}, Player two: {self.result['p2']}.")
            self.p1.learn(move1, move2)
            self.p2.learn(move1, move2)
        else:
            self.end = True

    def play_game(self):
        print("Game start!")
        round = 1
        while self.end == False and round <= 3:
            print(f'round: {round}')
            self.play_round()
            round += 1
        print('最终结果:')
        if self.result['p1'] == self.result['p2']:
            print('势均力敌！')
        elif self.result['p1'] > self.result['p2']:
            print('Player 1 胜出！')
        else:
            print('Player 2 胜出！')
        print(f'最后比分为: \n Player one: {self.result["p1"]} Player two: {self.result["p2"]}')

        
if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()