import sympy as sp
import os
import importlib

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

def bisection_solver(func_latex, a, b, iterations, error_threshold):
    x = sp.Symbol('x')
    func = sp.sympify(func_latex)
    
    table = []
    
    for i in range(iterations):
        m = (a + b) / 2
        m_fraction = sp.Rational(m).limit_denominator()
        f_m = func.subs(x, m_fraction)
        error_fraction = sp.Rational(b - a, 2 ** (i + 1)).limit_denominator()
        error = float(error_fraction)
        marker = "X" if error >= error_threshold else "✔"
        table.append([i, a, b, m_fraction, "+" if f_m >= 0 else "-", error_fraction, marker])
        
        if f_m * func.subs(x, a) < 0:
            b = m
        else:
            a = m
    
    return table

# Ejemplo de uso
while True:
    user_input_iterations = input("Ingrese nº Iterations (default=10): ")
    
    if user_input_iterations:
        if is_integer(user_input_iterations):
            iterations = int(user_input_iterations)
        else:
            print("Entrada no válida. Ingrese un número entero.")
            continue
    else:
        iterations = 10

    valor_entero_int_a = False
    while not valor_entero_int_a:
        user_input_int_a = input("Ingrese valor de Intervalo A (default= -1): ")
        if user_input_int_a:
            if is_integer(user_input_int_a):
                a = int(user_input_int_a)
                valor_entero_int_a = True
            else:
                print("Entrada no válida. Ingrese un número entero.")
        else:
            a = -1
            valor_entero_int_a = True

    valor_entero_int_b = False
    while not valor_entero_int_b:
        user_input_int_b = input("Ingrese valor de Intervalo B (default= +1): ")
        if user_input_int_b:
            if is_integer(user_input_int_b):
                b = int(user_input_int_b)
                valor_entero_int_b = True
            else:
                print("Entrada no válida. Ingrese un número entero.")
        else:
            b = 1
            valor_entero_int_b = True

        user_input_error_threshold = input("Ingrese el umbral de error (Ejemplo 10^-4 => 1e-4): ")
        if user_input_error_threshold:
            if user_input_error_threshold.lower() == "default":
                error_threshold = 1e-4
            else:
                # Intentar interpretar el valor como un número, considerando el formato 10^-4
                if "^" in user_input_error_threshold:
                    base, exponent = user_input_error_threshold.split("^")
                    try:
                        base = float(base)
                        exponent = int(exponent)
                        error_threshold = base ** exponent
                    except ValueError:
                        print("Entrada no válida. Ingrese un número real para el umbral de error.")
                        continue
                else:
                    try:
                        error_threshold = float(user_input_error_threshold)
                    except ValueError:
                        print("Entrada no válida. Ingrese un número real para el umbral de error.")
                        continue
        else:
            error_threshold = 1e-4


    func_latex = '5*x**5 - 9*x**4 + 23*x**3 - 15*x**2 + 16*x + 4'

    table = bisection_solver(func_latex, a, b, iterations, error_threshold)

    # Imprimir la tabla de manera estética
    headers = ["m", "an", "bn", "mn+1", "f(mn+1)", "error", "Marcador"]
    print(tabulate(table, headers, tablefmt="pretty"))
    break
