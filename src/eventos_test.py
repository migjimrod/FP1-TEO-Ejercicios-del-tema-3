from eventos import es_dia_no_laborable,calcular_siguiente_valida,planificar_eventos
from datetime import date,timedelta

def es_dia_no_laborable_test():
    assert es_dia_no_laborable(date(2026,10,22))==False
    assert es_dia_no_laborable(date(2026,1,1))==True
    assert es_dia_no_laborable(date(2026,10,25))==True

def calcular_siguiente_valida_test():
    assert calcular_siguiente_valida(date(2026,10,20),3)==date(2026,10,23)
    assert calcular_siguiente_valida(date(2026,1,1),3)==date(2026,1,5)
    assert calcular_siguiente_valida(date(2026,10,25),2)==date(2026,10,27)



def planificar_eventos_test():
    assert planificar_eventos(date(2026,1,1),10,5)













#es_dia_no_laborable_test()
#calcular_siguiente_valida_test()
planificar_eventos_test()
print("Todas las pruebas pasaron correctamente.")