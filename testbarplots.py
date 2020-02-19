import matplotlib.pyplot as plt
import numpy as np 

x=np.array([1,2,3])
w=0.4

fig,ax = plt.subplots()

ax.bar(x,[11,7,13],width=w)
ax.bar(x+w,[4,1,6],width=w)

ax.set_xticks(x+w/2)
ax.set_xticklabels(['a','b','c'])
ax.legend()


