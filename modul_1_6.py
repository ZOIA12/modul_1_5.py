my_dict={'Alena': 2017, 'Varia': 2015, 'Sascha': 2009}
print(my_dict)
print(my_dict['Varia'])
my_dict['Dima'] = 1973
print(my_dict['Dima'])
my_dict['Zoia'] = 1985
my_dict['Petia'] = 1980
print(my_dict)
del my_dict['Petia']
print(my_dict.get('Petia'))
print(my_dict)


set_={3,5,4,6,7,6,8,5,6, 'name Zoia', True, (6,4,5)}
print(set_)
# В ВИДЕОУРОКЕ И ЛЕКЦИИ НЕ БЫЛО НАПИСАНО И СКАЗАНО КАК ДОБАВИТЬ ЭЛЕМЕНТЫ В МНОЖЕСТВО
# ЕСТЬ ИНФОРМАЦИЯ КАК ПЕРЕВЕСТИ ЧТО-ТО ВО МНОЖЕСТВО ИЛИ СОЗДАТЬ МНОЖЕСТВО
# list_=[10,12,26,13,10,10, 'name Sascha']
# list_=(set_(list_))
# print(list_)
# ЗАДАНИЕ:- Добавьте 2 произвольных элемента во множество my_set, которых ещё нет.
# ПОЭТОМУ ПОЛЬЗУЮСЬ ДОПОЛНИТЕЛЬНЫМИ ИСТОЧНИКАМИ ИНФОРМАЦИИ В ИНТЕРНЕТЕ
list_ = [10,12,26,13,10,10, 'name Sascha']
set_.update(list_)
print('Modified Set: ')
print(set_)
# Источник: https://python-lab.ru/kak-dobavit-spisok-vo-mnozhestvo-v-python
# http://www.sql-tutorial.ru/ru/book_xml_data_type_methods/page5.html?ysclid=m0xiha6m3t263819039
print(set_.remove(5))
print(set_)
print(set_.remove(6))
print(set_)
