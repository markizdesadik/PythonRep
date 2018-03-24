str = 'ambulance'
str = input('')
spisok_glasnux = 'aAeEyYuUiIoO'
count_GL = 0
for i in str:
    for j in spisok_glasnux:
        if j == i:
            count_GL += 1
print('В строке "{}" найдено {} гласных букв.'.format(str, count_GL))
