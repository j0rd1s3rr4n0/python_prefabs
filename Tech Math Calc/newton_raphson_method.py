import sympy as sp
import os
import importlib

"""
{ MANUAL DE USO }
El usuario debe proporcionar la información en los siguientes pasos durante 
la ejecución del programa:

1. Ingrese la función en formato LaTeX, por ejemplo:
   "5*x**5 - 9*x**4 + 23*x**3 - 15*x**2 + 16*x + 4"

2. Ingrese el valor inicial (guess) para el método de Newton-Raphson,
   por ejemplo: -1.0

3. Ingrese el número máximo de iteraciones que desea realizar,
   por ejemplo: 20

4. Ingrese el umbral de error límite deseado, por ejemplo, si debe ser menor a 0.5 * 10^-5. 
   Por ejemplo, puede ingresar "1e-6" o "0.000001" si desea un umbral de error de 0.000001,
   que es menor a 0.5 * 10^-5.

El programa interactuará con el usuario en cada uno de estos pasos, y el usuario proporcionará
los valores correspondientes en el formato adecuado según las indicaciones.

{ EJEMPLO DE USO (OUTPUT) }
Ingrese la función en formato LaTeX: 5*x**5 - 9*x**4 + 23*x**3 - 15*x**2 + 16*x + 4
Ingrese el valor inicial (guess): -1
Ingrese el número máximo de iteraciones: 20
Ingrese el umbral de error (Ejemplo 10^-4 => 1e-4): 1e-6

+-----------+--------------------+------------------------+------------------+-----------------------+
| Iteración |         x          |          f(x)          |      f'(x)       |         Error         |
+-----------+--------------------+------------------------+------------------+-----------------------+
|     0     | -0.636363636363636 |   -64.0000000000000    | 176.000000000000 |   64.0000000000000    |
|     1     | -0.372248803827751 |   -20.1810358209511    | 76.4100812786012 |   20.1810358209511    |
|     2     | -0.233266114026571 |   -5.42946049449302    | 39.0657318710701 |   5.42946049449302    |
|     3     | -0.201360791823986 |   -0.870487062586045   | 27.2834437169707 |   0.870487062586045   |
|     4     | -0.200002313280859 |  -0.0341976974850476   | 25.1735278838718 |  0.0341976974850476   |
|     5     | -0.200000000006689 | -0.0000580357580095003 | 25.0881450894924 | 0.0000580357580095003 |
|     6     | -0.200000000000000 | -1.67816011087396E-10  | 25.0880000004195 | 1.67816011087396E-10  |
+-----------+--------------------+------------------------+------------------+-----------------------+

"""

# Comprobar si sympy está instalado
if importlib.util.find_spec("sympy") is None:
    print("sympy no está instalado. Instalando...")
    os.system('pip install sympy')
    import sympy as sp  # Importar sympy después de la instalación

from tabulate import tabulate
import sympy as sp

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parse_error_threshold(user_input_error_threshold):
    if "e" in user_input_error_threshold:
        # Interpretar la notación científica
        base, exponent = user_input_error_threshold.split("e")
        try:
            base = float(base)
            exponent = int(exponent)
            error_threshold = base * 10 ** exponent
            return error_threshold
        except ValueError:
            pass
    try:
        # Intentar interpretar el valor como un número real
        error_threshold = float(user_input_error_threshold)
        return error_threshold
    except ValueError:
        return None

def newton_raphson_solver(func_latex, initial_guess, max_iterations, error_threshold):
    x = sp.Symbol('x')
    func = sp.sympify(func_latex)
    
    table = []
    x_value = initial_guess
    
    for i in range(max_iterations):
        f_x = func.subs(x, x_value)
        f_prime_x = sp.diff(func, x).subs(x, x_value)
        if f_prime_x == 0:
            print("Derivada en el punto es cero. El método de Newton-Raphson no puede continuar.")
            break
        x_value = x_value - f_x / f_prime_x
        error = abs(f_x)
        table.append([i, x_value, f_x, f_prime_x, error])
        
        if error < error_threshold:
            break
    
    return table

# Ejemplo de uso
while True:
    func_latex = input("Ingrese la función en formato LaTeX: ")
    initial_guess = float(input("Ingrese el valor inicial (guess): "))
    max_iterations = int(input("Ingrese el número máximo de iteraciones: "))
    
    user_input_error_threshold = input("Ingrese el umbral de error (Ejemplo 10^-4 => 1e-4): ")
    error_threshold = parse_error_threshold(user_input_error_threshold)
    
    if error_threshold is None:
        print("Entrada no válida. Ingrese el umbral de error en el formato adecuado.")
        continue

    table = newton_raphson_solver(func_latex, initial_guess, max_iterations, error_threshold)

    # Imprimir la tabla de manera estética
    headers = ["Iteración", "x", "f(x)", "f'(x)", "Error"]
    print(tabulate(table, headers, tablefmt="pretty"))

    # Calcular el intervalo que contiene la solución
    interval_start = min(table, key=lambda x: abs(x[2]))[1]
    interval_end = max(table, key=lambda x: abs(x[2]))[1]
    solution = table[-1][1]  # La solución se toma del último valor de x en la tabla
    formatted_solution = "{:.6f}".format(solution)  # Formatear la solución con 6 decimales
    print(f"Intervalo que contiene la solución: {{{interval_start},{interval_end}}}, solución del intervalo: {formatted_solution}")
    break
