with open('input.txt', 'r') as file:
    input = list(map(int, file.readlines()))

# first problem
biggerCount = 0
for i, depth in enumerate(input):
    if i > 0:
        if depth > input[i-1]:
            biggerCount += 1

print("Increased depth: %d" % biggerCount)

# second problem
biggerCount = 0
for i, depth in enumerate(input[:-3]):
    sum1 = sum(input[i:i+3])
    sum2 = sum(input[i+1:i+4])
    if sum2 > sum1:
        biggerCount += 1

print("Increased depth: %d" % biggerCount)
