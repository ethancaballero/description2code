# my solve
def solve():
    _, k = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    return sum(a * b for a, b in zip(A, B)) + k * max(map(abs, B))

if __name__ == '__main__':
    for _ in xrange(input()):
        print solve()
