import pygame
from enemy_bullet import Enemy_bullet

class Enemies():
    
    def __init__(self, x, y):
        
        self.imageInit = pygame.image.load("img/enemies.png")
        
        self.image = pygame.transform.scale(self.imageInit, (100, 175))
        
        self.rect = self.image.get_rect(center=(x, y))
        
        self.health = 20
        
        self.speed = 2
        
    def update(self):
        
        self.TimeStart = pygame.time.get_ticks()
                
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.x + self.rect.width >= 900:
            self.speed *= -1
        
        if self.speed < 0 and self.rect.x <= 0:
            self.speed *= -1
    
    def shootPattern(self):
        time_spent_ticks = (pygame.time.get_ticks() - self.TimeStart) //1000
        if time_spent_ticks == 2:
            # self.shoot()
            time_spent_ticks = 0