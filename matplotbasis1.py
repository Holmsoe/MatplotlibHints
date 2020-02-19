import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class testplot():
    def __init__(self):
        self.kurver()
        
    def kurver(self):
        self.x=np.linspace(-np.pi,np.pi,50,endpoint=True)
        
        
        self.y1=np.sin(self.x)
        self.y2=np.cos(self.x)
        
        #Transformering til data i søjler er nødvendig
        self.gsin=np.array([self.x,self.y1]).T
        self.gcos=np.array([self.x,self.y2]).T
             
        self.figtabel=np.array([self.x,self.y1,self.y2]).T
        
    
        self.pd_sin=pd.DataFrame(self.gsin,columns=["x","sin"])
        self.pd_cos=pd.DataFrame(self.gcos,columns=["x","cos"])
        
        self.pd_figtabel=pd.DataFrame(self.figtabel,columns=["x","sin","cos"])


#Simple plot        
    def plot1(self):
        #Simpelt plot
        #Gentagne kald giver flere grafer på samme kurve
        plt.plot(self.x,self.y1)
        plt.plot(self.x,self.y2)

#Subplot         
    def plot2(self):
        fig1=plt.figure()
        a=plt.subplot()
        a.plot(self.x,self.y1)
        a.plot(self.x,self.y2)
        
    def plot3(self):
        fig1=plt.figure()
        #der er kun defineret et plot i 2x2 figur. derfor bliver plot mindre
        a=plt.subplot(221)
        a.plot(self.x,self.y1)
        a.plot(self.x,self.y2)

        
    def plot4(self):
        fig1=plt.figure()
        #Format er (rækker,sæjler,placering)
        a=plt.subplot(221)
        a.plot(self.x,self.y1)
        a.plot(self.x,self.y2)
        
        b=plt.subplot(222)
        c=plt.subplot(223)
        d=plt.subplot(224)

        plt.tight_layout()

    def plot5(self):
        #som plot3 men med gridspec
        fig1=plt.figure()
        grid = plt.GridSpec(2, 2)
        a=plt.subplot(grid[1,1])
        a.plot(self.x,self.y1)
        a.plot(self.x,self.y2)   
        
    def plot6(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Her printes to grafer med en linie
        #Første kolonne i figurtabel er x  - [:,0]
        #Herefter vælges øvrige kolonner som y - [:,1:]
        #Flere kurver kan gives som liste/np array
        a.plot(self.figtabel[:,0],self.figtabel[0:,1:])
        
    def plot7(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Det er også muligt at printe to (eller flere) kurver ved at angive et dobbeltsæt af data.
        a.plot(self.x,self.y1,self.x,self.y2)

    def plot8(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Line style kan sættes med kombination af 3 elementer, 
        #1) Marker type, 2) Line style, 3) color
        # Se her for detaljer: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
        a.plot(self.x,self.y1,'+--r')
        a.plot(self.x,self.y2,'*:b')
    
    def plot9(self):
        fig1=plt.figure()
        a=plt.subplot()
        #style kan også sættes separat i sekvenser
        a.plot(self.x,self.y1,':.r',self.x,self.y2,'d-.b')
        
    def plot10(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Alternativt til Marker,Line,Color styling kan styling laves med keywords
        # Her er nogle:
        # color
        # marker
        # linestyle        
        # linewidth
        # label. For at label skal blive synlig skal der kommandoen .legend() anvendes
        #se: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
                       
        a.plot(self.x,self.y1,marker='+',color='r',linestyle='--',linewidth=2,label="line1")
        a.plot(self.x,self.y2,color='g',linestyle='--',linewidth=5,label="line2")
        
        a.legend()
        #uden location code finder legend bedste placering

        
    def plot11(self):
        fig1=plt.figure()
        # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.figure.Figure.html
        plt.suptitle('Figurnavn')
        plt.xlabel('x-værdi')
        plt.ylabel('resultat')
        plt.xlim(-np.pi,np.pi)
        plt.ylim(-1,1)
        
        a=plt.subplot()
        a.plot(self.x,self.y1)
        a.plot(self.x,self.y2)
                
        #Fjerne akse skala. Bemærk at det er uafhængig af linier
        #a.set_xticklabels([])
        #a.set_yticklabels([])


    def plot12(self):
        fig1=plt.figure()
        a=plt.subplot()
                
        # Parametrene kan sættes separat efterfølgende med set_ kommandoer 
       
        #NB: line1,line2 er plot[0] da plot giver en liste med linier 
        #Når der kun er en linie er det [0]
        #Linier er line2D objekter
        line1=a.plot(self.x,self.y1,marker='+',color='r',linestyle='--',linewidth=2,label="line1")[0]
        line2=a.plot(self.x,self.y2,color='g',linestyle='--',linewidth=5,label="line2")[0]     
        a.legend(loc="lower center")
        #Se location codes her: https://www.kaggle.com/andyxie/matplotlib-plot-multiple-lines
        
        line1.set_linewidth(5)
        #andre muligheder for at sættelinieparametre
        #se: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D
        #set_data  - x og y koordinater
        #set_xdata
        #set_ydata
        #set_linestyle 
        #set_marker
        #set_markersize
        
        #NB: de samme parametre kan hentes med 
        #get_etc

    def plot13(self):
        fig1=plt.figure()
        a=plt.subplot()
        #gridlines
        #se: https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.grid.html
        a.grid(color='r', alpha=0.5, linestyle='dashed', linewidth=1.0)
        linier=a.plot(self.x,self.y1,':.r',self.x,self.y2,'d-.b') 
        #Der to linier defineret ved a.plot. Vi modificerer den anden
        linier[1].set_marker('')
        linier[1].set_linestyle('-')
        linier[1].set_linewidth(5)


#Pandas plots       
    def plot14(self):
        fig1=plt.figure()
        a=plt.subplot()
        #To sæt data for at plotte med en linie.
        #Vi plottet med subpot og anfører database i plot kommando
        a.plot(self.pd_sin["x"],self.pd_sin["sin"],self.pd_cos["x"],self.pd_cos["cos"])

    def plot15(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Vi plotter med data og anfører subplot a i kald. 
        self.pd_figtabel.plot(x="x",y="sin",ax=a)
        
    def plot16(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Pandas: Vi plotter med a.plot og angiver df i data
        a.plot("x","sin",data=self.pd_figtabel)
        a.plot("x","cos",data=self.pd_figtabel)
        
        
    def plot17(self):
        fig1=plt.figure()
        a=plt.subplot()
        #Pandas: Vi plotter flere kurver med liste af y data
        self.pd_figtabel.plot(x="x",y=["sin","cos"],ax=a)
        a.legend(loc="lower center")

#Subplots og gridspec
    def plot18(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y1)
        #I dette tilfælde er der kun et subplot
        #ax.plot er en liste med linier
        ax.set_title('Sinus plot')

    def plot19(self):
        fig, ax = plt.subplots()
        linie=ax.plot(self.x, self.y1)[0]
        #Linie er første linie(eneste) i subplot ax. derfor [0]
        #I dette tilfælde er der kun et subplot ax
        #ax.plot er en liste med linier
        ax.set_title('Sinus plot') 
        linie.set_linewidth(5)
        
    def plot20(self):
        fig, ax = plt.subplots(1,2,sharey=True)
        #notationen ax[] er ok fordi der kun er en dimension i figur. subplot i en retning. lodret eller vandret
        
        #fælles y-akse
        ax[0].plot(self.x, self.y1)
        ax[1].plot(self.x, self.y2)

        ax[0].set_title('Sinus')
        ax[1].set_title('Cosinus')
        
    def plot21(self):
        fig, ax = plt.subplots(2,2,sharey=True,sharex=True,num=2,clear=True)
        #Figur nummer 2. Hvis den findes slettes alt tidligere
        #fælles y-akse
        fig.suptitle('Diverse grafer',size=20,x=0.5,y=1.08)
        #lower left er 0,0 og upper right er 1,1
        ax[0][0].plot(self.x, self.y1)
        ax[0][1].plot(self.x, self.y2)
        ax[1][0].plot(self.x, self.y1,self.x, self.y2)
        ax[1][1].plot(self.x,self.x)

        ax[0][0].set_title('Sinus')
        ax[0][1].set_title('Cosinus')
        ax[1][0].set_title('Sinus og cosinus')
        ax[1][1].set_title('Ret linie')
        
        fig.tight_layout()
        
    def plot22(self):
        fig, ax = plt.subplots(2,2,sharey=True,sharex=True,gridspec_kw={'hspace': 0,'wspace': 0})
        #Finjustere afstand mellem subplots. 
        #Se:https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec
        fig.suptitle('Diverse grafer',size=20,x=0.5,y=1.08)
        #lower left er 0,0 og upper right er 1,1
        
        ax[0][0].plot(self.x, self.y1,'r')
        ax[0][1].plot(self.x, self.y2)
        ax[1][0].plot(self.x, self.y1,self.x, self.y2)
        ax[1][1].plot(self.x,self.x,'--g')
        
        fig.tight_layout()
        
    def plot23(self):
        #fig = plt.subplot()
        fig = plt.figure()
        fig.suptitle('Diverse grafer',size=20,x=0.5,y=1.08)
        grid = plt.GridSpec(3, 3, wspace=0.6, hspace=1.0)
            
        a=plt.subplot(grid[0,0:])
        b=plt.subplot(grid[1, :-1])
        c=plt.subplot(grid[2, 0])
        d=plt.subplot(grid[2, 1])
        e=plt.subplot(grid[1:, 2])

        e.plot(self.x,self.y1)          
        e.set_title("Sinus")

        b.plot(self.x,self.y2)        
        b.set_title("Cos")
        
        c.plot(self.x,self.x,':g')        
        c.set_title("Line")
        
        d.plot(self.x,-self.x,'--r')    
        d.set_title("Line")

        a.plot(self.x,self.y1,label="sin")
        a.plot(self.x,self.y2,label="cos")
        a.legend(loc="upper left")            
        a.set_title("Sin og Cos")         

    def plot24(self):
        fig = plt.figure()
        fig.suptitle('Diverse grafer',size=20,x=0.5,y=1.08)
        sub1 = plt.subplot(2, 2, 1)
        sub1.set_xticks(())
        sub1.set_yticks(())
        sub1.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center',
                size=20, alpha=.5)
        
        sub2 = plt.subplot(2, 2, 2)
        sub2.set_xticks(())
        sub2.set_yticks(())
        sub2.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center',
                size=20, alpha=.5)
        
        sub3 = plt.subplot(2, 2, 3)
        sub3.set_xticks(())
        sub3.set_yticks(())
        sub3.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center',
                size=20, alpha=.5)
        
        sub4 = plt.subplot(2, 2, 4)
        sub4.set_facecolor('green')
        sub4.set_xticks(())
        sub4.set_yticks(())
        sub4.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center',
                size=20, alpha=.5, color="y")

        fig.tight_layout()
        
    def plot25(self):
        fig = plt.figure()
        fig.suptitle('Diverse grafer',size=20,x=0.5,y=1.08)
        #Bemærk hvordan en figur spænder over flere celler med tuple 
        #Celler næves enkeltvis
        sub1 = plt.subplot(2, 3, (1,2))
        sub1.set_xticks(())
        sub1.set_yticks(())
        
        sub2 = plt.subplot(2, 3, 4)
        sub2.set_xticks(())
        sub2.set_yticks(())
        
        sub3 = plt.subplot(2, 3, 5)
        sub3.set_xticks(())
        sub3.set_yticks(())
        
        #Celle 3 og 6 
        sub4 = plt.subplot(2, 3,(3,6))
        sub4.set_xticks(())
        sub4.set_yticks(())

        fig.tight_layout() 

    def plot26(self):
        fig = plt.figure()
        fig.suptitle('Diverse grafer',size=20,x=0.5,y=1.08)
        
        G = plt.GridSpec(3, 3)
        
        axes_1 = plt.subplot(G[0, :])
        plt.xticks(())
        plt.yticks(())
        plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)
        
        axes_2 = plt.subplot(G[1, :-1])
        plt.xticks(())
        plt.yticks(())
        plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)
        
        axes_3 = plt.subplot(G[1:, -1])
        plt.xticks(())
        plt.yticks(())
        plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)
        
        axes_4 = plt.subplot(G[-1, 0])
        plt.xticks(())
        plt.yticks(())
        plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)
        
        axes_5 = plt.subplot(G[-1, -2])
        plt.xticks(())
        plt.yticks(())
        plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=.5)
        
        fig.tight_layout()
             
        
#fplot1=testplot()
#fplot1.plot1()
       

fplot2=testplot()
fplot2.plot1()
fplot2.plot2()

