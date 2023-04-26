import pygame

class Powerup:
    
    def __init__(self):
        
        self.shieldOn = False
        
        self.speedOn = False
        
        self.imageInit_shield = pygame.image.load("img/shield.png")

        self.image_shield = pygame.transform.scale(self.imageInit_shield, (150, 150))
        
        self.rect_shield = self.image_shield.get_rect()

    def PowerOn(self, indice):
        if indice == 1:
            self.shieldOn = True
        if indice == 2:
            self.speedOn = True
        self.TimeStart = pygame.time.get_ticks()
        
    def updateShield(self, x ,y):
        if self.shieldOn == True:
            time_spent_ticks = (pygame.time.get_ticks() - self.TimeStart) //1000
            self.rect_shield.x = x
            self.rect_shield.y = y
            if time_spent_ticks == 6:
                time_spent_ticks = 0
                self.shieldOn = False
        
    def SpeedBoost(self, player):
        if self.speedOn == True:
            time_spent_ticks = (pygame.time.get_ticks() - self.TimeStart) //1000
            player.speed = 8
            if time_spent_ticks == 6:
                time_spent_ticks = 0
                player.speed = 5
                self.speedOn = False