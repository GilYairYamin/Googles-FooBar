from queue import Queue


def directions(src):
    res = []
    if src >= 8 and src % 8 >= 2:  # (-1, -2)
        res.append(src - 10)
    if src >= 8 and src % 8 <= 5:  # (-1, 2)
        res.append(src - 6)
    if src >= 16 and src % 8 >= 1:  # (-2, -1)
        res.append(src - 17)
    if src >= 16 and src % 8 <= 6:  # (-2, 1)
        res.append(src - 15)
    if src <= 55 and src % 8 >= 2:  # (1, -2)
        res.append(src + 6)
    if src <= 55 and src % 8 <= 5:  # (1, 2)
        res.append(src + 10)
    if src <= 46 and src % 8 >= 1:  # (2, -1)
        res.append(src + 15)
    if src <= 46 and src % 8 <= 6:  # (2, 1)
        res.append(src + 17)
    return res


def solution(src, dest):
    if src == dest:
        return int(0)

    visited = [False for _ in range(64)]
    next_Queue = Queue()
    next_Queue.put([src, 0])

    while not next_Queue.empty():
        curr = next_Queue.get()
        visited[curr[0]] = True
        len = curr[1] + 1.0

        for dir in directions(curr[0]):
            if visited[dir]:
                continue
            if dir == dest:
                return int(len)
            else:
                next_Queue.put([dir, len])
    return -1


if __name__ == "__main__":
    print(solution(0, 1))
    print(solution(19, 36))
