from my_module import input_list
list1=input_list('Введите первый список')
list2=input_list('Введите второй список')
for number in list2:
    while number in list1:                      #удалить все вхождения
    #if number in list1:                        #или удалить первое вхождение
        list1.remove(number)
print(list1)