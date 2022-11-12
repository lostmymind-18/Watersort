def reconstruct(comeFrom,current):
    backtrack=[]
    backtrack.append(current)
    while current in comeFrom:
        current=comeFrom[current]
        backtrack.append(current)
    return backtrack