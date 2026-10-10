def letra_a_posicion (letra):
    ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    if letra in ALFABETO:
        letra = ALFABETO.find(letra)
        return letra
    else:
        return None

def posicion_a_letra(posicion):
    ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    if 0 <= posicion < len(ALFABETO):
        return ALFABETO[posicion]
    return None


def cifra_cesar(texto_a_codificar:str,clave:int)->str:
    ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    texto_codificado= ""
    for c in texto_a_codificar:
        posi = letra_a_posicion(c)
        if posi is None:
            texto_codificado += c
        else:
            nueva_posicion = (posi + clave) % len(ALFABETO)
            nueva_letra = posicion_a_letra(nueva_posicion)
            texto_codificado += nueva_letra
    return texto_codificado

def rompe_cesar(mensaje_cifrado:str):
    ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    for c in range(1,len(ALFABETO)):
        mensaje_descifrado = cifra_cesar(mensaje_cifrado,-c)
        print(mensaje_descifrado)  

rompe_cesar("j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!")