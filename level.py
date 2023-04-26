import pygame
from obstacle import Obstacle
from enemies import Enemies
from enemy_bullet import Enemy_bullet
from random import randint

class Level():
    
    def __init__(self):
    
        self.nbrbot = 3
        self.botlist = []
        
        self.bullet_list = []
        
        self.create = True
        
        self.enemies = [5,5,5]
    
        
    def update(self, game):
        
        self.TimeStart = pygame.time.get_ticks()
        
        for i in self.botlist:
            i.update(game)
         
        for i in range(len(self.enemies)-1, -1, -1):   
            if self.enemies[i] < (pygame.time.get_ticks() - game.timeStart) // 1000:
                if len(self.botlist) < 3:
                    self.enemies.pop(i)
                    self.botlist.append(Enemies(5 - game.player.score / 200))
                    self.enemies.append(randint(self.enemies[-1],self.enemies[-1] + 5 ))   
                
    def dislpay(self, game):
        for i in self.botlist:
            game.screen.blit(i.image, i.rect)

            