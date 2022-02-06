def get_row(seat_id):
    return seat_id // 8


def get_seat(seat_id):
    return seat_id % 8


with open("input.txt") as fin:
    content = []
    for i in fin.readlines():
        try:
            if i != "" and len(i) == 11:
                content.append(
                    i.replace("\n", "")
                    .replace("L", "0")
                    .replace("R", "1")
                    .replace("F", "0")
                    .replace("B", "1")
                )
        except:
            pass

content = [(int("0b" + i[:7], base=2), int("0b" + i[7:], base=2)) for i in content]
seat_ids = [i[0] * 8 + i[1] for i in content]
q1 = max(seat_ids)

my_id = []
for i in range(len(seat_ids)):
    if not ((seat_ids[i] - 1 in seat_ids) and (seat_ids[i] + 1 in seat_ids)):
        my_id.append(seat_ids[i])

print(q1, my_id)
