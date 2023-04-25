import pygame 

class Bullet():

    def __init__(self, player_x, player_y):

        # Load images
        self.imageInit = pygame.image.load("img/egg.png")
            
        # Get good dimensions 
        self.image = pygame.transform.scale(self.imageInit, (10, 10))
        
        # Get rectangle from image
        self.rect = self.image.get_rect(center=(player_x,player_y))

        self.damage = 10
        
    def moveSelf(self, posx, posy):
        # Move
        self.rect = self.rect.move(posx, posy)
