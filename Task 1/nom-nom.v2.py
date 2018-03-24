str = 'om-nom-nomk-nomnom-nyam-nnoom-nyam-nyam-khenom-nyam'
str_nom = 'nom'
count_GL = 0
for i in range(len(str)):
    if str[i:i + 3] == str_nom:
        count_GL += 1
print('В строке "{}" найдено {} вхождений подстрок "{}".'.format(str, count_GL, str_nom))