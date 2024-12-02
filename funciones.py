import time
import winsound



def transformartexto(texto):
    

    codigo_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..',

        '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', '0': '-----', ' ': ' ', '.' : '.-.-.-'
        
    }

    texto_transformado = ''.join(codigo_morse.get(letra,letra) for letra in texto)
    return texto_transformado

def mostrar_texto_morse(texto_transformado):
    print("Texto transformado: ", texto_transformado)

def sonidos_morse(texto_morse):


    sonidos_para_texto = {'.': (1000, 500), '-': (1000, 900)}

    for letra in texto_morse:
        if letra in sonidos_para_texto:
            hz, duracion = sonidos_para_texto[letra]
            winsound.Beep(hz,duracion)
        elif letra == ' ':
            time.sleep(1.5)
        else:
            continue

            


    

