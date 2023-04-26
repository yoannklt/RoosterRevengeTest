import pygame 

class Enemy_bullet():

    def __init__(self, enemie_x, enemie_y):

        self.imageInit = pygame.image.load("img/laser.png")
            
        self.image = pygame.transform.scale(self.imageInit, (20, 20))
        
        self.rect = self.image.get_rect(center=(enemie_x,enemie_y))

        self.bullet_damage = 10
        
        self.velocity = 10