from tabulate import tabulate

DICT_LIST = [{'programming language': 'Python', 'type': 'interpreted', 'year': '1991'},
             {'programming language': 'JAVA', 'type': 'compiled', 'year': '1995'},
             {'programming language': 'C', 'type': 'compiled', 'year': '1972'}]

# print(tabulate(DICT_LIST, headers='keys', tablefmt='grid'))

# print(tabulate(DICT_LIST, headers='keys', tablefmt='pipe'))

# print(tabulate(DICT_LIST, headers='keys', tablefmt='html'))

print(tabulate(DICT_LIST, headers='keys', tablefmt='pipe', stralign='center'))