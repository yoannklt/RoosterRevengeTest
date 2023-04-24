import pygame

class Player():
    
    def __init__(self):
        
        # Load images
        self.imageInit = pygame.image.load("img/character.png")
        
        # Get good dimensions 
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        # Get rectangle from image
        self.rect = self.image.get_rect()
    
    def moveSelf(self, posx, posy):
        # Move
        self.rect = self.rect.move(posx, posy)
