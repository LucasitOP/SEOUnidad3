from helpers import *
name=   'Gafas VR'
price=450.25
avaible= True
units =20


def func1(x): 
      return x*x

num1 = int(input('Introduce valor x: '))
num2 = int(input('Introduce valor de y: '))

# Imprimir los resultados utilizando f-string
print(f"""Producto disponible: {name} 
      El precio es: {price}$ 
      Número de unidades: {units}
      El resultado de multiplicar 2*2: {func1(2)}
      La suma de {num1} y de {num2} es: {suma(num1, num2)}
      La resta de {num1} y de {num2} es: {resta(num1, num2)}
""")

 