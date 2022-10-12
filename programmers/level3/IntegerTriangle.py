# tree = []
# dp = []

# def get_max(depth, width):
#     global tree, dp

#     if depth >= len(tree) or width >= len(tree[depth]): return 0
#     if dp[depth][width] != -1: return dp[depth][width]

#     dp[depth][width] = tree[depth][width] + max(get_max(depth + 1, width), get_max(depth + 1, width + 1))

#     return dp[depth][width]

# def solution(triangle):
#     global tree, dp

#     tree = triangle

#     for i in range(len(triangle)):
#         leaves = []
#         for j in range(len(triangle[i])):
#             leaves.append(-1)
#         dp.append(leaves)

#     return get_max(0, 0)


solution = lambda t, l = []: max(l) if not t else solution(t[1:], [x + max(y, z) for x,y,z in zip(t[0], [0] + l, l + [0])])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
ans = solution(triangle)
print('ans => ' + f'{ans}')