from decimal import *


def solution(str_n):
    with localcontext() as ctx:
        ctx.prec = 110
        r = Decimal(2).sqrt()
        s = Decimal(2).sqrt() + Decimal(2)
        num = int(str_n)
        return str(int(sum(num, r, s)))


def sum(n, r, s):
    if n <= 1:
        return n

    N = int(n * r)
    m = int(Decimal(N) / s)
    res = (N * (N + 1)) / 2 - m * (m + 1) - sum(m, r, s)
    return res


if __name__ == "__main__":
    print(solution("5"))
    print(solution("77"))
