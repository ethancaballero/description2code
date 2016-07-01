# Think for about 20 minutes and then look at constraints 
# Why why whyyy you thought so much on this one
for t in range(input()):
    h, m = map(int , raw_input().split())
    count = 0 
    for i in range(h):
        for j in range(m):
            string = str(i)+ str(j)
            if(len(set(string)) == 1):
                count += 1

    print count
