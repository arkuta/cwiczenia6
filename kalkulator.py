def suma(x,y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie mozna dzielic przez zero"

x=3
y=4
print (dzielenie(x,y))
