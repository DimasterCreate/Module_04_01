from math import inf
def divide(first, second):
    if second == 0:
        print(inf)
    else:
        second = int(second)
        division = round((first / second), 2)
        print('Полученое частное: ', division)

