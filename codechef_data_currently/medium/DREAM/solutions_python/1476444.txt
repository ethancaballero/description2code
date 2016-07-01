n, k = map(int, raw_input().split())
times = map(int, raw_input().split())
times = sorted(zip(times, xrange(len(times))), key=lambda x: x[0])

cnt, i = 0, 0
while(i < n):
  j = i+1
  while(j < n and times[i][0] == times[j][0] and times[j][1] - times[i][1] < k):
   j += 1
  cnt += 1
  i = j
print cnt
