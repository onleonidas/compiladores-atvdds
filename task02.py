from enum import Enum

class TokenType(Enum):
    NUM = 1
    OP = 2

class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

class Scanner:
    def __init__(self):
        self.tokens = []
        self.posicao = 0

    def scan(self, expr):
        while self.posicao < len(expr):
            if expr[self.posicao].isspace():
                self.posicao += 1
            elif expr[self.posicao].isdigit():
                start = self.posicao
                while self.posicao < len(expr) and (expr[self.posicao].isdigit() or expr[self.posicao] == "."):
                    self.posicao += 1
                self.tokens.append(Token(TokenType.NUM, expr[start:self.posicao]))
            elif expr[self.posicao] in "+-*/":
                self.tokens.append(Token(TokenType.OP, expr[self.posicao]))
                self.posicao += 1
            else:
                raise ValueError(f"Caractere inesperado: {expr[self.posicao]}")
        return self.tokens

class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def empilha(self, x):
        self.pilha.append(x)

    def desempilha(self):
        return self.pilha.pop()

    def avaliar(self, tokens):
        for token in tokens:
            if token.token_type == TokenType.OP:
                y = self.desempilha()
                x = self.desempilha()
                if token.lexeme == "+":
                    self.empilha(x + y)
                elif token.lexeme == "-":
                    self.empilha(x - y)
                elif token.lexeme == "*":
                    self.empilha(x * y)
                elif token.lexeme == "/":
                    self.empilha(x / y)
            elif token.token_type == TokenType.NUM:
                self.empilha(float(token.lexeme))
            else:
                raise ValueError(f"Token desconhecido: {token.lexeme}")
        return self.desempilha()

scanner = Scanner()
expr = "10 10 +"
tokens = scanner.scan(expr)
for token in tokens:
    print(token)
calc = CalculadoraRPN()
resultado = calc.avaliar(tokens)
print(resultado)
