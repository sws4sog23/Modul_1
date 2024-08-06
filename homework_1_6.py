my_dict = {'Den': 365, 'Serg': 132, 'Al': 697}
print(my_dict)
print(my_dict.get('Al'))
print(my_dict.get('Ann'))
my_dict.update({'Ben':333,'Jon': 444})
del_p=my_dict.pop('Den')
print(del_p)
print(my_dict)
my_set = {1,2,3,(1,4),3,2,4,5,'str'}
print(my_set)
my_set.update([99, 'new'])
my_set.discard(3)
print(my_set)
