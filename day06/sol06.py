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
        self.time = []
        self.distance = []
        self.records = []

    def handleLine(self, line, i):
        x = line.replace('\n', '')

        if i == 0:
            nums = list(filter(lambda x: x.isdigit(), x.split(' ')))
            self.time = list(map(int, nums))
        else:
            nums = list(filter(lambda x: x.isdigit(), x.split(' ')))
            self.distance = list(map(int, nums))
    
        return x
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))

    
    def finishWays(self, time, distance):
        res = 0

        i, j = 1, time - 1
        done_i, done_j = False, False

        while not (done_i and done_j):
            leftover_time_i = time - i
            leftover_time_j = time - j

            if not done_i and leftover_time_i * i > distance:
                done_i = True
            else:
                i += 1

            if not done_j and leftover_time_j * j > distance:
                done_j = True
            else:
                j -= 1
        
        return j - i + 1
            

    def part1(self):
        res = 1

        for i in range(len(self.time)):
            ways = self.finishWays(self.time[i], self.distance[i])
            res *= ways

        return res

    def part2(self):
        time = int(''.join(list(map(str, self.time))))
        distance = int(''.join(list(map(str, self.distance))))

        return self.finishWays(time, distance)


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 288
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 71503
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
