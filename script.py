__author__ = 'Cátedra de AED'


def cargar():
    global a, b
    a = int(input('A: '))
    b = int(input('B: '))


def calcular():
    c = a * b
    d = a / b

# script principal...
cargar()
calcular()

print('Producto:', c)
print('Cociente:', d)