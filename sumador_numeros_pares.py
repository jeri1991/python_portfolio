def sumar_pares():
    numbers = []
    suma = 0
    
    i = 1
    while i <= 100:
        numbers.append(i)
        i += 1

    for number in numbers:
        if number % 2 == 0:
            suma += number
        
    print(suma)
            
sumar_pares()