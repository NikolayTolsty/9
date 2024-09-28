def input_list(message):
    sep_list=[',',';','/']                #Список возможных разделителей
    digits=''                             #Цифры из string
    number_list=[]                        #Сюда складываем числа из string
    sep=None                              #Разделитель, вводимый пользователем
    string=input(f'{message} через разделитель {sep_list}> ')
    for sym in string:                    #Перебираем строку
        if sym.isdigit():                               #Если попадается цифра,
            digits=digits+sym                           #добавляем её в цифры
        else:                                               #Иначе
            if sep==None:                                   #проверяем, входит ли она
                if sym in sep_list:                         #в список допустимых
                    sep=sym
                else:
                    print('Недопустимый символ')
                    break
            else:
                if sym!=sep:
                    print(f'Недопустимый символ "{sym}"')
                    break
            number_list.append(digits)                   #Добавляем число в новый список
            digits=''
    number_list.append(digits)
    return number_list