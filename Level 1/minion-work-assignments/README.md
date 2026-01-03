# Minion Work Assignments (Google FooBar Level 1)

## 🚀 The Challenge

Commander Lambda's minions are upset! They're given the worst jobs on the whole space station, and some of them are starting to complain that even those worst jobs are being allocated unfairly. If you can fix this problem, it'll prove your chops to Commander Lambda so you can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, one time for each day they'll work that task. As shifts are planned well in advance, the lists for each task will contain up to 99 integers. When a minion is scheduled for the same task too many times, they'll complain about it until they're taken off the task completely. Some tasks are worse than others, so the number of scheduled assignments before a minion will refuse to do a task varies depending on the task. You figure you can speed things up by automating the removal of the minions who have been assigned a task too many times before they even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, answer(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

**The Goal:**
Write a function called `solution(data, n)` that takes in a list of less than 100 integers and a number `n`, and returns that same list but with all of the numbers that occur more than `n` times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations!

**Example:**
If `data` was `[5, 10, 15, 10, 7]` and `n` was `1`, `solution(data, n)` would return the list `[5, 15, 7]` because `10` occurs twice, and thus was removed from the list entirely.

## 🧪 Test Cases

| Input `data`                  | Input `n` | Output      |
| :---------------------------- | :-------- | :---------- |
| `[1, 2, 3]`                   | `0`       | `[]`        |
| `[1, 2, 2, 3, 3, 3, 4, 5, 5]` | `1`       | `[1, 4]`    |
| `[1, 2, 3]`                   | `6`       | `[1, 2, 3]` |

# Solution Approach

The objective is to filter the input list based on element frequency while preserving the original order. The solution implemented in `solution.py` achieves this via a two-pass algorithm.

### Algorithm

1.  **Frequency Analysis:** The solution first iterates through the input `data` list to count the occurrences of every minion ID. These counts are stored in a hash map (dictionary) where the key is the Minion ID and the value is the frequency.
2.  **Filtering:** It performs a second pass over the original list. For each ID, it checks the pre-calculated frequency. If the count is less than or equal to `n`, the ID is retained.
3.  **Order Preservation:** By iterating through the original list sequentially during the filtering phase, the relative order of the remaining elements is naturally preserved.

### Complexity

- **Time Complexity:** $O(K)$, where $K$ is the number of elements in `data`. The list is traversed exactly twice.
- **Space Complexity:** $O(K)$ to store the frequency dictionary.


