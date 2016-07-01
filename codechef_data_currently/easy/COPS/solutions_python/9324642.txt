T = int(raw_input())

for i in range(T):
    M, x, y = map(int, raw_input().split())
    houses = map(int, raw_input().split())
    extrema = x*y
    num = 0
    for j in range(1, 101):
        flag = True
        for house in houses:
            if ((house - extrema) <= j <= (house + extrema)):
                flag = False
                break
        if flag:
            num += 1
    print num
            
