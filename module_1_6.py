my_dict = {'Alice': 1999, 'Max': 2001, 'Anastasija': 1989}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alice'])
print('Not existing value:', my_dict.get ('Natasha'))
my_dict.update({'Natasha': 2014, 'Grigorij': 2009})
print('Deleted value:', my_dict.pop('Max'))
print('Modified dictionary:', my_dict)

my_set = {'North', 'South', 'West', 'East', 'West', 'North', 'East'}
print('Set:', my_set)
my_set.add('World')
my_set.add('Earth')
my_set.remove('East')
print('Modified set:', my_set)