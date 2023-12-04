adj = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1),
    (1, 1), (1, -1),
    (-1, 1), (-1, -1)
]


class Solution:
    def __init__(self):
        self.records = []
        self.symbols = []
        self.visited = set()

    def handleLine(self, line, i):
        x = line.replace('\n', '')

        for j, c in enumerate(x):
            if not (c.isdigit() or c == '.'):
                self.symbols.append((i, j))

        return x
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))

    def dfs(self, i, j):
        in_boundary = -1 < i < len(self.records) and -1 < j < len(self.records[0])

        left = j - 1
        right = j + 1

        if in_boundary and self.records[i][j].isdigit() and (i, j) not in self.visited:
            number = self.records[i][j]
            self.visited.add((i, j))

            while 0 <= left and self.records[i][left].isdigit():
                number = self.records[i][left] + number
                self.visited.add((i, left))
                left -= 1

            while len(self.records[i]) > right and self.records[i][right].isdigit():
                number += self.records[i][right]
                self.visited.add((i, right))
                right += 1

            return int(number)

        return 0
            

    def part1(self):
        res = 0

        for i, j in self.symbols:
            for x, y in adj:
                res += self.dfs(i + x, j + y)

        return res

    def part2(self):
        res = 0

        for i, j in self.symbols:
            cur_res = []
            for x, y in adj:
                t = self.dfs(i + x, j + y)
                if t > 0:
                    cur_res.append(t)

            if len(cur_res) == 2:
                res += cur_res[0] * cur_res[1]

        return res


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 4361
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 467835
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
