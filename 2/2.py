
def part_1():

    okay_count = 0
    for line in open('input'):

        #  parse
        cnt, letter, pwd = line.split()
        min_cnt, max_cnt = [int(x) for x in cnt.split('-')]
        letter = letter[0]

        pwd_cnt = pwd.count(letter)
        if pwd_cnt >= min_cnt and pwd_cnt <= max_cnt:
            okay_count += 1

    print(okay_count)


def part_2():

    okay_count = 0
    for line in open('input'):

        # parse
        cnt, letter, pwd = line.split()
        first_pos, second_pos = [int(x)-1 for x in cnt.split('-')]
        letter = letter[0]

        if (first_pos <= len(pwd) and pwd[first_pos] == letter) ^ (second_pos <= len(pwd) and pwd[second_pos] == letter):
            okay_count += 1

    print(okay_count)


part_1()
part_2()
