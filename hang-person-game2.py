user_chars = []
word_to_guess = "cumbias"
guess_word = ""
user_option = ""
display_word = "_  "*len(word_to_guess)
print(display_word)
hang_person = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
print(hang_person[0])
while user_option != "3":
    print("Bienvenido al ahorcadito \n")
    print("Adivina la palabra si quieres vivir!!!\n")
    print("1. Adivinar")
    print("2. Resultados")
    print("3. Salir")
    user_option = input("Indica una opción\n")

    if user_option == "1":
        exit_game = False
        while not exit_game:
            print("Intenta adivinando una letra o la palabra completa ")
            print("Escribe 'salir' para volver al menu principal")
            user_guess = input()
            guess_word =""

            #si el susuario ingreso una letra 
            if len(user_guess) == 1:
                if len(user_guess) == 1:
                #si es una letra nueva se agrega al listado de letras intentadas
                    if not user_guess in user_chars:
                        user_chars.append(user_guess)

                    if(user_guess in word_to_guess):
                        print("Adivinaste una letra")
                        for char in word_to_guess:
                            if char in user_chars: 
                                guess_word += char
                            else:
                                guess_word += "_ "
                        print(guess_word)
                    else:
                        print("Esa letra no está en la palabra")
                        print(hang_person [len(user_chars)])
                #Si el usuario intento una palabra 
            elif user_guess == "salir":
                    exit_game = True 
            else: # Si la palabra del usuario es la misma 
                if(user_guess == word_to_guess):
                    print("Ganaste") 
                else:
                    print("No No No")
                    print("Perdiste y te quemaras en infierno por los siglos de los siglos sin netflix muajajaja")
                    hang_person[-1]
                    exit()

    elif user_option == "2":
        print(f"Has intentado las siguientes letras: {user_chars}")
    elif user_option == "3":
        print("Chaitooooooo")
