from secure_password_generator_ikac.foo import generar_contrasena, generar_lista_contrasenas

def solicitar_opcion(mensaje: str) -> bool:
    """Solicita al usuario una respuesta sí/no y la devuelve como un valor booleano."""
    while True:
        respuesta = input(mensaje + " (y/n): ").strip().lower()
        if respuesta == 'y':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Por favor, responde con 'y' o 'n'.")

def solicitar_numero(mensaje: str, minimo: int) -> int:
    """Solicita al usuario un número entero mayor o igual al valor mínimo especificado."""
    while True:
        try:
            numero = int(input(mensaje + f" (mínimo {minimo}): "))
            if numero >= minimo:
                return numero
            else:
                print(f"El número debe ser al menos {minimo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    print("Generador de Contraseñas Seguras")

    # Preguntar al usuario qué opciones desea para la contraseña
    usar_letras = solicitar_opcion("¿Deseas incluir letras (mayúsculas y minúsculas)?")
    usar_numeros = solicitar_opcion("¿Deseas incluir números?")
    usar_simbolos = solicitar_opcion("¿Deseas incluir símbolos?")
    longitud = solicitar_numero("¿Cuál debería ser la longitud de la contraseña?", minimo=6)
    cantidad = solicitar_numero("¿Cuántas contraseñas deseas generar?", minimo=1)

    # Generar y mostrar la(s) contraseña(s)
    lista_contrasenas = generar_lista_contrasenas(
        cantidad=cantidad,
        longitud=longitud,
        usar_letras=usar_letras,
        usar_numeros=usar_numeros,
        usar_simbolos=usar_simbolos
    )

    print("Lista de Contraseñas Generadas:")
    for i, contrasena in enumerate(lista_contrasenas, start=1):
        print(f"{i}: {contrasena}")
