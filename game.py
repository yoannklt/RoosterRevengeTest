import pygame
from player import Player

class Game():
    
    def __init__(self):
        self.screenWidth = 900 
        self.screenHeight =  700
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Rooster Revenge')
        
        self.player = Player()
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 0, 0))
            self.screen.blit(self.player.player, self.player.rectPlayer)
            pygame.display.flip()
        
  
  
              
        