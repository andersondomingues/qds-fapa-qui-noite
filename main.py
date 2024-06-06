def soma(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mult(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int ) -> int:
    if(b != 0):
        return a / b
    else: 
        return None

def neg(a: int) -> int:
    if(a < 0):
        return a
    else:
        return -a