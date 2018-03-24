str = "sabrrtuwacaddabra"
start = ''
temp = ''
fin = ''
for i in str:
    if i >= start:
        temp += i
        if len(fin) < len(temp):
            fin = temp
    else:
        temp = i
    start = i
print('В строке "{}" самая длинная подстрока, в которой '
      'буквы упорядочены в порядке алфавитного возрастания - "{}". '
      'Её длина {} букв.".'.format(str, fin, len(fin)))
