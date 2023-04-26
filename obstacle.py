import pygame

class Obstacle():
    
    def __init__(self, x, y , w, h):
        
        self.imageInit = pygame.image.load("img/obstacle.png")
        
        self.image = pygame.transform.scale(self.imageInit, (w, h))

        self.rect = self.image.get_rect(topleft=(x,y))

