my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6.5]
n = 0 # переменная для начала цикла по списку
while n <= len(my_list): # условие продолжение цикла while
    list_idx = n # присвоение номера индекса в списке
    if my_list[list_idx] > 0: # условие вывода на печать
        print(my_list[list_idx])
        n = list_idx + 1 # новое число переменной для выполнения следующего цикла при значении больше 0
    elif my_list[list_idx] == 0: # еше одно условие если значение равно 0
        n = list_idx + 1 # новое число переменной для выполнения следующего цикла при значении равным 0
        continue # продолжение цикла при значении равным нулю без печати
    else: # условие если значение меньше нуля
        break # прерывание цикла при значении меньше нуля



