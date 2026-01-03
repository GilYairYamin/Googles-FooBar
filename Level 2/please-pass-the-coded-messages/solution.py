def solution(L):
    sorted_L = sorted(L)
    mark_L = [True for _ in L]
    mod_L = [val % 3 for val in sorted_L]

    sum = 0
    for val in sorted_L:
        sum += val

    mod_sum = sum % 3

    if mod_sum != 0:
        for i, mod_val in enumerate(mod_L):
            if mod_val == mod_sum:
                mark_L[i] = False
                mod_sum = 0
                break

    if mod_sum != 0:
        for i in range(len(mod_L)):
            for j in range(i + 1, len(mod_L)):
                if (mod_L[i] + mod_L[j]) % 3 == mod_sum:
                    mark_L[i] = False
                    mark_L[j] = False
                    mod_sum = 0
                    break
            if mod_sum == 0:
                break

    if mod_sum != 0:
        return 0

    res = 0
    for i in range(len(sorted_L) - 1, -1, -1):
        if mark_L[i]:
            res = res * 10 + sorted_L[i]
    return res


if __name__ == "__main__":
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
