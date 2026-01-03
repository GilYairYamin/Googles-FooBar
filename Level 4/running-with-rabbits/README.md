# Running with Bunnies

You and the bunny workers need to get out of this collapsing death trap of a space station -- and fast! Unfortunately, some of the bunnies have been weakened by their long work shifts and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close.

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave -- you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest worker IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by worker ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.

For instance, in the case of\
[\
[0, 2, 2, 2, -1], # 0 = Start\
[9, 0, 2, 2, -1], # 1 = Bunny 0\
[9, 3, 0, 2, -1], # 2 = Bunny 1\
[9, 3, 2, 0, -1], # 3 = Bunny 2\
[9, 3, 2, 2, 0], # 4 = Bulkhead\
]\
and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:

Start End Delta Time Status - 0 - 1 Bulkhead initially open\
0 4 -1 2\
4 2 2 0\
2 4 -1 1\
4 3 2 -1 Bulkhead closes\
3 4 -1 0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the solution is [1, 2].

# Test cases

Input: solution([\
 [0, 2, 2, 2, -1], \
 [9, 0, 2, 2, -1], \
 [9, 3, 0, 2, -1], \
 [9, 3, 2, 0, -1], \
 [9, 3, 2, 2, 0] \
], 1)\
Output: [1, 2]

Input: solution([\
 [0, 1, 1, 1, 1], \
 [1, 0, 1, 1, 1], \
 [1, 1, 0, 1, 1], \
 [1, 1, 1, 0, 1], \
 [1, 1, 1, 1, 0] \
], 3)\
Output: [0, 1]

# Running with Bunnies (Google FooBar Level 4)

## The Challenge

You and the bunny workers need to get out of this collapsing death trap of a space station -- and fast! Unfortunately, some of the bunnies have been weakened by their long work shifts and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close.

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave -- you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

**The Goal:**
Write a function of the form `solution(times, time_limit)` to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest worker IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by worker ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.

**Example:**
For instance, in the case of:

```text
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2, 0],   # 4 = Bulkhead
]
```

## Test Cases

| Input `times`                                                                               | Input `time_limit` | Output   |
| :------------------------------------------------------------------------------------------ | :----------------- | :------- |
| `[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]` | `1`                | `[1, 2]` |
| `[[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]`     | `3`                | `[0, 1]` |

# Solution Approach

This problem can be modeled as finding the longest path (most nodes visited) in a weighted directed graph that satisfies a total weight constraint. Since the graph is very small ($N \le 7$), we can use computationally expensive exact algorithms.

### 1. All-Pairs Shortest Path (Bellman-Ford Logic)

First, we simplify the graph. We don't care about the exact path taken _between_ two bunnies, only the minimum time required to travel between them.

- Since the graph contains **negative edge weights**, Dijkstra's algorithm cannot be used.
- The solution implements the **Bellman-Ford** relaxation logic to compute the shortest path from every node to every other node.
  - It relaxes edges $|V|-1$ times to propagate shortest paths.
  - It runs a second pass to detect **Negative Cycles**. If a distance can still be improved after $|V|-1$ iterations, it means there is a loop that generates infinite time.

### 2. Negative Cycle Detection

If the graph contains a negative cycle accessible from the start and leading to the exit, we can generate infinite time.

- The `single_distances` function marks nodes involved in negative cycles with `-inf`.
- The `hasNegativeCycles` check scans the distance matrix. If _any_ node is marked `-inf`, we immediately return **all bunnies** (sorted by ID), as we can technically save everyone.

### 3. Permutation Search (DFS)

If no negative cycles exist, we must find the largest group of bunnies we can visit within the `time_limit`.

- **Search Strategy:** We iterate through possible group sizes, starting from the largest (all bunnies) down to 1.
- **Recursive Pathfinding:** The `findRouteRec` function performs a Depth-First Search (DFS) to try and visit `gather` distinct bunnies.
  - It maintains an `enters` array to track visited bunnies in the current path.
  - It checks if the current path time + distance to exit $\le$ `time_limit`.
  - Because we iterate sizes descending and bunnies by ID ascending, the first valid path we find is guaranteed to be the optimal solution.

### Complexity

- **Time Complexity:** $O(N^3)$ for the All-Pairs Shortest Path (Bellman-Ford run $N$ times) + $O(N!)$ for the permutation search. Since $N \le 7$, $7! = 5040$, making this extremely fast.
- **Space Complexity:** $O(N^2)$ to store the distance matrix.
