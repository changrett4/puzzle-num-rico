import random as rd
from PriorityQueue import PriorityQueue
import copy


class PuzzleState():
    final_state = [[0,1,2],[3,4,5],[6,7,8]]
    moves = {"UP":(1,0),"DOWN":(-1,0),"LEFT":(0,1),"RIGHT":(0,-1)}
    
    def __init__(self,puzzle,cost=0,parent=None,move=""):
        self.puzzle = puzzle
        self.cost = cost+ self.heuristic()
        self.parent = parent
        self.move = move
        
    
    def calculate_manhattan_distance(self,i_initial,i_final,j_inital,j_final):
        return abs(i_initial-i_final)+ abs(j_inital-j_final)
    
    def heuristic(self):
        distance =0
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                final_line = self.puzzle[i][j]//3
                final_column = self.puzzle[i][j] %3
                distance += self.calculate_manhattan_distance(i,final_line,j,final_column)
        return distance
    
    def find_index_0(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if(self.puzzle[i][j] ==0):
                    return i,j
    
    def do_movement(self,move):
        i,j = self.moves[move]
        i_0,j_0 = self.find_index_0()
        self.puzzle[i_0][j_0], self.puzzle[i_0+i][j_0+j] = self.puzzle[i_0+i][j_0+j], self.puzzle[i_0][j_0]
    
    def possible_moves(self):
        possible_moves =[]
        i,j = self.find_index_0()
        
        if(i>0):
            possible_moves.append("DOWN")
        if(i<len(self.puzzle)-1):
            possible_moves.append("UP")
        if(j>0):
            possible_moves.append("RIGHT")
        if(j<len(self.puzzle)-1):
            possible_moves.append("LEFT")
        possible_moves.append("SOLVE")
        return possible_moves
    
    def lista_matrix(lista):
        matrix=[]
        for i in range(0,len(lista),3):
            linha = [lista[i],lista[i+1],lista[i+2]]
            matrix.append(linha)
        return matrix
    
    def generate_puzzle():
        puzzle = list(range(9))
        rd.shuffle(puzzle)    
        inversions = 0
        
        for i in range(len(puzzle)):
            for j in range(i+1,len(puzzle)):
                if (puzzle[i]> puzzle[j] and (puzzle[i]!=0 and puzzle[j]!=0)):
                    inversions+=1        
        if(inversions%2!=0):
            puzzle[0],puzzle[len(puzzle)-1] = puzzle[len(puzzle)-1],puzzle[0]
        matrix=[]
        for i in range(0,len(puzzle),3):
            linha = [puzzle[i],puzzle[i+1],puzzle[i+2]]
            matrix.append(linha)
        return matrix
                   
    def get_neighbors(self):
        neighbors = []
        i, j = self.find_index_0()
        if i > 0:
            new_board = [row[:] for row in self.puzzle]
            new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
            neighbors.append(PuzzleState(new_board,self.cost+1,self,"DOWN"))
        if i < 2:
            new_board = [row[:] for row in self.puzzle]
            new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
            neighbors.append(PuzzleState(new_board, self.cost+1,self,"UP"))
        if j > 0:
            new_board = [row[:] for row in self.puzzle]
            new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
            neighbors.append(PuzzleState(new_board, self.cost+1,self,"RIGHT"))
        if j < 2:
            new_board = [row[:] for row in self.puzzle]
            new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
            neighbors.append(PuzzleState(new_board, self.cost+1,self,"LEFT"))
        return neighbors
            
    def print_puzzle(self):
        print("-------------")
        for i in range(len(self.puzzle)):
            print("|",end=" ")
            for j in range(len(self.puzzle)):
                print(f"{self.puzzle[i][j]} |",end=" ")
            print()  
            print("-------------")
    

    def solve_puzzle(self,state):
        start_puzzle = copy.deepcopy(state)
        frontier = PriorityQueue()
        frontier.insert_item((0,start_puzzle))
    
        visited = set()
    
        while frontier.queue:           
            current_puzzle = frontier.pop_item()[1]
            if current_puzzle.puzzle == current_puzzle.final_state:
                passos = []
                while current_puzzle:
                    passos.append(current_puzzle)
                    current_puzzle = current_puzzle.parent
                passos.reverse()
                return passos
        
            visited.add(str(current_puzzle.puzzle))
        
            for neighbor in current_puzzle.get_neighbors():
                if str(neighbor.puzzle) not in visited:
                    frontier.insert_item((neighbor.cost,neighbor))
        return -1              
        