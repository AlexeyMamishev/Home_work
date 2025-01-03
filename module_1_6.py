my_dict = {'вперед': 8, 'назад': 2, 'влево': 4, 'вправо': 6}
print(my_dict)
print(my_dict['назад'])
print(my_dict.get('центр'))
my_dict.update({'вверх': 9,
                'вниз': 3})
a = my_dict.pop('назад')
print(a)
print(my_dict)
my_set = {1, 'кровать', 2.125, 'кровать', 2.125, 1}
print(my_set)
my_set.update({305, 'диван'})
my_set.remove(2.125)
print(my_set)