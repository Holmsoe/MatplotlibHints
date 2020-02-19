import matplotlib.pyplot as plt
import numpy as np

def testprint():
    
    plt.axes()
    rectangle = plt.Rectangle((0,0), 20, 10, fc='blue',ec="red")
    circle = plt.Circle((20,20),5, fc=farveliste[1],ec="red")
    plt.gca().add_patch(circle)
    plt.gca().add_patch(rectangle)

    from matplotlib.patches import Polygon
    pts = np.array([[15,15], [15,5], [3,np.sqrt(5**2 - 2**2)]])
    p = Polygon(pts, closed=False)
    plt.gca().add_patch(p)

    plt.axis("off")
    plt.axis('scaled')


#testprint()

farveliste={1:'tab:blue',2:'tab:orange',3:'tab:green',4:'tab:red',5:'tab:purple',
            6:'tab:brown',7:'tab:pink',8:'tab:gray',9:'tab:olive',10:'tab:cyan'}

h=3
b=3
farve=1
plt.axes()
for row in range(h):
    for col in range(b):  
        rectangle = plt.Rectangle((row,col), 1, 1, fc=farveliste[farve],ec="black")
        plt.gca().add_patch(rectangle)
        farve+=1
plt.axis("off")
plt.axis('scaled')