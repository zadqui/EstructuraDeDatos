def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Generar la secuencia
n = 10
secuencia = [fibonacci_recursivo(i) for i in range(n)]

print(f"Los primeros {n} números de Fibonacci son:")
print(secuencia)
