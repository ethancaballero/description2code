"""
 Problem: Tree product
 URL: http://codechef.com/MAY11/problems/TPRODUCT
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def read_tree():
    tree = [42] #starting with index 1
    tree.extend(map(lambda x: int(x), raw_input().split()))
    return tree

pre = []
h = -1
def dfs(tree, pos):
    if (pos >= (1 << (h - 1))):
        return tree[pos]

    if (pre[2*pos] != -1):
        left = pre[2*pos]
    else:
        left = dfs(tree, 2*pos)

    if (pre[2*pos + 1] != -1):
        right = pre[2*pos + 1]
    else:
        right = dfs(tree, 2*pos + 1)
   
    (left, right) = (tree[pos]*left, tree[pos]*right);
    if left > right:
        return left
    return right


h = int(raw_input())
while(h):
    tree = read_tree()
    pre = [-1]*(1 << h)
    print dfs(tree, 1) % 1000000007
    h = int(raw_input())
