import matplotlib.pyplot as plt
import numpy as np

ymin=5
ymax=20
ymingraf=0
ydel=2
if ymax>40: ydel=5
w=0.4
c1="green"
c2="red"

xlabels=np.array(["A" + str(i) for i in range(10)])
yakse=np.array([i for i in range(ymingraf,ymax+2) if i%ydel==0])
ylabel=np.array([n for n in range(ymingraf,ymax+2)  if n%ydel==0 ])
x=np.arange(len(xlabels))
y1=np.array([np.random.randint(ymin,ymax) for i in range(len(xlabels))])
y2=np.array([np.random.randint(ymin,ymax) for i in range(len(xlabels))])

#===========================
#Side by side bar chart
fig,ax=plt.subplots()

ax.set_xticks(x)
ax.set_xticklabels(xlabels)
ax.set_yticks(yakse)
ax.set_yticklabels(ylabel)
ax.set_title("Min bargraf")
ax.set_ylabel("antal")
ax.set_xlabel("kategori")
ax.set_ylim(ymingraf,ymax+1)

ax.bar(x-w/2,y1,width=w,color=c1,label="y1")
ax.bar(x+w/2,y2,width=w,color=c2,label="y2")
ax.legend()

def bartekst(ax,barnr,x,y,w):
    for b,nr in enumerate(x):
        ax.annotate(str(y[nr]),xy=((b-2*w+barnr*w),y[nr]+w))
        
bartekst(ax,1,x,y1,w)
bartekst(ax,2,x,y2,w)

#=============================
#Stacked bar chart
fig1,ax1=plt.subplots()
ax1.bar(x,y1,width=w,color=c1,label="y1")
ax1.bar(x,y2,bottom=y1,width=w,color=c2,label="y2")
ax1.plot(x,y2)
ax1.legend()
ax1.set_xticks(x)
ax1.set_xticklabels(xlabels)

#=============================
#Horizontal bar chart
fig, ax = plt.subplots()

ax.barh(x, y1,color=c1)

ax.set_yticks(x)
ax.set_yticklabels(xlabels)
ax.set_xticks(yakse)
ax.set_xticklabels(ylabel)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('antal')
ax.set_ylabel('kategori')
ax.set_title("Min bargraf")