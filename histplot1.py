import matplotlib.pyplot as plt
import numpy as np

nsample=20
vmin=1
vmax=6
w=0.8
data1=[np.random.randint(vmin,vmax+1) for n in range(nsample)]
data2=[np.random.randint(vmin,vmax+1) for n in range(nsample)]
b=np.array([i for i in range(vmin,vmax+2)]) # +2 da sidst bin indeholder både næstesidste og sidste interval. Så der skal være en extra bin.
xdel=np.array([i+w/2 for i in range(vmin,vmax+1)]) # ticks i centrum
xlabel=np.array([i for i in range(vmin,vmax+1)]) #ticks text

#================
#Et datasæt
fig,ax = plt.subplots()
 
ax.hist(data1,bins=b,width=w,color='b')
ax.set_xticks(xdel)
ax.set_xticklabels(xlabel)


#====================
# To datasæt med to sæt labels
fig1,ax1 = plt.subplots()
 
ax1.hist([data1,data2],bins=b,rwidth=w,color=['g','r'],align='left',label=['a','b'])
ax1.legend()
ax1.set_title('To slag')
ax1.set_xlabel('slag')
ax1.set_ylabel('antal')
# Lave x ticks og x labels
dellist=[]
labellist=[]
for i in range(vmin,vmax+1):
    dellist.append(i-w/4)
    dellist.append(i+w/4)
    labellist.append('A'+str(i))
    labellist.append('B'+str(i))
ax1.set_xticks(dellist)
ax1.set_xticklabels(labellist)

#===================
#individuelle søjler
fig,ax = plt.subplots()

#Bemærk hvordan man får adgang til data for histogram
N, bins, patches=ax.hist(data1,bins=b,width=w,color='b')
ax.set_xticks(xdel)
ax.set_xticklabels(xlabel)


print(N) #Dette er liste med søjleværdier
print(bins) #Liste med bins
print(patches) #Giver adgang til hver enkelt søjle

farver=['r','g','b','y','m','c']
farver1=['olivedrab','coral','orange','skyblue','slateblue','indianred']

#se også patches.rectangle
for nr,s in enumerate(patches):
    s.set_facecolor(farver1[nr])
    s.set_edgecolor('k')
    s.set_linewidth(2)
