from enum import Enum
import re

class Color(str, Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

class Solution:
    def __init__(self):
        self.records = []

    def handleLine(self, line):
        x = line.replace('\n', '')
        red = list(map(lambda x: int(x.replace(f' {Color.RED.value}', '')), re.findall(f'\d+ {Color.RED.value}', x)))
        green = list(map(lambda x: int(x.replace(f' {Color.GREEN.value}', '')), re.findall(f'\d+ {Color.GREEN.value}', x)))
        blue = list(map(lambda x: int(x.replace(f' {Color.BLUE.value}', '')), re.findall(f'\d+ {Color.BLUE.value}', x)))

        return {
            Color.RED.value: max(red),
            Color.GREEN.value: max(green),
            Color.BLUE.value: max(blue),
        }

    def readInput(self, filename):
        f = open(filename, 'r')

        for line in f.readlines():
            self.records.append(self.handleLine(line))

    def part1(self):
        result = 0

        bag = {
            Color.RED.value: 12,
            Color.GREEN.value: 13,
            Color.BLUE.value: 14,
        }

        for i, record in enumerate(self.records):
            correct = True

            for color in Color:
                if record[color] > bag[color]:
                    correct = False

            if correct:
                result += i + 1

        return result

    def part2(self):
        result = 0

        for record in self.records:
            power = 1

            for color in Color:
                power *= record[color]

            result += power

        return result


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 8
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 2286
    example = Solution()
    example.readInput('ex2.txt')
    
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
