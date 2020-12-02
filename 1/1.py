vals = []
for line in open('inputs'):
    vals.append(int(line.strip()))


def part_1():
    for i in vals:
        if 2020 - i in vals:
            print(f"part1: {i * (2020 - i)}")
            return


def part_2():
    for i in vals:
        for j in vals:
            z = 2020 - i - j
            if z in vals:
                print(f"part2: {i * j * z}")
                return


part_1()
part_2()
