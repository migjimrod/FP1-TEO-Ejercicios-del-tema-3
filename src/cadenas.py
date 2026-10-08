def invierte_cadena(texto: str) -> str:
    '''
    Invierte el texto q recibe por parámetro

    Parámetros:
    -texto(str): El texto a invertir

    Devuelve:
    (str) El texto recibido, al revés
    '''
    res = ""
    for c in texto:
        res = c + res 
    return res  


def es_palindromo(texto: str, ignora_espacio: bool = False, ignora_mayuscula: bool = False) -> bool:
    '''Devuelve True si el texto es palindromo
    Parámetros:
    texto: el texto que queremos testear
    ignora_espacio: si es true, se ignora
    ignora_espacio: si es true, se ignora'''

    if ignora_espacio:
        texto = texto.replace(" ","")
    if ignora_mayuscula:
        texto = texto.lower()
    return texto == invierte_cadena(texto)


def estiliza_mensaje(texto:str, alterna_may_min: bool = True, sustituye_espacios: str = " ") -> str:
    txt=""
    if alterna_may_min:
        contador_letras = 0
        for c in texto:
            if c.isalpha():
                if contador_letras % 2 == 0:
                    txt += c.upper()
                else:
                    txt += c.lower()
                contador_letras += 1
            else:
                txt += c  
    else:
        txt = texto
    if sustituye_espacios:
        txt= txt.replace(" ",sustituye_espacios)
    return txt
        
