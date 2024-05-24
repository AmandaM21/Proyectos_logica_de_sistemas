def menu1():
    print('1. Convertir entre Km y Millas')
    print('2. Convertir entre m3 y pie3')
    print('3. Convertir entre pies, mts y yardas')
    print('10. Salir')
    opcion=int(input('Ingrese su opción: '))
    return opcion

def conversion_Km_millas(opcion):
    if opcion == 1:
        millas = float(input("Ingresa la distancia en millas: "))
        kilometros = millas * 1.60934
        print(f"La distancia en kilómetros es: {kilometros:.2f}")
        
    elif opcion == 2:
        kilometros = float(input("Ingresa la distancia en kilómetros: "))
        millas = kilometros / 1.60934
        print(f"La distancia en millas es: {millas:.2f}")

    else:
        print("\nEl múmero de opción que elegiste no existe.")


def conversion_v_p_3(opcion):
    if opcion == 1:
        metros_cubicos = float(input("Ingresa el volumen en metros cúbicos: "))
        pies_cubicos = metros_cubicos * 35.314
        print(f"El volumen en pies cúbicos es: {pies_cubicos:.2f}")

    elif opcion == 2:
        pies_cubicos = float(input("Ingresa el volumen en pies cúbicos: "))
        metros_cubicos = pies_cubicos / 35.314
        print(f"El volumen en metros cúbicos es: {metros_cubicos:.2f}")

    else:
        print("\nEl múmero de opción que elegiste no existe.")


def conversion_p_m_y(opcion):
    if opcion == 1:
        metros = float(input("Ingresa la distancia en metros: "))
        pies = metros * 3.28084
        print(f"La distancia en pies es: {pies:.2f}")

    elif opcion == 2:
        pies = float(input("Ingresa la distancia en pies: "))
        metros = pies / 3.28084
        print(f"La distancia en metros es: {metros:.2f}")

    elif opcion == 3:
        yardas = float(input("Ingresa la distancia en yardas: "))
        metros = yardas * 0.9144
        print(f"La distancia en metros es: {metros:.2f}")

    else:
        print("\nEl múmero de opción que elegiste no existe.")


while True:
    menu1()
    opcion = int(input("\nSelecciona una opción: "))
    if opcion == 1:
        print("\n1. Millas a Kilómetros")
        print("2. Kilómetros a Millas")
        opcion = int(input("\nSelecciona una conversión: "))
        conversion_Km_millas(opcion)  

    elif opcion == 2:
        print("\n1. Metros Cúbicos a Pies Cúbicos")
        print("2. Pies Cúbicos a Metros Cúbicos")
        opcion = int(input("\nSelecciona una conversión: "))
        conversion_v_p_3(opcion)

    elif opcion == 3:
        print("\n1. Metros a Pies")
        print("2. Pies a Metros")
        print("3. Yardas a Metros")
        opcion = int(input("\nSelecciona una conversión: "))
        conversion_p_m_y(opcion)

    elif opcion == 4:
        break

    else:
        print("\nOpción inválida.")