import math
def calculate():
    operation = input('''
Wpisz co chcesz zrobic:
+ jesli chcesz dodac
- jesli chcesz odjac
* jesli chcesz pomnozyc
/ jesli chcesz podzielic
** jesli chcesz spotegowac
// jesli chcesz spierwiastkowac
''')

    if operation == '//':
        number_1 = int(input('Wpisz liczbe ktore chcesz spierwiastkowac: '))
    else:    
        number_1 = int(input('Wpisz pierwsza liczbe: '))
        number_2 = int(input('Wpisz druga liczbe: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '**':
        print('{}**{} = '.format(number_1,number_2))
        print(number_1**number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        try:
            print(number_1 / number_2)
            raise ValueError("") 
        except ZeroDivisionError:
            print('podzieliles przez zero')

    elif operation == '//':
            print(math.sqrt(number_1))

    else:
        print('nieprawidlowe uruchom ponownie program')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
    chcesz jeszcze raz obliczyc? T/N
''')

    if calc_again.upper() == 'T':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()