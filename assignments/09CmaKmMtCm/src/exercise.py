def main():
    # Escribe tu código abajo de esta línea
    c = int(input("Introduce los cm: "))
    if c<100: # Caso en que los cm son menores a 100, solamente usar cm
        print(c,"cm")
    elif c<1000: # Caso en que los cm son menores a 1000, solamente usar m y cm
        x=c//100 # Cálculo de cm en m mediante división entera (piso)
        y=c-(x*100) # Cálculo de cm a considerar 
        print(x,"m")
        if y!=0: # Considerar los cm si el valor de y es diferente a 0
            print(y,"cm")
    else: # Caso en que los cm son mayores a 1000, usar km, m y cm
        x=c//100000 # Cálculo de cm en km mediante división entera
        y=(c-(x*100000))//100 # Cálculo de m mediante división entera
        z=(c-(x*100000)-(y*100)) # Cálculo de cm restantes
        if x!=0:
            print(x,"km")
        if y!=0:
            print(y,"m")
        if z!=0:
            print(z,"cm")

if __name__ == '__main__':
    main()
