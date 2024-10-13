import pyray as pr
import physics
from assocs import *
from utils import get_circle_rect


class Circle:
    def __init__(self, r, pos: Vector2 = Vector2(0, 0), col=Color, label='', fontsize=10):
        self.r = r
        self.pos = pos
        self.col = col
        self.rb = physics.RigidBody(get_circle_rect(self.pos, self.r))
        self.label = label
        self.fontsize = fontsize


def main():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    while not pr.window_should_close():
        pr.clear_background(pr.BLACK)
    pr.close_window()


if __name__ == '__main__':
    main()
