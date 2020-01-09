# deep-learning

## assignment1
In this assignment, i made up a model to show the location of 10 agents on the "environment" 
As for the agents, they can "eat" the "environment" and move randomly.
'''python
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
'''
As for the figure, it shows the animation of the movement of the agents and it also shows the change of the "environment".
'''
def update(frame_number):
    
    fig.clear()   
    global carry_on
    


    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()#eat
            agents[i].share_with_neighbours(neighbourhood)
        
    #if random.random() < 0.1:
        #carry_on = False
        #print("stopping condition")
    S=[]
    L=[]
    for i in range(num_of_agents):
        S.append(matplotlib.pyplot.scatter(agents[i].x,agents[i].y))
        #        print(agents[i][0],agents[i][1])
        #        matplotlib.legend(loc='best')
        #print (Si)
        L.append(i+1)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    
    
    #    matplotlib.legend(loc='best')
    matplotlib.pyplot.imshow(environment,cmap='bone')
    matplotlib.pyplot.title('Agents',fontsize='large',fontweight='bold')
    matplotlib.pyplot.colorbar(shrink=0.8)
    matplotlib.pyplot.legend(handles=S,labels=L,loc='upper right')
 '''
