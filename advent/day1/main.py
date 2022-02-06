def search(item, array):
    if array == []:
        return False

    middle = array[len(array) // 2]
    if middle == item:
        return True
    elif middle > item:
        return search(item, array[: len(array) // 2])
    else:
        return search(item, array[len(array) // 2 + 1 :])


def get_pairs(array, number=3, s=2020):
    head = 0
    while head < len(array) - 2:
        for i in range(head + 1, len(array)):
            for j in range(i + 1, len(array)):
                if array[head] + array[i] + array[j] == 2020:
                    print(array[head] * array[i] * array[j])
        head += 1


fin = open("bill.txt", "r")
content = [int(i.replace(" ", "").replace("\n", "")) for i in fin.readlines()]
content.sort()

print(get_pairs(content))
