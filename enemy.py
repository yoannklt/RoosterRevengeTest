import pygame

class Enemy():
    
    def __init__(self):
        
        self.enemy = pygame.image.load("img/enemy.png")
        
        self.rectEnemy = self.enemy.get_rect()
        
        self.rectEnemy = self.rectEnemy.move(300, 100)