import testGenerator
import astar, bfs
import globals, draw,time

def initialState():
    globals.numBot = int(input("How many bottles do you want?\n"))
    globals.botHei = int(input("How high are the bottles?\n"))
    globals.numCol = globals.numBot - 2
    goalCase = testGenerator.genTest(globals.numBot,globals.botHei)
    draw.draw(goalCase,0)
    a = None
    while a != 'C':
        a = input("This is our testcase. Press 'C' to continue...")
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
    step = len(backtrack)
    c = None
    while c != 'C':
        c = input("Solution fount, press C for the show :))")
    while len(backtrack) != 0:
        current = backtrack.pop()
        draw.draw(current,None)
        time.sleep(0.5)
    print(step,"steps")
    print(count,"traversed states") 
main()