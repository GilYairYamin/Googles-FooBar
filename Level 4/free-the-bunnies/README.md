# Free the Bunnies! (Google FooBar Level 4)

## The Challenge

You need to free the bunny workers before Commander Lambda's space station explodes! Unfortunately, the Commander was very careful with the highest-value workers -- they all work in separate, maximum-security work rooms. The rooms are opened by putting keys into each console, then pressing the open button on each console simultaneously. When the open button is pressed, each key opens its corresponding lock on the work room. So, the union of the keys in all of the consoles must be all of the keys. The scheme may require multiple copies of one key given to different minions.

The consoles are far enough apart that a separate minion is needed for each one. Fortunately, you have already relieved some bunnies to aid you - and even better, you were able to steal the keys while you were working as Commander Lambda's assistant. The problem is, you don't know which keys to use at which consoles. The consoles are programmed to know which keys each minion had, to prevent someone from just stealing all of the keys and using them blindly. There are signs by the consoles saying how many minions had some keys for the set of consoles. You suspect that Commander Lambda has a systematic way to decide which keys to give to each minion such that they could use the consoles.

You need to figure out the scheme that Commander Lambda used to distribute the keys. You know how many minions had keys, and how many consoles are by each work room. You know that Command Lambda wouldn't issue more keys than necessary (beyond what the key distribution scheme requires), and that you need as many bunnies with keys as there are consoles to open the work room.
Given the number of bunnies available and the number of locks required to open a work room, write a function solution(num_buns, num_required) which returns a specification of how to distribute the keys such that any num_required bunnies can open the locks, but no group of (num_required - 1) bunnies can.

Each lock is numbered starting from 0. The keys are numbered the same as the lock they open (so for a duplicate key, the number will repeat, since it opens the same lock). For a given bunny, the keys they get is represented as a sorted list of the numbers for the keys. To cover all of the bunnies, the final solution is represented by a sorted list of each individual bunny's list of keys. Find the lexicographically least such key distribution - that is, the first bunny should have keys sequentially starting from 0.

num_buns will always be between 1 and 9, and num_required will always be between 0 and 9 (both inclusive). For example, if you had 3 bunnies and required only 1 of them to open the cell, you would give each bunny the same key such that any of the 3 of them would be able to open it, like so:\
[ [0], [0], [0] ]\
If you had 2 bunnies and required both of them to open the cell, they would receive different keys (otherwise they wouldn't both actually be required), and your solution would be as follows:\
[ [0], [1] ]\
Finally, if you had 3 bunnies and required 2 of them to open the cell, then any 2 of the 3 bunnies should have all of the keys necessary to open the cell, but no single bunny would be able to do it. Thus, the solution would be:\
[ [0, 1], [0, 2], [1, 2] ]

**The Goal:**
Write a function `solution(num_buns, num_required)` which returns a list of lists representing the key distribution. Each inner list contains the keys held by a specific bunny. The keys should be lexicographically distributed (sorted).

**The Logic:**

- You have `num_buns` minions available to hold keys.
- You need `num_required` minions to be present to open the door.
- The goal is to distribute duplicate keys such that **any** group of `num_required` bunnies has all the keys needed to open the door, but **no** group of `num_required - 1` bunnies can do it.

**Constraints:**

- `num_buns` will be between 1 and 9.
- `num_required` will be between 0 and 9.

**Example:**
If `num_buns = 3` and `num_required = 2`:
Any single bunny (group of 1) cannot open the door. Any pair (group of 2) must be able to.
The solution gives keys like this: `[[0, 1], [0, 2], [1, 2]]`.

- Bunny 0 has keys 0, 1.
- Bunny 1 has keys 0, 2.
- Bunny 2 has keys 1, 2.
- Bunny 0 + Bunny 1 have keys {0, 1, 2} (All keys).

## Test Cases

| Input `num_buns` | Input `num_required` | Output                                                                                                 |
| :--------------- | :------------------- | :----------------------------------------------------------------------------------------------------- |
| `2`              | `1`                  | `[[0], [0]]`                                                                                           |
| `4`              | `4`                  | `[[0], [1], [2], [3]]`                                                                                 |
| `5`              | `3`                  | `[[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]` |

# Solution Approach

This problem is a classic application of **Combinatorics**.

### The Insight

If we need `num_required` bunnies to open the door, it implies that if we have a group of `num_required - 1` bunnies, they must be **missing at least one key**.
Conversely, for every possible group of `num_buns - (num_required - 1)` bunnies, there must be a unique key that **only they** possess.

Let $K$ be the number of copies of each key.
$$K = \text{num\_buns} - \text{num\_required} + 1$$

To satisfy the condition, we generate every possible **combination** of bunnies of size $K$. For each unique combination, we mint a new Key ID and assign it to every bunny in that group.

### Algorithm

The solution implements a manual **Combination Generator** without relying on external libraries like `itertools`.

1.  **Initialization:**

    - We verify how many copies of each key are needed (`helper` size).
    - We initialize the `helper` array with the first combination of bunny indices: `[0, 1, ..., K-1]`.
    - We create a result list `res` with empty lists for each bunny.

2.  **Generation Loop:**
    - **Distribute:** For the current combination stored in `helper`, we append the current `counter` (Key ID) to every bunny listed in `helper`.
    - **Advance:** We call `increaseHelper` to generate the next lexicographical combination.
      - This function works recursively from the end of the array, finding the rightmost index that can be incremented without overflowing the bounds `num_buns`.
      - This mimics the behavior of `itertools.combinations`.
    - **Repeat:** Increment the key `counter` and repeat until no more combinations can be generated.

### Complexity

- **Time Complexity:** $O(\binom{N}{K} \cdot K)$, where $N$ is `num_buns` and $K$ is the copies per key. Since $N \le 9$, this is computationally trivial (max $\binom{9}{4} = 126$ iterations).
- **Space Complexity:** $O(\text{Total Keys})$, which is proportional to the binomial coefficient.
