
for numero in range (11):
    print("analizando el numero:", numero)
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzzi")
    else:
        print("sin resultado", numero)
    