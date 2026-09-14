from estudiantes import (
    agregar_estudiante,
    mostrar_estudiantes,
    buscar_estudiante,
)

from notas import (
    agregar_nota,
    calcular_promedio,
    estado_estudiante,
)


def mostrar_menu():
    print("==================================")
    print("   SISTEMA DE GESTIÓN ACADÉMICA   ")
    print("==================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Registrar nota")
    print("5. Consultar promedio")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            agregar_nota()
        elif opcion == "5":
            promedio = calcular_promedio()
            if promedio is not None:
                estado_estudiante(promedio)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()