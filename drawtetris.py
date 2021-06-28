import pygame
import copy
import math
from pygame.locals import (K_1,K_2,K_3,K_4,K_5,K_6,K_7,KEYDOWN,QUIT)
setpieces=[[[50,0],[100,0],[100,50],[150,50],[150,100],[0,100],[0,50],[50,50]],
        [[0,0],[50,0],[50,50],[150,50],[150,100],[0,100]],
        [[100,0],[150,0],[150,100],[0,100],[0,50],[100,50]],
        [[0,0],[100,0],[100,50],[150,50],[150,100],[50,100],[50,50],[0,50]],
        [[50,0],[150,0],[150,50],[100,50],[100,100],[0,100],[0,50],[50,50]],
        [[0,0],[200,0],[200,50],[0,50]],
        [[0,0],[100,0],[100,100],[0,100]]
        ]
setpieces2=[[[0,1,0],
             [1,1,1]],
            [[1,0,0],
             [1,1,1]],
            [[0,0,1],
             [1,1,1]],
            [[1,1,0],
             [0,1,1]],
            [[0,1,1],
             [1,1,0]],
            [[1,1,1,1]],
            [[1,1],
             [1,1]]
            ]

def drawtetris(pieces,pos,getinputs=False,numpieces=10):
    if getinputs:
        mypieces=[0,0,0,0,0,0,0]
    pygame.init()
    screen=pygame.display.set_mode((1440,900))
    screen.fill((255,255,255))
    cur=0
    for piece in pieces:
        if piece!=math.floor(piece):
            coords=copy.deepcopy(setpieces[math.floor(piece)])
            rotate90s=math.modf(piece)[0]//0.25
            if rotate90s==1:
                for coord in coords:
                    tempcoord=coord[:]
                    coord[0]=-tempcoord[1]+len(setpieces2[math.floor(piece)])*50
                    coord[1]=tempcoord[0]
            elif rotate90s==2:
                for coord in coords:
                    tempcoord=coord[:]
                    coord[0]=-tempcoord[0]+len(setpieces2[math.floor(piece)][0])*50
                    coord[1]=-tempcoord[1]+len(setpieces2[math.floor(piece)])*50
            elif rotate90s==3:
                for coord in coords:
                    tempcoord=coord[:]
                    coord[0]=tempcoord[1]
                    coord[1]=-tempcoord[0]+len(setpieces2[math.floor(piece)][0])*50
            else:
                print("I can't believe you've done this")
            pygame.draw.polygon(screen,(0,0,0),translate(coords,pos[cur]),5)
        else:
            pygame.draw.polygon(screen,(0,0,0),translate(copy.deepcopy(setpieces[piece]),pos[cur]),5)
        cur+=1
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if getinputs and event.type==KEYDOWN:
                if event.key==K_1:
                    mypieces[0]+=1
                elif event.key==K_2:
                    mypieces[1]+=1
                elif event.key==K_3:
                    mypieces[2]+=1
                elif event.key==K_4:
                    mypieces[3]+=1
                elif event.key==K_5:
                    mypieces[4]+=1
                elif event.key==K_6:
                    mypieces[5]+=1
                elif event.key==K_7:
                    mypieces[6]+=1
                if sum(mypieces)==numpieces:
                    pygame.quit()
                    return mypieces
            if event.type==QUIT:
                pygame.quit()
                running=False

def translate(coords,dist):
    for coord in coords:
        coord[0]+=dist[0]
        coord[1]+=dist[1]
    return coords

#Draw all rotatable pieces
#drawtetris([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,4,4.25,5,5.25],[[0,0],[200,0],[350,0],[550,0],[0,150],[200,150],[350,150],[550,150],[0,300],[200,300],[350,300],[550,300],[0,450],[200,450],[0,600],[200,600],[0,750],[250,750]])
