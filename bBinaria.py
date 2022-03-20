
def busqueda_binaria(lista , elemento):
    menor=0
    mayor=len(lista)-1

    #Se tiene que mover entre los margenes
    # de mayor y menor 
    while menor <= mayor:
        #division entera
        medio = (menor+mayor)//2
        print("medio",str(medio))
        print("lista[medio]", str(lista[medio]))
        if lista[medio]< elemento:
            menor = medio+1
        elif lista[medio]> elemento:
            mayor = medio -1
        else:
            return medio
    return None
        
mi_lista = [1, 3, 5, 7, 9]

print("resultado a :",str(busqueda_binaria(mi_lista, 3)))
#print("resultado b: ",str(busqueda_binaria(mi_lista, -3)))


            
            
