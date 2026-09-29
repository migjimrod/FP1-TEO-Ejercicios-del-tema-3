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


def estiliza_mensajes(texto:str, alterna_may_min: bool = True) -> str:
    
