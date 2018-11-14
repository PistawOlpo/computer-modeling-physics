import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


N = 1000 # size of the world
center = [int(N/2), int(N/2)] #center of the world
MaxRiner = 3 # starting radius of inner circle
MaxRouter = 6


world =np.zeros((N,N))
# center of world
world[center[0]][center[1]] = 1

def on_circle(teta, r):
    return [center[0] + int(np.rint(math.sin(teta)*r)), center[1] + int(np.rint(math.cos(teta)*r))]

wolker = on_circle(2*np.pi*np.random.random_sample(), MaxRiner)

def wolk(wolker):
    x = int((np.random.random_sample())*3  ) -1
    y = int((np.random.random_sample())*3  ) -1
    return [wolker[0]+x, wolker[1]+y]

def if_hit(wolker):
    if world[wolker[0]][wolker[1]-1] == 1:
        return True
    if world[wolker[0]][wolker[1]+1] == 1:
        return True
    if  world[wolker[0]-1][wolker[1]] == 1:
        return True
    if  world[wolker[0]+1][wolker[1]] == 1:
        return True
    return False

def if_outerCircle(wolker):
    global MaxRouter
    if ( (wolker[0] - center[0])**2 + (wolker[1] - center[1])**2 )**0.5  > MaxRouter:
            return True


plt.clf()
F = plt.gcf()
a = plt.gca()
plt.xlim((0,N))
plt.ylim((0,N))

cir = Circle((center[0],center[1]), radius=0.5,color='black')
        # put a circle at the position of the sticking particle
a.add_patch(cir)

counter =0
w=0
while(MaxRouter <= N/2):
#    print("w",w, " wolker " , wolker)
    wolker = wolk(wolker)
    w+=1
    if if_outerCircle(wolker):
        print("out of outer circle, wolker=", wolker," w =", w , "\n")
        wolker = on_circle(2*np.pi*np.random.rand(1), MaxRiner) # reset wolker

    if if_hit(wolker):
        if np.random.random_sample()<1/8: #podej prawdopodobienstwo
            
            world[wolker[0]][wolker[1]] = 1
            if ( (wolker[0] - center[0])**2 + (wolker[1] - center[1])**2 )**0.5 > MaxRiner-3:
                MaxRiner =((wolker[0] - center[0])**2 + (wolker[1] - center[1])**2 )**0.5 + 3
                MaxRouter =2*MaxRiner + 3
        
        
#           print(world)
            print(MaxRiner)
            print(MaxRouter)
            print("\n")

        
            cir = Circle((wolker[0],wolker[1]), radius=0.5,color='black')
        # put a circle at the position of the sticking particle
            a.add_patch(cir)
        # add this circle to the plot
        
            if (counter%10==0):
                plt.plot()                                         # plot it
                F.set_size_inches((30,30))            # physical size of the plot
                nStr=str(counter)
                # convert counter to a string
                nStr=nStr.rjust(6,'0') 
                #pad with zeros
                plt.savefig('plot'+nStr+'.png') 
            # save the figure
            counter=counter+1
            wolker = on_circle(2*np.pi*np.random.rand(1), MaxRiner) # reset wolker
#           print("wolker on start = ", wolker)

        
        
        

        
    
