my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Petya'))
my_dict.update({'Ivan': 1985,
                'Alex': 2000})
print(my_dict)
del my_dict['Vasya']
print(my_dict)

my_set = {'Kefirr', 39, True, 39, 3.14, 39, (1,2,3)}
print(my_set)
my_set.add((12, 13, 14))
my_set.add('Anton')
my_set.discard(3.14)
print(my_set)