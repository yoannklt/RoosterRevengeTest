import pygame

class Player():
    
    def __init__(self):
        
        self.imageInit = pygame.image.load("img/player.png")
        
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        self.rect = self.image.get_rect(center=(450,600))
        
        self.health = 100

    def move(self, x, y):
        # Move
        self.rect.x = x
        self.rect.x = y
