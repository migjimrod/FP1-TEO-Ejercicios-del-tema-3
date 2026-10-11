def invierte_numero(numero:int)->int:
    cuenta=0
    while numero>0:
        ultima_cifra = numero%10 #Extrae la ultima cifra de un numero
        cuenta = (cuenta*10)+ultima_cifra #Añade una cifra en la ultima posicion 
        numero = numero//10 #Elimina la ultima cifra de un numero
    return cuenta
