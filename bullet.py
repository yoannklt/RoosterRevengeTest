import pygame 

class Bullet():

    def __init__(self, player_x, player_y):

        self.imageInit = pygame.image.load("img/egg.png")
            
        self.image = pygame.transform.scale(self.imageInit, (10, 10))
        
        self.rect = self.image.get_rect(center=(player_x,player_y))

        self.bullet_damage = 10
        
        self.bullet_type = 0
        
        self.velocity = 15
    
    def typeChange(self, type):
        self.bullet_type = type
        if type == 1:
            self.velocity = 5
            self.bullet_damage = 5
        elif type == 2:
            self.velocity = 8
            self.bullet_damage = 15
