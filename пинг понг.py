from pygame import *
#from random import randint
win_height=500
win_width=700
player_image='roket'
def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x, size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y< win_height-80:
            self.rect.y+=self.speed
class Player2(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y< win_height-80:
            self.rect.y+=self.speed
'''
class Ball(GameSprite):
    def update(self):
        keys=key.get_pressed()
        self.rect.x += self.speed
        self.rect.y += self.speed
        if sprite.spritecollide(ball,valls):
            self.rect.y *= -1
'''





FPS=60


window= display.set_mode((700,500))
clock=time.Clock()
display.set_caption('Ping pong')
background = transform.scale(image.load('background.jpg'),(700, 500))

player1=Player1('roket.png',10,win_height/2,4, 80, 80)
player2=Player2('roket.png',win_width-80,win_height/2,4, 80, 80)
ball=GameSprite('ball.png',win_height/2,win_width/2,2, 50,50)
vall1=GameSprite('vall.png', 0, win_height-5,2, 1000,1000)
vall2=GameSprite('vall.png', 0,  0,2, 1000,10)

speed_x = 3
speed_y= 3
run= True
finish = False
while run:
    for e in event.get():
        if e.type==QUIT:
            run= False
    
    if finish !=True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *=-1
            speed_y*= 1
        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1
        player1.update()
        player2.update()
        ball.update()
        vall1.update()
        vall2.update()
        player1.reset()
        player2.reset()
        ball.reset()
        vall1.reset()
        vall2.reset()
        '''if sprite.spritecollide(player1,ball,False) or lost >=max_lost:
        if sprite.spritecollide(player2,ball,False) or lost >=max_lost:'''



    display.update()
    clock.tick(FPS)

