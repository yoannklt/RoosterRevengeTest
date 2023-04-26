import pygame
from enemy_bullet import Enemy_bullet
from random import randint

class Enemies():
    
    def __init__(self):
        
        self.imageInit = pygame.image.load("img/enemies.png")
        
        self.image = pygame.transform.scale(self.imageInit, (160, 123))
        self.image = pygame.transform.flip(self.image, True, False)
        

        # Get rectangle from image
        self.rect = self.image.get_rect()
        
        self.rect.x = randint(0, 900)
        self.rect.y = randint(0, 300)
        
        self.health = 20
        self.damage = 5
        
        self.speed = 2
        
        
    def update(self):
        
        self.TimeStart = pygame.time.get_ticks()
                
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.x + self.rect.width >= 900:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
        
        if self.speed < 0 and self.rect.x <= 0:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
        
        
        
         
            