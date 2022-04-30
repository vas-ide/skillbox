# -*- coding: utf-8 -*-

import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def bubble(point=sd.get_point(-400, -400), step=10):
    radius = 1700
    for _ in range(7):
        radius += step
        sd.circle(point, radius, width=15, color=rainbow_colors[_])


def sun(center_position=sd.get_point(400, 500), radius=50, width=3):
    sd.circle(center_position=sd.get_point(400, 500), radius=50, width=0)
    sd.line(start_point=sd.get_point(320, 500), end_point=sd.get_point(480, 500), width=4)
    sd.line(start_point=sd.get_point(400, 580), end_point=sd.get_point(400, 420), width=4)
    sd.line(start_point=sd.get_point(350, 560), end_point=sd.get_point(450, 440), width=4)
    sd.line(start_point=sd.get_point(350, 440), end_point=sd.get_point(450, 560), width=4)





