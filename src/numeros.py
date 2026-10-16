def invierte_numero(numero:int)->int:
    cuenta=0
    while numero>0:
        ultima_cifra = numero%10 #Extrae la ultima cifra de un numero
        cuenta = (cuenta*10)+ultima_cifra #Añade una cifra en la ultima posicion 
        numero = numero//10 #Elimina la ultima cifra de un numero
    return cuenta



def convierte_binario (n: int)-> str:
    numero_binario = "" #1/0/1/1
    conciente = (n//2) #13/2 = 6
    resto1 = str(n%2) # 1
    numero_binario += resto1
    while conciente != 0: #Conciente =6 / 3 / 1
        resto = str(conciente%2) #6%2 = 0 3%2=1 1%2= 1
        numero_binario += resto 
        conciente = conciente//2 #6/2=3 3/2= 1 1/2=0
    res =""
    for c in numero_binario: #1/0/1/1
        res = c + res #1101
    return res 
