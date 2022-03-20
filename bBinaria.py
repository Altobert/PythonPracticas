
def busqueda_binaria(lista , elemento):
    menor=0
    mayor=len(lista)-1

    #Se tiene que mover entre los margenes
    # de mayor y menor 
    while menor <= mayor:
        medio = (menor+mayor)//2
        if lista[medio]< elemento:
            menor = medio+1
        elif lista[medio]> elemento:
            mayor = medio -1
        else:
            return medio
    return None
        
mi_lista = [1, 3, 5, 7, 9]

print(busqueda_binaria(mi_lista, 3))
print(busqueda_binaria(mi_lista, -3))


            
            
