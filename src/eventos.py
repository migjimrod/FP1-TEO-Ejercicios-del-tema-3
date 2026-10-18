from datetime import date, timedelta 

def es_dia_festivo(fecha: date) -> bool:
    """
    Verifica si una fecha corresponde a un día festivo recurrente (ignora el año).
    
    Parámetros:
        fecha (date): La fecha a verificar.
        
    Devuelve:
        bool: True si el mes y día coinciden con un festivo, False en caso contrario.
    """    
    dias_festivos = {
        (1, 1),    # Año Nuevo
        (1, 6),    # Día de Reyes
        (3, 19),   # San José
        (5, 1),    # Día del Trabajo
        (8, 15),   # Asunción de la Virgen
        (10, 12),  # Fiesta Nacional de España
        (11, 1),   # Todos los Santos
        (12, 6),   # Día de la Constitución
        (12, 8),   # Inmaculada Concepción
        (12, 25)   # Navidad
    }
    
    return (fecha.month, fecha.day) in dias_festivos

def es_dia_no_laborable (fecha: date)->bool:
    if fecha.weekday() == 5:
        return True
    elif fecha.weekday() == 6:
        return True
    elif es_dia_festivo(fecha) == True:
        return True
    else:
        return False


def calcular_siguiente_valida(fecha_anterior: date, intervalo_dias: int)->date:
    proxima_fecha = fecha_anterior + timedelta(days = intervalo_dias)
    while es_dia_no_laborable(proxima_fecha) == True:
        proxima_fecha += timedelta(days=1)
    return proxima_fecha


def planificar_eventos(fecha_inicio: date, intervalo_dias: int, num_eventos: int)-> date:
    actual = fecha_inicio
    if es_dia_no_laborable(fecha_inicio) == True:
        actual = calcular_siguiente_valida(fecha_inicio,0)
    print(f"Evento 1: {actual}")
    for c in range(2,num_eventos +1):
        nueva_fecha = calcular_siguiente_valida(actual,intervalo_dias)
        actual= nueva_fecha
        print(f"Evento {c}: {nueva_fecha}")

