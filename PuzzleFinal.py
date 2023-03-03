import PuzzleState as ps

teste = ps.PuzzleState(ps.PuzzleState.generate_puzzle())

#teste.puzzle = [[1,0,2],[3,4,5],[6,7,8]]
print(teste.puzzle == teste.final_state)

while teste.puzzle != teste.final_state:
    teste.print_puzzle()
    print("Escolha uma movimentação")
    print(teste.possible_moves())
    move = input()
    teste.do_movement(move)

print("Parabains")   
    

