# Задача "Распаковка позиционных параметров"

def print_params(a=1, b='строка', c=True):

    print(f'Параметры: ', a, b, c)


print_params()
print_params('проверка', False, 0.15)
print_params(c=False, b=20)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [30, True, 'Привет!']
values_dict = {'a': 'кот', 'b': 45, 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5.5, "щенок"]
print_params(*values_list_2, 42)
