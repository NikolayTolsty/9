list1=[]
n=int(input('Введите количество элементов списка> '))
for i in range(n):
    list1.append(int(input(f'Введите элемент {i} из {n}> ')))
print(sorted(list1))