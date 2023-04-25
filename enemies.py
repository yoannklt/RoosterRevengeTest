import pygame

class Enemies():
    
    def __init__(self, posx, posy):
        
        self.imageInit = pygame.image.load("img/enemies.png")
        
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        self.rect = self.image.get_rect(center=(posx,posy))

        self.health = 20
