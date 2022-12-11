from enum import Enum
from math import gcd

class math_op(Enum):
    ADD = 1
    MULT = 2

class Monkey:
    def __init__(self, items, op, op_num, test_num, pass_monkey, fail_monkey):
        self.items = items
        self.op = op
        self.op_num = op_num
        self.test_num = test_num
        self.pass_monkey = pass_monkey
        self.fail_monkey = fail_monkey
        self.inspection_count = 0

def part1_worry_adjustor(worry):
    return worry // 3

def part2_worry_adjustor(worry):
    global lcm
    return worry % lcm

counts = [20, 10000]
worry_adjustors = [part1_worry_adjustor, part2_worry_adjustor]

for i in range(len(counts)):

    monkeys = []
    items = []
    op = math_op.ADD
    op_num = 0
    test_num = 0
    pass_monkey = 0
    fail_monkey = 0
    with open('python/11.in','r') as f:
        for x in f.readlines():
            x = x.strip()
            if x.startswith('Monkey'):
                pass
            elif x.startswith('Starting'):
                parts = x.split(':')
                parts[1].replace(' ','')
                nums = parts[1].split(',')
                items = [int(num) for num in nums]
            elif x.startswith('Operation'):
                parts = x.split(':')
                terms = parts[1].split(' ')
                if terms[-2] == '*':
                    op = math_op.MULT
                elif terms[-2] == '+':
                    op = math_op.ADD
                if terms[-1] == 'old':
                    op_num = -1
                else:
                    op_num = int(terms[-1])
            elif x.startswith('Test'):
                parts = x.split('divisible by ')
                test_num = int(parts[1])
            elif x.startswith('If true'):
                parts = x.split(' monkey ')
                pass_monkey = int(parts[1])
            elif x.startswith('If false'):
                parts = x.split(' monkey ')
                fail_monkey = int(parts[1])
            elif x == '':
                monkeys.append(Monkey(items, op, op_num, test_num, pass_monkey, fail_monkey))
                items = []
                op = math_op.ADD
                op_num = 0
                test_num = 0
                pass_monkey = 0
                fail_monkey = 0
        monkeys.append(Monkey(items, op, op_num, test_num, pass_monkey, fail_monkey))

    all_divisors = [monkey.test_num for monkey in monkeys]

    lcm = 1
    for divisor in all_divisors:
        lcm = lcm * divisor


    for _ in range(counts[i]):
        for monkey in monkeys:
            while(len(monkey.items) > 0):

                worry_score = monkey.items.pop(0)
                monkey.inspection_count += 1

                term = monkey.op_num
                if term == -1:
                    term = worry_score

                if monkey.op == math_op.ADD:
                    worry_score += term
                else:
                    worry_score *= term

                worry_score = worry_adjustors[i](worry_score)

                if worry_score % monkey.test_num == 0:
                    monkeys[monkey.pass_monkey].items.append(worry_score)
                else:
                    monkeys[monkey.fail_monkey].items.append(worry_score)

    inspection_counts = [monkey.inspection_count for monkey in monkeys]

    inspection_counts.sort()
    print(inspection_counts[-1] * inspection_counts[-2])

# too high: 14400960000


