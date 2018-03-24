# ----1----------------------------------
str = 'ambulance'
str = input('')
print(str[::-1])

# ----2----------------------------------
str_reverse = ''
for i in str[::-1]:
    str_reverse += i
print(str_reverse)

# ----3----------------------------------
str_list = list(str)
str_list.reverse()
str_reverse = ''.join(str_list)
print(str_reverse)
