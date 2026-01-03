def solution(num_buns, num_required):
    res = [[] for i in range(num_buns)]
    helper = [i for i in range(num_buns - num_required + 1)]
    counter = 0

    while True:
        for i in helper:
            res[i].append(counter)

        if not increaseHelper(helper, num_buns):
            break
        counter += 1
    return res


def increaseHelper(helper, num_buns):
    return increaseHelperRec(helper, len(helper) - 1, num_buns)


def increaseHelperRec(helper, index, num_buns):
    if index < 0:
        return False

    helper[index] += 1
    if helper[index] < num_buns:
        return True

    if increaseHelperRec(helper, index - 1, num_buns - 1):
        helper[index] = helper[index - 1] + 1
        return True
    return False
