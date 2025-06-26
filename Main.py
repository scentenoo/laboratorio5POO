from Aritmetica import Aritmetica
from Geometrica import Geometrica
from Fibonacci import Fibonacci

def main():
    print("Vamos con la progresion Aritmetica")
    incremento = int(input("Incremento: "))
    inicio = int(input("Valor inicial: "))
    print("ahora ingrese la cantidad de numeros a imprimir")
    ni= int(input("Cantidad de numeros: "))
    print("Resultado de la progresion Aritmetica")
    p1= Aritmetica(incremento, inicio)
    p1.imprimirP(ni)

    print("Vamos con la progresion Geometrica")
    base = int(input("Base: "))
    inicio = int(input("Valor inicial: "))
    print("ahora ingrese la cantidad de numeros a imprimir")
    ni= int(input("Cantidad de numeros: "))
    print("Resultado de la progresion Geometrica")
    p2= Geometrica(base, inicio)
    p2.imprimirP(ni)

    print("Vamos con la progresion Fibonacci")
    ni= int(input("Ingrese la cantidad de numeros a imprimir: "))
    p3=Fibonacci()
    p3.imprimirP(ni)
if __name__ == "__main__":
    main()