#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'haoyuanhsu'

import random


def guess_number():
    game_count = 0
    guess_count_list = list()
    min_number = int(input("範圍最小值(不包含)："))
    max_number = int(input("範圍最大值(不包含)："))
    init_min_number = min_number
    init_max_number = max_number
    while True:
        game_count += 1
        guess_count = 0
        answer = random.randint(init_min_number+1, init_max_number-1)
        game_finish = True
        while game_finish:
            player_guess = int(input("請輸入您要猜的數字(%d~%d)：" % (min_number, max_number)))
            if player_guess < min_number or player_guess > max_number:
                print("請猜範圍內的數字")
                continue
            guess_count += 1
            game_finish, max_number, min_number = compare_answer(
                player_guess, answer, game_finish, max_number, min_number)
        guess_count_list.append(guess_count)
        continue_play = input("是否要繼續玩(Y/N)：")
        if continue_play.upper() == "Y":
            # min_number, max_number 初始化
            min_number, max_number = init_min_number, init_max_number
            continue
        else:
            print("總共玩了 %s 局" % game_count)
            print("每一局分別猜了 %s 次" % guess_count_list)
            average_times = round(float(sum(guess_count_list)) / len(guess_count_list), 2)
            print("平局每一局玩了 %s 次" % average_times)
            break


def compare_answer(player_guess, answer, game_finish, max_number, min_number):
    if player_guess == answer:
        game_finish = False
        print("您猜對啦~~")
    elif player_guess > answer:
        max_number = player_guess
        print("猜太大啦~~")
    elif player_guess < answer:
        min_number = player_guess
        print("猜太小啦~~")
    return game_finish, max_number, min_number


if __name__ == '__main__':
    guess_number()
