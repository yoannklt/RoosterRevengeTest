import pygame

class Enemies():
    
    def __init__(self):
        
        # Load images
        self.imageInit = pygame.image.load("img/enemies.png")
        
        # Get good dimensions 
        self.image = pygame.transform.scale(self.imageInit, (100, 175))

        # Get rectangle from image
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 0

        self.health = 20
        
    def update(self):
        
        goingRight = True
        goingLeft = False
        while goingRight:
            if self.rect.x + self.rect.width <= 900:
                self.rect.x += 2
            else :
                goingRight = False
                goingLeft = True
            
        while goingLeft:
            if self.rect.x >= 0:
                self.rect.x -= 2
            else :
                goingLeft = False
                goingRight = True
                

            
        
        
