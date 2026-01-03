from itertools import permutations


def all_distances(times):
    allDis = []
    for i in range(len(times)):
        allDis.append(single_distances(i, times))
    return allDis


def single_distances(index, times):
    distance = [float("inf") for i in range(len(times))]
    distance[index] = 0

    for k in range(len(times) - 1):
        for i in range(len(times)):
            for j in range(len(times)):
                if i == j:
                    continue
                distance[j] = min(distance[j], distance[i] + times[i][j])

    for k in range(len(times) - 1):
        for i in range(len(times)):
            for j in range(len(times)):
                if i == j:
                    continue
                if distance[j] > distance[i] + times[i][j]:
                    distance[j] = float("-inf")
    return distance


def hasNegativeCycles(distances):
    for row in distances:
        for num in row:
            if num == float("-inf"):
                return True
    return False


def findRoute(gather, limit, distances):
    enters = [False for i in range(len(distances) - 2)]
    res = None
    for i in range(1, len(distances) - 1):
        newDis = distances[0][i]
        res = findRouteRec(i, newDis, gather - 1, limit, distances, enters)
        if res != None:
            break

    return res


def findRouteRec(curr, distance, gather, limit, distances, enters):
    if gather == 0:
        if distance + distances[curr][len(distances) - 1] <= limit:
            return [curr - 1]
        else:
            return None

    enters[curr - 1] = True
    res = None
    for i in range(1, len(distances) - 1):
        if enters[i - 1]:
            continue
        newDis = distance + distances[curr][i]
        res = findRouteRec(i, newDis, gather - 1, limit, distances, enters)
        if res != None:
            res.append(curr - 1)
            return res

    enters[curr - 1] = False
    return None


def solution(times, time_limit):
    distances = all_distances(times)
    if hasNegativeCycles(distances):
        return [i for i in range(len(times) - 2)]

    for i in range(len(times) - 1, 1, -1):
        res = findRoute(i, time_limit, distances)
        if res != None:
            res.sort()
            return res

    return []


if __name__ == "__main__":
    mat = [
        [0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0],
    ]
    print(solution(mat, 1))
    mat = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
    ]
    print(solution(mat, 3))
