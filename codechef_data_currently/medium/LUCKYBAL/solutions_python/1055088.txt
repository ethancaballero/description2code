n = input()
for i in range(n):
    str = raw_input()
    l = len(str)
    megacounter = 0
    counter = 0
    i = 0
    while(1):
        while(i<l and str[i]=='7'):
            i=i+1
            counter=counter+1
        if(i>=l):
            break
        megacounter = megacounter + (counter*(counter+1))/2
        i=i+1
        counter=0
    megacounter = megacounter + (counter*(counter+1))/2
    supercounter = (l*(l+1))/2 - megacounter
    print supercounter