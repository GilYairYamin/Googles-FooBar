def solution(n):
    num = abs(int(n))
    res = 0

    while num > 1:
        res += 1
        if num % 2 == 0:
            num >>= 1
            continue

        res += 1
        if num > 3 and num % 4 > 1:
            num += 1

        num >>= 1

    return res


if __name__ == "__main__":
    print(solution("4"))
    print(solution("15"))
    print(solution("12345678945678945315374764513874653456412348613545434"))
