from imc.calculate_imc import calculate_imc
from imc.classify_imc import classify_imc

def main():
    print('==== Calculadora de IMC ====')
    try:
        peso = float(input('Digite seu peso (Kg): '))
        altura = float(input('Digite sua altura (m): '))
        
        imc = calculate_imc(peso, altura)
        classification = classify_imc(imc)
        
        print(f'\nSeu IMC é: {imc: .2f}')
        print(f'Classificação: {classification}')
    except ValueError:
        print('ERRO: Insira valores númericos válidos.')

if __name__ == 'main':
    main()