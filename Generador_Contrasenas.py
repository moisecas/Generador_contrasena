import random

def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres= MAYUS+MINUS+NUMS+CHARS

    contrasena = []

    for i in range(15):
        
        caracter_random=random.choice(caracteres) #choice, esta dentro de random, se usa para escoger de la lista y que guarde en la variable contrasena
        contrasena.append(caracter_random) 

    contrasena="".join(contrasena) 
    return contrasena  



def tayson():
    contrasena=generar_contrasena()
    print("tu nueva contrasena es: " + contrasena) 

if __name__=="__main__":
    tayson() 