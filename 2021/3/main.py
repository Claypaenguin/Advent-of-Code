with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

table = []
for line in lines:
    line = list(line)
    line = list(map(int, line))
    table.append(line)


def binary_to_decimal(list):
    sum = 0
    power = 0
    for i in list[::-1]:
        sum += i * 2 ** power
        power += 1
    return sum


# PART ONE
gamma = []
epsilon = []
for column in range(len(table[0])):
    col_sum = sum(row[column] for row in table)
    if col_sum > len(table)/2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

print("Power Consumption = " + str(binary_to_decimal(gamma)*binary_to_decimal(epsilon)))

# PART TWO

# oxygen levels
save_list = list(table)
column = 0
while len(table) > 1 and column < len(table[0]):
    col_sum = sum(row[column] for row in table)
    if col_sum >= len(table)/2:
        common_bit = 1
    else:
        common_bit = 0

    table = list(filter(lambda row: row[column] == common_bit, table))
    column += 1
oxygen = binary_to_decimal(table[0])

# cO2 levels
table = list(save_list)
column = 0
while len(table) > 1 and column < len(table[0]):
    col_sum = sum(row[column] for row in table)
    if col_sum >= len(table)/2:
        common_bit = 0
    else:
        common_bit = 1

    table = list(filter(lambda row: row[column] == common_bit, table))
    column += 1
cO2 = binary_to_decimal(table[0])

print("Life support rating = " + str(cO2*oxygen))
