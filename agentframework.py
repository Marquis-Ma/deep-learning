# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:36:36 2019

@author: ml18gm
"""

import random

class Agent():
    def __init__(self,environment,neighbourhood,agents):
        self.x=random.randint(0,99)
        self.y=random.randint(0,99)
        
        self.environment = environment
        self.store = 0 # We'll come to this in a second.
    
        self.neighbourhood=neighbourhood
        self.agents=agents
        
        
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.x][self.y] > 10:
            self.environment[self.x][self.y] -= 10
            self.store += 10
         
    def share_with_neighbours(self,neighbourhood):
        
        for agent in self.agents:
            dist=self.distance_between(agent)
            if dist<=neighbourhood:
                sum=self.store+agent.store
                ave=sum/2
                self.store=ave
                agent.store=ave
                #print("sharing"+str(dist)+""+str(ave))
                
    def distance_between(self,agent):
        return(((self.x-agent.x)**2)+((self.y-agent.y)**2))**0.5
        
        
        