fio_full = "Rusanova Svetlana Vyacheslavovna"
fio_list = fio_full.split()
fio_short = ''
for item in fio_list:
    fio_short += item[0] + '.'
print(fio_short)