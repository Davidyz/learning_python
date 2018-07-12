#!/usr/bin/python3

import random, time

out_of_circle = 0
number = int(input("Please enter the number of random tuple you want.\nTheoriotically the greater the number is, the more accurate the result is.\n"))

def not_in_circle(x, y):
    return not x ** 2 + y ** 2 < 1

def drop():
    global out_of_circle
    x, y = random.uniform(-1, 1), random.uniform(-1,1)
    #all_points += 1
    if not_in_circle(x, y):
        out_of_circle += 1

def time_unit(s):
    hour = s // 3600
    minute = (s - 3600 * hour) // 60
    sec = (s - 3600 * hour - 60 * minute)
    return [int(hour), int(minute), round(sec, 3)]

n = number

if __name__ == '__main__':
    start = time.time()

    while number >= 0:
        drop()
        number -= 1

    end = time.time()
    t = end - start

    print('The result is {res}, computed in {hour}h {minute}min {sec}sec.'.format(res = round(4 - out_of_circle / float(n) * 4, 10),
                                                                                  hour = time_unit(t)[0],
                                                                                  minute = time_unit(t)[1],
                                                                                  sec = time_unit(t)[2]))
