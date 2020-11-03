z = 1


def definir():
    global x1
    global x2
    x1 = int(input("Ingresa el primer numero: "))
    x2 = int(input("Ingresa el segundo numero: "))


def calcular():
    i = 1
    while i <= x1 and i <= x2:
        if x1 % i == 0 and x2 % i == 0:
            gcd = i
        i = i + 1

        xgcd1 = x1/gcd
        xgcd2 = x2/gcd

    print("El maximo comun divisor es:", gcd)
    print(xgcd1, xgcd2)




def continuar():
    global y
    y = input("1 para escoger otro numero, 0 para terminar la ejecucion: ")


while z == 1:
    definir()
    calcular()
    continuar()
    z = y
