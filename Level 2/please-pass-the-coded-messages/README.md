# Please Pass the Coded Messages (Google FooBar Level 2)

## 🚀 The Challenge

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

**The Goal:**
You have `L`, a list containing some digits (0 to 9). Write a function `solution(L)` which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. `L` will contain anywhere from 1 to 9 digits. The same digit may appear multiple times in the list, but each element in the list may only be used once.

**Example:**
If `L` is `[3, 1, 4, 1]`, the valid combinations divisible by 3 are numbers like 3, 111, etc. The largest possible number formed is `4311`.

## 🧪 Test Cases

| Input `L`            | Output  |
| :------------------- | :------ |
| `[3, 1, 4, 1]`       | `4311`  |
| `[3, 1, 4, 1, 5, 9]` | `94311` |

# Solution Approach

This solution implements a **Recursive Backtracking** approach to explore the problem space.

### Algorithm

1.  **Frequency Analysis:** The solution first counts the occurrences of each digit (0-9) and stores them in a `count` array to handle duplicates efficiently.
2.  **Recursive Construction (`maxValue`):** A recursive function explores all possible numbers that can be constructed:
    - It iterates from the largest digit (9) down to 0.
    - At each step, it branches: it either uses a digit (appending it to `curr`) or skips it.
    - This ensures we attempt to build the largest numbers first (greedy preference for higher significant digits).
3.  **Validation:** The base case checks if the constructed number is divisible by 3 (`curr % 3 == 0`). If valid, it returns the number; otherwise, it returns 0.

### 👨‍💻 Technical Note: Why Java?

Unlike the previous solutions which utilized Python for brevity or system control, this solution was intentionally architected in **Java**.

- **Goal:** To refresh and strengthen Object-Oriented Programming (OOP) skills and static typing discipline after a period of focusing on low-level languages.
- **Implementation:** The code utilizes static methods and class-level members (`count` array) to manage state across recursive calls.

### Complexity

- **Time Complexity:** Exponential $O(2^N)$ in the worst case due to the branching recursion, but constrained by the small input size ($N \le 9$).
- **Space Complexity:** $O(N)$ due to the recursion stack depth.

# 🐍 Alternative Approach (Python): The "Sum of Digits" Trick

While the Java solution uses recursion to explore all combinations, this Python solution utilizes a mathematical property of the number 3 to solve the problem in near-linear time.

**The Math:**
A number is divisible by 3 if and only if the **sum of its digits** is divisible by 3.

- If the sum of digits has a remainder of **0**, we use all digits.
- If the remainder is **1**, we remove the smallest digit with a remainder of 1 (e.g., 1, 4, 7). If none exist, we remove the two smallest digits with a remainder of 2.
- If the remainder is **2**, we remove the smallest digit with a remainder of 2 (e.g., 2, 5, 8). If none exist, we remove the two smallest digits with a remainder of 1.

**Algorithm:**

1.  **Sort:** We sort the input list `L` to ensure we always remove the _smallest_ possible digits to fix the remainder, keeping the larger digits for the final number.
2.  **Calculate Remainder:** We compute `sum(L) % 3`.
3.  **Filter:** Based on the remainder, we mark 1 or 2 specific digits for removal.
4.  **Construct:** We traverse the sorted list backwards (largest to smallest) to build the final number.

**Complexity Analysis:**

- **Time Complexity:** $O(N \log N)$ due to sorting. This is significantly faster than the Java recursive approach ($O(2^N)$) for large inputs.
- **Space Complexity:** $O(N)$ for storing the sorted list and markers.
