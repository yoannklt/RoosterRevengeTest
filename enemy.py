import pygame

class Enemy():
    
    def __init__(self):
        
        self.imageInit = pygame.image.load("img/enemy.png")
        self.image = pygame.transform.scale(self.imageInit, (150, 100))

        self.rect = self.image.get_rect()
        
        self.rect = self.rect.move(300, 100)