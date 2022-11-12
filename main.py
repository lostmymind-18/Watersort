import testGenerator
import astar, bfs
import globals

def initialState():
    globals.numBot = int(input("How many bottles do you want?\n"))
    globals.botHei = int(input("How high are the bottles?\n"))
    globals.numCol = globals.numBot - 2
    goalCase = testGenerator.genTest(globals.numBot,globals.botHei)
    return goalCase

#Ham nay dung de ve, tuong tac va goi ham algorithm
def main(option = None):
    globals.initialize()
    backtrack = None
    count = None 
    #Chon BFS or Astar
    while option != 'A' and option != 'B':
        option = input("Please press 'B' for BFS, 'A' for Astar\n")
        if option == 'A':
            backtrack,count = astar.algorithm(initialState())
        elif option == 'B':
            backtrack,count = bfs.algorithm(initialState())
    for i in range(len(backtrack)-1,0,-1):
        #Chay doc theo cac binh, neu ma thay co su thay doi ve length
    #neu ma la be hon thi binh do la binh cho, con neu ma lon hon la binh nhan
        bcho,bnhan=0,0
        for j in range(globals.numBot):
            if(len(backtrack[i][j]) > len(backtrack[i-1][j])):
                bcho = j+1
            elif (len(backtrack[i][j]) < len(backtrack[i-1][j])):
                bnhan=j+1
        print(bcho,'->',bnhan)
    #while backtrack:
     #   current = backtrack.pop()
      #  print(current.state)
    print(len(backtrack),"steps")
    print(count,"traversed states") 
main()