def contar_nombres(mi_lista_nombres):
    nombre_a_buscar=input("Ingresa un nombre a buscar: ")
    frecuencia=mi_lista_nombres.count(nombre_a_buscar)

    print("El nombre", nombre_a_buscar, "se repite", frecuencia, "veces.")

mi_lista_nombres=["Jose", "Carlos", "Amanda", "Liliana", "Susana", "Jose", "Brandon"]
contar_nombres(mi_lista_nombres)



