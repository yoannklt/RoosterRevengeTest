import pygame

class Player():
    
    def __init__(self):
        
        # Load images
        self.player = pygame.image.load("img/character.png")
        
        # Get rectangle from image
        self.rectPlayer = self.player.get_rect()
        
        # Move
        self.rectPlayer = self.rectPlayer.move(100, 100)