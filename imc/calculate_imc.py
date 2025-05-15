from ast import main


def calculate_imc(peso, altura):
    return peso / (altura ** 2)

if __name__ == '__main__':
    main()