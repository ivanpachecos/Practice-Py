import random

def guess_number():
    number_random = random.randint(1, 100)

    print("WELCOME TO GAME OF GUESS THE NUMBER")
    print("====================================")
    print("Insert a number of 1 to 100")

    count = 0

    while(True):

        try:
            input_number = int(input("Indrudece tu adivinanza: "))
            count += 1

            if input_number < number_random:
                print("Abajo de tu numero, Intenta de nuevo")
            elif input_number >= 101:
                print("Recuerda que juagamos de 1 a 100")
            elif input_number > number_random:
                print("Arriba de tu numero, Intenta de nuevo")
            else:
                print("FELICITACIONES, LO LOGRASTE en {} intento con el numero {} !"
                    .format(count, input_number))
                break      
        except ValueError:
            print("POR FAVOR, INGRESE VALORES NUMEROS")

guess_number()
