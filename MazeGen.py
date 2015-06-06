import math

import random
from random import randrange
from MazeCell import MazeCell

# pushes the index to end of the neighbourlist and returns it 
def pushIntoTuple(neighbourlist,index):
    neighbourlist=neighbourlist[:len(neighbourlist)]+(index,)
    return neighbourlist

# returns the index of QUATRAPLE 'dim'
def getIndex(dim):
    _index= dim[0]*n_cube+dim[1]*n_square+dim[2]*n+dim[3]
    return _index

def printMazesToFile():        
    file = open("output.dat", "w")
    for cell in mazeCells:
        file.write(str(int(cell._walls)))
        file.write("\n")
        arr[int(cell._walls)]=arr[int(cell._walls)]+1 #test for randomness

def printNeighbours():
    for _index in range(0,n_power_4):
        neighbourIndices=getNeighbours(_index)
        print (_index,neighbourIndices)


#removes walls in both direction between 'index1' and 'index2' and assuming offset to be positive always 
def removeDirectionalWalls(index1,index2,offset): 
    offset_base_n=math.log(offset,n)*2  #      
        
    index1_walls=mazeCells[index1].getWalls() 
    mazeCells[index1].setWalls(index1_walls - pow(2, offset_base_n))
    
    index2_walls=mazeCells[index2].getWalls()  
    mazeCells[index2].setWalls(index2_walls - pow(2, offset_base_n+1))

#removes walls between index and neighbour
def removeWalls(index,neighbour): 
    offset=neighbour-index # neighbour distance
    if offset>0:
        removeDirectionalWalls(index,neighbour,offset)
    elif offset<0:
        removeDirectionalWalls(neighbour,index,-offset)            

def getNeighbours(index):
    neighbours=()
    t=index / n_cube
    temp1=index % n_cube
    z=temp1 / n_square
    temp2=temp1 % n_square
    y=temp2 / n
    x=temp2 % n
    if t+1 < n:
        neighbour_index=getIndex((t+1,z,y,x))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if t-1 >= 0:
        neighbour_index=getIndex((t-1,z,y,x))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if z+1 < n:
        neighbour_index=getIndex((t,z+1,y,x))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if z-1 >= 0:
        neighbour_index=getIndex((t,z-1,y,x))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if y+1 < n:
        neighbour_index=getIndex((t,z,y+1,x))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if y-1 >= 0:
        neighbour_index=getIndex((t,z,y-1,x))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if x+1 < n:
        neighbour_index=getIndex((t,z,y,x+1))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    if x-1 >= 0:
        neighbour_index=getIndex((t,z,y,x-1))
        if mazeCells[neighbour_index].isVisited()==False:
            neighbours=pushIntoTuple(neighbours, neighbour_index)
    return neighbours

def traverseBFS():
    visitedCount=1  #Counting the Number of Visited Maze Cells
    visitedCells=[] # append all the visited Maze Cells in this Array
    
    visitedCells.append(firstMazeIndex)                              # add visited cells to the visitedCells Array
    mazeCells[firstMazeIndex].visit()
    _mazeNeighbourCells=[] # Neighbours of the current Maze Cell
    currentVisitingMazeIndex=firstMazeIndex 
    while len(visitedCells)>0 and visitedCount != n_power_4:
        _mazeNeighbourCells=list(getNeighbours(currentVisitingMazeIndex)) # getNeighbours are the Neighbours of the current Visiting Maze Index 
        random.shuffle(_mazeNeighbourCells,random.random) # Shuffling is done inorder to pick a random Neighbour 
       
        if len(_mazeNeighbourCells) > 0:         
            _neighbour=_mazeNeighbourCells.pop(0) # pick a last neighbour generated randomly
            mazeCells[_neighbour].visit()       # and address him as visited as he is the next travesing cell
            removeWalls(currentVisitingMazeIndex,_neighbour)    # remove the walls between currentCell and next choosen neighbour 
            visitedCount=visitedCount+1
            visitedCells.append(_neighbour)            
        else:
            visitedCells.pop()
            _neighbour=visitedCells[len(visitedCells)-1]    # pick the last visited cell to be traversed next                            
        currentVisitingMazeIndex=_neighbour # next visiting Maze Index        
                        
n=2
n_square=pow(n,2)
n_cube=pow(n,3)
n_power_4=pow(n,4)
mazeCells=[]
firstMazeIndex=randrange(0,n_power_4)

# initialize 4D array of Mazes
for _index in range(0,n_power_4):    
    cell=MazeCell()
    mazeCells.insert(_index, cell)
    
traverseBFS()
print "------------ output "
arr=[0]*255
printMazesToFile()

print "(Wallindex,Frequency)"
for i in range(0,255):
    if arr[i]!=0:
        print (i,"-",arr[i])
print "(index,visited )"
for _index in range(0,n_power_4):    
    print(_index,cell.isVisited()) 
    
    
    
    
    