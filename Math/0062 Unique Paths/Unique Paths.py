# time: O(N)
# space: O(N)

import numpy as np
from itertools import product

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 生成全為 1 的array
        paths = np.ones((m, n))
        # paths = [[1]*n for _ in range(m)]

        # itertools.product 為 leecode 自行協助安裝的函式
        for i, j in product(range(1, m), range(1, n)):
            # 上方 + 左方
            paths[i][j] = paths[i-1][j] + paths[i][j-1]

        # np.ones 產生的 array 內部的資料
        return int(paths[m-1][n-1])
