import pygame
import random

class Zone :
    
    def __init__(self):

        self.zonetype = random.randrange(0,2,1)
        
        if self.zonetype == 0:
            self.imageInit = pygame.image.load("img/water.png")
            
        elif self.zonetype == 1:
            self.imageInit = pygame.image.load("img/fire.png")
        
        self.image = pygame.transform.scale(self.imageInit, (100, 25))

        self.rect = self.image.get_rect(center=(450,350))