from datetime import datetime, timedelta

entrada = input().split()
c, g = list(map(int, entrada)) 

def fechamento (c: int, g: int):
    dia_inicial = datetime.strptime("20/09/2019",'%d/%m/%Y').date()
    dia_máximo = datetime.strptime("31/10/2019",'%d/%m/%Y').date()
    dia = dia_inicial
    while dia <= dia_máximo:
        
        dia = dia + timedelta(1)
        if c < 1 or c < g :
            break
        else:
            c = c - g
    
    return dia

def formated(month: str):
    month_name = {
        '1': 'janeiro',
        '2': 'fevereiro',
        '3': 'março',
        '4': 'abril',
        '5': 'maio',
        '6': 'junho',
        '7': 'julho',
        '8': 'agosto',
        '9': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'        
    }
    mon_for = month_name[month]

    return mon_for

print("A UFSC fecha dia "+str(fechamento(c, g).day)+" de "+formated(str(fechamento(c, g).month))+".")


       
