"""
let n = x1 + ... + xk where xi = 1, 3, or 4. what is the # of possible combinations x1,...,xk s.t. they sum to n?
xk can only be 1, 3, or 4. thus, the sum of combinations x1,...,xk s.t. they sum to n will be:
(# combinations x1,...,xk-1 s.t. they sum to n-1) + (# combinations x1,...,xk-1 s.t. they sum to n-3) +
(# combinations x1,...,xk-1 s.t. they sum to n-4)
when we choose xk = 1, the other numbers must sum to n-1, so we count how many ways that's possible
when we choose xk = 3, the other numbers must sum to n-3, so we count how many ways that's possible
when we choose xk = 4, the other numbers must sum to n-4, so we count how many ways that's possible
these 3 counts are smaller versions of this problem hence we can obtain a recurrence relation
Dn = Dn-1 + Dn-3 + Dn-4 where Dk = # different ways to write k as a sum of 1s, 3s, and 4s.
what base cases do we need? we know the following:
Dn = 0 for n <= 0 because it's impossible to write 0 as a combination of 1s, 3s, and 4s.
D1 = 1 but D0 + D-2 + D-3 = 0 != 1 = D1
D2 = 1 because we can only write it as 1 + 1. D1 + D-1 + D-2 = 1 + 0 + 0 = 1 = D2
thus, the base cases we need are: Dn = 0 for n <= 0, D1 = 1 for n = 1
"""


def different_ways_rec(n):
    """Recursive implementation of different ways, O(n3^n) time and O(n) space maximum"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return different_ways_rec(n - 1) + different_ways_rec(n - 3) + different_ways_rec(n - 4)


def different_ways_dp(n):
    """DP implementation of different ways, O(n) time and O(n) space preallocated"""

    # build array such that d[i] = # ways to write i as sum of 1s, 3s, and 4s
    d = [0] * (n + 1)

    # d allows use to define D0 = 0, and we can set D1 = 1 but not for negatives, so we have to write alternative base
    # cases. D2 = D1 + D-1 + D-2, so we need to define it. D3 = D2 + D0 + D-1, so we need to define that too.
    # D2 = 1 because we can only write 1 + 1 = 2, but D3 = 2 because we can write 1 + 1 + 1 = 3 and 3 = 3.
    # D4 and D5 can be expressed: D4 = D0 + D2 + D3, D5 = D1 + D2 + D4 so we don't have to set anymore base cases
    d[1] = 1
    d[2] = 1
    d[3] = 2

    # d[0] was set previously, and now we can derive from d Di for 4 <= i <= n
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 3] + d[i - 4]

    return d[n]
