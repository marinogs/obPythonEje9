# OpenBootcamp Curso Python Ejercicio 9

# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados
# alfabéticamente y separados por comas.
#
# Por otro lado, tienes que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro
# con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

def main():

    lista = ["", "", "", "", "", ""]
    i = 0
    while i < 6:
        pais = input("Introduce un pais")
        lista[i] = pais
        i += 1

    sinRepes = set(lista)
    paises = sorted(sinRepes)
    print(paises)

if __name__ == '__main__':
    main()

