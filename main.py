import math

OPTIONS = [
    '1. Calcular valor futuro',
    '2. Calcular interes',
    '3. Calcular número de periodos',
    '4. Calcular valor presente',
    '5. Calcular valor futuro con tasa nominal',
    '6. Convertir tasa nominal mensual a tasa efectiva anual',
    '7. salir'
]


def calculate_future_value(present_value, interest, periods):
    return present_value * (1 + (interest / 100)) ** periods


def calculate_interest(present_value, future_value, periods):
    return ((future_value / present_value)**(1 / periods)) - 1


def calculate_periods(present_value, future_value, interest):
    return math.log(future_value / present_value) / math.log(1 + (interest/100))


def calculate_present_value(future_value, interest, periods):
    return future_value / (1 + (interest/100))**periods


def calculate_effective_interest_rate(nominal_rate):
    return nominal_rate / 12


def calculate_future_value_with_nominal_rate(present_value, interest, periods):
    return present_value * (interest * periods)


def run():
    for option in OPTIONS:
        print(option + '\n')

    present_value_label = 'Ingrese el valor presente de su inversión: '
    interest_label = 'Ingrese el porcentaje de interes de su inversión: '
    periods_label = 'Ingrese el número de periodos de su inversión: '
    future_value_label = 'Ingrese el valor futuro de su inversión: '

    selected_option = str(input('Escoja la opción que desea: '))
    while selected_option != '7':
        if selected_option == '1':
            present_value = float(input(present_value_label))
            interest = float(input(interest_label))
            periods = float(input(periods_label))
            future_value = calculate_future_value(present_value, interest, periods)
            print(f'El valor futuro de su inversión es de: {future_value}')

        if selected_option == '2':
            present_value = float(input(present_value_label))
            future_value = float(input(future_value_label))
            periods = float(input(periods_label))
            interest = calculate_interest(present_value, future_value, periods)
            print(f'El interes de su inversión es de: {interest}')

        if selected_option == '3':
            present_value = float(input(present_value_label))
            interest = float(input(interest_label))
            future_value = float(input(future_value_label))
            periods = calculate_periods(present_value, future_value, interest)
            print(f'El número de periodos de su inversión es de: {periods}')

        if selected_option == '4':
            future_value = float(input(future_value_label))
            interest = float(input(interest_label))
            periods = float(input(periods_label))
            present_value = calculate_present_value(future_value, interest, periods)
            print(f'El valor presente de su inversión es de: {present_value}')

        if selected_option == '5':
            present_value = float(input(present_value_label))
            interest = float(input(interest_label))
            periods = float(input(periods_label))
            future_value = calculate_future_value_with_nominal_rate(present_value, interest, periods)
            print(f'El futuro de su inversión con interes nominal es de: {future_value}')

        if selected_option == '6':
            nominal_rate = float(input('Ingrese el porcentaje de su tasa nominal mensual: '))
            effective_interest_rate = calculate_effective_interest_rate(nominal_rate)
            print(f'El interes nominal mensual convertido a efectivo anual es del: {effective_interest_rate}%')

        selected_option = str(input('Escoja la opción que desea: '))


if __name__ == '__main__':
    print('Calculadora financiera')
    run()
