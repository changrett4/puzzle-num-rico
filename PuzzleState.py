import random as rd

class PuzzleState():
    final_state = [[0,1,2],[3,4,5],[6,7,8]]
    moves = {"UP":(1,0),"DOWN":(-1,0),"LEFT":(0,1),"RIGHT":(0,-1)}
    
    def __init__(self,puzzle,cost=0):
        self.puzzle = puzzle
        self.cost = cost+ self.heuristic()
    
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
        return possible_moves
    
    def count_inversions(puzzle):
        inversions =0
        for i in range(len(puzzle)):
            for j in range(i+1,len(puzzle)):
                if (puzzle[i]> puzzle[j]):
                    inversions+=1
        return inversions
    
    def validate_puzzle(self,puzzle):
        inversions = self.count_inversions(puzzle)
        if(inversions%2 != 0):
            puzzle[0],puzzle[1] = puzzle[1], puzzle[0]
        return puzzle

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
                if (puzzle[i]> puzzle[j]):
                    inversions+=1
        if(inversions%2 != 0):
            puzzle[0],puzzle[1] = puzzle[1], puzzle[0]
        matrix=[]
        for i in range(0,len(puzzle),3):
            linha = [puzzle[i],puzzle[i+1],puzzle[i+2]]
            matrix.append(linha)
        puzzle = matrix
        return puzzle
    
    def do_movement(self,move):
        i,j = self.find_index_0()
        move_i,move_j = self.moves[move]
        self.puzzle[i][j],self.puzzle[move_i+i][move_j+j] = self.puzzle[move_i+i][move_j+j],self.puzzle[i][j]            
        return self.puzzle
        
    def transition(self):
        possible_moves = self.possible_moves()
        new_states = []
        for i in possible_moves:
            new_state = PuzzleState(self.do_movement(i),1)
            new_states.append(new_state)             
            
    def print_puzzle(self):
        print("-------------")
        for i in range(len(self.puzzle)):
            print("|",end=" ")
            for j in range(len(self.puzzle)):
                print(f"{self.puzzle[i][j]} |",end=" ")
            print()  
            print("-------------")
    
     
    def __eq__(self, other) -> bool:
        return self.puzzle == other.puzzle
    
    def __lt__(self, other):
        return self.cost < other.cost
     