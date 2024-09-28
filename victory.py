import random

def convert_date(ddmmyyyy):
    day=days[ddmmyyyy[:2]]
    month=months[ddmmyyyy[3:5]]
    year=ddmmyyyy[6:]
    return(day+' '+month+' '+year+' года')

months={'01':'января','02':'февраля','03':'марта','04':'апреля','05':'мая','06':'июня','07':'июля',
        '08':'августа','09':'сентября','10':'октября','11':'ноября','12':'декабря'}
days={'01':'первое','02':'второе','03':'третье','04':'четвертое','05':'пятое','06':'шестое','07':'седьмое',
      '08':'восьмое','09':'девятое','10':'десятое','11':'одиннадцатое','12':'двенадцатое','13':'тринадцатое',
      '14':'четырнадцатое','15':'пятнадцатое','16':'шестнадцатое','17':'семнадцатое','18':'восемнадцатое',
      '19':'девятнадцатое','20':'двадцатое','21':'двадцать первое','22':'двадцать второе','23':'двадцать третье',
      '24':'двадцать четвертое','25':'двадцать пятое','26':'двадцать шестое','27':'двадцать седьмое',
      '28':'двадцать восьмое','29':'двадцать девятое','30':'тридцатое','31':'тридцать первое'}
persons=['В.И.Ленин','Том Круз','Петр I','Жак-Ив Кусто','И.А.Бунин','Холли Берри',
         'Пирс Броснан','Д.И.Менделеев','В.С.Высоцкий','Ф.Нансен']
borndate=['22.04.1870','03.07.1962','09.06.1672','11.06.1910','22.10.1870','14.08.1966','16.05.1953',
          '08.02.1834','25.01.1938','10.10.1861']
numbers=list(range(len(persons)))
total_quests=5
while True:
    samples=random.sample(numbers,total_quests)
    corrects=0
    incorrects=0
    for sample in samples:
        answer=input(f'Когда родился(лась) {persons[sample]} (dd.mm.yyyy)?> ')
        if answer==borndate[sample]:
            print('Верно!')
            corrects+=1
        else:
            print(f'Правильный ответ - {convert_date(borndate[sample])}')
            incorrects+=1
    print(f'Вы дали {corrects} ({round(corrects/total_quests*100)}%) правильных ответов \
и {incorrects} ({round(incorrects/total_quests*100)}%) неправильных')
    while True:
        repeat=input('Хотите повторить игру с начала (да/нет)?> ')
        if repeat=='да' or repeat=='нет':
            break
        else: print('Ведите "да" или "нет"')
    if repeat=='нет': break