import bisect

def gen_fib(upper_bound):
  a, b = 0, 1
  fibs = [a]
  while b <= upper_bound:
    fibs += [b]
    a, b = b, a + b
  return fibs

fibs = gen_fib(10**1000)
n = int(raw_input())
for i in range(n):
  f = int(raw_input())
  i = bisect.bisect_left(fibs, f)
  if fibs[i] == f:
    print 'YES'
  else:
    print 'NO'
