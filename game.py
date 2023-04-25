import pygame
from player import Player
from bullet import Bullet
from enemies import Enemies

class Game():
    
    def __init__(self):
        self.screenWidth = 900 
        self.screenHeight =  700
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Rooster Revenge')
        self.clock = pygame.time.Clock()
        self.ticks = pygame.time.get_ticks()
        
        self.cooldown = 0
        self.player = Player()
        self.enemies = Enemies(450, 100)
        self.up = pygame.K_z
        self.down = pygame.K_s
        self.left = pygame.K_q
        self.right = pygame.K_d
        self.shoot = pygame.K_SPACE
        self.shots = []
        
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            key_states = pygame.key.get_pressed()
            if key_states[self.up]:
                self.player.rect.y -= 5
            if key_states[self.down]:
                self.player.rect.y += 5
            if key_states[self.left]:
                self.player.rect.x -= 5
            if key_states[self.right]:
                self.player.rect.x += 5
                 
            if key_states[self.shoot] and self.cooldown < pygame.time.get_ticks():
                self.cooldown = pygame.time.get_ticks() + 16 * 10
                self.shots.append(Bullet((self.player.rect.x + (self.player.rect.w // 2)), self.player.rect.y))

            self.screen.fill((0, 0, 0))
            
            for projectile in self.shots:
                self.screen.blit(projectile.image,projectile.rect)
                projectile.rect.y -= 10
                if projectile.rect.colliderect(self.enemies.rect):
                    self.shots.remove(projectile)
                    self.enemies.health -= projectile.damage 
                    if self.enemies.health <= 0:
                        print("mort")
                if projectile.rect.y < 0 :
                    self.shots.remove(projectile)
                    
                
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.enemies.image, self.enemies.rect)
            pygame.display.flip()
            clock.tick(60)
        
  
  
              
        