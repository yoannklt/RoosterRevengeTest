import pygame
from player import Player
from enemy import Enemy

class Game():
    
    def __init__(self):
        self.screenWidth = 900 
        self.screenHeight =  700
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Rooster Revenge')
        
        self.player = Player()
        self.enemy = Enemy()
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if pygame.Rect.colliderect(self.player.rectPlayer, self.enemy.rectEnemy):
                    self.player.rectPlayer = self.player.rectPlayer.move(-10, 0)


            self.screen.fill((255, 0, 0))
            self.screen.blit(self.player.player, self.player.rectPlayer)
            self.screen.blit(self.enemy.enemy, self.enemy.rectEnemy)
            pygame.display.flip()
        
  
  
              
        