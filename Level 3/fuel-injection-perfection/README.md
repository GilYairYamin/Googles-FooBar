# Fuel Injection Perfection (Google FooBar Level 3)

## 🚀 The Challenge

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

**The Goal:**
The fuel control mechanisms have three operations:

1.  Add one fuel pellet.
2.  Remove one fuel pellet.
3.  Divide the entire group of fuel pellets by 2 (only allowed if there is an even number of pellets).

Write a function called `solution(n)` which takes a positive integer as a string and returns the **minimum number of operations** needed to transform the number of pellets to 1.

**Constraints:**

- The fuel intake control panel can only display a number up to **309 digits** long.
- Your solution must be efficient enough to handle these massive numbers.

**Example:**
`solution("15")` returns `5` because the optimal path is:
`15` $\to$ `16` $\to$ `8` $\to$ `4` $\to$ `2` $\to$ `1`.

## 🧪 Test Cases

| Input `n` | Output |
| :-------- | :----- |
| `"4"`     | `2`    |
| `"15"`    | `5`    |

# Solution Approach

This is a shortest-path problem that can be solved greedily using **Bitwise Operations**. Since the input can be 309 digits long, we treat the number as a binary string and use integer arithmetic rather than standard recursion (which would hit stack limits).

### Algorithm: Greedy Reduction

The goal is to reach `1` as fast as possible. Dividing by 2 (right bit shift) is the most powerful operation as it reduces the number size exponentially. Therefore, our strategy is to make the number even as often as possible.

1.  **Even Numbers:**
    If `n` is even, we simply divide by 2 (`n >>= 1`). This is always the optimal move.

2.  **Odd Numbers:**
    If `n` is odd, we must either Add 1 or Subtract 1 to make it even. The greedy choice depends on which operation creates **more trailing zeros** (allowing for more subsequent divisions). We look at the last 2 bits (`n % 4`):
    - **Case A (Ends in `01` / Remainder 1):** Subtracting 1 makes it end in `00` (multiple of 4). Adding 1 makes it end in `10` (multiple of 2). **Optimal: Subtract 1.**
    - **Case B (Ends in `11` / Remainder 3):** Adding 1 causes a carry, making it end in `00` (multiple of 4) or better. Subtracting 1 makes it end in `10`. **Optimal: Add 1.**
    - **Edge Case Exception (`3`):** For `n=3`, adding 1 leads to `4 -> 2 -> 1` (2 ops). Subtracting 1 leads to `2 -> 1` (1 op). So for 3, we subtract.

### Code Breakdown

The Python solution processes the number in a loop until it reaches 1.

- **Initial Setup:** We convert the string `n` to a Python integer (which supports arbitrary precision automatically).
- **The Loop:**
  - **Even Path:** If `num % 2 == 0`, shift right and increment ops by 1.
  - **Odd Path:** We increment ops by 2 (one for the +/- and one for the subsequent division which we perform immediately). We check `num % 4` to decide whether to increment or decrement, applying the logic described above.

### Complexity

- **Time Complexity:** $O(\log N)$. In each step, we reduce the number of bits by at least 1. For a 309-digit number (approx $2^{1024}$), this takes roughly 1000 iterations.
- **Space Complexity:** $O(1)$ (ignoring the space for the large integer itself).
