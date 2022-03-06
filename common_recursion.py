"""
Derivation for factorial:

n! = n * (n-1) * .... * 1, by definition 0! = 1
recurrence: n! = n * (n-1)! assuming n > 0
"""


def factorial_rec(n):
    """Recursive implementation of factorial: O(n) runtime, O(n) max stack frames"""
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial_tabulation(n):
    """Tabulation implementation of factorial: O(n) runtime, O(n) space"""
    d = [0] * (n + 1)
    d[0] = 1
    # could alternatively have base case of d[1] = 1 and compute d[n] from there, looping from i = 2
    for i in range(1, n + 1):
        d[i] = i * d[i - 1]
    return d[n]


def factorial_memoization(n):
    """Memoization implementation of factorial: O(n) runtime, O(n) max stack frames, O(n) pre-allocated space"""
    d = [0] * (n + 1)
    d[0] = 1

    def factorial_memoization_helper(k):
        if d[k] == 0:
            d[k] = k * factorial_memoization_helper(k - 1)
        return d[k]

    return factorial_memoization_helper(n)


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
    """Recursive implementation of fibonacci. O(2^n) runtime, O(n) max stack frames"""
    if n <= 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_memoization(n):
    """Memoization implementation of fibonacci. O(n) runtime, O(n) max stack frames, O(n) pre-allocated space"""
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1

    def fibonacci_memoization_helper(k):
        if d[k] == 0:
            d[k] = fibonacci_memoization_helper(k - 1) + fibonacci_memoization_helper(k - 2)
        return d[k]

    return fibonacci_memoization_helper(n)


def fibonacci_tabulation(n):
    """DP implementation of fibonacci. O(n) runtime, O(n) space"""
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]


def fibonacci_iter(n):
    """Iterative implementation of fibonacci. O(n) runtime, O(1) space"""
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


"""
Different ways derivation:

let n = x1 + ... + xk where xi = 1, 3, or 4. what is the # of possible combinations x1,...,xk s.t. they sum to n?
xk can only be 1, 3, or 4. thus, the sum of combinations x1,...,xk s.t. they sum to n will be:
(# combinations x1,...,xk-1 s.t. they sum to n-1) + (# combinations x1,...,xk-1 s.t. they sum to n-3) +
(# combinations x1,...,xk-1 s.t. they sum to n-4)
when we choose xk = 1, the other numbers must sum to n-1, so we count how many ways that's possible
when we choose xk = 3, the other numbers must sum to n-3, so we count how many ways that's possible
when we choose xk = 4, the other numbers must sum to n-4, so we count how many ways that's possible
these 3 counts are smaller versions of this problem hence we can obtain a recurrence relation
Dn = Dn-1 + Dn-3 + Dn-4 where Dk = # different ways to write k as a sum of 1s, 3s, and 4s.
what base cases do we need? assume that the user will enter n > 0.
D1 = D0 + D-2 + D-3, if xk = 1, there is 1 way to write 1 hence D0 = 1. it is impossible for xk = 3 or xk = 4 in this
case hence D-2, D-3 (and in fact any Dn for n < 0) should be 0 to indicate it is impossible to express n in a way that
xk being 1, 3, or 4 results in x1,...,xk-1 having to sum to a negative number. It is ok to have them sum to 0 because
that just means n = xk (there is no requirement that k be anymore than 1) ==> base cases are D0 = 1, Dn = 0 for n < 0
"""


def different_ways_rec(n):
    """Recursive implementation of different ways, O(3^n) time and O(n) space maximum"""
    if n < 0:
        return 0
    if n == 0:
        return 1
    return different_ways_rec(n - 1) + different_ways_rec(n - 3) + different_ways_rec(n - 4)


def different_ways_tabulation(n):
    """Tabulation implementation of different ways, O(n) time and O(n) space pre-allocated"""

    # build array such that d[i] = # ways to write i as sum of 1s, 3s, and 4s
    d = [0] * (n + 1)

    # d allows us to define D0 = 1 as above, but we cannot represent Dn = 0 for negative n in d, thus we need different
    # base cases. consider the following that have Dn n<0 on the RHS:
    # D1 = D0 + D-2 + D-3 => we know D1 = 1 (1 = 1), add this as a base case
    # D2 = D1 + D-1 + D-2 => we know D2 = 1 (1 + 1 = 2), add this as a base case
    # D3 = D2 + D0 + D-1 => we know D3 = 2 (1 + 1 + 1 = 3, 3 = 3) add this as a base case
    # we can express Dn for n >= 4 without negative numbers, example:
    # D4 = D0 + D1 + D3 = 1 + 1 + 2 (1 way if xk = 4 i.e. when x1 + ... + xk-1 = 0, 1 way if xk = 3 i.e. when x1 + ...
    # + xk-1 = 1, 2 ways if xk = 1 i.e. when x1 + ... + xk-1 = 3)
    # thus we now have 4 base cases (which is the minimum here)
    d[0] = 1
    d[1] = 1
    d[2] = 1
    d[3] = 2

    # now we can derive from d Di for 4 <= i <= n with our recursive step
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 3] + d[i - 4]

    return d[n]


def different_ways_memoization(n):
    """Memoization implementation of different ways, O(n) time, O(n) max stack frames, O(n) pre-allocated space"""
    d = [0] * (n + 1)
    d[0] = 1

    def different_ways_memoization_helper(k):
        if k < 0:
            return 0
        if d[k] == 0:
            d[k] = different_ways_memoization_helper(k - 1) + different_ways_memoization_helper(
                k - 3) + different_ways_memoization_helper(k - 4)
        return d[k]

    return different_ways_memoization_helper(n)
