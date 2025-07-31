def board(table):
    for i in range (10):
        print("\n")

    for i in range (3):
        for j in range (3):
            if table[i][j]:
                print(f" {table[i][j]} ",end="")
            else:
                print("   ",end="")
            if j<2 :
                print("|",end="")
        if i<2:        
            print("\n-----------")
    print("\n")
    
    
def verify_winner(table,symbol):
    winner=False
    for i in range (3):
        if table[i][0]==table[i][1]==table[i][2]==symbol:
            winner=True
    
    for j in range (3):
        if table[0][j]==table[1][j]==table[2][j]==symbol:
            winner=True
    
    if table[0][0]==table[1][1]==table[2][2]==symbol:
        winner=True
    
    if table[0][2]==table[1][1]==table[2][0]==symbol:
        winner=True
    

    if winner:
        if symbol=="X":
            return 1
        else:
            return 2
        
    
    full=True
    for i in range(3):
        for j in range(3):
            if not table[i][j]:
                full=False

    if full==True:
        return 2
    
    return 0



def new_turn(symbol,table):
    turn=True
    while turn:
        try:
            row = int(input("Enter the row: "))
            column = int(input("Enter the column: "))
        except ValueError:
            print("Please enter a valid number.")
            continue


        if row <0 or row>2 or column<0 or column>2:
            print("Invalid values")
        elif table[row][column]:
            print("There is already a sign on that place")
        else:
            table[row][column]=symbol
            turn=False
