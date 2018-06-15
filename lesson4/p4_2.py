for j in 'hello world':
    if j == 'w':
        continue
    print(j * 3, end = '')
    
for j in 'hello world':
    if j == 'а':
        break
else:
    print("Буквы а нету в слове")