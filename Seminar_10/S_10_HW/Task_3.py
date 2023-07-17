from random import randint, uniform

UPPER_LIMIT = 1000
LOVER_LIMIT = -1000


class File:
    def __int__(self, count):
        self.count = count

    def file(filename, count):
        with open('Task_1.md', 'w', encoding='utf-8') as Task_1:
            for i in range(count):
                int_num = randint(LOVER_LIMIT, UPPER_LIMIT)
                float_num = uniform(LOVER_LIMIT, UPPER_LIMIT)
                Task_1.write(f'{int_num:>5} | {float_num:.3f}\n')


f = File.file('Task_1.md', 5)
