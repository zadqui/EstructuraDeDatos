class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return len(self.items) == 0
    def apilar(self, item):
        self.items.append(item)
    def desapilar(self):
        return self.items.pop()
    def ver_tope(self):
        return self.items[-1]

def prioridad(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

def infija_a_posfija(expresion):
    salida = []
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():  
            salida.append(token)
        elif token in "+-*/":
            while (not pila.esta_vacia() and 
                   prioridad(pila.ver_tope()) >= prioridad(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)
        elif token == "(":
            pila.apilar(token)
        elif token == ")":
            while not pila.esta_vacia() and pila.ver_tope() != "(":
                salida.append(pila.desapilar())
            pila.desapilar()
    while not pila.esta_vacia():
        salida.append(pila.desapilar())
    return " ".join(salida)


def infija_a_prefija(expresion):
    tokens = expresion.split()
    tokens = tokens[::-1]
    for i in range(len(tokens)):
        if tokens[i] == "(":
            tokens[i] = ")"
        elif tokens[i] == ")":
            tokens[i] = "("
    posfija = infija_a_posfija(" ".join(tokens))
    return " ".join(posfija.split()[::-1])

def evaluar_posfija(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            b = pila.desapilar()
            a = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
    return pila.desapilar()

def evaluar_prefija(expresion):
    pila = Pila()
    for token in expresion.split()[::-1]:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            a = pila.desapilar()
            b = pila.desapilar()
            if token == '+': pila.apilar(a + b)
            elif token == '-': pila.apilar(a - b)
            elif token == '*': pila.apilar(a * b)
            elif token == '/': pila.apilar(a / b)
    return pila.desapilar()

expresion_infija = input("Ingresa expresión infija (usa espacios, ej: ( 3 + 4 ) * 2 ): ")

posfija = infija_a_posfija(expresion_infija)
prefija = infija_a_prefija(expresion_infija)

print("Posfija:", posfija)
print("Prefija:", prefija)
print("Evaluación Posfija:", evaluar_posfija(posfija))
print("Evaluación Prefija:", evaluar_prefija(prefija))
