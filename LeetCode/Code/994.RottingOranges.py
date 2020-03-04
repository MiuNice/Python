import collections


def orangesRotting(grid):
    R, C = len(grid), len(grid[0])
    # 生成一个队列
    q = collections.deque()

    # 找到所有坏橘子
    for r, r_val in enumerate(grid):
        for c, c_val in enumerate(r_val):
            if c_val == 2:
                q.append((r, c, 0))

    d = 0  # 初始化时间

    # 对坏橘子周围的四个产生影响
    while q:
        r, c, d = q.popleft()
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, d + 1))
    if any(1 in i for i in grid):
        return -1
    return d


r = orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(r)
