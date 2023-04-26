import pygame

class Player():
    
    def __init__(self):
        
        self.imageInit = pygame.image.load("img/player.png")
        
        self.image = pygame.transform.scale(self.imageInit, (75, 150))

        # Get rectangle from image
        self.rect = self.image.get_rect(center=(450, 600))

        
        self.health = 100
        
        self.takenDamage = 0
        
        self.speed = 5
    
    def update_health(self , screen , screenH):
        
        # si il se prend des dégâts on fait ça : self.player.damageTaken += self.ennemy_bullet.damage
        
        healthBar = 0
        if self.health != 0:
            healthBar = (self.takenDamage * 100)//self.health
        barW = 100 - healthBar
        barH = 15
        pygame.draw.rect(screen , (237, 0, 0)  , (5 , screenH - barH - 10, barW * 3 , barH))
        
    def drawScore(self, screen, posx, posy):
        myfont = pygame.font.SysFont("monospace", 32)
        self.score_display = myfont.render(str(self.score), 1, (0,0,0), (255, 255, 255))
        screen.blit(self.score_display, (posx, posy))

    def updateScore(self, value):
        self.score += value