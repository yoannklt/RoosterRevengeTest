import pygame 
import random

class Crates():

    def __init__(self, x, y):

        # self.crate_type = random.randrange(1 , 4)
        self.crate_type = 3
        
        if self.crate_type == 1:
            self.imageInit = pygame.image.load("img/heal.png")
        else:
            self.imageInit = pygame.image.load("img/powerup.png")
            
        self.image = pygame.transform.scale(self.imageInit, (20, 20))
        
        self.rect = self.image.get_rect(center=(x,y))
        
        self.velocity = 2
        
        self.heal = 10
        
    