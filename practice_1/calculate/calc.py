def evaluate(a: int | float, b: int | float, op: int) -> int | float:
    """Функция калькулятор

    Args:
        a (int | float): Первый операнд с необходимым типом int или float
        b (int | float): Второй операнд с необходимым типом int или float

    Returns:
        int | float: Возвращаемый результат типа int или float
    
    Op:
    `+` - 1
    `-` - 2
    `*` - 3
    `/` - 4
    """
    match op:
        case 1: return __sum(a, b)
        case 2: return __dif(a, b)
        case 3: return __mul(a, b)
        case 4: return __div(a, b)
        case _: return "Почитате Summary"

def __sum(a: int | float, b: int | float) -> int | float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return f"{a} + {b} = {a + b}"
    return "Какое-то число или оба не являются числами"

def __dif(a: int | float, b: int | float) -> int | float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return f"{a} - {b} = {a - b}"
    return "Какое-то число или оба не являются числами"

def __mul(a: int | float, b: int | float) -> int | float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return f"{a} * {b} = {a * b}"
    return "Какое-то число или оба не являются числами"

def __div(a: int | float, b: int | float) -> int | float:
    if b == 0:
        return "На ноль делить нельзя!!!"
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return f"{a} / {b} = {a / b}"
    return "Какое-то число или оба не являются числами"