import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import matplotlib.cm as cm
Nx =520
Ny =180
u0 = 0.04
Re =220
q=9

vlb = u0*(Ny/2)/Re

tau=3*vlb+1/2

W = np.array([4/9,1/9,1/9,1/9,1/36,1/36,1/9,1/36,1/36])

#fout=np.zeros((q,Nx,Ny))
ro=np.ones((Nx,Ny))

def get_ro():
    global ro
    global fin
    ro=np.zeros((Nx,Ny))
    for i in range(q):
        ro[:,:]+=fin[i,:,:]
    for i in range(Ny):
        ro[0,i]=(2*(fin[3,0,i]+fin[4,0,i]+fin[5,0,i]) +fin[0,0,i]+fin[1,0,i]+fin[2,0,i])/(1-u0)
        
obstacle = np.fromfunction(lambda x,y: abs(x-Nx/4)+abs(y)<Ny/2, (Nx,Ny))
for i in range(Nx):
    obstacle[i,0] = True
    obstacle[i,Ny-1] = True

def equilibrium(roo,vel):
    global W
    if roo ==0:
        get_ro()
    return np.fromfunction(lambda f,x,y: W[f]*ro[x,y]*(1+3*(c[f,0]*vel[0,x,y]+c[f,1]*vel[1,x,y])+ 9/2*(c[f,0]*vel[0,x,y]+c[f,1]*vel[1,x,y])**2-3/2*(vel[0,x,y]**2+vel[1,x,y]**2)),(q,Nx,Ny),dtype=int)

def get_vel():
    global fin
    global u
#    get_ro()
    u =np.zeros((2,Nx,Ny))
    for i in range(q):
        u[0,:,:] += fout[i,:,:]*c[i,0]
        u[1,:,:] += fout[i,:,:]*c[i,1]
    for i in range(Nx):
        for j in range(Ny):
            u[0,i,j]/=ro[i,j]
            u[1,i,j]/=ro[i,j]

c =  np.array([(x,y) for x in [0,-1,1] for y in [0,-1,1]])
noslip = [c.tolist().index((-c[i]).tolist()) for i in range(q)]
u =np.ones((2,Nx,Ny))

vel0 = np.fromfunction(lambda d,x,y: (1-d)*u0,(2,Nx,Ny))
feq  = equilibrium(1.0,vel0);
fin = feq.copy()
global fout
#fout = np.ones((q,Nx,Ny))

#print(fin)
#fin=fout = np.ones((q,Nx,Ny))
for time in range(200000):
    
    fout = fin - (fin-feq)/tau 
    for i in range(q):
        #fout[i,~obstacle] = fin[i,~obstacle]
        fout[i,obstacle] = fin[noslip[i],obstacle]
        
    print(time)   
    #print(fin)
    #print(fout)
    for i in range(q):
        fin[i,:,:] = np.roll(np.roll(fout[i,:,:],c[i,0],axis=0),c[i,1],axis=1)

    for i in [3,4,5]:
        fin[i,Nx-1,:]=fin[i,Nx-2,:]

    for i in [6,7,8]:
        fin[i,0,:]=feq[i,0,:]

    
   # if time ==0:
    #    for i in range(Ny-10):
     #       fin[7,10,i+5]=2
#    get_vel()
#    feq  = equilibrium(0,u);
    fout =fin
    get_ro()
    get_vel()
    feq=equilibrium(0,u)
#    print(ro[0,:])
 #   print("piotr")
  #  print(fin[2,0,:])
    if (time%100==0):
     #   get_vel()
        plt.clf();
        plt.imshow(np.sqrt(u[0]**2+u[1]**2).transpose(),cmap=cm.Reds)
        plt.savefig("vel"+str(int(time/100)).zfill(4)+".png")
   
    

#rray fin = np.array(

get_vel()


plt.clf()
plt.imshow(np.sqrt(u[0]**2+u[1]**2))#,cmap=cm.Reds)
plt.show()


