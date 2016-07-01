test_cases = int(raw_input() )

for j in range(test_cases):
  input = raw_input().split() 
  X = int(input[0])
  Y = int(input[1])
  K = int(input[2])
  N = int(input[3])

  max = 0
  flag = 0
  pages = []

  for i in range(N):
    input = raw_input().split() 
    if int( input[1] ) <= K:
      if( int( input[0] ) >= (X-Y) ):
        flag =1
        for number in range(i+1 , N):
          raw_input()
        break
  if flag:
    print "LuckyChef"
  else:  
    print "UnluckyChef"





