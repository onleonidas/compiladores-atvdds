class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def empilha(self, x):
        self.pilha.append(x)

    def desempilha(self):
        return self.pilha.pop()

    def avaliar(self, expr):
        tokens = expr.split()
        for token in tokens:
            if token == "+":
                self.empilha(self.desempilha() + self.desempilha())
            elif token == "-":
                y = self.desempilha()
                x = self.desempilha()
                self.empilha(x - y)
            elif token == "*":
                self.empilha(self.desempilha() * self.desempilha())
            elif token == "/":
                y = self.desempilha()
                x = self.desempilha()
                self.empilha(x / y)
            else:
                self.empilha(float(token))
        return self.desempilha()

calc = CalculadoraRPN()
with open("Calc1.txt") as arquivo:
    expr = arquivo.read().strip()
resultado = calc.avaliar(expr)
print(resultado)
