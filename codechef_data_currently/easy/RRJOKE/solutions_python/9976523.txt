# Really a good joke has nothing to do with points value
for t in range(input()):
    n = input()
    for i in range(n):
        a = raw_input()

    ans = 0 
    for i in range(n+1):
        ans ^= i
    print ans 
