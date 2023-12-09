from enum import Enum
from collections import defaultdict, Counter
from functools import cmp_to_key


class Solution:
    def __init__(self):
        self.records = []
        self.actions = []
        self.initial = []
        self.mapper = {}

    def handleLine(self, line, i):
        x = line.replace('\n', '')
        if i == 0:
            self.actions = list(x)
        elif i > 1:
            key, val = x.split(' = ')
            self.mapper[key] = val[1:-1].split(', ')
            if key.endswith('A'):
                self.initial.append(key)
    
        return x
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))

    def part1(self):
        res = 0
        current_key = 'AAA'
        i = 0

        # straightforward solution using update of current value
        while True:
            if current_key == 'ZZZ':
                break

            side = 0 if self.actions[i] == 'L' else 1

            current_key = self.mapper[current_key][side]

            i = (i + 1) % len(self.actions)
            res += 1

        return res
    
    def lcm_of_array(self, arr):
        lcm = arr[0]
        for i in range(1, len(arr)):
            num1 = lcm
            num2 = arr[i]
            gcd = 1
            # Finding GCD using Euclidean algorithm
            while num2 != 0:
                temp = num2
                num2 = num1 % num2
                num1 = temp
            gcd = num1
            lcm = (lcm * arr[i]) // gcd
        return lcm


    def part2(self):
        res, i = 0, 0
        current_loc = self.initial[:]

        meets = {}

        # for each initial location it reaches final destination in n steps
        # and after that it will re-visit it again after n steps
        # ex: if n = 5, then cycle will be 5 10 15 20 etc

        # using logic above we can find n for each initial location
        # after that find first iteration at each all of them have same final destination (dest that ends with Z)
        while len(meets.keys()) < len(self.initial):
            side = 0 if self.actions[i] == 'L' else 1

            new_loc = []
            for j, key in enumerate(current_loc):
                new_key = self.mapper[key][side]

                new_loc.append(new_key)

                # find n for each initial location
                if new_key.endswith('Z') and j not in meets:
                    meets[j] = (res + 1)

            
            current_loc = new_loc[:]
            i = (i + 1) % len(self.actions)
            res += 1

        # compute lcm for array of n's
        # ex: lcm([2, 3]) = 6; lcm([2, 3, 4]) = 12; lcm([2, 3, 4, 8]) = 24
        nums = list(meets.values())

        return self.lcm_of_array(nums)


if __name__ == '__main__':#
    # verify part 1
    stage1Solution = 6
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 6
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
