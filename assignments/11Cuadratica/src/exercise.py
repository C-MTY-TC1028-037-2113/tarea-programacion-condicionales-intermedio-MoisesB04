import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    if (a==0) and (b==0): # Casos en que los valores de a y b son 0, no tienen solución
        print("No tiene solucion")
    elif (a==0): # Casos en que el valor de a es 0, se muestra el valor de raiz
        raiz=-c/b
        print(raiz) 
    else: # El resto de los casos se despliega un mensaje según el valor del discriminante
        discrim=b**2-4*a*c
        if (discrim)>0:
            x1=(-b+math.sqrt(discrim))/(2*a)
            x2=(-b-math.sqrt(discrim))/(2*a)
            print(x1)
            print(x2)
        elif (discrim < 0):
            print("Raices complejas")
        else:
            x=-b/(2*a)
            print(x)

if __name__ == '__main__':
    main()
