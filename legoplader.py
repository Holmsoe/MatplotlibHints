import numpy as np
import copy
import matplotlib.pyplot as plt

class Board:
    '''Starttabel med bredde b og højde h. 
    Som start har alle felter værdien 0
    Der indsættes en'ramme' omkring tabel med tallet 99.
    Dette undgår at tjekke om en ny brik er i tabel da feltet er optaget.
    '''
    def __init__(self,b,h):
        self.b=b
        self.h=h
        
    def MakeBoard(self):
        Board=np.array([[0 for i in range(self.b+2)] for j in range(self.h+2)])
        Board[0,:]=99 
        Board[:,self.b+1]=99 
        Board[self.h+1,:]=99 
        Board[:,0]=99
        return Board
  
class PlacerBrik:
    def __init__(self,Board,Brik):
        self.Board=Board
        self.Brik=Brik
        self.Brik_x=Brik[0]
        self.Brik_y=Brik[1]
        #bredde og højde tilpasses og ramme med 99 skal fjernes.
        self.b=len(Board[0])-2
        self.h=len(Board[:,0])-2
        
    def TjekPlacering(self,pkt):
        ''' Undersøger om felter som brikken dækker med startpunktet 'pkt' er optaget
        Hvis der blot er et felt>0 foretages ikke yderligere sammenligninger.
        Hvis brikken går ud i rammen stoppes også
        '''
        px=pkt[0]
        py=pkt[1]
        OK=True
        for row in range(self.Brik_x):
            for col in range(self.Brik_y):
                if OK:
                    if self.Board[px+row,py+col]>0: 
                        OK=False
        return OK
    
    def Placer(self,pkt,BrikNr):
        ''' Placerer brikken med et givent startpunkt. Fungerer kun med et tjek (TjekPlacering) på tomme felter.
        Bemærk deepcopy for at sikre at placering af tidligere brikker på brættet ikke forstyrrer.
        Tabellen udfyldes med nummeret af den aktuelle brik.
        '''
        px=pkt[0]
        py=pkt[1]
        BoardUd=copy.deepcopy(self.Board)
        for row in range(self.Brik_x):
            for col in range(self.Brik_y):
                BoardUd[px+row][py+col]=BrikNr
        return BoardUd

    def Beregn(self,BrikNr):
        '''Returnerer en liste med nye boards med mulige placeringer af en brik på et bræt.
        Brikken angives i tabellen med aktuel briknummer'''
        #PlacerInit=PlacerBrik(self.Board,self.Brik)
        BoardGem=[]
        for row in range(1,self.h+1):
            for col in range(1,self.b+1):
                if self.TjekPlacering([row,col]):
                    BoardGem.append(self.Placer([row,col],BrikNr))      
        return BoardGem    

class AlleBrikker:
    '''Gennemgår alle brikker og finder mulige placeringer per brik.
    AlleKombi bruges til at opsamle mulige tabeller for en given brik.
    Disse tabeller anvendes til placering af næste brik
    '''
    def __init__(self,b,h,Brikker):
        self.Brikker=Brikker
        self.b=b
        self.h=h
        self.antal=len(Brikker)
        
    def PlacerAlle(self):
        StartBoard=Board(self.b,self.h).MakeBoard()
        Muligheder=[[] for brik in range(self.antal)]
        AlleKombi=[[] for brik in range(self.antal)]
        for briknr in range(self.antal):
            Brik=Brikker[briknr]
            #Først StartBoard
            if briknr==0:
                #Muligheder er liste med alle placeringer af brik
                Muligheder[0]=PlacerBrik(StartBoard,Brik).Beregn(1)
                #AlleKombi er kombineret opsamlingsliste med alle muligheder
                AlleKombi[0]=Muligheder[0]
            else:
                #mulige kombinationer fra tidligere brik anvendes til at placere næste brik
                for kombi in AlleKombi[briknr-1]:
                    #Muligheder er liste med alle placeringer af brik
                    Muligheder[briknr]=PlacerBrik(kombi,Brik).Beregn(briknr+1)
                    #AlleKombi er kombineret opsamlingsliste med alle muligheder for alle gennemgåede brikker
                    AlleKombi[briknr]+=Muligheder[briknr]
        return AlleKombi[self.antal-1]

def PrintTabel(tabel):
    htabel=len(tabel[:,0])
    btabel=len(tabel[0])
    tabel=np.delete(tabel,htabel-1,axis=0)
    tabel=np.delete(tabel,btabel-1,axis=1)
    tabel=np.delete(tabel,0,axis=0)
    tabel=np.delete(tabel,0,axis=1)
    #print(tabel)
    return tabel

    


'''       
b=3
h=5
Brikker=[]
Brikker.append([2,1])
Brikker.append([3,2])
Brikker.append([2,3])   
Brikker.append([1,1])
'''

b=5
h=5
Brikker=[]
Brikker.append([2,1])
Brikker.append([3,2])
Brikker.append([2,3])   
Brikker.append([2,4])


AlleKombinationer=AlleBrikker(b,h,Brikker).PlacerAlle() 
for item in AlleKombinationer: 
    PrintTabel(item)
    print('')
    
antal=len(AlleKombinationer)


farveliste={0:'white',1:'tab:blue',2:'tab:orange',3:'tab:green',4:'tab:red',5:'tab:purple',
            6:'tab:brown',7:'tab:pink',8:'tab:gray',9:'tab:olive',10:'tab:cyan'}

for tab in range(antal):
    ex=AlleKombinationer[tab]
    tabel=PrintTabel(ex)
    fig,ax = plt.subplots()
    for row in range(h):
        for col in range(b): 
            farve=tabel[row,col]
            rectangle = plt.Rectangle((col,row), 1, 1, fc=farveliste[farve],ec="black")
            plt.gca().add_patch(rectangle)
        #farve+=1
    plt.axis("off")
    plt.axis('scaled')

print('antal kombinationer',antal)