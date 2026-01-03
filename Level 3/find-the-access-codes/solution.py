def solution(l):
    lucky_pair_count = [0 for _ in l]

    count = 0
    for j in range(len(l) - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            if l[j] % l[i] == 0:
                lucky_pair_count[i] += 1
                count += lucky_pair_count[j]

    return count

if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([1, 2, 3]))