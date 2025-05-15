from ast import main


def classify_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obesidade grau I'
    elif imc < 40:
        return 'Obesidade grau II'
    else:
        return 'Obesidade grau III (mórbida)'
    
if __name__ == 'main':
    main()