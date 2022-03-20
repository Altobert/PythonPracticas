
#ejercicio lista recursiva
#recibe una lista y va sumando cada uno de sus elementos de forma recursiva
#

def sumaRecursiva(list):
    if list == []:
        return 0
    print(str(list[0]))
    return list[0] + sumaRecursiva(list[1:])


listElementos =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(str(sumaRecursiva(listElementos)))

