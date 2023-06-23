# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

text = 'В южной части России расположилась столица Кубани - город Краснодар.\
 Это небольшой город с численностью населения чуть больше 800 тысяч человек. \
 В 1920 году город получил своё официальное название. Изначально представляя \
 собой небольшое военное поселение. Краснодар это красивый город.\
Под великим руководством Екатерины II казаки завоевали территорию между рекой \
Кубань и Азовским морем. И наименовали - Екатеринодарм, который 1860 году стал \
административным центром. Екатерина Великая в свою очередь решила отблагодарить \
казаков выделив им данную территорию, которая позднее и получила название - Краснодар.'

dict_counts = {}
SHOW_LIMIT = 10
new_sorted_dictionary = {}
new_text = text.replace(',', ''). \
    replace('.', ''). \
    replace('!', ''). \
    replace('?', ''). \
    replace('"', ''). \
    replace('-', ''). \
    lower(). \
    strip()
words_list = new_text.split()
for word in words_list:
    counter = words_list.count(word)
    dict_counts[word] = counter
sorted_values = sorted(dict_counts.values())[::-1]

for i in sorted_values:
    for k in dict_counts.keys():
        if dict_counts[k] == i:
            new_sorted_dictionary[k] = dict_counts[k]

print(list(new_sorted_dictionary.items())[0: SHOW_LIMIT])
