import pygame

class Player():
    
    def __init__(self):
        
        self.imageInit = pygame.image.load("img/player.png")
        
        self.image = pygame.transform.scale(self.imageInit, (75, 150))

        # Get rectangle from image
        self.rect = self.image.get_rect(center=(450, 600))

        
        self.health = 100