from enum import Enum
from collections import defaultdict, Counter
from functools import cmp_to_key

cards = [
    'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2',
]

cards2 = [
    'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J',
]

class Hand(int, Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

def sorting(hand1, hand2, c):
    for i in range(5):
        index1 = c.index(hand1[0][i])
        index2 = c.index(hand2[0][i])

        if index1 < index2:
            return 1
        elif index1 > index2:
            return -1

    return 1

def sortHand(hand1, hand2):
    return sorting(hand1, hand2, cards)

def sortHand2(hand1, hand2):
    return sorting(hand1, hand2, cards2)

def sortHandType(hand1: Hand, hand2: Hand):
    return 1 if hand1.value > hand2.value else -1

class Solution:
    def __init__(self):
        self.records = []

    def handleLine(self, line, i):
        x = line.replace('\n', '')
        hand, bid = x.split(' ')
    
        return (hand, int(bid))
        

    def readInput(self, filename):
        f = open(filename, 'r')

        for i, line in enumerate(f.readlines()):
            self.records.append(self.handleLine(line, i))

    def getHandType(self, hand):
        c = Counter(hand)

        # combination of hand
        unique_length = [
            [5],
            [1, 4],
            [2, 3],
            [1, 1, 3],
            [1, 2, 2],
            [1, 1, 1, 2],
            [1, 1, 1, 1, 1],
        ][::-1]

        # get Hand from enum based on combination index
        index = unique_length.index(sorted(list(c.values()))) + 1
        return Hand(index)

    def getHandType2(self, hand):
        unique = set(hand)

        if 'J' in unique:
            if len(unique) == 1:
                return Hand.FIVE_KIND

            # get highest hand based on possible replacements of Joker
            possible_hand = []
            for c in unique:
                if c != 'J':
                    possible_hand.append(self.getHandType(hand.replace('J', c)))
            possible_hand = sorted(possible_hand, key=cmp_to_key(sortHandType))
            return possible_hand[-1]
        else:
            return self.getHandType(hand)

    def part1(self):
        ordered_hand = defaultdict(list)

        for hand, bid in self.records:
            hand_type = self.getHandType(hand)
            ordered_hand[hand_type].append((hand, bid))

        # sort hand by strongest card
        for key, val in ordered_hand.items():
            ordered_hand[key] = sorted(val, key=cmp_to_key(sortHand))

        counter = 1
        res = 0

        for key in Hand:
            for val in ordered_hand[key]:
                res += val[1] * counter
                counter += 1

        return res


    def part2(self):
        ordered_hand = defaultdict(list)

        for hand, bid in self.records:
            hand_type = self.getHandType2(hand)
            ordered_hand[hand_type].append((hand, bid))

        for key, val in ordered_hand.items():
            ordered_hand[key] = sorted(val, key=cmp_to_key(sortHand2))

        counter = 1
        res = 0

        for key in Hand:
            for val in ordered_hand[key]:
                res += val[1] * counter
                counter += 1

        return res


if __name__ == '__main__':
    # verify part 1
    stage1Solution = 6440
    example = Solution()
    example.readInput('ex1.txt')
    assert example.part1() == stage1Solution

    # solution part 1
    sol = Solution()
    sol.readInput('input.txt')
    print('part 1:', sol.part1())

    # verify part 2
    stage2Solution = 5905
    example = Solution()
    example.readInput('ex2.txt')
    assert example.part2() == stage2Solution

    # solution part 2
    sol2 = Solution()
    sol2.readInput('input.txt')
    print('part 2:', sol2.part2())
