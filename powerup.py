import pygame

class Powerup():
    
    def __init__(self, x, y):
        
        self.imageInit = pygame.image.load("img/shield.png")
        
        self.image = pygame.transform.scale(self.imageInit, (150, 175))

        self.rect = self.image.get_rect(center=(x, y))
