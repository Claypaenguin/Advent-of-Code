# first and second part
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

mult1 = position['aim'] * position['horizontal']
mult2 = position['depth'] * position['horizontal']
print("Horizontal Pos. x Vertical Pos. = %d" %mult1)
print("Horizontal Pos. x Vertical Pos. = %d" %mult2)
