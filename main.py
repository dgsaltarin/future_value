# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

OPTIONS = [
    '1. Calcular valor futuro',
    '2. Calcular número de periodos',
    '3. Calcular interes',
    '4. Calcular valor presente'
]


def calculate_future_value(present_value, interest, periods):
    return present_value * (1 + (interest/100))**periods


def calculate_interest(present_value, future_value, periods):
    return (future_value/present_value)**(1/periods) - 1


def calculate_periods(present_value, future_value, interest):
    return math.log(future_value/present_value)/math.log(1 + interest)


def calculate_present_value(future_value, interest, periods):
    return future_value/(1 + interest)**periods


def run():
    for option in OPTIONS:
        print(option + '\n')

    selected_option = str(input('Escoja la opción que desea: '))
    if selected_option == '1':
        present_value = int(input('Ingrese el valor presente de su inversión: '))
        interest = int(input('Ingrese el porcentaje de interes de su inversión: '))
        periods = int(input('Ingrese el número de periodos de su inversión: '))
        future_value = calculate_future_value(present_value, interest, periods)
        print(f'El valor futuro de su inversión es de: {future_value}')

    if selected_option == '2':
        present_value = int(input('Ingrese el valor presente de su inversión: '))
        future_value = int(input('Ingrese el valor futuro de su inversión: '))
        periods = int(input('Ingrese el número de periodos de su inversión: '))
        interest = calculate_interest(present_value, future_value, periods)
        print(f'El interes de su inversión es de: {interest}')

    if selected_option == '3':
        present_value = int(input('Ingrese el valor presente de su inversión: '))
        interest = int(input('Ingrese el porcentaje de interes de su inversión: '))
        future_value = int(input('Ingrese el valor futuro de su inversión: '))
        periods = calculate_periods(present_value, future_value, interest)
        print(f'El número de periodos de su inversión es de: {periods}')

    if selected_option == '4':
        future_value = int(input('Ingrese el valor futuro de su inversión: '))
        interest = int(input('Ingrese el porcentaje de interes de su inversión: '))
        periods = int(input('Ingrese el número de periodos de su inversión: '))
        present_value = calculate_present_value(future_value, interest, periods)
        print(f'El valor presente de su inversión es de: {present_value}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Vienvenido al calculador de valor futuro')
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
