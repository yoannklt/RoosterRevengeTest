import pygame
from bullet import Bullet
from player import Player

class Powerup:
    
    def __init__(self):
        
        self.shieldOn = False
        
        self.imageInit_shield = pygame.image.load("img/shield.png")

        self.image_shield = pygame.transform.scale(self.imageInit_shield, (150, 150))
        
        self.rect_shield = self.image_shield.get_rect()

    def updateShield(self, x ,y):
        if self.shieldOn == True:
            time_spent_ticks = (pygame.time.get_ticks() - self.shieldTimeStart) //1000
            self.rect_shield.x = x
            self.rect_shield.y = y
            print(time_spent_ticks)
            if time_spent_ticks == 6:
                time_spent_ticks = 0
                self.shieldOn = False
        
    def setShieldOn(self):
        self.shieldOn = True
        self.shieldTimeStart = pygame.time.get_ticks()