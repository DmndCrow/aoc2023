class Solution:
    def __init__(self):
        self.lines = []
        self.total = 0

    def readInput(self, filename):
        f = open(filename, 'r')

        for line in f.readlines():
            x = line.replace('\n', '')
            self.lines.append(x)

    def replace(self, line):
        spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        d = { word: str(i + 1) for i, word in enumerate(spelled) }

        digits = []

        for i in range(1, len(line) + 1):
            check_five = d.get(line[i - 5:i], None)
            check_four = d.get(line[i - 4:i], check_five)
            var = d.get(line[i - 3:i], check_four)

            if var:
                digits.append(int(var))

            if line[i - 1].isnumeric():
                digits.append(int(line[i - 1]))

        return digits[0] * 10 + digits[-1]

    def part1(self):
        total = 0

        for line in self.lines:
            nums = list(filter(lambda x: x.isnumeric(), line))
            total += int(nums[0] + nums[-1])
        
        return total

    def part2(self):
        total = 0

        for line in self.lines:
            total += self.replace(line)

        return total


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 142
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 281
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
