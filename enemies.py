import pygame

class Enemies():
    
    def __init__(self):
        
        self.imageInit = pygame.image.load("img/enemies.png")
        
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        # Get rectangle from image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 0

        self.health = 20
        self.speed = 2
        
    def update(self):
        
        
        self.rect.x += self.speed
        if self.speed > 0 and self.rect.x + self.rect.width >= 900:
            self.speed *= -1
        
        if self.speed < 0 and self.rect.x <= 0:
            self.speed *= -1
        
        
