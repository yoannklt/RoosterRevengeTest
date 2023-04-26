import pygame
from enemy_bullet import Enemy_bullet

class Enemy_shot_mode():
    
    def __init__(self):
        self.bullet_list = []
        
    def shoot(self , x , y):
            self.bullet_list.append(Enemy_bullet(x, y))
                    
    def update(self):
        for enemy in self.bullet_list:
            enemy.rect.y += enemy.velocity
            
    def display(self, game):
        for enemy in self.bullet_list:
            game.screen.blit(enemy.image, enemy.rect)