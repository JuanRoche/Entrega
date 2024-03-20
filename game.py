import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
failures = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

# Menu
print("Seleccione una dificultad para jugar")
option = int(input("1 Facil, 2 media, 3 dificil\n"))

letters = []
match option:
    case 1:
        for letter in secret_word:
            if(letter in ["a","e","i","o","u","á","é","í","ó","ú"]):
                letters.append(letter)
                guessed_letters.append(letter)
            else:
                letters.append("_")
    case 2:
        counter = 0
        for letter in secret_word:
            if ((counter == 0) or (counter == (len(secret_word) -1))):
                letters.append(letter)
            else:
                letters.append("_")
            counter += 1
    case 3:
        word_displayed = "_" * len(secret_word)
    case _:
        print("Numero no valido, las opciones son 1, 2 o 3.")

if(option != 3):
    word_displayed = "".join(letters)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while(failures < 3):
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas si no es caracter vacio
     if(letter != ""):
         guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta, si estoy en la opcion 2 no incluye la pirmera ni la ultima letra de la cadena
     if(option == 2):
        if letter in secret_word[1:-1]:
            # Verifica que no sea caracter vacio
            if(letter != ""):
                print("¡Bien hecho! La letra está en la palabra.")
            else: 
                print("Caracter no válido, ingrese otro:")
        else:
            failures += 1
            print(f"Lo siento, la letra no está en la palabra. Fallos: {failures}")
     else:
        if letter in secret_word:
            # Verifica que no sea caracter vacio 
            if(letter != ""):
                print("¡Bien hecho! La letra está en la palabra.")
            else: 
                print("Caracter no válido, ingrese otro:")
        else:
            failures += 1
            print(f"Lo siento, la letra no está en la palabra. Fallos: {failures}")
     # Mostrar la palabra parcialmente adivinada
    
     letters = []
     # Si estoy en ficultad media, mostrar la primera y ultima letra, ademas de las adivinadas
     if(option == 2):
        counter = 0
        for letter in secret_word:
            if ((counter == 0) or (counter == (len(secret_word) -1)) or (letter in guessed_letters)):
                letters.append(letter)
            else:
                letters.append("_")
            counter += 1
     else:  
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! alcanzaste el limite de fallos")
     print(f"La palabra secreta era: {secret_word}")    