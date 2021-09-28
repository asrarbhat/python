
# using recursion and memoization
# returns -1 for invalid input
import time


def nth_fibonacci_number(integer_input):

    if not isinstance(integer_input, int) or integer_input < 0:
        return -1

    # dictionary for memoization
    memo = {0: 0, 1: 1}

    # recusive function to find fib(n)
    def fib(n):
        if (value := memo.get(n)) != None:
            return value
        value = fib(n-1)+fib(n-2)
        memo[n] = value
        return value

    return fib(integer_input)


# this one is neat and fast
def nth_fibonacci_number_iterative(integer_input):

    if not isinstance(integer_input, int) or integer_input < 0:
        return -1

    m, n = 0, 1
    for i in range(integer_input):
        m, n = n, m+n
    return m


tic = time.time()
# also has stack overflow issue.
recursive_one = nth_fibonacci_number(integer_input=100)
toc = time.time()
iterative_one = nth_fibonacci_number_iterative(
    integer_input=100)  # ten times faster
tok = time.time()
print(toc-tic, tok-toc)
