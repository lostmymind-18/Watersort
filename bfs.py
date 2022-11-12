from collections import deque
import state,reconstruct, copy, globals

def algorithm(initialState):
    count_gen=0 #Đếm các trạng thái đã tao ra
    count = 0 #Dem cac node da check
    backtrack=deque()   #dùng để backtrack lại path
    queue = []  #Queue
    cameFrom={} #Dùng để đánh dấu lại một trạng thái tới từ đâu
    checked = deque()
    #create an initial state object
    ini=initialState
    queue.append(ini) #Đưa trạng thái đầu tiên vào stack
    while len(queue)!=0:
        current=queue.pop(0)
        checked.append(current)
        count+=1
        #Kiểm tra goal
        if state.checkGoal(current):
            backtrack=reconstruct.reconstruct(cameFrom,current)
            return backtrack,count
		#Tao mot vong lap di qua tung binh
        for i in range(globals.numBot):
            bottle1 = current[i]
            if len(bottle1)!=0:
			#Neu binh hien tai khong rong,Tao mot vong lap di qua nhung binhf khac
                for j in range(globals.numBot):
                    bottle2=current[j]
				#Neu binh chua day, va top water 1 == top water 2
                    if not bottle2 or (len(bottle2) < globals.botHei and bottle1[-1]==bottle2[-1]):
                        #Tim luong nuoc top cua bottle1
                        x = len(bottle1)-1
                        h1=0
                        while(x >= 0 and bottle1[x]==bottle1[-1]):
                            h1+=1
                            x-=1

                        #Tinh phan con lai cua bottle2
                        h2 = globals.botHei - len(bottle2)
                        #Phan chuyen tu bottle 1 sang bottle2 la min
                    #cua 2 phan ta vua tinh
                        newState = [list(bottle) for bottle in current]
                        for x in range(min(h1,h2)):
                            newState[j].append(newState[i].pop())
                        newState = tuple(tuple(bottle) for bottle in newState)
                        if newState not in queue and newState not in checked:
                            queue.append(newState)
                            count_gen+=1
                            cameFrom[newState] = current

    #return backtrack
    print("Cannot find solution!")
    return None, None