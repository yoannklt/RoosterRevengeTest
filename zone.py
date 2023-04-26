import pygame
import random
from shootmode import *
from player import * 
from bullet import *

class Zone():
    
    def __init__(self):
        
        self.type = random.randrange(0,2,1)
        
        if self.type == 0:
            self.imageInit = pygame.image.load("img/water.png") 
        elif self.type == 1:
            self.imageInit = pygame.image.load("img/fire.png")
        
        self.image = pygame.transform.scale(self.imageInit, (100, 25))

        self.rect = self.image.get_rect(center=(450,350))
        
        # Initialize classes
        self.shootmode = Shootmode()
        self.player = Player()
        self.bullet = Bullet(self.player.rect.x, self.player.rect.y)
    
        
    def updateShot(self, bullet):

            bullet.rect.y -= bullet.velocity
            if bullet.rect.colliderect(self.rect):
                if self.type == 0:
                    bullet.typeChange(bullet.rect.x, bullet.rect.y, 1)
                elif self.type == 1:
                    bullet.typeChange(bullet.rect.x, bullet.rect.y, 2)
                    self.shootmode.split(bullet.rect.x, bullet.rect.y)
            
                    

            