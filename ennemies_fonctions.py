import pygame
from obstacle import Obstacle
from enemies import Enemies
from enemy_bullet import Enemy_bullet

class Ennemies_fonctions():
    
    def __init__(self):
    
        self.nbrbot = 3
        self.botlist = []
        self.bot_x = [100 , 450  , 800]
        self.bot_y = [100 , 150  , 200]
        
        self.bullet_list = []
        
        self.create = True

    def createBot(self) :
        for i in range (self.nbrbot) :
            self.botlist.append(Enemies(self.bot_x[i], self.bot_y[i]))
        
    def update(self):
        
        self.TimeStart = pygame.time.get_ticks()
                
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.x + self.rect.width >= 900:
            self.speed *= -1
        
        if self.speed < 0 and self.rect.x <= 0:
            self.speed *= -1
    
    def shoot(self, x , y):
            self.bullet_list.append(Enemy_bullet(x, y))

            