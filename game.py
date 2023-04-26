import pygame
from player import Player
from enemy_bullet import Enemy_bullet
from bullet import Bullet
from enemies import Enemies
from obstacle import Obstacle
from level import Level
from crates import Crates
from shootmode import Shootmode
from zone import Zone
from powerup import Powerup
from enemy_shot_mode import Enemy_shot_mode

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
        self.level = Level()
        self.shootmode = Shootmode()
        self.powerup = Powerup()
        self.enemy = Enemies()
        self.enemy_shot = Enemy_shot_mode()
        
        # Initialize keybinds
        self.up = pygame.K_z
        self.down = pygame.K_s
        self.left = pygame.K_q
        self.right = pygame.K_d
        self.shoot = pygame.K_SPACE
        
        self.crates = []
        
    def run(self):
        clock = pygame.time.Clock()
        self.timeStart = pygame.time.get_ticks()
        backgroundVelocity = 0
        running = True
        
        while running:
            
            backgroundY = -1400 + backgroundVelocity
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            key_states = pygame.key.get_pressed()
            
            if key_states[self.up]:
                self.player.rect.y -= self.player.speed
            if key_states[self.down]:
                self.player.rect.y += self.player.speed
            if key_states[self.left]:
                self.player.rect.x -= self.player.speed
            if key_states[self.right]:
                self.player.rect.x += self.player.speed
               
            if key_states[self.shoot] and self.cooldown < pygame.time.get_ticks():
                self.cooldown = pygame.time.get_ticks() + 120
                self.shootmode.shoot(self.player.rect.x + (self.player.rect.w // 2), self.player.rect.y)

    
            self.screen.fill((4, 16, 29))
            self.screen.blit(self.background, (0, backgroundY))
            
            # Lancer level 
            self.level.update(self)
            self.level.dislpay(self)
            
            if self.player.rect.colliderect(self.enemy.rect):
                self.player.takenDamage += self.enemy.bodyDamage
                                     
            for bullet in self.shootmode.bullet_list:
                self.screen.blit(bullet.image, bullet.rect)
                bullet.rect.y -= bullet.velocity
                if bullet.rect.colliderect(self.zone.rect):
                    if self.zone.type == 0:
                        bullet.typeChange(bullet.rect.x, bullet.rect.y, 1)
                    elif self.zone.type == 1:
                         bullet.typeChange(bullet.rect.x, bullet.rect.y, 2)
                         
                         
                        # ! split bullet cooldown DOIT ETRE REGLER !
                         if self.cooldown < pygame.time.get_ticks():
                            self.cooldown = pygame.time.get_ticks() + 20
                            self.shootmode.split(bullet.rect.x, bullet.rect.y)
                            
                            
                for bot in self.level.botlist :
                    if bullet.rect.colliderect(bot.rect):
                        if bullet in self.shootmode.bullet_list :
                            self.shootmode.bullet_list.remove(bullet)
                            bot.health -= bullet.bullet_damage 
                    if bot.health <= 0:
                        self.level.botlist.remove(bot)
                        self.crates.append(Crates(bot.rect.x + (bot.rect.w // 2), bot.rect.y + bot.rect.h))
                self.screen.blit(bullet.image, bullet.rect)
                if bullet.rect.y < 0:
                    self.shootmode.bullet_list.remove(bullet)
            
            for bullet in self.shootmode.bullet_list_left:
                bullet.typeChange(bullet.rect.x, bullet.rect.y, 2)
                self.screen.blit(bullet.image, bullet.rect)
                for bot in self.level.botlist :
                    if bullet.rect.colliderect(bot.rect):
                        self.shootmode.bullet_list_left.remove(bullet)
                        bot.health -= bullet.bullet_damage 
                    if bot.health <= 0:
                        self.level.botlist.remove(bot)
                        self.crates.append(Crates(bot.rect.x + (bot.rect.w // 2), bot.rect.y + bot.rect.h ))
                bullet.rect.y -= bullet.velocity
                bullet.rect.x -= bullet.velocity
                if bullet.rect.y < 0 or bullet.rect.x < 0:
                    self.shootmode.bullet_list_left.remove(bullet)

            for bullet in self.shootmode.bullet_list_right:
                bullet.typeChange(bullet.rect.x, bullet.rect.y, 2)
                self.screen.blit(bullet.image, bullet.rect)
                for bot in self.level.botlist :
                    if bullet.rect.colliderect(bot.rect):
                        if bullet in self.shootmode.bullet_list :
                            self.shootmode.bullet_list_right.remove(bullet)
                            bot.health -= bullet.bullet_damage 
                    if bot.health <= 0:
                        self.level.botlist.remove(bot)
                        self.crates.append(Crates(bot.rect.x + (bot.rect.w // 2), bot.rect.y + bot.rect.h ))
                bullet.rect.y -= bullet.velocity
                bullet.rect.x += bullet.velocity
                if bullet.rect.y < 0 or bullet.rect.x > 900:
                    self.shootmode.bullet_list_right.remove(bullet)
                
            for crates in self.crates:
                self.screen.blit(crates.image, crates.rect)
                crates.rect.y += crates.velocity   
                if crates.rect.colliderect(self.player.rect):
                    if crates.crate_type == 1:
                        self.player.health += crates.heal
                    elif crates.crate_type == 2:
                        self.powerup.PowerOn(1)
                    elif crates.crate_type == 3:
                        self.powerup.PowerOn(2)
                    self.crates.remove(crates) 
                if crates.rect.y < 0 :
                    self.crates.remove(crates)
            
            if self.powerup.speedOn == True:
                self.powerup.SpeedBoost(self.player)
                
            # Ajoute des éléments au rendu
            if self.powerup.shieldOn == True:
                self.powerup.updateShield(self.player.rect.x - (self.player.rect.w //2), self.player.rect.y)
                self.screen.blit(self.powerup.image_shield, self.powerup.rect_shield)
            
            self.screen.blit(self.zone.image, self.zone.rect)
            self.player.update_health(self.screen , self.screenHeight)
            self.screen.blit(self.player.image, self.player.rect)
            
            # Actualise le rendu
            pygame.display.flip()
            
            backgroundVelocity += 1
            clock.tick(60)
        
  
  
              
        