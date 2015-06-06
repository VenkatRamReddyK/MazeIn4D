#Initally No Maze Cell is visited and contains all walls.
#And we will try to break few Walls such that there is a at least one break of wall for each and every cell

class MazeCell:    
    def __init__(self):
        self._walls=255     # initializes with walls in all directions:  11111111
        self._visited=False # initializes No wall is visited. i.e no wall is broken

    def getWalls(self):
        return self._walls
    
    def visit(self):
        self._visited=True

    def setWalls(self,walls):
        self._walls=walls
    
    def isVisited(self):
        return self._visited