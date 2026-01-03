# Doomsday Fuel (Google FooBar Level 3)

## The Challenge

Making fuel for the LAMBCHOP’s reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state). You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven’t seen all of them.

**The Goal:**
Write a function `solution(m)` that takes an array of array of non-negative integers representing how many times that state has gone to the next state and return an array of integers for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form.

**Constraints:**

- The matrix is at most 10 by 10.
- It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state (the graph is absorbing).
- The ore starts in state 0.
- The denominator will fit within a signed 32-bit integer.

## Test Cases

| Input `m`                                                                                                                  | Output             |
| :------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| `[[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]`                                    | `[7, 6, 8, 21]`    |
| `[[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]` | `[0, 3, 2, 9, 14]` |

# Solution Approach

This problem models the ore transitions as an **Absorbing Markov Chain**. The goal is to calculate the limiting probability of being absorbed into each specific terminal state starting from the initial state ($s_0$).

The solution implements the standard linear algebra approach for Markov Chains: computing the **Fundamental Matrix**.

### Algorithm

1.  **State Classification & Reordering:**
    The input matrix `m` is often unordered. The solution first identifies **Stable (Terminal)** states (rows with all zeros) and **Transient** states. It then swaps rows and columns to rearrange the matrix into the **Canonical Form**:

    $$
    P = \begin{pmatrix}
    I & 0 \\
    R & Q
    \end{pmatrix}
    $$

    Where:

    - $I$: Identity matrix (Stable $\to$ Stable transitions).
    - $0$: Zero matrix (Stable $\to$ Transient transitions).
    - $R$: Transient $\to$ Stable transitions.
    - $Q$: Transient $\to$ Transient transitions.

2.  **Probability Normalization:**
    The input provides raw counts. The code converts these to probabilities using Python's `fractions.Fraction` class to maintain exact precision without floating-point errors.

3.  **The Fundamental Matrix ($N$):**
    The Fundamental Matrix $N$ represents the expected number of times the process is in a transient state $j$ given that it started in transient state $i$. It is calculated as:
    $$N = (I - Q)^{-1}$$
    The code implements custom matrix subtraction and Gaussian elimination for matrix inversion to handle the `Fraction` objects.

4.  **Absorption Probabilities ($B$):**
    The probability of being absorbed in a specific stable state is given by the product of the Fundamental Matrix and the Transient-to-Stable matrix:
    $$B = N \times R$$
    The solution computes this product and extracts the probabilities corresponding to the starting state (State 0).

5.  **Output Formatting:**
    Finally, the code finds the **Least Common Multiple (LCM)** of the denominators in the result vector to format the output as `[numerator1, numerator2, ..., common_denominator]`.
