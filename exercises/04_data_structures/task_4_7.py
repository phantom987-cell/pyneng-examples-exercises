# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"
##mac_sp = mac.split(':')
    #print(mac_sp)
##mac1, mac2, mac3 = (int((mac_sp[0]), 16)),(int((mac_sp[1]), 16)), (int((mac_sp[2]), 16))
    #mac2 = int((mac_sp[1]), 16)
    #mac3 = int((mac_sp[2]), 16)
    #print(mac1, mac2, mac3)
    #print('{:b} {:b} {:b}'.format(mac_sp[0], mac_sp[1], mac_sp[2]))
    #print('{:b} {:b} {:b}'.format(mac1, mac2, mac3))
##result = ('{:b} {:b} {:b}'.format(mac1, mac2, mac3))
##result1 = result.replace(' ', '')
##print(result1)
    #result1 = result.split()

result = '{:b}'.format(int(mac.replace(':',''), 16))
print(result)
#mac1 = mac_sp[0]
#mac2 = mac_sp[1]
#mac3 = mac_sp[2]

#mac1_bin = '{:b}'.format(int(mac1,16))
#mac2_bin = '{:b}'.format(int(mac2,16))
#mac3_bin = '{:b}'.format(int(mac3,16))

#result = mac1_bin + mac2_bin + mac3_bin
#print(result)