#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

var = 399
print(var)




# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

type(8.5)



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

type(var)



# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre = 'solid snake'


# 5) Crear una variable que contenga un número complejo

# In[3]:

var_n_complejo = 90 + 6j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


type(var_n_complejo)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:



# No son lo mismo, var2 (True) representa un valor booleano y var1 ('True') representa un String (cadena de carracteres)

var1 = 'True'
var2 = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:


print('var1 es de tipo ', type(var1), ' y var2 es de tipo ' , type(var2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 23 + 3.5



# 11) Realizar una operación de suma de números complejos

# In[2]:

var1 = 5j
var2 = 3j

print(var1 + var2)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

var1 = 2j
var2 = 1.34

print(var1 + var2)


# 13) Realizar una operación de multiplicación

# In[5]:

var = 5 * 5

print(var1)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

var = 2 ** 8

print(var)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:


var  = 27 / 4 
print(var)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

var = 27 // 4
print(var)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


var = 27 % 4
print(var)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

var = 6 * 4 + 3
print(var)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

var1 = 'Que'
var2 = ' Onda'

print(var1 + var2)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

var1 = '2'
var2 = 2
print(var1 == var2)


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:


var1 = '2'
var2 = 2
print(int(var1) == var2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

var = 3
var -= 1

print(var)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:





# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

var1 = 2
var2 = '2'
            #No esta permitido porque vae1 es un "Numero" y var2 es un "String"
var1 + var2

#-----------------------------------------------------------------------------

var1 + int(var2)

str(var1) + var2



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

var1 = 'Hola '

var2 = 5


print(var1 * var2)

print(var1 + 'Se repitio ' + str(var2))





# %%
