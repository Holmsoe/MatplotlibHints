import numpy as np
import pylab as pl

def basisplot(): 

    n=10
    
    x=[i for i in range(n)]
    x1=[i for i in range(2*n) if i%2==0]
    y=[i*i for i in range(n)]
    y1=[5*i for i in range(n)]
    
    pl.plot(x,y,'b*',color='red',label='i anden')
    pl.plot(x1,y1,'bD',label='gange fem')
    #pl.legend(loc='upper left')
    pl.legend(loc='best')
    
    
    pl.xlabel("antal")
    pl.ylabel("resultat")
    pl.title("Min kurve")

def histogram():

    histgraf=np.random.normal(5,3,1000)
    b=np.arange(-5.,16.,1.)
    pl.hist(histgraf,b)
    
def canvasplot1():
    x=[i for i in range(n)]
    x1=[i for i in range(2*n) if i%2==0]
    y=[i*i for i in range(n)]
    y1=[5*i for i in range(n)]
    y2=[i*i -i for i in range(n)]
    
    f1=pl.figure(1)
    pl.subplot(221)
    pl.plot(x,y,'b*',color='red',label='i anden')
    pl.subplot(222)
    pl.plot(x1,y1,'bD',label='gange fem')
    pl.subplot(212)
    pl.plot(x1,y2,color='green',label='anden funktion')
    
    pl.subplots_adjust(left=0.01,right=1.2,wspace=0.50,hspace=0.50)
    
def canvasplot2():
    
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)
    
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Navnet på figuren')
    axs[0, 0].plot(x, y)
    axs[0, 0].set_title('Axis [0,0]')
    axs[0, 1].plot(x, y, 'tab:orange')
    axs[0, 1].set_title('Axis [0,1]')
    axs[1, 0].plot(x, -y, 'tab:green')
    axs[1, 0].set_title('Axis [1,0]')
    axs[1, 1].plot(x, -y, 'tab:red')
    axs[1, 1].set_title('Axis [1,1]')
    
    
    for ax in axs.flat:
        ax.set(xlabel='x-label', ylabel='y-label')
    
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
     
#basisplot()
#histogram()
#canvasplot1()
canvasplot2()