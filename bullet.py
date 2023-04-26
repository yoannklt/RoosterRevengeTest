import pygame 

class Bullet():

    def __init__(self, player_x, player_y):

        self.imageInit = pygame.image.load("img/egg.png")
            
        self.image = pygame.transform.scale(self.imageInit, (10, 10))      
        
        self.imageInit_white = pygame.image.load("img/egg_white.png")   
        self.image_white = pygame.transform.scale(self.imageInit_white, (10, 10))
                  
        self.imageInit_yellow = pygame.image.load("img/egg_yellow.png")  
        self.image_yellow = pygame.transform.scale(self.imageInit_yellow, (10, 10))
            
        self.rect = self.image.get_rect(center=(player_x,player_y))

        self.bullet_damage = 10
        
        self.velocity = 15
    
    def typeChange(self, bullet_x, bullet_y, type):
        
        self.bullet_type = type
        
        if type == 1:
            
            self.imageInit = self.imageInit_white 
            self.image = self.image_white
            self.rect = self.image.get_rect(topleft=(bullet_x,bullet_y))
            
            self.velocity = 5
            self.bullet_damage = 5
            
        elif type == 2:

            self.imageInit = self.imageInit_yellow
            self.image = self.image_yellow
            self.rect = self.image.get_rect(topleft=(bullet_x,bullet_y))
            
            self.velocity = 2
            self.bullet_damage = 15
