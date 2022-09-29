def main():
    init_value = int(input('input init number: '))
    while True:
        action = input('action: ')
        if(action == 'exit'):
            print('calculator terminated....')
            break

        operator, value = action.split()

        if operator == '+':
            init_value = init_value + int(value)
        elif operator == '-':
            init_value = init_value - int(value)
        elif operator == '*':
            init_value = init_value * int(value)
        elif operator == '/':
            init_value = int(init_value / int(value))

        print('state =>', init_value)

if __name__ == '__main__':
    main()