from sys import stdin
from heapq import heappush, heappop

def v_con(M, graph, N):
	while M > 0:
		a, b = map(int, stdin.readline().split())
		graph[a][b] = 0
		if not graph[b].has_key(a):
			if a == 1 and b == N:
				graph[b][a] = 1
			elif a != 1:
				graph[b][a] = 1
		M = M - 1
	return graph

def relax(G, u, v, D):
	d = D.get(u, float('inf'))+G[u][v]
	if d < D.get(v, float('inf')):
		D[v] = d
		return True

def dijkstra(G, s=1):
	D, Q, S = {s:0}, [(0,s)], set()
	while Q:
		_, u = heappop(Q)
		if u in S:	continue
		S.add(u)
		for v in graph[u]:
			relax(graph, u, v, D)
			heappush(Q, (D[v], v))
	return D

N, M = map(int, stdin.readline().split())

graph = [0]
L = N
while L>0:
	graph.append({})
	L = L - 1


graph = v_con(M, graph, N)
D = dijkstra(graph)
if D.has_key(N):
	print D[N]
else:
	print -1