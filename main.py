from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,
                player_x, player_y,
                size_x, size_y,
                player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(
            image.load(player_image), (
                size_x, size_y
            ))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (
            self.rect.x, self.rect.y
        ))
 
 
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:

            self.rect.x += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.x += self.speed


back = (6, 94, 189)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60


racket_1 = Player("racket.png", 20, 200, 4, 50, 150)
racket_2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER1 LOSE", 1, (180, 0, 0))
lose2 = font.render("PLAYER1 LOSE", 1, (180, 0, 0))

speedx = 3
speedy = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish is not True:
        window.fill(back)
        racket_1.update_l()
        racket_2.update_r()
        ball.rect.x += speedx
        ball.rect.y += speedy
        racket_1.reset()
        racket_2.reset()
        ball.reset()
    display.update
    clock.tick(FPS)