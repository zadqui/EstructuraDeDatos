# Proyecto: Registro de Ventas por Departamentos

Este proyecto contiene dos programas, uno en **Python** y otro en **Java**, que permiten gestionar las ventas mensuales de tres departamentos de una tienda: **Ropa**, **Deportes** y **Juguetería**.  

La información se organiza en un **arreglo bidimensional** (matriz), donde:  
- Cada **fila** representa un mes (de Enero a Diciembre).  
- Cada **columna** representa un departamento.  

El programa implementa las siguientes funcionalidades principales:  

1. **Insertar** una venta en un mes y departamento específico.  
2. **Buscar** el valor de una venta en particular.  
3. **Eliminar** una venta (equivalente a ponerla en cero).  
4. **Mostrar** una tabla completa con los meses y los valores de cada departamento.  

---

## Análisis del problema

El uso de un arreglo bidimensional permite representar de manera clara la relación **mes vs departamento**.  
- En **Python**, se utiliza una lista de listas para simular filas y columnas.  
- En **Java**, se emplea un arreglo bidimensional (`int[][] ventas`).  

Ambos lenguajes implementan la misma lógica:  
- Inicializar una matriz con ceros.  
- Definir métodos para insertar, buscar y eliminar.  
- Mostrar los datos en formato tabular.  

---

## Código en Python

Archivo: `ventas.py`

### Explicación:
1. **Definición de datos**  
   Se crean dos listas (meses y departamentos) y se inicializa la matriz `ventas` en 12x3 con ceros.  

2. **Insertar venta**  
   Usa el índice del mes y el departamento para colocar el valor en la celda correspondiente.  

3. **Buscar venta**  
   Devuelve el valor almacenado en una celda específica.  

4. **Eliminar venta**  
   Sustituye la celda por cero.  

5. **Mostrar tabla**  
   Recorre las filas y columnas de la matriz para imprimir los datos en formato tabular.  

### Fragmento de ejemplo:
```python
insertar_venta("Enero", "Ropa", 1500)
insertar_venta("Febrero", "Deportes", 2200)

print("Buscar Febrero-Deportes:", buscar_venta("Febrero", "Deportes"))
eliminar_venta("Enero", "Ropa")
mostrar_tabla()
```

Salida esperada:
```
Mes          Ropa       Deportes   Juguetería
--------------------------------------------
Enero        0          0          0
Febrero      0          2200       0
Marzo        0          0          0
...
Diciembre    0          0          0
```

---

## Código en Java

Archivo: `VentasTabla.java`

### Explicación:
1. **Definición de datos**  
   Se crean dos arreglos para meses y departamentos, y una matriz `ventas` de 12x3 inicializada en ceros.  

2. **Insertar venta**  
   Busca el índice del mes y departamento, y asigna el valor en la celda correspondiente.  

3. **Buscar venta**  
   Devuelve el valor de una celda.  

4. **Eliminar venta**  
   Sustituye el valor de una celda por cero.  

5. **Mostrar tabla**  
   Recorre el arreglo bidimensional e imprime los valores formateados con `printf`.  

6. **Totales por departamento**  
   Recorre por columnas la matriz y acumula el total de cada departamento.  

### Fragmento de ejemplo:
```java
insertarVenta("Enero", "Ropa", 1500);
insertarVenta("Febrero", "Deportes", 2200);
System.out.println("Buscar Febrero-Deportes: " + buscarVenta("Febrero", "Deportes"));
eliminarVenta("Enero", "Ropa");
mostrarTabla();
totalPorDepartamento();
```

Salida esperada:
```
Mes          Ropa       Deportes   Juguetería
---------------------------------------------------
Enero        0          0          0
Febrero      0          2200       0
Marzo        0          0          0
...
Diciembre    0          0          0

Buscar Febrero-Deportes: 2200
Después de eliminar Enero-Ropa: 0

Totales por departamento:
Ropa: 0
Deportes: 2200
Juguetería: 0
```

---

## Conclusión

Ambos códigos resuelven el mismo problema de gestión de ventas mensuales utilizando un **arreglo bidimensional**.  
- En **Python**, se emplean listas anidadas para simular filas y columnas.  
- En **Java**, se utiliza un arreglo bidimensional que ofrece la misma funcionalidad.  

Estos programas permiten practicar la manipulación de estructuras bidimensionales, mostrando cómo insertar, buscar, eliminar y recorrer datos en dos dimensiones para organizar información de manera clara.  
