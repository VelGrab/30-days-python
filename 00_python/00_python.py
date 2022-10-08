import math

# Este es un comentario
# Este es un hola mundo
"""
Este es un
comentario
en varias lineas
"""
print("Hola mundo!")
print('Hola mundo!')

'''
Este tambien
es un comentario
de varias lineas
'''

# Consultar el tipo de dato

print(type("Soy un STR")) # Tipo "str"
print(type(10)) # Tipo int
print(type(1.5)) # Tipo float
print(type(1 + 3j)) # Tipo complex
print(type(True)) # Tipo bool
print(type([1, 2 , 3])) # Tipo list



p = 10
q = 8
distance = math.sqrt((p - q)**2)

print(distance)