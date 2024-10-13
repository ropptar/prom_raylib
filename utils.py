import pyray as pr

from assocs import *


def equal_rect(rec1: pr.Rectangle, rec2: pr.Rectangle):
    return (rec1.x == rec2.x
            and rec1.y == rec2.y
            and rec1.width == rec2.width
            and rec1.height == rec2.height)


def get_circle_rect(pos, r):
    return Rect(pos.x - r, pos.y - r,
                r * 2, r * 2)
