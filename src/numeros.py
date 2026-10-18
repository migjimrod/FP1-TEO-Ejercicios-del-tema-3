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


def sumar_divisores_propios (n:int)->int:
    resultado = 0
    for c in range(1,n):
        resto = n%c
        if resto == 0:
            resultado = c + resultado
    return resultado  

def clasifica_numero(n:int)->str:
    if sumar_divisores_propios(n) == n:
        return "Perfecto" 
    elif sumar_divisores_propios(n) > n:
        return "Abundante"
    else: 
        return "Deficiente"

def clasifica_rango(n:int)->int:
    for c in range(1,n+1):
        print(f"{c}: {clasifica_numero(c)}")

def busca_perfecto(n:int)->int:
    busqueda_de_perfectos = n
    c = 1
    while busqueda_de_perfectos > 0:
        if clasifica_numero(c) == "Perfecto":
            resultado = c 
            busqueda_de_perfectos -= 1
        c+=1
    return resultado

#Ejercicio 9
             




