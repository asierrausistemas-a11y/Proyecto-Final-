"""
==================================================
        💰 GESTOR DE GASTOS PERSONALES 💰
==================================================

Autor: Andrés Sierra Aguirre

Descripción:
Este proyecto consiste en el desarrollo de un sistema
en Python que permite gestionar los gastos personales
de manera sencilla, organizada y eficiente.

Propósito:
Brindar al usuario una herramienta que le permita
llevar un control claro de sus finanzas, registrando,
visualizando y analizando sus gastos diarios.

Importancia:
Hoy en día, muchas personas no tienen un control
adecuado de su dinero, lo que puede generar problemas
financieros. Este sistema busca aportar una solución
práctica a esta situación, promoviendo una mejor
educación financiera.

Funcionalidades iniciales:
-Registro de gastos-
-Visualización de gastos-
-Cálculo del total gastado-

==================================================
        INICIANDO SISTEMA...
==================================================
"""

#1 MENÚ

def mostrar_menu():
    print("\n" + "="*50)
    print("MENÚ PRINCIPAL".center(50))
    print("="*50)
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Total de gastos")
    print("4. Salir")
    print("="*50)
