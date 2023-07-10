'''
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл
'''

import random

VOLEWELS = 'аеиоуяюёэы'
ALFAVIT = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1) if chr(char) not in VOLEWELS])


def random_name(amount_of_names: int):
    count = 0
    all_names = []

    while count != amount_of_names:
        word_len = random.randint(4, 7)
        word = random.choices(VOLEWELS + ALFAVIT, k=word_len)
        if any(ch in VOLEWELS for ch in word):          # если есть хотя бы одна гласная в слове
            all_names.append(''.join(word).capitalize() + '\n')
            count += 1
    with open('Task_2.md', 'w', encoding='utf-8') as f:
        f.writelines(all_names)

if __name__ == '__main__':
    random_name(20)
