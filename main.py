from funciones import *

print(" ")
print(" ")
print("-------------------------------------------------------------------------------------------------------------")
print("CODIGO MORSE")
print(" ")
print("Caracteres disponibles: ")
print("Letras 'A-Z' , la letra ñ no esta disponible en el código morse, se mostraria como texto normal sin sonido.")
print("Números '0-9' ")
print("Caracteres especiales solo '.' , el resto de caracteres se mostrarian como texto sin sonido")
print(" ")
print("-------------------------------------------------------------------------------------------------------------") 
print(" ")
print(" ")

mensaje = input("Escribe el texto a traducir: ").upper()
texto_morse = transformartexto(mensaje)

mostrar_texto_morse(texto_morse)
sonidos_morse(texto_morse)