import re

def read(path):
    f = open('./demo.txt') # Заменить на нужное имя файла. Файл подаётся без шапки и конца.
    # Только со значениями. Пример в репозитории
    l = [line.strip() for line in f]
    array = [] # Список списков.
    # Каждый элемент array - список значений [X,Y,Z]
    for i in range(1, len(l), 4):
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', l[i])]
        s[0] = s[0]*(10**(-s[1]))
        del s[1]
        s[1] = s[1] * (10 ** s[2])
        del s[2]
        s[2] = s[2] * (10 ** s[3])
        del s[3]
        array.append(s)
    return array