# Esta función convierte a mayúsculas un mensaje y lo repite
# un número de veces introducido por el usuario

mensaje = input("Introduce un mensaje: \n")
print()
print("MENSAJE CONVERTIDO A MAYÚSCULAS!!")
while True:
    try:
        veces = int(input("Introduce un número entero:"))
        print()
        break
    except ValueError:
        print("El número debe ser entero. Por favor introduce nuevamente el mensaje y el número.")

def repetir_mensaje(mensaje, veces):
    if veces <= 0:
        print("El mensaje no se puede imprimir.")
    else:
        i = 1
        while i <= veces:
            print(f'{i}. {mensaje}.')
            i += 1

repetir_mensaje(mensaje, veces)