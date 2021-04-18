from pygame import *
from time import*
#создаём окошко
win_width = 700
win_height = 500
img_rocet = 'roket.jpg'
img_ball = 'ball.jpg'
display.set_caption("pin-pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('cartoon-stone.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
   

rocket1 = Player(img_rocet, 30, 200, 40, 50, 150)
rocket2 = Player(img_rocet, 520, 200, 40, 50, 150)
ball = GameSprite(img_ball, 200 , 200 , 4, 50, 50)

run = True
finish = False
FPS = 60
clock = time.Clock()
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while run:
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        #обновляем их в новом местоположении при каждой итерации цикла
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
        speed_x *= -1
        speed_y *= 1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
        game_over = True

    rocket1.reset()
    rocket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
   

    
