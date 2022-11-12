import globals
import os
#used to draw something to look at
def draw(state, count):
    os.system('cls' if os.name == 'nt' else 'clear')
    #Ve mot lan 5 chai
    #Tao mot bien luu vi tri cua chai bat dau ve
    pos = 0
    #Tinh so chai con lai: lay len - vi tri
    remain = len(state) - pos
    while remain > 0:
        #So chai duoc ve la min(tren, 5)
        numDraw = min(remain,5)
        #Tien hanh ve 5 chai do
        for i in range (globals.botHei+1):
            for j in range (pos,pos+numDraw):
                if i < globals.botHei:
                    if globals.botHei-i-1 < len(state[j]):
                        print("| ",state[j][globals.botHei-i-1]," |",end='\t')
                    else:
                        print("| ",'.'," |",end='\t')
                if i == globals.botHei:
                    print('\_____/',end='\t')
            print('')
        print('')
        #Cap nhat vi tri + 5
        pos+=5
        remain = len(state) - pos
    if count != None:
        print("Count: ",count)