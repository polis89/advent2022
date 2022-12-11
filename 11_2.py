import math

monkeys = []
class Monkey:
    def __init__(self, id):
        self.id = id
        # self.items = items
        # self.test_value = test_value
        # self.operation_op = operation_op
        # self.operation_value = operation_value
        # self.monkey_true = monkey_true
        # self.monkey_false = monkey_false
        self.inspected = 0

    def __repr__(self):
        return f"Monkey {self.id} inspected {self.inspected}, items: {self.items}"

    def addItem(self, item):
        self.items.append(item)

    def process_items(self):
        for item in self.items:
            if self.operation_op == "+":
                item += item if self.operation_value == "old" else int(self.operation_value)
            elif self.operation_op == "*":
                item *= item if self.operation_value == "old" else int(self.operation_value)
            item = item % lcm
            # item = item // 3
            self.inspected += 1
            if item % self.test_value == 0:
                monkeys[self.monkey_true].addItem(item)
            else:
                monkeys[self.monkey_false].addItem(item)
        self.items = []

with open('11_input.txt', 'r') as f:
    monkeycount = 0
    for line in f:
        if line.startswith("Monkey"):
            monkey = Monkey(monkeycount)
            monkeycount += 1
        if line.strip().startswith("Starting"):
            values = line.strip().split(": ")
            values = [int(x) for x in values[1].strip().split(",")]
            monkey.items = values
        if line.strip().startswith("Operation"):
            operation = line.strip().split("= old ")
            monkey.operation_op = operation[1].strip().split(" ")[0]
            monkey.operation_value = operation[1].strip().split(" ")[1]
        if line.strip().startswith("Test"):
            monkey.test_value = int(line.strip().split("by ")[1])
        if line.strip().startswith("If true"):
            monkey.monkey_true = int(line.strip().split("monkey ")[1])
        if line.strip().startswith("If false"):
            monkey.monkey_false = int(line.strip().split("monkey ")[1])
            monkeys.append(monkey)

lcm = math.lcm(*[x.test_value for x in monkeys])
print(f"lcm: {lcm}")

for step in range(0,10000):
    print(f"simulating {step}")
    for monkey in monkeys:
        monkey.process_items()

# print(inspected.sort[0,2])

inspected = [x.inspected for x in monkeys]
inspected.sort(reverse=True)
print(monkeys)
for m in monkeys:
    print(m)
print(inspected)
print(inspected[0] * inspected[1])
