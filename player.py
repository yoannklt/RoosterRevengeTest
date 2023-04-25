import pygame

class Player():
    
    def __init__(self):
        
        # Load images
        self.imageInit = pygame.image.load("img/player.png")
        
        # Get good dimensions 
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        # Get rectangle from image
        self.rect = self.image.get_rect()
        self.rect.x = 200

