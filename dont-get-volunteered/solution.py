from queue import Queue

def directions(src):
    res = []
    if src >= 8 and src % 8 >= 2:  # (-1, -2)
        res.append(src - 10) 
    if src >= 8 and src % 8 <= 5:   # (-1, 2)
        res.append(src - 6)
    if src >= 16 and src % 8 >= 1:  # (-2, -1)
        res.append(src - 17)
    if src >= 16 and src % 8 <= 6:  # (-2, 1)
        res.append(src - 15)
    if src <= 55 and src % 8 >= 2:  # (1, -2)
        res.append(src + 6)
    if src <= 55 and src % 8 <= 5:   # (1, 2)
        res.append(src + 10)
    if src <= 46 and src % 8 >= 1:  # (2, -1)
        res.append(src + 15)
    if src <= 46 and src % 8 <= 6:  # (2, 1)
        res.append(src + 17)
    return res
    
def solution(src, dest):
    if src == dest:
        return int(0)
    
    visited = {}
    for i in range(64):
        visited[i] = False
    print(visited)
    queue = Queue()
    queue.put([src, 0])
    
    while not queue.empty():
        curr = queue.get()
        visited[curr[0]] = True
        len = curr[1] + 1.
        
        for dir in directions(curr[0]):
            if visited[dir]:
                continue
            if dir == dest:
                return int(len)
            else:
                queue.put([dir, len])
    return int(-1)