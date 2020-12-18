#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'haoyuanhsu'

import random


def guess_number():
    game_count = 0
    guess_count_list = list()
    while True:
        game_count += 1
        guess_count = 0
        min_number = int(input("範圍最小值："))
        max_number = int(input("範圍最大值："))
        answer = random.randint(min_number, max_number)
        while True:
            player_guess = int(input("請輸入您要猜的數字(%d~%d)：" % (min_number, max_number)))
            if player_guess < min_number or player_guess > max_number:
                print("請猜範圍內的數字")
                continue
            guess_count += 1
            if player_guess == answer:
                break
            elif player_guess > answer:
                max_number = player_guess
                print("猜太大啦~~")
            elif player_guess < answer:
                min_number = player_guess
                print("猜太小啦~~")
        print("您猜對啦~~")
        guess_count_list.append(guess_count)
        continue_play = input("是否要繼續玩(Y/N)：")
        if continue_play.upper() == "Y":
            continue
        else:
            print("總共玩了 %s 局" % game_count)
            print("每一局分別猜了 %s 次" % guess_count_list)
            average_times = round(float(sum(guess_count_list)) / len(guess_count_list), 2)
            print("平局每一局玩了 %s 次" % average_times)
            break


if __name__ == '__main__':
    guess_number()
