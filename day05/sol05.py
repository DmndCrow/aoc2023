from enum import Enum
from collections import defaultdict

class Mapper(str, Enum):
    SEED = 'seed'
    SOIL = 'soil'
    FERTILIZER = 'fertilizer'
    WATER = 'water'
    LIGHT = 'light'
    TEMP = 'temperature'
    HUMIDITY = 'humidity'
    LOCATION = 'location'

class Solution:
    def __init__(self):
        self.mapper = defaultdict(list)
        self.seeds = []
        self.records = []

        self.insert_new = False
        self.key = ''
        self.keys = []

    def handleLine(self, line, i):
        x = line.replace('\n', '')

        if i == 0:
            self.seeds = list(map(int, x.split(' ')[1:]))
        elif x == '':
            self.insert_new = True

        elif self.insert_new:
            key = x.split(' ')[0]
            self.insert_new = False
            self.key = key
            self.keys.append(key)
        else:
            self.mapper[self.key].append(list(map(int, x.split(' '))))
    
        return x
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))

    def getLowestLocation(self, seed):
        cur = seed

        for key in self.keys:
            mapper = self.mapper[key]

            for dest, source, length in mapper:
                if source <= cur < source + length:
                    dif = cur - source
                    cur = dest + dif
                    break

        return cur
            

    def part1(self):
        res = 1e9

        for seed in self.seeds:
            res = min(res, self.getLowestLocation(seed))

        return res

    def part2(self):
        res = 1e9

        seeds = set()

        for i in range(0, len(self.seeds), 2):
            for j in range(self.seeds[i + 1]):
                seeds.add(self.seeds[i] + j)

        print(seeds)

        for seed in seeds:
            res = min(res, self.getLowestLocation(seed))

        return res


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 35
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 46
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
