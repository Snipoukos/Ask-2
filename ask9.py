for i in range (1,10) :
    for z in range (1,21) :
        board[i,z] = 0
end = false
L = 0
option = [1,2,3,4]
import random
while (end == false):
    move = random.choice(option)
    if (option == 1) :
        a = [1,2,3,4,5,6,7,8,9]
        hplace = random.choice(a)
        for i in range (1,20) :
            if (board[hplace,i] != 0 or board[hplace+1,i] !=0):
                vplace = i+1
    board[hplace,vplace] = "X"
    board[hplace+1,vplace] = "X"
    board[hplace,vplace+1] = "X"
    board[hplace,vplace+2] = "X"
    L = L + 1
    elif (option == 2) :
        a = [1,2,3,4,5,6,7]
        hplace = random.choice(a)
        for i in range (1,20) :
            if ((board[hplace,i] != 0 or board[hplace+1,i] != 0) or board[hplace+2,i] != 0 ):
                vplace = i + 1
    board[hplace,vplace] = "X"
    board[hplace+1,vplace] = "X"
    board[hplace+2,vplace] = "X
    board[hplace+2,vplace+1] = "X"
    L = L + 1
    elif (option == 3) :
        a = [1,2,3,4,5,6,7,8,9,10]
        hplace = random.choice(a)
        for i in range (1,20) :
            if ((board[hplace,i] !=  and board[hplace,i+2] == 0 and board[hplace+1,i+2] == 0) or (board[hplace,i+2] !=0 or board[hplace+1,i+2] != 0)) :
                vplace = i + 1
    board[hplace+1,vplace] = "X"
    board[hplace+1,vlpace+1] = "X"
    board[hplace+1,vplace+2] = "X"
    board[hplace,vplace+2] = "X"
    L = L + 1
    elif (option == 4) :
        a = [ 1,2,3,4,5,6,7]
        hplace = random.choice(a)
        for i in range (1,20) :
            if ((board[hplace,i] != 0 and board[hplace,i+2] == 0 and board[hplace+1,i+2] == 0 and board[hplace+,i+2] == 0) or (board[hplace+1,i+1] != 0 or board[hplace+2,i+1] != 0 )) :
                vplace = i + 1
    board[hplace,vplace] = "X"
    board[hplace,vplace+1] = "X"
    board[hplace+1,vplace+1] = "X"
    board[hplace+2,vplace+1] = "X"
    L = L + 1
    for i in range (1,20) :
        flag = true 
        for z in range (1,10) :
            if (board[i,z] != "X") :
                flag = flase
        if ( flag = true ) :
            for z in range (1,10) :
                board[i,z] = 0
                for y in range (i+1,20) :
                    board[z,y] = board[z,y+1]
    for i in range(1,10) :
        if (board[i,21] != 0 ) :
            end = true
print L                 
    
