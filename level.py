import pygame
from obstacle import Obstacle
from enemies import Enemies

class Level:
    
    def __init__(self):
        
        # obstacle
        self.obstaclelist = []
        
        self.create = True 
        
        # Full Map
        self.nbrobstacle = 45
        self.obstacle_x = [0, 100, 0, 0, 500, 250, 575, 0, 650, 0, 500, 0, 825, 0, 400, 500, 0, 100, 0, 100, 0, 500, 0, 325, 500, 675, 325, 500, 0, 325, 225, 0, 100, 0, 0, 500, 0, 600, 0, 500, 0, 825, 0, 400, 500]
        self.obstacle_y = [-1200, -1400, -1600, -1800, -1800, -2750, -2750, -2750, -2750, -3000, -3000, -3550, -3550, -3625, -3625, -3625, -3900, -4100, -4300, -4500, -4700, -4700, -5000, -5000, -5000, -5000, -5375, -5375, -5375, -5450, -5525, -5750, -5950, -6150, -6350, -6350, -8100, -8100, -8300, -8300, -8850, -8850, -8925, -8925, -8925]
        self.obstacle_W = [800, 800, 800, 400, 400, 75, 75, 250, 250, 400, 400, 75, 75, 400, 100, 400, 800, 800, 800, 800, 400, 400, 225, 75, 75, 225, 75, 75, 325, 250, 450, 800, 800, 800, 400, 400, 300, 300, 400, 400, 75, 75, 400, 100, 400]
        self.obstacle_H = [75, 75, 75, 75, 75, 750, 750, 75, 75, 75, 75, 550, 550, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 375, 375, 75, 75, 75, 75, 75, 75, 75, 75, 1000, 1000, 75, 75, 550, 550, 75, 75, 75]
              
        # Level 1 
        # self.nbrobstacle = 5
        # self.obstacle_x = [0, 100, 0, 0, 500]
        # self.obstacle_y = [-1200, -1400, -1600, -1800, -1800]
        # self.obstacle_W = [800, 800, 800, 400, 400]
        # self.obstacle_H = [75, 75, 75, 75, 75,]
        
        # Level 2
        # self.nbrobstacle = 4
        # self.obstacle_x = [250, 575, 0, 650]
        # self.obstacle_y = [-2750, -2750, -2750, -2750]
        # self.obstacle_W = [75, 75, 250, 250]
        # self.obstacle_H = [750, 750, 75, 75]
        
        # Level 3
        # self.nbrobstacle = 7
        # self.obstacle_x = [0, 500, 0, 825, 0, 400, 500]
        # self.obstacle_y = [-3000, -3000, -3550, -3550, -3625, -3625, -3625]
        # self.obstacle_W = [400, 400, 75, 75, 400, 100, 400]
        # self.obstacle_H = [75, 75, 550, 550, 75, 75, 75]
        
        # Level 4 
        # self.nbrobstacle = 20
        # self.obstacle_x = [0, 100, 0, 100, 0, 500, 0, 325, 500, 675, 325, 500, 0, 325, 225, 0, 100, 0, 0, 500]
        # self.obstacle_y = [-3900, -4100, -4300, -4500, -4700, -4700, -5000, -5000, -5000, -5000, -5375, -5375, -5375, -5450, -5525, -5750, -5950, -6150, -6350, -6350]
        # self.obstacle_W = [800, 800, 800, 800, 400, 400, 225, 75, 75, 225, 75, 75, 325, 250, 450, 800, 800, 800, 400, 400]
        # self.obstacle_H = [75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 375, 375, 75, 75, 75, 75, 75, 75, 75, 75]
        
        # Level 5
        # self.nbrobstacle = 9
        # self.obstacle_x = [0, 600, 0, 500, 0, 875, 0, 400, 500]
        # self.obstacle_y = [-8100, -8100, -8250, -8250, -8900, -8900, -8925, -8925, -8925]
        # self.obstacle_W = [300, 300, 400, 400, 25, 25, 400, 100, 400]
        # self.obstacle_H = [1000, 1000, 25, 25, 650, 650, 25, 25, 25]
    
        self.nbrbot = 3
        self.botlist = []
        self.bot_x = [100 , 450  , 800]
        self.bot_y = [100 , 150  , 200]
        
    def createObsatcle(self) :    
        for i in range (self.nbrobstacle) :
            self.obstaclelist.append(Obstacle(self.obstacle_x[i], self.obstacle_y[i], self.obstacle_W[i], self.obstacle_H[i]))
    
    def createBot(self) :
        for i in range (self.nbrbot) :
            self.botlist.append(Enemies(self.bot_x[i], self.bot_y[i]))