def solution(data, n):
    minion_amounts = {}
    for minion in data:
        if minion not in minion_amounts.keys():
            minion_amounts[minion] = 0
        minion_amounts[minion] += 1

    return [minion for minion in data if minion_amounts[minion] <= n]

if __name__ == "__main__":
    print(solution([1, 2, 3], 0))
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
    print(solution([1, 2, 3], 6))