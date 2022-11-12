import globals

class State:
    def __init__(self,state=[]):
        self.state=state

#Kiem tra trang thai hien tai da la goal hay chua
def checkGoal(state):
    #Di tung binh, neu binh nao khong rong va co 2 mau khac nhau thi return false
    count = 0
    for bottle in state:
        if bottle:
            if not all(water==bottle[-1] for water in bottle):
                return False
            count+=1
    return count==globals.numCol