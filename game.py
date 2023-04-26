import pygame
from player import Player
from bullet import Bullet
from enemies import Enemies
from obstacle import Obstacle
from level import Level
from crates import Crates
from shootmode import Shootmode
from zone import Zone

class Game():
    
    def __init__(self):
        self.screenWidth = 900 
        self.screenHeight =  700
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption('Rooster Revenge')
        
        self.cooldown = 0
        # Initialize backgrounds
        self.background = pygame.image.load('img/background.jpg')
        self.background.convert()
        
        # Initialize classes
        self.player = Player()
        self.zone = Zone()
        self.testlevel = Level()
        self.shootmode = Shootmode()
        self.up = pygame.K_z
        self.down = pygame.K_s
        self.left = pygame.K_q
        self.right = pygame.K_d
        self.shoot = pygame.K_SPACE
        self.crates = []
        
    def run(self):
        clock = pygame.time.Clock()
        backgroundVelocity = 0
        running = True
        
        while running:
            backgroundY = -1400 + backgroundVelocity
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
                self.cooldown = pygame.time.get_ticks() + 120
                self.shootmode.shoot(self.player.rect.x + (self.player.rect.w // 2), self.player.rect.y)
                # (Bullet((self.player.rect.x + (self.player.rect.w // 2)), self.player.rect.y))

            # Lancer level 
            if self.testlevel.create == True :
                # self.testlevel.createObsatcle()
                self.testlevel.createBot()
                self.testlevel.create = False
                    
            self.screen.fill((4, 16, 29))
            self.screen.blit(self.background, (0, backgroundY))
            
            # for obstacle in self.testlevel.obstaclelist :
            #     self.screen.blit(obstacle.image, obstacle.rect)
            #     obstacle.rect.y += 2
            for bot in self.testlevel.botlist :
                bot.update()
                self.screen.blit(bot.image, bot.rect)
                              
            for projectile in self.shootmode.bullet_list:
                self.screen.blit(projectile.image, projectile.rect)
                projectile.rect.y -= projectile.velocity
                if projectile.rect.colliderect(self.zone.rect):
                    if self.zone.zonetype == 0:
                        projectile.typeChange(projectile.rect.x, projectile.rect.y, 1)
                    elif self.zone.zonetype == 1:
                         projectile.typeChange(projectile.rect.x, projectile.rect.y, 2)
                         self.shootmode.split(projectile.rect.x, projectile.rect.y)
                for bot in self.testlevel.botlist :
                    if projectile.rect.colliderect(bot.rect):
                        self.shootmode.bullet_list.remove(projectile)
                        bot.health -= projectile.bullet_damage 
                    if bot.health <= 0:
                        self.testlevel.botlist.remove(bot)
                        self.crates.append(Crates(bot.rect.x + (bot.rect.w // 2), bot.rect.y + bot.rect.h ))
                if projectile.rect.y < 0 :
                    self.shootmode.bullet_list.remove(projectile)
            
            for projectile in self.shootmode.bullet_list_left:
                self.screen.blit(projectile.image, projectile.rect)
                projectile.rect.y -= projectile.velocity
                projectile.rect.x -= projectile.velocity
                if projectile.rect.y < 0 or projectile.rect.x < 0:
                    self.shootmode.bullet_list_left.remove(projectile)

            for projectile in self.shootmode.bullet_list_right:
                self.screen.blit(projectile.image, projectile.rect)
                projectile.rect.y -= projectile.velocity
                projectile.rect.x += projectile.velocity
                if projectile.rect.y < 0 or projectile.rect.x > 900:
                    self.shootmode.bullet_list_right.remove(projectile)
                
            for crates in self.crates:
                self.screen.blit(crates.image, crates.rect)
                crates.rect.y += crates.velocity   
                if crates.rect.colliderect(self.player.rect):
                    if crates.crate_type == 1:
                        self.player.health += crates.heal
                    self.crates.remove(crates) 
                if crates.rect.y < 0 :
                    self.crates.remove(crates)
            
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.zone.image, self.zone.rect)
            pygame.display.flip()
            backgroundVelocity += 1
            clock.tick(60)
        
  
  
              
        