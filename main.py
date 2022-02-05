def es_primo(num):
    contador = 0

    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False


def main():
    n = int(input('Ingresa el número a verificar: '))
    if es_primo(n):
        print('El número es primo')
    else:
        print('El número no es primo')


if __name__ == "__main__":
    main()
