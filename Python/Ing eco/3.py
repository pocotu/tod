'''
crear una funcion que valide la fecha dia/mes/año
Sin usar librerias
'''
# Lista con meses, dias y años bisiestos
def validar_fecha(dia, mes, año):
    A_N = [31,28,31,30,31,30,31,31,30,31,30,31]
    A_B = [31,29,31,30,31,30,31,31,30,31,30,31]
    Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        if mes > 0 and mes <= 12:
            if dia > 0 and dia <= A_B[mes - 1]:
                return "La fecha es valida"
            else:
                return "El dia no es valido"
        else:
            return "El mes no es valido"
    

def main():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    print(validar_fecha(dia, mes, anio))

main()