import itertools
import bisect
import math
import collections

_primes = list(map(int, open("10000primes.txt").read().split()))

def _grow_primes(_primes=_primes):
    '''
    >>> primes = [2, 3]
    >>> _grow_primes(primes)
    >>> len(primes)
    102
    >>> len({2, 3, 5, 7, 11, 13} & set(primes))
    6
    >>> len({4, 6, 8, 9, 10, 12, 14, 15, 16, 18} & set(primes))
    0
    '''
    _primes 
    n = _primes[-1] + 2
    for _ in range(100):
        while not all(n % p for p in _primes):
            n += 2
        _primes.append(n)

def is_prime(n, _primes=_primes):
    '''
    >>> is_prime(1)
    False
    >>> is_prime(257)
    True
    >>> is_prime(109453)
    True
    >>> is_prime(109455)
    False
    >>> is_prime(109459)
    False
    '''
    if _primes[-1] < n:
        next_prime(n)
    i = bisect.bisect_left(_primes, n)
    return _primes[i] == n

def next_prime(n, primes=_primes):
    i = bisect.bisect_left(primes, n+1)
    if i < len(primes):
        return primes[i]
    while primes[-1] <= n:
        _grow_primes(primes)
    return primes[bisect.bisect(primes, n)]

def primes(_primes=_primes):
    '''
    >>> list(zip(range(10), primes()))
    [(0, 2), (1, 3), (2, 5), (3, 7), (4, 11), (5, 13), (6, 17), (7, 19), (8, 23), (9, 29)]
    '''
    p = 1
    while True:
        p = next_prime(p, _primes)
        yield p

def nth_prime(n, _primes=_primes):
    '''
    >>> nth_prime(1)
    2
    >>> nth_prime(10)
    29
    '''
    while n > len(_primes):
        _grow_primes()
    return _primes[n-1]

def square_root_cf(s):
    a0 = int(math.sqrt(s))
    yield a0
    if a0 * a0 == s: return
    a = a0
    m = 0
    d = 1
    while a != 2*a0:
        m = d * a - m
        d = (s - m * m) // d
        a = (a0 + m) // d
        yield a

def convergents(cf_expansion):
    it = iter(cf_expansion)
    p = next(it)
    q = 1
    p_ = 1
    q_ = 0
    for a in itertools.cycle(it):
        yield p, q
        p_, p = p, a * p + p_
        q_, q = q, a * q + q_

def solve_diophantine(d):
    for x, y in convergents(square_root_cf(d)):
        if x*x - d*y*y == 1:
            return x, y

def factors(n, _primes=_primes):
    '''
    >>> list(factors(1))
    []
    >>> list(factors(6))
    [2, 3]
    >>> list(factors(8))
    [2, 2, 2]
    '''
    for p in primes(_primes):
        while n % p == 0 and n > 1:
            yield p
            n /= p
        if n <= 1:
            return

def prod(*args):
    '''
    >>> prod()
    1
    >>> prod(2, 3, 4)
    24
    '''
    acc = 1
    for i in args:
        acc *= i
    return acc

def gcd(n, m):
    '''
    >>> gcd(2, 3)
    1
    >>> gcd(3, 2)
    1
    >>> gcd(4, 2)
    2
    >>> gcd(2**10, 256)
    256
    '''
    if n < m:
        n, m = m, n
    while m > 0:
        n, m = m, n % m
    return n

def mcm(*args):
    '''
    >>> mcm(2, 3, 5)
    30
    >>> mcm(2, 2, 4)
    4
    >>> mcm(1, 2, 2, 4)
    4
    >>> mcm(1, 2, 2, 4, 10)
    20
    '''
    deduped_factors = collections.defaultdict(int)
    for n in args:
        grouped_factors = collections.Counter(factors(n))
        for f, p in grouped_factors.items():
            deduped_factors[f] = max(deduped_factors[f], p)
    return prod(*[f ** p for (f, p) in deduped_factors.items()])

def by_tuples(lst, size):
    '''
    # staggered tuples of `size` elements
    >>> list(by_tuples(range(6), 3))
    [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
    '''
    return zip(*[lst[i:] for i in range(size)])
