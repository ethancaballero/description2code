t = int(raw_input())

for i in range(t):
    num = int(raw_input())

    a = []
    b = []

    no = raw_input().split()
    for n in no:
        a.append(int(n))

    no = raw_input().split()

    for n in no:
        b.append(int(n))

    count = 0

    for i in xrange(num):
        if i == 0:
            if b[i] <= a[i]:
                count = count + 1
        else:
            if b[i] <= a[i] - a[i - 1]:
                count = count + 1

    print count
