import pygame

class Enemies():
    
    def __init__(self, posx, posy):
        
        # Load images
        self.imageInit = pygame.image.load("img/enemies.png")
        
        # Get good dimensions 
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        # Get rectangle from image
        self.rect = self.image.get_rect(center=(posx,posy))

        self.health = 20

    def move(self, x, y):
        # Move
        self.rect.x = x
        self.rect.x = y
