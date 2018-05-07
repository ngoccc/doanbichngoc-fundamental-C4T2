# hự chưa xong đâu ạ a đừng xemm ;-;

import pygame, sys
from pygame.locals import *

# make colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window_height = 300
window_width = 400

display_surf = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping pong")

fps = 60
fps_clock = pygame.time.Clock()


class Paddle():
    def __init__(self, x, w, h):
        self.w = w
        self.h = h
        self.x = x
        self.y = int(window_height) / 2
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        pygame.draw.rect(display_surf, WHITE, self.rect)

    def move(self, y):
        self.y += y
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.draw()


class Scoreboard():
    def __init__(self, fontSize=20, score1=0, score2=0):
        self.x = window_width - 150
        self.y = 20
        self.score1 = score1
        self.score2 = score2
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)

    def display(self, score1, score2):
        result_srf = self.font.render(str(score1) + " - " + str(score2), True, WHITE)
        display_surf.blit(result_srf, (window_width / 2 - 20, 20))


class Ball():
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.dir_x = -1  # left = -1 and right = 1
        self.dir_y = -1  # up = -1 and down = 1
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        pygame.draw.rect(display_surf, WHITE, self.rect)

    def bounce(self, axis):
        if axis == 'x':
            self.dir_y *= -1
        if axis == 'y':
            self.dir_x *= -1

    def hit_ceiling(self):
        if self.dir_y == -1 and self.rect.top <= self.h:
            return True
        else:
            return False

    def hit_floor(self):
        if self.dir_y == 1 and self.rect.bottom >= window_height - self.h:
            return True
        else:
            return False

    def hit_wall1(self):
        if self.dir_x == -1 and self.rect.left <= self.w:
            return True
        else:
            return False

    def hit_wall2(self):
        if self.dir_x == 1 and self.rect.right >= window_width - self.w:
            return True
        else:
            return False

    def hit_paddle1(self, paddle):
        if (self.rect.left <= paddle.rect.right) and (self.rect.bottom >= paddle.rect.top) and (
                self.rect.top <= paddle.rect.bottom):
            return True
        else:
            return False

    def hit_paddle2(self, paddle):
        if (self.rect.right >= paddle.rect.left) and (self.rect.bottom >= paddle.rect.top) and (
                self.rect.top <= paddle.rect.bottom):
            return True
        else:
            return False

    def move(self):
        self.rect.x += self.dir_x * self.speed
        self.rect.y += self.dir_y * self.speed

        if self.hit_ceiling() or self.hit_floor():
            self.bounce('x')

    def setpos(self, x, y):
        self.x = x
        self.y = y

# bảo là đừng xem cơ màaa

class Game():
    def __init__(self, line_thickness=10, speed=1):
        self.line_thickness = line_thickness
        self.speed = speed
        ball_x = int(window_width / 2)
        ball_y = int(window_height / 2)
        ball_w = self.line_thickness
        ball_h = self.line_thickness
        self.ball = Ball(ball_x, ball_y, ball_w, ball_h, self.speed)

        self.paddles = {}
        paddle_x = 20
        paddle_w = self.line_thickness
        paddle_h = 50

        self.paddles['user1'] = Paddle(paddle_x, paddle_w, paddle_h)
        self.paddles['user2'] = Paddle(window_width - paddle_x - self.line_thickness, paddle_w, paddle_h)

        self.score = Scoreboard()

    def draw_arena(self):
        display_surf.fill((255, 255, 255))
        pygame.draw.rect(display_surf, BLACK, (10, 10, window_width - 20, window_height - 20))
        pygame.draw.line(display_surf, WHITE, (window_width / 2, 0), (window_width / 2, window_height))

    def update(self):
        self.ball.move()
        if self.ball.hit_paddle1(self.paddles['user1']):
            self.ball.bounce('y')

        if self.ball.hit_paddle2(self.paddles['user2']):
            self.ball.bounce('y')

        if self.ball.hit_wall1():
            if self.score.score2 == 5:
                return True
            else:
                self.restart()
                #self.score.score2 += 1

        if self.ball.hit_wall2():
            if self.score.score1 == 5:
                return True
            else:
                self.restart()
                #self.score.score1 += 1

        self.draw_arena()
        self.ball.draw()
        self.paddles['user1'].draw()
        self.paddles['user2'].draw()
        self.score.display(self.score.score1, self.score.score2)
    
    # ơ hay đừng xem nữa mà ạ em đang fix lỗi chỗ nì :"( e đi ngủ đây đã
    def restart(self):
        self.ball.setpos(int(window_width / 2), int(window_height / 2))


def main():
    pygame.init()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                m1 = 0
                m2 = 0
                if keys[pygame.K_UP]:
                    m1 = -20
                elif keys[pygame.K_DOWN]:
                    m1 = 20
                elif keys[pygame.K_w]:
                    m2 = -20
                elif keys[pygame.K_s]:
                    m2 = 20
                game.paddles['user1'].move(m1)
                game.paddles['user2'].move(m2)
        game.update()
        if game.update():
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fps_clock.tick(fps)
    # print('Your score: ',game.score.score)


if __name__ == '__main__':
    main()
