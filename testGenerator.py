import random
def genTest(numBot,botHei):
    #Du ra 2 bottle trong
    numCol = numBot - 2
    #Tao goal case
    #Tao mot list co numBot list thanh phan, sau do lap day numCol list thanh phan dau tien voi so luong botHei cac ki tu
    goalCase = [[] for _ in range(numBot)]
    #Lap day numCol dau tien voi botHei ki tu cung mau
    for i in range(numCol):
        #Mau sac cua binh
        col = chr(i+97)
        for j in range(botHei):
            goalCase[i].append(col)

    #Tao ra 2 set de luu nhung binh khong rong va nhung binh chua day
    notEmpty = {i for i in range(numCol)}
    notFull = {numCol,numCol+1}

    for _ in range(1000):
        #Chon ngau nhien mot binh trong set ko rong
        botA = random.choice(list(notEmpty))

        #Chon ngau nhien mot binh trong set chua day
        botB = random.choice(list(notFull))

        #Tinh do cao cua khoang mau tren cung
        #Luu mau tren cung
        topCol = goalCase[botA][-1]
        #Tang dan cho toi khi gap mau khac hoac la di den cuoi list
        i = len(goalCase[botA])-1
        topHei = 0
        while i >=0 and goalCase[botA][i] == topCol:
            topHei+=1
            i-=1

        #Tinh khoang trong con lai
        empHei = botHei - len(goalCase[botB])

        #Tinh luong nuoc do sang ngau nhien 
        amount = 0
        while amount == 0:
            amount = random.choice(list(range(min(empHei,topHei)+1)))

        #Thay doi chieu trang thai cua binh A va B
        #Lay ra amount phan tu dau tien cua A
        movepart = goalCase[botA][-amount:]
        goalCase[botA] = goalCase[botA][:-amount]
        #Bo vo B amount phan tu
        goalCase[botB] = goalCase[botB] + movepart

        #Cap nhat 2 set
        #Kiem tra neu bottle A rong thi lay ra khoi not Emtpy set
        notFull.add(botA)
        if(len(goalCase[botA]) == 0):
            notEmpty.remove(botA)

        #Kiem tra neu bottle B day
        notEmpty.add(botB) 
        if(len(goalCase[botB]) == botHei):
            notFull.remove(botB)
    print("Test case just generated: ",goalCase)
    #goalCase = [[],[],['g', 'r' ,'r', 'b0'],['po', 'g0', 'br', 'po'],['br', 'y', 'y' ,'g0'],['g', 'o', 'o', 'g0'],['g', 'y', 'po', 'br'],['b0', 'po', 'b', 'o'],['b', 'b0', 'br', 'r'],['b', 'y', 'o', 'b'],['b0', 'g', 'r', 'g0']]
    return goalCase