def fibonacci(n):
    secuencia = [0, 1]  # Los dos primeros números
    for i in range(2, n):
        siguiente = secuencia[i-1] + secuencia[i-2]
        secuencia.append(siguiente)
    return secuencia

# Cambia el número para decidir cuántos términos quieres
n = 10
print(f"Los primeros {n} números de Fibonacci son:")
print(fibonacci(n))
