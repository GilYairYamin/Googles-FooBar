# Don't Get Volunteered! (Google FooBar Level 2)

## 🚀 The Challenge

As a henchman on Commander Lambda’s space station, you’re expected to be resourceful, smart, and a quick thinker. It’s not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories.

It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get “volunteered” as a test subject for the LAMBCHOP doomsday device!

**The Goal:**
Write a function called `solution(src, dest)` which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.

The function should return an integer representing the **smallest number of moves** it will take for you to travel from the source square to the destination square using a chess knight’s moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an “L” shape).

**The Board:**
Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

```text
0   1   2   3   4   5   6   7
8   9   10  11  12  13  14  15
16  17  18  19  20  21  22  23
24  25  26  27  28  29  30  31
32  33  34  35  36  37  38  39
40  41  42  43  44  45  46  47
48  49  50  51  52  53  54  55
56  57  58  59  60  61  62  63
```

## Test cases

| Input `src` | Input `dest` | Output |
| :---------- | :----------- | :----- |
| `0`         | `1`          | `3`    |
| `19`        | `36`         | `1`    |

# Solution Approach

## 1. Problem Analysis

The chessboard is essentially a **graph** where:

- **Nodes** are the 64 squares (numbered 0–63).
- **Edges** are the valid moves a Knight can make from one square to another.
- **Goal:** Find the _minimum_ number of edges (moves) to traverse from a starting node (`src`) to a target node (`dest`).

Since the "edges" (moves) are unweighted (every move costs exactly 1 step), the most efficient algorithm to find the shortest path is **Breadth-First Search (BFS)**.

## 2. Board Representation

Instead of using a 2D grid `[row][col]`, the board is flattened into a single 1D array of integers ranging from 0 to 63.

### Movement Logic

A knight moves in an "L" shape: 2 squares in one cardinal direction (horizontal/vertical) and 1 square perpendicular.
In a 1D array with a row width of 8, these moves correspond to specific integer offsets:

- **Move Right 2, Down 1:** `+2` (Right) `+8` (Down) $\rightarrow$ **`+10`**
- **Move Right 2, Up 1:** `+2` (Right) `-8` (Up) $\rightarrow$ **`-6`**
- **Move Left 2, Down 1:** `-2` (Left) `+8` (Down) $\rightarrow$ **`+6`**
- ...and so on for all 8 possible moves.

### Boundary Handling

To prevent the Knight from "wrapping around" the board (e.g., moving right from square 7 to square 8, which is actually the next row), we calculate the current column using modulo arithmetic: `current_col = src % 8`.

- **Right Moves:** If moving right by 2, we check `current_col <= 5`.
- **Left Moves:** If moving left by 2, we check `current_col >= 2`.

## 3. The Algorithm (BFS)

The solution uses a Queue to explore the board layer-by-layer:

1.  **Initialization:**

    - Push the starting square `[src, distance=0]` into the queue.
    - Create a boolean `visited` array (size 64) to ensure we don't process the same square twice.

2.  **Processing Loop:**

    - While the queue is not empty, dequeue the current square.
    - Mark the square as `visited`.
    - Generate all valid knight moves from this square using the logic described above.

3.  **Termination:**
    - For each neighbor found, check: **Is this the `dest` square?**
    - **Yes:** Return `current_distance + 1`.
    - **No:** Mark as visited and enqueue it with `current_distance + 1`.

## 4. Complexity

- **Time Complexity:** $O(1)$.
  - The board size is fixed at 64 squares. In the absolute worst-case scenario, the algorithm visits every square once. Therefore, the time taken does not grow with input size (the input is always just two integers).
- **Space Complexity:** $O(1)$.
  - The `visited` array has a constant size of 64.
  - The `queue` will never hold significantly more than 64 items.
