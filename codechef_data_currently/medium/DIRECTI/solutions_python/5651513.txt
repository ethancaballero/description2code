t = int(raw_input())
while t:
    n = int(raw_input())
    directions = []
    for i in range(n):
        directions.append(raw_input().split())
        if i:
            directions[i-1][0]="Left" if directions[i][0]=="Right" else "Right"
    directions[n-1][0]="Begin"
    while n:
        print ' '.join(directions.pop())
        n-=1
    t-=1