array=["1","2","3","4","5","6","7","8","9"]
array1=["1","2","3","4","5","6","7","8","9"]
array2=["1","2","3","4","5","6","7","8","9"]
 


Hand1=['SB1','SB2','MB1','MB2','LB1','LB2']
Hand2=['SR1','SR2','MR1','MR2','LR1','LR2']
turn=1
flag3=0
while (flag3==0):
    if (turn % 2 !=0):
        print "Player1 plays"
        print "Place new piece into the board or move a current piece from the board"
        option=raw_input("enter move or place")
        if (option=="place") :
            pawn=raw_input("Choose: Size S<M<L, Color B, Number 1,2")
            flag=0
            flag1=0
            while (flag==0 and flag1==0):
                for i in range(5):
                    if (Hand1[i]==pawn):
                        flag=1
                        print "Give a number from 0 to 8"
                        x=input()
                        if (array[x]=="0"):
                            array[x]=pawn
                            flag1=1
                        elif (array[x][0]=="L"):
                            print "There is a large piece, invalid move"
                        elif (array[x][0]=="S" and (pawn[0]=="M" or pawn[0]=="L")):
                            array1[x]=array[x]
                            array[x]=pawn
                            flag1=0
                        elif (array[x][0]=="L" and pawn[0]=="L"):
                            array2[x]=array[x]
                            array[x]=pawn
                            flag1=0

        elif (turn != 1) :
            print " Give the number of the array the pawn you wanna move is"
            y=input()
            print "Give a number from 0 to 8"
            x=input()
            if (array[y][o]=="S"):
                print "you cant move the small ones"
            elif (array[y][o]=="M" and array[x][0]=="S"):
                  array1[x]=array[x]
                  array[x]=array[y]
                  array[y]=array1[y]
            elif (array[y][0]=="L" and array[x][0]=="S"):
                  array1[x]=array[x]
                  array[x]=array[y]
                  array[y]=array2[y]
            elif (array[y][0]=="L" and array[x][0]=="M"):
                  array2[x][0]=array[x]
                  array[x]=array[y]
                  array[y]=array2[y]

    turn = turn + 1
    
    elif (turn % 2 ==0):
        print "player2 plays"
        print "Place new piece into the board or move a current piece from the board"
        option=raw_input("enter move or place")
        if (option=="place") :
            pawn=raw_input("Choose: Size S<M<L, Color R, Number 1,2")
            flag=o
            flag1=0
            while (flag==0 and flag1==0) :
                for i in range(5):
                    if (Hand2[i]==pawn):
                        flag=1
                        print "Give a number from 0 to 8"
                        x=input()
                        if (array[x]=="0"):
                            array[x]=pawn
                            flag1=1
                        elif (array[x][0]=="L"):
                            print "There is a large piece, invalid move"
                        elif (array[x][0]=="S" and (pawn[0]=="M" or pawn[0]=="L")):
                            array1[x]=array[x]
                            array[x]=pawn
                            flag1=0
                        elif (array[x][0]=="L" and pawn[0]=="L"):
                            array2[x]=array[x]
                            array[x]=pawn
                            flag1=0
                elif (turn !=2) :
                    print " Give the number of the array the pawn you wanna move is"
                    y=input()
                    print "Give a number from 0 to 8"
                    x=input()
                    if (array[y][o]=="S"):
                        print "you cant move the small ones"
                    elif (array[y][o]=="M" and array[x][0]=="S"):
                        array1[x]=array[x]
                        array[x]=array[y]
                        array[y]=array1[y]
                    elif (array[y][0]=="L" and array[x][0]=="S"):
                        array1[x]=array[x]
                        array[x]=array[y]
                        array[y]=array2[y]
                    elif (array[y][0]=="L" and array[x][0]=="M"):
                        array2[x][0]=array[x]
                        array[x]=array[y]
                        array[y]=array2[y]

    turn = turn + 1
                        
if (array[1][1]==array[2][1]==array[3][1]):
    print "The player with the color",array[1][1],"wins"
    flag3=1
elif (array[4][1]==array[5][1]==array[6][1]):
    print "The player with the color",array[4][1],"wins"
    flag3=1
elif (array[7][1]==array[8][1]==array[9][1]):
    print "The player with the color",array[7][1],"wins"
    flag3=1
elif (array[1][1]==array[3][1]==array[7][1]):
    print "The player with the color",array[1][1],"wins"
    flag3=1
elif (array[2][1]==array[4][1]==array[8][1]):
    print "The player with the color",array[2][1],"wins"
    flag3=1
elif (array[3][1]==array[6][1]==array[9][1]):
    print "The player with the color",array[3][1],"wins"
    flag3=1
elif (array[1][1]==array[5][1]==array[9][1]):
    print "The player with the color",array[1][1],"wins"
    flag3=1
elif (array[3][1]==array[5][1]==array[7][1]):
    print "The player with the color",array[3][1],"wins"
    flag3=1
else:
    print "No winner"            
