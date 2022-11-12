import globals
import os
#used to draw something to look at
def draw(state, count):
    os.system("clear")
    #Ve mot lan 5 chai
    #Tao mot bien luu vi tri cua chai bat dau ve
    pos = 0
    #Tinh so chai con lai: lay len - vi tri
    remain = len(state) - pos
    while remain > 0:
        #So chai duoc ve la min(tren, 5)
        numDraw = min(remain,5)
        #Tien hanh ve 5 chai do
        for i in range (4+1):
            for j in range (pos,pos+numDraw):
                if i < 4:
                    if 4-i-1 < len(state[j]):
                        print("| ",state[j][4-i-1]," |",end='\t')
                    else:
                        print("| ",'.'," |",end='\t')
                if i == 4:
                    print('\_____/',end='\t')
            print('')
        print('')
        #Cap nhat vi tri + 5
        pos+=5
        remain = len(state) - pos
    if count != None:
        print("Count: ",count)