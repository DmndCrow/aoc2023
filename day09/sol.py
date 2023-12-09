from enum import Enum
from collections import defaultdict, Counter
from functools import cmp_to_key


class Solution:
    def __init__(self):
        self.records = []

    def handleLine(self, line, i):
        x = line.replace('\n', '')
        
        return list(map(int, x.split(' ')))
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))

    def computeNext(self, nums):
        i = 0
        sequence = { i: nums }
        cur_sequence = nums[:]

        while True:
            if len(set(cur_sequence)) == 1:
                break

            new_sequence = []

            for k in range(1, len(cur_sequence)):
                new_sequence.append(cur_sequence[k] - cur_sequence[k - 1])

            i += 1
            sequence[i] = new_sequence
            cur_sequence = new_sequence[:]

        j = i

        while i >= 0:
            if i == j:
                new_arr = [sequence[i][0]] + sequence[i] + [sequence[i][0]]
            else:
                front = sequence[i][0] - sequence[i + 1][0]
                back = sequence[i + 1][-1] + sequence[i][-1]
                new_arr = [front] + sequence[i] + [back]

            sequence[i] = new_arr
            
            i -= 1

        return sequence[0]
        

    def part1(self):
        res = 0
        
        for record in self.records:
            v = self.computeNext(record)[-1]
            res += v

        return res

    def part2(self):
        res = 0
        
        for record in self.records:
            v = self.computeNext(record)[0]
            res += v

        return res


if __name__ == '__main__':#
    # verify part 1
    stage1Solution = 114
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 5
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
