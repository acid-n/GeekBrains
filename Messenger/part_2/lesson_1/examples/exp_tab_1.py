from tabulate import tabulate

TUPLES_LIST = [('Python', 'interpreted', '1991'),
               ('JAVA', 'compiled', '1995'),
               ('C', 'compiled', '1972')]

print(tabulate(TUPLES_LIST))

COLUMNS = ['programming language', 'type', 'year']
print(tabulate(TUPLES_LIST, headers=COLUMNS))
print()

TUPLES_LIST = [('programming language', 'type', 'year'),
               ('Python', 'interpreted', '1991'),
               ('JAVA', 'compiled', '1995'),
               ('C', 'compiled', '1972')]

print(tabulate(TUPLES_LIST, headers='firstrow'))