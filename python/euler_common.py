import itertools
import bisect
import math
import collections

_primes = list(map(int, open("10000primes.txt").read().split()))

def _grow_primes():
    n = _primes[-1] + 2
    for _ in range(100):
        while not all(n % p for p in _primes):
            n += 2
        _primes.append(n)

def is_prime(n):
    if _primes[-1] < n:
        next_prime(n)
    i = bisect.bisect_left(_primes, n)
    return _primes[i] is n

def next_prime(n):
    i = bisect.bisect_left(_primes, n+1)
    if i < len(_primes):
        return _primes[i]
    while _primes[-1] <= n:
        _grow_primes()
    return _primes[bisect.bisect(_primes, n)]

def primes():
    p = 1
    while True:
        p = next_prime(p)
        yield p

def nth_prime(n):
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

def factors(n):
    for p in primes():
        while n % p == 0 and n > 1:
            yield p
            n /= p
        if n <= 1:
            return

def prod(*args):
    acc = 1
    for i in args:
        acc *= i
    return acc

def gcd(n, m):
    if n < m:
        n, m = m, n
    while m > 1:
        n, m = m, n % m
    return n

def mcm(*args):
    deduped_factors = collections.defaultdict(int)
    for n in args:
        grouped_factors = collections.Counter(factors(n))
        for f, p in grouped_factors.items():
            deduped_factors[f] = max(deduped_factors[f], p)
    return prod(*[f ** p for (f, p) in deduped_factors.items()])

def by_tuples(lst, size):
    return zip(*[lst[i:] for i in range(size)])
