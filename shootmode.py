import pygame
from bullet import Bullet

class Shootmode :
    
    def __init__(self):
        self.bullet_list = []
        self.bullet_list_left = []
        self.bullet_list_right = []
        self.type = 3
        
        
    def shoot(self , x , y):
        if self.type == 1 :
            self.bullet_list.append(Bullet(x, y))
        elif self.type == 2 :
            self.bullet_list.append(Bullet(x - 20, y + 30))
            self.bullet_list.append(Bullet(x + 20, y + 30))
        elif self.type == 3 :
            self.bullet_list.append(Bullet(x, y))
            self.bullet_list.append(Bullet(x - 20, y + 30))
            self.bullet_list.append(Bullet(x + 20, y + 30))
            
    def split(self, x, y):
        self.bullet_list_left.append(Bullet(x, y))
        self.bullet_list_right.append(Bullet(x, y))