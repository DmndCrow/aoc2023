from enum import Enum
from collections import defaultdict, Counter
from functools import cmp_to_key
import numpy as np
import itertools

class Solution:
    def __init__(self):
        self.records = []
        self.grid = []

        self.empty_x = []
        self.empty_y = []

    def handleLine(self, line, i):
        x = line.replace('\n', '')
        self.grid.append(list(x))

        if '#' not in x:
            self.empty_x.append(i)

        return x
    
        a = np.array(self.grid)
        new_a = np.transpose(a)
        new_grid = []

        for line in new_a:
            new_grid.append(line)

            if '#' not in line:
                new_grid.append(line)


        self.grid = np.transpose(np.array(new_grid))

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))
        
        # transpose matrix to count empty cols easier
        a = np.array(self.grid)
        for i, l in enumerate(np.transpose(a)):
            if '#' not in l:
                self.empty_y.append(i)

    def part1(self, mult = 2):
        res = 0
        k = 0
        star = {}

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '#':
                    star[k] = (i, j)
                    k += 1

        comb = itertools.combinations([i for i in range(len(star.keys()))], 2)
        for c in list(comb):
            x1, y1 = star[c[0]]
            x2, y2 = star[c[1]]

            mid_x, mid_y = 0, 0

            # count number of empty rows in between 2 points
            for v in self.empty_x:
                if min(x1, x2) < v < max(x1, x2):
                    mid_x += 1

            # count number of empty cols in between 2 points
            for v in self.empty_y:
                if min(y1, y2) < v < max(y1, y2):
                    mid_y += 1

            # since each empty row and empty col already counted, add the rest using mult - 1
            res += abs(x1 - x2) + abs(y1 - y2) + (mult - 1) * (mid_x + mid_y)

        return res

    def part2(self, mult):
        return self.part1(mult)


if __name__ == '__main__':#
    # verify part 1
    stage1Solution = 374
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution1 = 1030
    stage2Solution2 = 8410
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2(10) == stage2Solution1
    assert example.part2(100) == stage2Solution2

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2(1000000))
