import pygame
from enemy_bullet import Enemy_bullet
from random import randint

class Enemies():
    
    def __init__(self, cooldown):
        
        self.imageInit = pygame.image.load("img/enemies.png")
        
        self.image = pygame.transform.scale(self.imageInit, (160, 123))
        self.image = pygame.transform.flip(self.image, True, False)
        

        # Get rectangle from image
        self.rect = self.image.get_rect()
        
        self.rect.x = randint(0, 900)
        self.rect.y = -100
        
        self.health = 100
        self.bodyDamage = 5
        
        self.speed = 2
        
        self.points = 10
        
        self.TimeStart = pygame.time.get_ticks()
        
        if cooldown < 2:
            self.cooldown = 2
        else:
            self.cooldown = cooldown
        
    def update(self, game):
                   
        self.rect.x += self.speed
        if self.rect.y < 100:
            self.rect.y += 2
        if self.speed > 0 and self.rect.x + self.rect.width >= 900:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
        
        if self.speed < 0 and self.rect.x <= 0:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.timeSpent = (pygame.time.get_ticks() - self.TimeStart) // 1000
        print(self.timeSpent)
        
        if self.timeSpent > self.cooldown:
            self.shoot(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, game)
            self.TimeStart += self.cooldown * 1000
            
            

    def shoot(self, x, y, game):
        game.bullet_enemies.append(Enemy_bullet(x, y))