import pygame
from player import Player
from enemy import Enemy

class Game():
    
    def __init__(self):
        self.screenWidth = 900 
        self.screenHeight =  700
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Rooster Revenge')
        
        # Initialize backgrounds
        self.background = pygame.image.load('img/background.jpg')
        self.background.convert()
        
        # Initialize classes
        self.player = Player()
        self.enemy = Enemy()
        
    def run(self):
        clock = pygame.time.Clock()
        backgroundVelocity = 0
        running = True
        
        while running:
            backgroundY = -1400 + backgroundVelocity
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if pygame.Rect.colliderect(self.player.rect, self.enemy.rect):
                    self.player.moveSelf(-10, 0)


            self.screen.fill((4, 16, 29))
            self.screen.blit(self.background, (0, backgroundY))
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.enemy.image, self.enemy.rect)
            pygame.display.flip()
            backgroundVelocity += 0.8
            clock.tick(60)
        
  
  
              
        