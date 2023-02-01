from time import time

timer = time()


def factorize(numbers: list) -> list:
    list_numbers = []
    counter = 0
    for num in numbers:
        list_numbers.append(nod(num))
        #print(list_numbers[counter])
        counter += 1
    print(f'час роботи функції: {round(time() - timer, 4)}')

    return list_numbers


def nod(num: int) -> list:
    del_n = []
    for i in range(1, num + 1):
        if num % i == 0:
            del_n.append(i)
    return del_n


if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060, 1234567, 12345678, 12345678]
    factorize(numbers)
