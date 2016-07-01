
import heapq


def solver(N, K, A):
    ans, heap = [], []
    prefix = [A[0]]
    for x in A[1:]:
        prefix.append(prefix[-1] + x)

    indexMap = set()
    heapq.heappush(heap, (-prefix[-1], 0, N - 1))
    indexMap.add((0, N - 1))

    while K > 0 and len(heap) != 0:
        val, i, j = heapq.heappop(heap)
        val = -val
        ans.append(val)
        if i != j:
            if (i + 1, j) not in indexMap:
                heapq.heappush(heap, (-(val - A[i]), i + 1, j))
                indexMap.add((i + 1, j))

            if (i, j - 1) not in indexMap:
                heapq.heappush(heap, (-(val - A[j]), i, j - 1))
                indexMap.add((i, j - 1))

        K -= 1
    return ans


if __name__ == '__main__':
    N, K = map(int, raw_input().split())
    A = map(int, raw_input().split())

    print ' '.join([str(i) for i in solver(N, K, A)])
