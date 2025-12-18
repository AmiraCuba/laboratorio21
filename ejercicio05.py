operacionStr = input("Ingresa la operación a realizar: ")
operacion = operacionStr.split()
numero1 = operacion[0]
operador = operacion[1]
numero2 = operacion[2]
class OperadorInvalidoError(Exception):
    "Ingresé un operador válido (+, -, *, /)"
    pass
operaciones = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
}
try:
    if len(operacion) != 3:
        raise ValueError
    numero1 = float(operacion[0])
    operador = operacion[1]
    numero2 = float(operacion[2])
    if operador not in operaciones:
        raise OperadorInvalidoError(f"El operador '{operador}' no existe.")
    resultado = operaciones[operador](numero1, numero2)
    print(f"Resultado final: {resultado}")
except ValueError:
    print("Asegúrate de ingresar números válidos y usar espacios")
except OperadorInvalidoError as error:
    print(error)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")