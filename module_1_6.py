my_dict = {'Den': 1998,'Alex':1980,'Michael':2007,'Masha':1990}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Nick'))
my_dict.update({'Nick' : 1999,
                'Anna': 2009})
my_dict.pop('Nick')
print(my_dict)
my_set = {9,'bycicle', 56.98,9,'bycicle',13,'Olimpic'}
my_set.update((4,8))
my_set.discard(56.98)
print(my_set)
