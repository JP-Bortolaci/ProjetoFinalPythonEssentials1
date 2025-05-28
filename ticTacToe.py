import random

choiceBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    
def move(playerOrPc, jogada = 5):
    if jogada < 1 or jogada > 9:
        print("Número inválido! Digite outro: ")
        return False
    else:
        if board[(jogada - 1) // 3][(jogada % 3) - 1] == jogada:
            board[(jogada - 1) // 3][(jogada % 3) - 1] = playerOrPc
            choiceBoard.remove(jogada)
            displayBoard(board)
            return True
        elif board[(jogada - 1) // 3][(jogada % 3) - 1] == "O" or board[(jogada - 1) // 3][(jogada % 3) - 1] == "X":
            print("Esta casa já está ocupada!")
            return False

def displayBoard(board):
    horizontalLine = "+-------+-------+-------+"

    for row in board:
        print(horizontalLine)
        print("|       |       |       |")
        
        # imprime os elementos centralizados
        print("|", end="")
        for element in row:
            print(f"  {str(element).center(3)}  |", end="")
        print()
        
        print("|       |       |       |")
    print(horizontalLine)

def hasWinner(board):
    playerCounter = 0
    pcCounter = 0
    for row in board:
        for element in row:
            if element == "O":
                playerCounter += 1
            if element == "X":
                pcCounter += 1
        if playerCounter > 2:
            print("O jogador venceu!")
            return True
        elif pcCounter > 2:
            print("O computador venceu!")
            return True
        pcCounter = 0
        playerCounter = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[j][i] == "O":
                playerCounter += 1
            if board[j][i] == "X":
                pcCounter += 1
        if playerCounter > 2:
            print("O jogador venceu na vertical!")
            return True
        elif pcCounter > 2:
            print("O computador venceu na vertical!")
            return True
        pcCounter = 0
        playerCounter = 0

    for i in range(len(board)):
        if board[i][i] == "O":
            playerCounter += 1
        if board[i][i] == "X":
            pcCounter += 1
        if playerCounter > 2:
            print("O jogador venceu na diagonal!")
            return True
        elif pcCounter > 2:
            print("O computador venceu na diagonal!")
            return True
    pcCounter = 0
    playerCounter = 0

    j = 2
    for i in range(len(board)):
        if board[i][j] == "O":
            playerCounter += 1
        if board[i][j] == "X":
            pcCounter += 1
        if playerCounter > 2:
            print("O jogador venceu na diagonal inversa!")
            return True
        elif pcCounter > 2:
            print("O computador venceu na diagonal inversa!")
            return True
        j -= 1
    pcCounter = 0
    playerCounter = 0

    if not hasInt(board):
        print("O jogo empatou!")
        return True

    return False

def hasInt(board):
    for row in board:
        for element in row:
            if isinstance(element, int):
                return True
    return False

winner = False
player = True

pcBool = move("X", 5)
while not winner:
    while(player):
        playerMove = int(input("Digite seu movimento: "))
        playerBool = move("O", playerMove)
        if playerBool:
            player = not player
    
    if hasWinner(board):
        break

    while(not player):
        pcMove = random.choice(choiceBoard)
        pcBool = move("X", pcMove)
        if pcBool:
            player = not player
        
    if hasWinner(board):
        break