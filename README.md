# Librerias Matrices Numeros Complejos

Librerias para operar matrices de numeros complejos

## Adición de vectores complejos.

* En esta libreria se requieren dos vectores uan hacer su respectiva suma
los vectores son de la forma A = [(a, b), (a1, b1) ...] donde a es la parte real del numero complejo 
y b es la parte imaginara. para poder sumar los vectores deben ser de longitud n

## Inverso (aditivo) de un vector complejo.

* En esta libreria se retorna el inverso adictivo de un vector de la forma A = [(a, b)] donde
a es la parte real del numero complejo y b es la parte imaginaria.

## Multiplicación de un escalar por un vector complejo.

* En esta libreria se retorna la multiplicacion de un escalar por un vector. Esta libreria recibe
un numero escarlar es de la forma (a, b) donde a es la parte real y b es la parte imaginaria del numero y
un vector de la forma A = [(a, b), (a1, b1) ...] donde se retorna un vector.

## Adición de matrices complejas.

* Esta libreria retorna la suma de dos matrices, de la forma A =  [[(a, b), (a1, b1)] [...]] donde a es la parte real
del numero y b la parte imaginaria. Para sumar las dos matrices deben ser n x n

## Inversa (aditiva) de una matriz compleja.

* Esta libreria retorna el inverso aditivo de uan matriz de la forma A = [[(a, b)],[....]] donde a es la parte real y b
la parte imaginaria del numero complejo.

## Multiplicación de un escalar por una matriz compleja.

* Esta libreria retorna la multiplicacion de un escalar por una matriz, donde el escalar es de la forma
(a, b) y la matriz es de la forma A = [[a, b],[...]] donde a es la parte real y b es la parte imaginaria del
numero complejo.

## Transpuesta de una matriz/vector

* Esta libreria retorna la transpuesta de una matriz y un vector es decir A[j][k] = A[k][j] donde la matriz 
es de la forma  A = [[a, b],[...]] y el vector es de la forma  A = [(a, b), (a1, b1) ...] donde a es la parte real 
y b es la pate imaginaria.

## Conjugada de una matriz/vector

* Esta libreria retorna la conjugada de una matriz y un vector conjugada(A[j][k]). la libreria
recibe un solo parametro un vector o una matriz de la forma A = [(a, b), (a1, b1) ...]  y A = [[a, b],[...]] donde
a es la parte real y b es la parte imaginaria.

## Adjunta (daga) de una matriz/vector

* Esta libreria retorna la adjuta de un vector y una matriz es decir A[j][k] (daga). la libreria 
recibe un solo parametro un vector o una matriz de la forma A = [(a, b), (a1, b1) ...] y A = [[a, b],[...]] dode
a es la parte real y b es la parte imaginaria.

## Producto de dos matrices (de tamaños compatibles)

* Esta libreria retorna el producto de dos matrices donde resive dos parametros la
matriz1 y la matriz2 donde la matriz2 debe tener la mima cantidad de filas de columnas de la matriz 1
para podeer realizar el producto. las matrices son de la forma  A = [[a, b],[...]] donde a es la parte
real y b es la parte imagiaria.

## Producto interno de dos vectores

* Esta libreria retorna el producto interno de dos vectores. Esta libreria recibe dos parametros **2 vectores**
de la forma A = [(a, b), (a1, b1) ...] donde a es la parte real y b la parte imaginaria del numero complejo.

## Norma de un vector

* Esta libreria retorna la norma de un vector. Esta libreria recibe un parmetro **1 vector** de la forma
A = [(a, b), (a1, b1) ...] donde a es la parte real y b es la parte imaginaria del numero.

## Distancia entre dos vectores

* Esta libreria retorna la distancia que hay entre dos vectores. Esta libreria recibe **2 parametros** de la forma
A = [(a, b), (a1, b1) ...] donde a es la parte real y b la parte imaginaria del numero complejo.

## Revisar si una matriz es unitaria

* Esta libreria retorna False o True si la matriz es **Unitaria** o no. Esta libreria recibe **1 parametro** de la forma
 A = [[a, b],[...]] donde a es la parte real y b la parte imaginaria del numero complejo.
 
 ## Revisar si una matriz es Hermitiana
 
* Esta libreria retorna False o True si la matriz es **Hermitania** o no. Esta libreria recibe **1 parametro** de la forma
A = [[a, b],[...]] donde a es la parte real y b la parte imaginaria del numero complejo.

## Producto tensor de dos matrices/vectores

* Esta libreria retorna el troducto tensor de una matriz o un vector de la forma  A = [[a, b],[...]] y A = [(a,b), ....] donde
a es la parte real y b la parte imaginaria. retorna una matriz de tamaño C**n O C**m = C**n+m.


