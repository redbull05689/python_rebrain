str_1 = "'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'"

print('----task 1.1-----')
print(str_1[1:16:1])

# or

array = str_1.split(' ')
output_string = " ".join(array[:3])
print(output_string.replace("'",""))


print('----task 1.2-----')
array = str_1.split(' ')
print(array[4])

# or

array = str_1.split(' ')
print(array[4].replace(":",""))

print('----task 1.3-----')
array = str_1.split(' ')
array[3] = "PC-12092"
print(array)

# or

str_1 = str_1.replace('ideapad',"PC-12092")
print(str_1)

print('----task 1.4-----')
result = 'failed'
if result in str_1:
    print(str_1.find(result))
else:
    print('-1')

# or

print(str_1.find('failed'))


print('----task 1.5-----')
litle_s = (len(str_1.split('s'))) -1
capital_s = (len(str_1.split('S'))) -1
print(litle_s + capital_s)

# or

print(int(str_1.count('S')) + int(str_1.count('s')))

print('----task 1.6-----')
array = str_1.split(' ')
array2 = array[2].split(':')
print(int(array2[0]) + int(array2[1]) + int(array2[2]))

print('----task 2-----')
str_2 = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
array = str_2.split(' ')
# print(str(array[10:12:1]))
print('The PC "' + array[3] + '" receive message from service "' + array[4] + '" what says "' + array[5] + '" because ' + str(" ".join(array[11:14])) + ' at ' + str(" ".join(array[0:3])) )