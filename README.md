# Google FooBar Challenge Solutions

![Google FooBar](https://i.imgur.com/y3y2eN3.png)

> **Note:** Google FooBar is a secret recruiting challenge triggered by specific search queries related to development. It consists of 5 levels of algorithmic problems of increasing difficulty.

This repository contains my personal solutions to the Google FooBar challenges. These problems required a deep understanding of **algorithms**, **data structures**, **linear algebra**, **number theory**, and **combinatorics**.

While many solve these for fun, I treated this as a rigorous test of efficiency and optimization. All solutions passed the hidden performance test cases (efficient time/space complexity).

## Languages & Technologies

- **Python:** Used for mathematical heavy-lifting (large integers, matrix operations) and rapid prototyping.
- **Java:** Used for object-oriented solutions and strict typing exercises.
- **Key Concepts:** Dynamic Programming, Absorbing Markov Chains, Bellman-Ford, Bitwise Operations, Recursion, and Beatty Sequences.

## Challenge Directory

| Level | Challenge Name                                             | Concept / Algorithm                           |   Language    |
| :---: | :--------------------------------------------------------- | :-------------------------------------------- | :-----------: |
| **1** | **[Minion Work Assignments](./Level 1/Exercise 1)**        | Set Theory & Filtering                        |    Python     |
| **2** | **[Don't Get Volunteered!](./Level 2/Exercise 1)**         | Breadth-First Search (Shortest Path)          |    Python     |
| **2** | **[Please Pass the Coded Messages](./Level 2/Exercise 2)** | Recursion vs. Number Theory                   | Java / Python |
| **3** | **[Doomsday Fuel](./Level 3/Exercise 1)**                  | Absorbing Markov Chains & Matrix Inversion    |    Python     |
| **3** | **[Find the Access Codes](./Level 3/Exercise 2)**          | Dynamic Programming (Divisibility Chains)     | Java / Python |
| **3** | **[Fuel Injection Perfection](./Level 3/Exercise 3)**      | Greedy Algorithms & Bitwise Manipulation      |    Python     |
| **4** | **[Free the Bunnies!](./Level 4/Exercise 1)**              | Combinatorics (Hall's Marriage Theorem logic) |    Python     |
| **4** | **[Running with Bunnies](./Level 4/Exercise 2)**           | Bellman-Ford (Negative Cycles) & Permutations |    Python     |
| **5** | **[Dodge the Lasers!](./Level 5/Exercise 1)**              | Beatty Sequences & Rayleigh's Theorem         |    Python     |

## Highlights

- **Mathematical Precision:** Implemented a custom solution for **Absorbing Markov Chains** using Python's `fractions` module to avoid floating-point errors in probability calculations (Level 3).
- **Optimization:** Reduced an $O(N^3)$ brute-force problem to $O(N^2)$ using **Dynamic Programming** with backwards iteration (Level 3).
- **Graph Theory:** Solved a variation of the **Traveling Salesperson Problem** with negative edge weights (Time Travel) using the Bellman-Ford algorithm to detect infinite negative cycles (Level 4).
- **Big O Efficiency:** Handled inputs of size $10^{100}$ using $O(\log N)$ mathematical shortcuts based on **Beatty Sequences** (Level 5).

---

_Disclaimer: These solutions are for educational purposes and portfolio demonstration. If you are currently taking the challenge, I highly encourage you to attempt them yourself first!_
