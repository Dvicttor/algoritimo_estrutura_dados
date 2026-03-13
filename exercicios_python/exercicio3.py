a = float(input("digite primeiro lado"))
b = float(input("digite segundo lado"))
c = float(input("digite terceiro lado"))

lados = sorted ([a,b,c])

if lados[0]**2 + lados[1]**2 == lados[2]**2:
    print("o triangulo e retangulo")
    
else:
    print("o triangulo nao e retagulo")