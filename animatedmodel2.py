# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:14:15 2019

@author: ml18gm
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import tkinter
import matplotlib.backends.backend_tkagg
import requests
import bs4

matplotlib.use('TkAgg')
'''
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
'''
num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood=20

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#####################
f = open("E:\geog5990mprogram\python\in.txt")
environment = []
#i = 0
for line in f:
    #parsed_line = str.split(line,",")
    parsed_line = line.split(",")
    #print("parsing line", i) # Th
    #i +=1 
    environment_line = []
    #j = 0
    for word in parsed_line:
        environment_line.append(float(word))
        #print("Parsing word ", j , "on line", i)
        #j = j +1
    environment.append(environment_line)
    #print("data ", data)

#print(data)
f.close()
#####################

#ax.set_autoscale_on(False)

# Make the agents.
#for i in range(num_of_agents):
#    agents.append([random.randint(0,100),random.randint(0,100)])
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,neighbourhood,agents))
carry_on = True	
	
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
    

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
######################



###########################

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
##animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)


#matplotlib.legend(loc='best')
#matplotlib.pyplot.show()
###############
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
root=tkinter.Tk()
root.wm_title('Agent')

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar=tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu=tkinter.Menu(menu_bar)
menu_bar.add_cascade(label='Model',menu=model_menu)
model_menu.add_command(label='Run',command=run)

tkinter.mainloop()


