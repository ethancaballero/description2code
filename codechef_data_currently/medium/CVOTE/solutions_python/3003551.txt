chef_country = {}
chef_count = {}
country_count = {}

def get_Best_name(d):
	cnt  = -1
	name = ""
	for k in d:
		if d[k] > cnt or (d[k] == cnt and k < name):
			name = k
			cnt = d[k]
	return name


def solve():
	n, m = (int(x) for x in raw_input().split())
	for _ in xrange(n):
		name, country = raw_input().split()
		chef_country[name] = country
		chef_count[name] = 0
		country_count[country] = 0
	for _ in xrange(m):
		name = raw_input().strip()
		chef_count[name] += 1
		country_count[chef_country[name]] += 1
	print get_Best_name(country_count)
	print get_Best_name(chef_count)


if __name__ == '__main__':
	solve()
