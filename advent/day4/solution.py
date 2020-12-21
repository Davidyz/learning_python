must_have = {'byr':(1920, 2002),
             'iyr':(2010, 2020),
             'eyr':(2020, 2030),
             'hgt':{'cm':(150, 193),
                    'in':(59, 76)},
             'hcl':None,
             'ecl':('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
             'pid':None}

hex_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']

fin = open('passports.txt')
content = fin.readlines()
fin.close()
count1 = 0

entry = []
count2 = 0

for i in range(len(content)):
    if content[i] != "\n":
        content[i] = content[i].replace("\n", ";")

for i in "".join(content).split("\n"):
    count1 += 1
    entry.append(i.replace(' ', ';'))
    for j in must_have:
        if not j in i:
            entry.remove(i.replace(' ', ';'))
            count1 -= 1
            break

for i in entry:
    i = i.split(';')
    valid = True
    for j in i:
        if valid == False:
            break
        if j == '':
            continue

        key = j.split(':')[0]
        value = j.split(':')[1]

        if key in ('byr', 'iyr', 'eyr'):
            valid = (must_have[key][0] <= float(value) <= must_have[key][1])
            
        if key == 'hcl':
            valid = (value[0] == '#') and all([k in hex_digits for k in value[1:]]) and (len(value) == 7)
        
        if key == 'pid':
            valid = (len(value) == 9) and all([k in hex_digits[:10] for k in value])
        
        if key == 'ecl':
            valid = value in must_have[key]

        if key == 'hgt':
            try:
                if value[-2:] == 'cm':
                    valid = (150 <= float(value[:-2]) <= 193)
                elif value[-2:] == 'in':
                    valid = (59 <= float(value[:-2]) <= 76)
                else:
                    valid = False
            except ValueError:
                valid = False

    count2 += int(valid)

print(count1, count2)
