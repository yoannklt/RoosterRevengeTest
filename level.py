import pygame
from obstacle import Obstacle
from enemies import Enemies
from enemy_bullet import Enemy_bullet

class Level():
    
    def __init__(self):
    
        self.nbrbot = 3
        self.botlist = []
        
        self.bullet_list = []
        
        self.create = True
        
        self.enemies = [1, 1, 1, 4, 4, 5, 7, 10, 11, 13, 15, 4, 4, 5, 7, 10, 4, 4, 5, 7, 10, 4, 4, 5, 7, 10]
        
    def update(self, game):
        
        self.TimeStart = pygame.time.get_ticks()
                
        # self.rect.x += self.speed
        # if self.speed > 0 and self.rect.x + self.rect.width >= 900:
        #     self.speed *= -1
        
        # if self.speed < 0 and self.rect.x <= 0:
        #     self.speed *= -1
            
        for i in range(len(self.enemies)-1, -1, -1):
            if self.enemies[i] < (pygame.time.get_ticks() - game.timeStart) // 1000:
                self.enemies.pop(i)
                self.botlist.append(Enemies())
                
    def dislpay(self, game):
        for i in self.botlist:
            game.screen.blit(i.image, i.rect)
    
    def shoot(self, x , y):
            self.bullet_list.append(Enemy_bullet(x, y))

            