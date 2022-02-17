# OpenBootcamp Curso Python Ejercicio 9

# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados
# alfabéticamente y separados por comas.
#
# Por otro lado, tienes que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro
# con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

import functools

def main():

    def elementos(lista):
        impares = filter(lambda x: x % 2 != 0, lista)
        return list(impares)

    lista = []
    control = True
    while control:
        numeroIntroducido = int(input("Intruduce un numero o pon 0 para terminar:"))
        if numeroIntroducido == 0:
            control = False
        else:
            lista.append(numeroIntroducido)

    print(f'Listado de numeros introducidos: {lista}')
    impares = elementos(lista)
    print(f'Filtrado de numeros impares: {impares}')
    suma = functools.reduce(lambda a, b: a + b, impares)
    print(f'Suma de todos los numeros: {suma}')

if __name__ == '__main__':
    main()
