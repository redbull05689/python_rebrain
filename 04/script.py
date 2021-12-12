import math

dicts = [
    {'total': 999641890816, 'used': 228013805568}, 
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

num_volume = input('Введите номер накопителя: ')
if not num_volume.isdigit():
    print('Введена некорректная строка!')
elif num_volume.isdigit() in range(len(dicts)):
    free_persent = ((dicts[int(num_volume)]['total'] -dicts[int(num_volume)]['used'])/(dicts[int(num_volume)]['total']/100) )

print('Free disk space = ', round(free_persent,2) , '% ')
# else:
#     print('За приделами массива')

