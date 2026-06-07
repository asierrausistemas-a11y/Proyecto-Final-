"""
          ------PROYECTO FINAL------
==================================================
         GESTOR DE GASTOS PERSONALES 
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

# ==========================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================
# time: permite hacer pausas (para animaciones)
# os: permite interactuar con el sistema (limpiar pantalla)

import time
import os


# ==========================================
# FUNCIONES DE INTERFAZ (VISUAL)
# ==========================================

# Esta función limpia la pantalla dependiendo del sistema operativo
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Esta función muestra títulos bonitos en consola
def titulo(texto):
    print("\n" + "="*50)
    print(texto.center(50))
    print("="*50)

# Esta función pausa el programa hasta que el usuario presione ENTER
def pausa():
    input("\nPresione ENTER para continuar...")

# Esta función simula el inicio del sistema (pantalla de carga)
def inicio_sistema():
    limpiar_pantalla()
    titulo("GESTOR DE GASTOS PERSONALES")

    print("Cargando sistema", end="")
    for i in range(4):  # bucle para animación
        print(".", end="", flush=True)
        time.sleep(0.4)

    print("\n\nSistema listo")
    time.sleep(1)


# ==========================================
# BASE DE DATOS (LISTA DE GASTOS)
# ==========================================
# Aquí se almacenan todos los gastos del usuario

gastos = []


# ==========================================
# FUNCIONES PRINCIPALES DEL SISTEMA
# ==========================================

# Esta función permite agregar un nuevo gasto
def agregar_gasto():
    titulo("AGREGAR GASTO")

    # Se solicitan los datos al usuario
    nombre = input("Nombre del gasto: ")
    categoria = input("Categoría (Comida, Transporte, etc): ")

    # Validación del monto con try/except
    try:
        monto = float(input("Monto: "))
    except:
        print("Error: Debe ingresar un número válido")
        pausa()
        return  # sale de la función si hay error

    # Se crea un diccionario con los datos del gasto
    gasto = {
        "nombre": nombre,
        "categoria": categoria,
        "monto": monto
    }

    # Se guarda el gasto en la lista
    gastos.append(gasto)

    print("\nGasto agregado correctamente")
    pausa()


# Esta función muestra todos los gastos registrados
def ver_gastos():
    titulo("LISTA DE GASTOS")

    # Si la lista está vacía
    if len(gastos) == 0:
        print("No hay gastos registrados")
    else:
        # Encabezado tipo tabla
        print(f"{'Nombre':<15}{'Categoría':<15}{'Monto':<10}")
        print("-"*40)

        # Recorrido de la lista
        for g in gastos:
            print(f"{g['nombre']:<15}{g['categoria']:<15}{g['monto']:<10}")

    pausa()


# Esta función calcula el total de todos los gastos
def total_gastos():
    titulo("TOTAL DE GASTOS")

    # sum() suma todos los montos
    total = sum(g["monto"] for g in gastos)

    print(f"Total gastado: ${total}")

    pausa()


# Esta función permite filtrar gastos por categoría
def filtrar_categoria():
    titulo("FILTRAR POR CATEGORÍA")

    categoria = input("Ingrese la categoría: ")

    # Lista filtrada con comprensión de listas
    encontrados = [g for g in gastos if g["categoria"].lower() == categoria.lower()]

    if len(encontrados) == 0:
        print("No se encontraron gastos")
    else:
        for g in encontrados:
            print(f"{g['nombre']} - ${g['monto']}")

    pausa()


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

# Esta función controla todo el flujo del programa
def menu():
    while True:
        titulo("MENÚ PRINCIPAL")

        print("""
╔══════════════════════════════════════════════╗
║                OPCIONES                      ║
╠══════════════════════════════════════════════╣
║  [1] ➤ Agregar gasto                        ║
║  [2] ➤ Ver gastos                           ║
║  [3] ➤ Total de gastos                      ║
║  [4] ➤ Filtrar categoría                    ║
║  [5] Salir                                   ║
╚══════════════════════════════════════════════╝
        """)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            ver_gastos()
        elif opcion == "3":
            total_gastos()
        elif opcion == "4":
            filtrar_categoria()
        elif opcion == "5":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("Opción inválida")
            pausa()


# ==========================================
# FUNCIÓN PRINCIPAL
# ==========================================

# Esta función inicia todo el programa
def main():
    inicio_sistema()  # muestra animación inicial
    menu()            # inicia el menú


# ==========================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================

# Aquí se ejecuta todo el sistema
main()
