import PuzzleState as ps
from PriorityQueue import PriorityQueue
teste = ps.PuzzleState(ps.PuzzleState.generate_puzzle(),move="START")

while teste.puzzle != teste.final_state:
    teste.print_puzzle()
    print(teste.possible_moves())
    move = input()
    if(move!="SOLVE"):
        teste.do_movement(move)
    else:
        solution = teste.solve_puzzle(teste)
        if(solution==-1):
            print("IMPOSSIVEL RESOLVER A PARTIR DESSE ESTADO")
        else:
            count =0
            for i in range(len(solution)):
                print(f" move: {solution[i].move} ; cost: {solution[i].heuristic() + i} ;n_passo: {i}")
                solution[i].print_puzzle()
            teste.puzzle = teste.final_state 
           






