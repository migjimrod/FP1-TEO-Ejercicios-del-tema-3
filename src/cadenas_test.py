from cadenas import *

def test_invierte_cadena():
    print("Probando invierte_cadena...")
    assert invierte_cadena("") == ""
    assert invierte_cadena("Texto de prueba") == "abeurp ed otxeT"
    assert invierte_cadena("seres") == "seres"

def test_es_palindromo():
    print("Probando es_palindromo")
    assert es_palindromo("reconocer") == True
    assert es_palindromo("rotor") == True
    assert es_palindromo("radar") == True
    assert es_palindromo("Amor a Roma") == False
    assert es_palindromo("Luz azul")  == False

def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1") == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    assert estiliza_mensaje("Murciélago", usa_dieresis=True) == "MüRcÏéLäGö"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=False, usa_dieresis=True, sustituye_espacios="-") == "Hölä-Mündö"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, usa_dieresis=False, sustituye_espacios="_") == "HoLa_MuNdO"

#test_invierte_cadena() 
#test_estiliza_mensaje()
#test_es_palindromo()
print("Todas las pruebas pasaron correctamente.")