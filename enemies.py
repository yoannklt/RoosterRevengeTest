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
        
        self.health = 20
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
        if self.timeSpent >= self.cooldown:
            self.shoot(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, game)
            self.TimeStart += self.cooldown + 1000
            self.timeSpent = 0

    def shoot(self, x, y, game):
        game.bullet_enemies.append(Enemy_bullet(x, y))
        
    def checkScore(self, score):
        if score > 50:
            self.cooldown = 2.75
        # if score < 100:
        #     self.cooldown = 2.5
        # if score < 150:
        #     self.cooldown = 2.25
        # if score < 200:
        #     self.cooldown = 2
        # if score < 250:
        #     self.cooldown = 1.75
        # if score < 300:
        #     self.cooldown = 1.5
        # if score < 350:
        #     self.cooldown = 1.25
        # if score < 400:
        #     self.cooldown = 1