import sys

if len(sys.argv) < 2:
    print('Not enough args')
    sys.exit()

filename = sys.argv[1]

prev = -1
prev_minus_1 = -1
prev_minus_2 = -1

increares_part1 = 0
increares_part2 = 0


with open(filename, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        current = int(line)
        if prev != -1 and prev < current:
            increares_part1 = increares_part1 + 1

        if prev != -1 and prev_minus_1 != -1 and prev_minus_2 != -1 and (prev + prev_minus_1 + prev_minus_2) < (current + prev + prev_minus_1):
            increares_part2 = increares_part2 + 1
        
        prev_minus_2 = prev_minus_1
        prev_minus_1 = prev
        prev = current


print(increares_part1)
print(increares_part2)
