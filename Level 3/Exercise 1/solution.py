from fractions import Fraction


def solution(m):
    stableCount, swapIndecies = findSwapIndices(m)
    m = swapMat(m, swapIndecies)
    addOnes(m, stableCount)
    convertToFraction(m)

    matI = createIdentity(len(m) - stableCount)
    matR = getSubMat(
        m, stableCount, stableCount, len(m) - stableCount, len(m) - stableCount
    )
    subMat(matI, matR)
    inverseMat(matI)

    matS = getSubMat(m, stableCount, 0, len(m) - stableCount, stableCount)
    matI = mulMat(matI, matS)

    putIn(m, matI, stableCount, 0)
    clearMat(m, stableCount, stableCount, len(m) - stableCount, len(m) - stableCount)

    vec = createVec(swapIndecies)
    vec = mulVecMat(vec, m)
    vec = restoreSwaps(vec, swapIndecies, stableCount)

    commonDen = int(smallestCommonDen(vec))
    for i in range(len(vec)):
        vec[i] *= commonDen
        vec[i] = int(vec[i])
    vec.append(commonDen)
    return vec


def smallestCommonDen(vec):
    scd = 1
    for num in vec:
        if num == 0:
            continue
        if not isinstance(num, Fraction):
            continue
        if abs(num.denominator) == scd:
            continue
        scd = smallestCommonDenNums(scd, num.denominator)
    return scd


def smallestCommonDenNums(num1, num2):
    num1 = abs(num1)
    num2 = abs(num2)
    res = 1
    i = 2
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            res *= i
            num1 /= i
            num2 /= i
        else:
            i += 1
    res *= num1 * num2
    return res


def restoreSwaps(vec, swap, count):
    res = []
    for i in range(len(vec)):
        if swap[i] < count:
            res.append(vec[swap[i]])
    return res


def mulVecMat(vec, m):
    res = []
    for i in range(len(m)):
        sum = Fraction(0, 1)
        for j in range(len(vec)):
            sum = sum + vec[j] * m[j][i]
        res.append(sum)

    return res


def createVec(swap):
    return [1 if swap[0] == i else 0 for i in range(len(swap))]


def clearMat(m, row, col, height, width):
    for i in range(height):
        for j in range(width):
            m[i + row][j + col] = 0


def putIn(m, subM, row, col):
    for i in range(len(subM)):
        for j in range(len(subM[0])):
            m[i + row][j + col] = subM[i][j]


def mulMat(m1, m2):
    res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            res[i][j] = Fraction(0, 1)
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


def createIdentity(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def getSubMat(m, row, col, height, width):
    return [[m[i + row][j + col] for j in range(width)] for i in range(height)]


def subMat(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] -= m2[i][j]


def mulRow(m, tRow, scalar):
    for i in range(len(m[tRow])):
        m[tRow][i] *= scalar


def subRow(m, tRow, adRow, scalar=1):
    addRow(m, tRow, adRow, scalar * -1)


def addRow(m, tRow, adRow, scalar=1):
    if not isinstance(scalar, Fraction):
        scalar = Fraction(scalar, 1)
    for i in range(len(m[tRow])):
        m[tRow][i] += m[adRow][i] * scalar


def addOnes(m, count):
    for i in range(count):
        m[i][i] = 1


def convertToFraction(m):
    for row in m:
        den = 0
        for num in row:
            den += num
        if den == 0:
            continue
        for i in range(len(row)):
            row[i] = Fraction(row[i], den)


def findStable(m):
    stable = []
    for row in m:
        test = True
        for num in row:
            if num != 0:
                test = False
                break

        stable.append(test)
    return stable


def findSwapIndices(m):
    stable = findStable(m)
    newOrder = []
    count = 0
    for i in range(len(stable)):
        if stable[i]:
            newOrder.append(i)
            count += 1

    for i in range(len(stable)):
        if not stable[i]:
            newOrder.append(i)

    swapIndecies = [0 for i in range(len(stable))]
    for i in range(len(stable)):
        swapIndecies[newOrder[i]] = i

    return (count, swapIndecies)


def swapMat(m, swap):
    newM = [[0 for _ in range(len(m))] for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            newM[swap[i]][swap[j]] = m[i][j]
    return newM


def inverseMat(m):
    for i in range(len(m)):
        m[i].extend([1 if j == i else 0 for j in range(len(m))])

    for i in range(len(m)):
        if m[i][i] == 0:
            for j in range(i + 1, len(m)):
                if m[i][j] != 0:
                    addRow(m, i, j)
                    break
        if m[i][i] == 0:
            continue

        mulRow(m, i, 1 / m[i][i])
        for j in range(len(m)):
            if j == i or m[j][i] == 0:
                continue
            subRow(m, j, i, m[j][i])

    for i in range(len(m)):
        m[i] = m[i][len(m) :]
