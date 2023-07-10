def iter2(last):
    iterator = iter(last)

    try:
        while True:
            print(next(iterator))

    except StopIteration:
        print('Превышен порог итерации')


last_list = [1, 2, 3, 4, 5, 6, 7, 8]

iter2(last_list)
