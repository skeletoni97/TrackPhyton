diskSize = 1.44 * 1024 * 1024
pages = 100
lines = 50
simbol = 25
SizeSimbol = 4

count = int(diskSize // (SizeSimbol * simbol * lines * pages))
print('Количество книг, помещающихся на дискету:', count)