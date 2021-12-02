# first part
with open('input.txt', 'r') as file:
    position = {'horizontal': 0, 'depth': 0}
    for line in file:
        direction, steps = line.rstrip('\n').split()
        if direction == 'forward':
            position['horizontal'] += int(steps)
        if direction == 'down':
            position['depth'] += int(steps)
        if direction == 'up':
            position['depth'] -= int(steps)

mult = position['depth'] * position['horizontal']
print("Horizontal Pos. x Vertical Pos. = %d" % mult)

# second part
with open('input.txt', 'r') as file:
    position = {'horizontal': 0, 'depth': 0, 'aim': 0}
    for line in file:
        direction, steps = line.rstrip('\n').split()
        if direction == 'forward':
            position['horizontal'] += int(steps)
            position['depth'] += position['aim'] * int(steps)
        if direction == 'down':
            position['aim'] += int(steps)
        if direction == 'up':
            position['aim'] -= int(steps)

mult = position['depth'] * position['horizontal']
print("Horizontal Pos. x Vertical Pos.: %d" %mult)
