# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DqKpgFK4wq6FFtFWY7cPapZj8ASIu8JZ
"""

#   Codigo que implementa el esquema numerico
#   de punto fijo para determinar la raiz de
#   una ecuacion
#
#           Autor:
#   Angel Gabriel Chim Vera
#   angchimvera@gmail.com
#   Version 1.0 : 13/02/2025
#

import numpy as np
import matplotlib.pyplot as plt

# Definir la función g(x) para el método de punto fijo
# Reescribiendo la ecuación cos(x) - x = 0 en la forma x = g(x)
def g(x):
    return np.cos(x)

# Criterio de convergencia: derivada de g(x)
def g_prime(x):
    return -np.sin(x)

# Funciones para calcular los errores
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old)

def error_relativo(x_new, x_old):
    return abs((x_new - x_old) / x_new)

def error_cuadratico(x_new, x_old):
    return (x_new - x_old) ** 2

# Implementación del método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []

    x_old = x0
    for i in range(max_iter):
        x_new = g(x_old)
        e_abs = error_absoluto(x_new, x_old)
        e_rel = error_relativo(x_new, x_old)
        e_cuad = error_cuadratico(x_new, x_old)

        iteraciones.append((i + 1, x_new, e_abs, e_rel, e_cuad))
        errores_abs.append(e_abs)
        errores_rel.append(e_rel)
        errores_cuad.append(e_cuad)

        if e_abs < tol:
            break

        x_old = x_new

    return iteraciones, errores_abs, errores_rel, errores_cuad

# Parámetro inicial
x0 = 0.5
iteraciones, errores_abs, errores_rel, errores_cuad = punto_fijo(x0)

# Imprimir tabla de iteraciones
print("Iteración | x_n      | Error absoluto | Error relativo | Error cuadrático")
print("-----------------------------------------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e} | {it[3]:.6e} | {it[4]:.6e}")

# Graficar la convergencia de la función g(x)
x_vals = np.linspace(-1, 1, 100)
y_vals = g(x_vals)

g_prime_vals = np.abs(g_prime(x_vals))

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$g(x) = \cos(x)$", color="blue")
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.title("Método de Punto Fijo - Convergencia")
plt.savefig("punto_fijo_convergencia.png")
plt.show()

# Graficar errores
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")
plt.plot(range(1, len(errores_rel) + 1), errores_rel, marker="s", label="Error relativo")
plt.plot(range(1, len(errores_cuad) + 1), errores_cuad, marker="^", label="Error cuadrático")
plt.xlabel("Iteración")
plt.ylabel("Error")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.title("Evolución de los Errores")
plt.savefig("errores_punto_fijo.png")
plt.show()

# Analizar el criterio de convergencia |g'(x)| < 1
plt.figure(figsize=(8, 5))
plt.plot(x_vals, g_prime_vals, label=r"$|g'(x)| = |\sin(x)|$", color="purple")
plt.axhline(y=1, color='r', linestyle='dashed', label="|g'(x)| = 1")
plt.xlabel("x")
plt.ylabel("|g'(x)|")
plt.legend()
plt.grid(True)
plt.title("Criterio de Convergencia de Punto Fijo")
plt.savefig("criterio_convergencia.png")
plt.show()