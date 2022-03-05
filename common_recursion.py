"""
Derivation for factorial:

n! = n * (n-1) * .... * 1, by definition 0! = 1
recurrence: n! = n * (n-1)! assuming n > 0
"""


def factorial_rec(n):
    """Recursive implementation of factorial: O(n) runtime, O(n) space"""
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial_dp(n):
    """DP implementation of factorial: O(n) runtime, O(n) space"""
    d = [0] * (n + 1)
    d[0] = 1
    # could alternatively have base case of d[1] = 1 and compute d[n] from there, looping from i = 2
    for i in range(1, n + 1):
        d[i] = i * d[i - 1]
    return d[n]


def factorial_iter(n):
    """Iterative implementation of factorial: O(n) runtime, O(n) space"""
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


"""
Fibonacci sequence: f(n) = 1 for n = 1, 2 and f(n) = f(n-1) + f(n-2) for n > 2
"""


def fibonacci_rec(n):
    """"""
    if n <= 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_dp(n):
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]


def fibonacci_iter(n):
    if n <= 2:
        return 1

    prev_prev_term = 1  # f(k-2)
    prev_term = 1  # f(k-1)
    for k in range(3, n + 1):
        tmp = prev_term
        # f(k) = f(k-1) + f(k-2) => f(k) at current term becomes f(k-1) at next term
        prev_term += prev_prev_term
        # f(k-1) at current term becomes f(k-2) at next term
        prev_prev_term = tmp
    return prev_term
