from pprint import pprint

DICT_DICTS = {'el_1': {'el_1.1': 'val_1.1', 'el_1.2': 'val_1.2', 'el_1.3': 'val_1.3'},
              'el_2': {'el_2.1': 'val_2.1', 'el_2.2': 'val_2.2', 'el_2.3': 'val_2.3'},
              'el_3': {'el_3.1': 'val_3.1', 'el_3.2': 'val_3.2', 'el_3.3': 'val_3.3'}}

print(DICT_DICTS)
print('-' * 20)
pprint(DICT_DICTS)

STR_PP = '\n programming language Python\n type interpreted\n year 1991\n license free \n'
print(STR_PP)
pprint(STR_PP)