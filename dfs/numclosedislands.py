"""A closed island is an island that is 
totally surrounded by 0s (i.e., water). 
This means all horizontally and vertically 
connected cells of a closed island are water. 
This also means that, by definition, a closed 
island can't touch an edge (as then the edge 
cells are not connected to any water cell)."""



class Solution:
  def countClosedIslands(self, matrix):
    countClosedIslands = 0
    # TODO: Write your code here
    for r in range(1,len(matrix)-1):
        for c in range(1, len(matrix)-1):
            if matrix[r][c] == 1:
                closed_island = self.isClosed(r,c,matrix)
                if closed_island:
                    countClosedIslands += 1
    return countClosedIslands
  def isClosed(self, r,c,matrix):
    if (r < 1 or r>len(matrix)-1 or c < 1 or c > len(matrix[0])-1) and matrix[r][c] == 1:
        return False
    else:
        return True 
    
    matrix[r][c] = 0

    isIsland = True
    
    isIsland &= self.isClosed(r+1, c, matrix) 
    isIsland &=self.isClosed(r-1, c, matrix) 
    isIsland &=self.isClosed(r, c+1, matrix) 
    isIsland &=self.isClosed(r, c-1, matrix)

    return isIsland
    