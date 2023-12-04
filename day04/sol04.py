class Solution:
    def __init__(self):
        self.records = []
        self.winning = []
        self.all = []

    def handleLine(self, line, i):
        x = line.replace('\n', '')

        splitted = x.split('|')
        winning = splitted[0].split(' ')[2:]

        self.winning.append(list(filter(lambda x: len(x) > 0, winning)))
        self.all.append(splitted[1].split())

        return x
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))
            

    def part1(self):
        res = 0

        for i, numbers in enumerate(self.winning):
            counter = 0

            for num in numbers:
                if num in self.all[i]:
                    counter += 1

            if counter > 0:
                res += 2 ** (counter - 1)

        return res

    def part2(self):
        res = 0

        res = [1 for _ in range(len(self.winning))]

        for i, numbers in enumerate(self.winning):
            counter = 0

            for num in numbers:
                if num in self.all[i]:
                    counter += 1

            for j in range(i + 1, min(i + 1 + counter, len(self.winning))):
                res[j] += res[i]

        return sum(res)


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 13
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 30
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
