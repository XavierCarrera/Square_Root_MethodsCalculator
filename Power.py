def exhaustive(objective):
    answer = 0

    while answer**2 < objective:
        answer += 1

    if answer**2 == objective:
        print(f'Sqaure root of {objective} is {answer}')
    else:
        print(f'{objective} has no exact square root')
    

def aprox(objective, epsilon):
    step = epsilon**2
    answer = 0.0
    iterations = 0

    while abs(answer**2 - objective) >= epsilon and answer <= objective:
        answer += step
        iterations += 1

    if abs(answer**2 - objective) >= epsilon:
        print(f'There is no exact square root of {objective}')
    else:
        print(f'The square root of {objective} is {answer}')

def binary(objective, epsilon):
    low = 0.0
    high = max(1.0, objective)
    answer = (high + low) / 2

    while abs(answer**2 - objective) >= epsilon:
        print(f'low={low}, high={high}, answer={answer}')
        if answer**2 < objective:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2   

        print(f'The square root of {objective} is {answer}')  

option = int(input(f'Choose a square root method \n 1. Exhaustive Method \n 2. Aproximation Method \n 3. Binary Search \n'))

if option == 1:
    print("1. Exhaustive Method")
    num = int(input('Choose a numer: '))
    exhaustive(num)
elif option == 2:
    print('2. Aproximation Method')
    num = int(input('Choose a numer: '))
    parameter_epsilon = float(input('* Choose an epsilon: '))
    aprox(num,parameter_epsilon)
elif option == 3:
    print('3. Busqueda Binaria')
    num = int(input('Choose a numer: '))
    parameter_epsilon = float(input('* Choose an epsilon: '))
    binary(num,parameter_epsilon)
else:
    print('Opcion no valida')
