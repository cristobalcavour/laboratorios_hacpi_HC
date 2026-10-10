def calcular_potencia(v,r):
    if r<=0:
        print("no existe resistencia <0" )
        return 0
    potencia = (v**2)/r
    return potencia

voltaje=float(input("ingrese voltaje: "))
resistencia=float(input("ingrese resistencia: "))



resultado=calcular_potencia(voltaje,resistencia)
print(f'el resultado es: {resultado:.2f}watss')
print(f'el valor redondeado es: {round(resultado)} watts')

      




