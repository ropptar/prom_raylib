import math

import pyray as pr

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_REC = pr.Rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)


class Emoji:
    def __init__(self, pos: pr.Vector2 = pr.Vector2(0, 0), angle=9, r=100, face='0-o', font_size=50, text_col=pr.BLACK,
                 is_hollow=False,
                 col=pr.PURPLE):
        self.pos = pos
        self.angle = angle
        self.r = r
        self.face = face
        self.font_size = font_size
        self.text_col = text_col
        self.is_hollow = is_hollow
        self.col = col
        self.measure = pr.measure_text(face, font_size)
        self.rect=pr.Rectangle(self.pos.x-r,
                              self.pos.y-r,
                              self.pos.x+r,
                              self.pos.y+r)

    # move
    def move_xy(self, x_inc=1, y_inc=1):
        self.pos.x += x_inc
        self.pos.y += y_inc

    def move(self, inc):
        if self.check_wall():
            self.inverse_angle()
        self.pos.x += inc * math.cos(self.angle)
        self.pos.y -= inc * math.sin(self.angle)

    # draw
    def check_wall(self):
        return pr.get_collision_rec(self.rect,WINDOW_REC)!=self.rect

    def update(self):
        if self.is_hollow:
            pr.draw_circle_lines_v(self.pos, self.r, self.col)
        else:
            pr.draw_circle_v(self.pos, self.r, self.col)
        pr.draw_text(self.face, int(self.pos.x - self.measure / 2), int(self.pos.y - self.font_size / 2),
                     self.font_size,
                     self.text_col)

    # utils
    def inverse_angle(self):
        return self.update_angle(180)

    def update_angle(self, inc):
        self.angle = (self.angle + inc) % 360
        return self.angle


def main():
    emoji1 = Emoji(pr.Vector2(200, 300),angle=45, is_hollow=True)
    pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "graph_app")
    pr.set_window_state(2)
    pr.set_target_fps(60)
    while not pr.window_should_close():
        emoji1.move(10)
        pr.begin_drawing()
        pr.clear_background(pr.GRAY)
        emoji1.update()
        pr.end_drawing()


if __name__ == '__main__':
    main()
