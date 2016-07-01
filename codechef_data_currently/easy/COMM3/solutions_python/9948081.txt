import math
no_of_testcases = int(input())
for each in range(no_of_testcases):
    dist = int(input())
    point_1 = map(int,raw_input().split())
    point_2 = map(int,raw_input().split())
    point_3 = map(int,raw_input().split())    
    point_12 =math.sqrt( math.pow((point_1[0] -point_2[0]),2) + math.pow((point_1[1] -point_2[1]),2))
    point_23 =math.sqrt( math.pow((point_2[0] -point_3[0]),2) + math.pow((point_2[1] -point_3[1]),2))
    point_31 =math.sqrt( math.pow((point_3[0] -point_1[0]),2) + math.pow((point_3[1] -point_1[1]),2))
    count =0
    if point_12 <= dist:
        count =count+1
    if point_23 <= dist:
        count =count+1
    if point_31 <= dist:
        count =count+1
    if count >=2:
        print "yes"
    else:
        print "no"