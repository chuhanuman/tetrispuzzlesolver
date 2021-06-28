import sys
import drawtetris
import copy
from time import time

def rotate(piece):
    newpiece=[]
    for i in range(len(piece[0])):
        temp=[]
        for j in range(len(piece)):
            temp.append(piece[j][i])
        newpiece.append(temp[::-1])
    return newpiece

def findemptyregions(board):
    regions=[]
    y=-1
    for line in board:
        y+=1
        x=-1
        for tile in line:
            x+=1
            if tile==0:
                region=[]
                if y!=0:
                    if board[y-1][x]==0:
                        temp=0
                        for reg in regions:
                            if [y-1,x] in reg:
                                region.append(temp)
                            else:
                                temp+=1
                if x!=0:
                    if board[y][x-1]==0:
                        temp=0
                        for reg in regions:
                            if [y,x-1] in reg:
                                if temp not in region:
                                    region.append(temp)
                            else:
                                temp+=1
                if region==[]:
                    regions.append([[y,x]])
                else:
                    regions[region[0]].append([y,x])
                    if len(region)>1:
                        regions[region[0]]+=regions[region[1]]
                        regions.pop(region[1])
    miniboards=[]
    positions=[]
    for region in regions:
        if len(region)%4!=0:
            return False
        """miny=100
        minx=100
        maxy=0
        maxx=0
        for [y,x] in region:
            if y<miny:
                miny=y
            if y>maxy:
                maxy=y
            if x<minx:
                minx=x
            if x>maxx:
                maxx=x
        tempboard=[]
        for y in range(miny,maxy+1):
            tempboard.append(board[y][minx:maxx+1])
        miniboards.append(tempboard)
        positions.append([miny,minx])
    return [miniboards,positions]"""
    return True

def justdoit(h,w,pieces,pieces2,board,piecesleft,piecesplaced):
    if sum(piecesleft)==1:
        print("Making progress ...")
        print("Time since start: "+str((time()-starttime)//3600)+" hours "+str((time()-starttime)%3600//60)+" minutes "+str((time()-starttime)%60)+" seconds")
    for x in range(w):
        for y in range(h):
            if piecesleft[0]>0:
                if w-3>=x and h-2>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[0]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[0]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([0,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[0]:
                        if tempboard[y-tile[1]+1][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y-tile[1]+1][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[0]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([0.5,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                if h-3>=y and w-2>=x:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[0]:
                        if tempboard[y+tile[0]][x+tile[1]]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x+tile[1]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[0]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([0.75,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[0]:
                        if tempboard[y+tile[0]][x-tile[1]+1]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x-tile[1]+1]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[0]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([0.25,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
            if piecesleft[1]>0:
                if w-3>=x and h-2>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[1]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[1]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([1,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[2]:
                        if tempboard[y-tile[1]+1][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y-tile[1]+1][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[1]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([1.5,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                if h-3>=y and w-2>=x:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[2]:
                        if tempboard[y+tile[0]][x+tile[1]]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x+tile[1]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[1]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([1.75,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[1]:
                        if tempboard[y+tile[0]][x-tile[1]+1]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x-tile[1]+1]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[1]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([1.25,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
            if piecesleft[2]>0:
                if w-3>=x and h-2>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[2]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[2]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([2,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[1]:
                        if tempboard[y-tile[1]+1][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y-tile[1]+1][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[2]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([2.5,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                if h-3>=y and w-2>=x:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[1]:
                        if tempboard[y+tile[0]][x+tile[1]]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x+tile[1]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[2]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([2.75,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[2]:
                        if tempboard[y+tile[0]][x-tile[1]+1]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x-tile[1]+1]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[2]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([2.25,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
            if piecesleft[3]>0:
                if w-3>=x and h-2>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[3]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[3]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([3,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                if h-3>=y and w-2>=x:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[4]:
                        if tempboard[y+tile[0]][x+tile[1]]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x+tile[1]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[3]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([3.25,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
            if piecesleft[4]>0:
                if w-3>=x and h-2>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[4]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[4]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([4,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                if h-3>=y and w-2>=x:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[3]:
                        if tempboard[y+tile[0]][x+tile[1]]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x+tile[1]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[4]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([4.25,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
            if piecesleft[5]>0:
                if w-4>=x:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[5]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[5]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([5,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
                if h-4>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[5]:
                        if tempboard[y+tile[0]][x+tile[1]]==1:
                            good = False
                            break
                        tempboard[y+tile[0]][x+tile[1]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[5]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([5.25,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)
            if piecesleft[6]>0:
                if w-2>=x and h-2>=y:
                    tempboard=copy.deepcopy(board)
                    good = True
                    for tile in pieces2[6]:
                        if tempboard[y+tile[1]][x+tile[0]]==1:
                            good = False
                            break
                        tempboard[y+tile[1]][x+tile[0]]+=1
                    if good and tempboard not in positionsseen[sum(piecesleft)-1] and findemptyregions(tempboard):
                        temppiecesleft=piecesleft[:]
                        temppiecesleft[6]-=1
                        temppiecesplaced=copy.deepcopy(piecesplaced)
                        temppiecesplaced.append([6,x,y])
                        if sum(temppiecesleft)==0:
                            return temppiecesplaced
                        else:
                            ans=justdoit(h,w,pieces,pieces2,tempboard,temppiecesleft,temppiecesplaced)
                            if ans!=None:
                                return ans
                            positionsseen[sum(piecesleft)-1].append(tempboard)

h=int(input("How tall is the puzzle?"))
w=int(input("How wide is the puzzle?"))
if (h*w)%4!=0:
    print("Recheck your inputs.")
    sys.exit()
pieces=[[[0,1,0],
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
pieces2=[[[1,0],[0,1],[1,1],[2,1]],
         [[0,0],[0,1],[1,1],[2,1]],
         [[2,0],[0,1],[1,1],[2,1]],
         [[0,0],[1,0],[1,1],[2,1]],
         [[1,0],[2,0],[0,1],[1,1]],
         [[0,0],[1,0],[2,0],[3,0]],
         [[0,0],[1,0],[1,1],[0,1]]
         ]
print("Enter the number of all of your pieces one by one using the second window.")
mypieces=drawtetris.drawtetris([0,1,2,3,4,5,6],[[0,0],[200,0],[400,0],[600,0],[800,0],[1000,0],[1250,0]],True,(h*w)/4)
starttime=time()
board=[]
piecesleft=mypieces
piecesplaced=[]
for i in range(h):
    board.append([0]*w)
global positionsseen
positionsseen = [[]]*int((h*w)/4)
solution=justdoit(h,w,pieces,pieces2,board,piecesleft,piecesplaced)
if solution == None:
    print("No solution")
pieces=[]
positions=[]
for i in solution:
    pieces.append(i[0])
    positions.append([i[1]*50,i[2]*50])
print(pieces,positions)
print("Time since start: "+str((time()-starttime)//3600)+" hours "+str((time()-starttime)%3600//60)+" minutes "+str((time()-starttime)%60)+" seconds")
drawtetris.drawtetris(pieces,positions)

#TODO solve each region individually
                
