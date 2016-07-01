t=int(input())
for T in range(0,t):
    s=raw_input()
    str=s.split()
    a = [0]*200
    b = [0]*200
    flag =""
    stop =0
   # print str
    for i in str[0]:
        i=ord(i)
        a[i] +=1
    for i in str[1]:
        i=ord(i)
        if a[i]==0:
            flag = "YES"
            stop=1
            break
        else:
            b[i]+=1
    if stop:
        print flag
        continue
    else :
       for i in str[0]:
           i=ord(i)
           if b[i]==0:
               flag="YES"
               stop=1
               break
       if not stop:
           for i in str[0]:
               i=ord(i)
               if b[i]!=a[i]:
                   flag="NO"
                   break
               else:
                   flag="YES"
            
    print flag

