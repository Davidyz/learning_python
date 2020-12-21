def evaluate(n, acc=0, executed=set(), end=622) :
    if n in executed:
        return acc, max(executed)
    
    finished = n == end
    executed.add(n)
    content = commands[n].split(' ')
    if content[0] == 'acc':
        acc += int(content[1])
        n += 1
    elif content[0] == 'nop':
        n += 1
    elif content[0] == 'jmp':
        n += int(content[1])
    if finished:
        return acc, end
    return evaluate(n, acc, executed)

with open('input.txt') as fin:
    commands = [i.replace('\n', '') for i in fin.readlines()]

print(evaluate(0)[0])

for i in range(len(commands)):
    if 'nop' in commands[i]:
        commands[i] = commands[i].replace('nop', 'jmp')
        ans, executed = evaluate(0, 0, set())

        if len(commands) == executed + 1:
            print(ans)
            break
        else:
            commands[i] = commands[i].replace('jmp', 'nop')

    elif 'jmp' in commands[i]:
        commands[i] = commands[i].replace('jmp', 'nop')
        ans, executed = evaluate(0, 0, set())

        if len(commands) == executed + 1:
            print(ans)
            break
        else:
            commands[i] = commands[i].replace('nop', 'jmp')
