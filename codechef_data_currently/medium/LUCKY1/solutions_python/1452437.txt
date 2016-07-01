res, four, seven, cnt = [0], [0], [0], [1] + [0] * 11111

for i in xrange(1, 100001):
  s = str(i)
  four.append(s.count("4") + four[-1])
  seven.append(s.count("7") + seven[-1])

  diff = four[-1] - seven[-1]
  res.append(cnt[diff] + res[-1])
  cnt[diff] += 1

for _ in xrange(int(raw_input())):
  print res[int(raw_input())]