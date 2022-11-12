from queue import PriorityQueue
from collections import deque
import state,reconstruct, copy, globals
#Heuristic function
def h(currentState):
    bottom={}
    value = 0
    for bottle in currentState:
        if bottle:
            if bottle[0] not in bottom.keys():
                bottom[bottle[0]] = 0
            else:
                bottom[bottle[0]]+=1
            top = bottle[-1]
            for water in bottle:
                if water != top:
                    value+=1
                    top = water
    value+=sum(bottom.values())
    return value

def algorithm(initialState):
    count_gen=0 #Đếm các trạng thái đã tao ra
    count = 0 #Dem cac node da check
    backtrack=deque()   #dùng để backtrack lại path
    queue=PriorityQueue()   #Dùng để chọn node ưu tiên để xét
    g_score = {} #Dùng để lưu các giá trị g của các trạng thái, cũng như là để so sánh và cập nhật giá trị tối ưu cho g
    cameFrom={} #Dùng để đánh dấu lại một trạng thái tới từ đâu
    #create an initial state object
    ini=initialState()
    queue.put((0,count_gen,ini)) #Đưa trạng thái đầu tiên vào stack
    g_score[ini] = 0  #Giá trị g cho trạng thái khởi đầu là 0.
    while queue:
        current=queue.get()[2]
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
					#Kiểm tra trạng thái mới sinh không có trong g thì thêm vô luôn, nếu có trong g thì kiểm tra xem có bé hơn g không
                #Nếu g bé hơn thì thay giá trị g của trạng thái và thay node cha của trạng thái
                        if newState not in g_score:
                            count_gen+=1
                            g_score[newState] = g_score[current]+1
                            queue.put((h(newState)+g_score[newState],count_gen,newState)) 
                            cameFrom[newState] = current
                        elif g_score[current]+1 < g_score[newState]:
                            g_score[newState] = g_score[current]+1
                            cameFrom[newState] = current

    #return backtrack
    print("Cannot find solution!")