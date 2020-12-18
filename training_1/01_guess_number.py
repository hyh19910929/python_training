#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'haoyuanhsu'

import random


def guess_number():
    game_count = 0
    guess_count_list = list()
    min_number = int(input("Guess Minimum(not included)："))
    max_number = int(input("Guess Maximum(not included)："))
    init_min_number = min_number
    init_max_number = max_number
    while True:
        game_count += 1
        guess_count = 0
        answer = random.randint(init_min_number+1, init_max_number-1)
        game_finish = True
        while game_finish:
            player_guess = int(input("The number you guess (%d~%d): " %
                                     (min_number, max_number)))
            if player_guess < min_number or player_guess > max_number:
                print("The number you guess is out of range.")
                continue
            guess_count += 1
            game_finish, max_number, min_number = \
                compare_answer(player_guess, answer, game_finish,
                               max_number, min_number)
        guess_count_list.append(guess_count)
        continue_play = input("Continue? (Y/N): ")
        if continue_play.upper() == "Y":
            # initialize min_number and max_number initialize
            min_number = init_min_number
            max_number = init_max_number
            continue
        else:
            print("Totally play %s rounds." % game_count)
            print("Guess %s Rounds in each rounds." % guess_count_list)
            average_times = round(float(sum(guess_count_list)) /
                                  len(guess_count_list), 2)
            print("Averagely play %s times per round" % average_times)
            break


def compare_answer(player_guess, answer, game_finish, max_number,
                   min_number):
    if player_guess == answer:
        game_finish = False
        print("Wonderful! You have the correct answer!")
    elif player_guess > answer:
        max_number = player_guess
        print("It\'s too big.")
    elif player_guess < answer:
        min_number = player_guess
        print("It\'s too small.")
    return game_finish, max_number, min_number


if __name__ == '__main__':
    guess_number()
