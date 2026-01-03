# Find the Access Codes (Google FooBar Level 3)

## The Challenge

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple $(x, y, z)$ where $x$ divides $y$ and $y$ divides $z$, such as $(1, 2, 4)$. With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

**The Goal:**
Write a function `solution(l)` that takes a list of positive integers `l` and counts the number of "lucky triples" of $(l_i, l_j, l_k)$ where the list indices meet the requirement $i < j < k$. The length of `l` is between 2 and 2000 inclusive. The elements of `l` are between 1 and 999999 inclusive. The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

**Example:**
`[1, 2, 3, 4, 5, 6]` has the triples: `[1, 2, 4]`, `[1, 2, 6]`, `[1, 3, 6]`, making the solution 3 total.

## Test Cases

| Input `l`            | Output |
| :------------------- | :----- |
| `[1, 2, 3, 4, 5, 6]` | `3`    |
| `[1, 1, 1]`          | `1`    |

# Solution Approach

The problem asks us to find the number of triplets $(l_i, l_j, l_k)$ such that $i < j < k$ and the divisibility chain $l_i | l_j | l_k$ holds.

The solution implemented in `Solution.java` uses a direct **Brute Force** approach to iterate through all valid combinations of indices.

### Algorithm

1.  **Triple Loop Iteration:**
    - The code uses three nested loops to select indices $i$, $j$, and $k$ such that $0 \le i < j < k < \text{length}$.
2.  **Pruning (Optimization):**
    - After selecting $l_i$ and $l_j$, the code immediately checks if `l[j] % l[i] == 0`.
    - If $l_j$ is **not** divisible by $l_i$, the inner loop (for $k$) is skipped entirely using `continue`. This optimization significantly reduces the number of operations for non-divisible inputs.
3.  **Verification:**
    - Inside the inner loop, the code checks the second divisibility condition: `l[k] % l[j] == 0`.
    - If true, it increments the `counter`.

### Complexity

- **Time Complexity:** $O(N^3)$ in the worst-case scenario (e.g., an array like `[1, 1, ..., 1]` where every pair is divisible), where $N$ is the number of elements in the list.
- **Space Complexity:** $O(1)$, as the solution modifies no data structures and uses only integer counters.

# Alternative Approach (Python): Dynamic Programming

While the brute-force Java approach is intuitive, it scales poorly ($O(N^3)$). This Python solution utilizes **Dynamic Programming** with **Backwards Iteration** to solve the problem in $O(N^2)$ time, making it suitable for the maximum input size ($N=2000$).

**The Core Insight:**
A "lucky triple" $(i, j, k)$ is essentially a "lucky pair" $(i, j)$ connected to another "lucky pair" $(j, k)$. Instead of finding all three at once, we can cache the number of valid $(j, k)$ pairs and reuse that information when we find a valid $i$.

**Algorithm:**

1.  **Cache State:** We maintain an array `lucky_pair_count` where index `i` stores the count of valid divisors found _after_ index `i` (i.e., potential $k$'s for a future $j$).
2.  **Backwards Iteration:** By iterating from the end of the list to the start, we ensure that when we process index $i$, we have already fully computed the necessary data for all indices $j > i$.
3.  **The Accumulation Step:**
    - We iterate $j$ backwards from `len(l)` down to `0`.
    - We iterate $i$ backwards from `j` down to `0`.
    - If `l[j]` is divisible by `l[i]`:
      1.  **Cache Update:** `lucky_pair_count[i] += 1`. We record that index $i$ has a valid multiple at $j$. (This prepares $i$ to act as a $j$ for a future, smaller number).
      2.  **Count Triples:** `count += lucky_pair_count[j]`. We know we just formed a pair $(i, j)$. We look up how many pre-calculated multiples $j$ has (represented by `lucky_pair_count[j]`). Each of those multiples forms a valid triple $(i, j, k)$.

**Code Snippet:**

```python
def solution(l):
    lucky_pair_count = [0 for _ in l]
    count = 0
    # Iterate backwards to build the cache from right to left
    for j in range(len(l) - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            if l[j] % l[i] == 0:
                lucky_pair_count[i] += 1
                count += lucky_pair_count[j]
    return count
```
