# -*- coding: utf-8 -*-

import simple_draw as sd


def snowfall_initional(N):
    def snowdrift():
        left_bottom = sd.get_point(-100, -100)
        right_top = sd.get_point(350, 7)
        sd.ellipse(left_bottom, right_top, color=sd.COLOR_WHITE)

    dict_x_snowfall = {}
    dict_y_snowfall = {}
    dict_len_snowfall = {}
    for _ in range(N):
        dict_x_snowfall[_] = sd.random_number(50, 200)
        dict_y_snowfall[_] = sd.random_number(100, 600)
        dict_len_snowfall[_] = sd.random_number(10, 25)

    couter = 0
    while True:
        sd.clear_screen()
        sd.start_drawing()
        snowdrift()
        for _ in range(N):
            x = dict_x_snowfall[_]
            y = dict_y_snowfall[_]
            length = dict_len_snowfall[_]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length)
            if y > 0:
                dict_x_snowfall[_] += sd.random_number(-15, 15)
                dict_y_snowfall[_] -= 5
            if x < 20 and y > 0:
                dict_x_snowfall[_] += 20
                dict_y_snowfall[_] -= 5
            if x > 230 and y > 0:
                dict_x_snowfall[_] -= 20
                dict_y_snowfall[_] -= 5
            if y < -5:
                dict_y_snowfall[_] = -5

        sd.finish_drawing()
        sd.sleep(0.1)
        if y <= 0:
            break
        if sd.user_want_exit():
            break

