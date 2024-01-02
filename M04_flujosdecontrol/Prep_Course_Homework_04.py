#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

var = 23

if(var > 0 ):
    print(var, ' Es mayor a 0')
elif (var < 0 ):
    print(var, ' Es menor a 0')
else:
   print(var, ' Es igual a 0')



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

var1 = 5
var2 = False

if(type(var1) == type(var2)):
    print('Ambos valores son', type(var1))
else:
    print('Los valores son de diferente Tipo')


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1, 21):
    if(i % 2 == 0):
        print(i ,'es par')
    else:
        print(i,'es impar')




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
    print(i, 'Elevado a potecia de 3 es igual a ', i**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

var = 5

for i in range(0, var):
    print(i)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

var = 3

if (type(var) == int):
    if (var > 0):
        factorial = var
        while (var > 2):
            var = var - 1
            factorial = factorial * var
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')






# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

var =  3

while(var < 5):
    var += 1
    for i in range(0,var):
        print('while', var)
        print('for', var)



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

var = 5

for i in range(0, var):
    while(var < 5):
        var -= 1
        print('for', var)
        print('while', var)




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for i in range(1,31):
    if( i % i == 0):
        print(str(i))




# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:





# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:



