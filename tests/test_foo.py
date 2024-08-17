import unittest
import sys
import os

# Agregar el directorio raíz al sys.path para poder importar el módulo `secure_password_generator_ikac.foo`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from secure_password_generator_ikac.foo import generar_contrasena, generar_lista_contrasenas

class TestGeneradorContraseñas(unittest.TestCase):
    
    def test_generar_contrasena_longitud(self):
        # Prueba que la longitud de la contraseña generada sea la especificada.
        longitud = 16
        contrasena = generar_contrasena(longitud)
        self.assertEqual(len(contrasena), longitud)
    
    def test_generar_contrasena_minima_longitud(self):
        # Prueba que se lance un ValueError si la longitud especificada es menor a 6 caracteres.
        with self.assertRaises(ValueError):
            generar_contrasena(5)
    
    def test_generar_contrasena_composicion(self):
        # Prueba que la contraseña generada contenga al menos una mayúscula, una minúscula, un dígito y un símbolo.
        contrasena = generar_contrasena(12)
        self.assertTrue(any(c.isupper() for c in contrasena), "La contraseña no contiene una letra mayúscula.")
        self.assertTrue(any(c.islower() for c in contrasena), "La contraseña no contiene una letra minúscula.")
        self.assertTrue(any(c.isdigit() for c in contrasena), "La contraseña no contiene un dígito.")
        self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in contrasena), "La contraseña no contiene un símbolo.")

    def test_generar_contrasena_opciones(self):
        # Prueba que la contraseña generada contiene solo los tipos de caracteres especificados.
        contrasena = generar_contrasena(12, usar_letras=True, usar_numeros=True, usar_simbolos=False)
        self.assertTrue(all(c.isalnum() for c in contrasena), "La contraseña contiene caracteres no alfanuméricos.")

        contrasena = generar_contrasena(12, usar_letras=True, usar_numeros=False, usar_simbolos=False)
        self.assertTrue(all(c.isalpha() for c in contrasena), "La contraseña contiene caracteres no alfabéticos.")

        contrasena = generar_contrasena(12, usar_letras=False, usar_numeros=True, usar_simbolos=False)
        self.assertTrue(all(c.isdigit() for c in contrasena), "La contraseña contiene caracteres no numéricos.")

        contrasena = generar_contrasena(12, usar_letras=False, usar_numeros=False, usar_simbolos=True)
        self.assertTrue(all(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in contrasena), "La contraseña contiene caracteres no simbólicos.")

    def test_generar_lista_contrasenas(self):
        # Prueba que se genere la cantidad correcta de contraseñas con la longitud especificada y composición válida.
        cantidad = 5
        lista_contrasenas = generar_lista_contrasenas(cantidad, 12)
        self.assertEqual(len(lista_contrasenas), cantidad, "La cantidad de contraseñas generadas no es correcta.")
        
        for contrasena in lista_contrasenas:
            self.assertEqual(len(contrasena), 12, "Una de las contraseñas no tiene la longitud correcta.")
            self.assertTrue(any(c.isupper() for c in contrasena), "Una de las contraseñas no contiene una letra mayúscula.")
            self.assertTrue(any(c.islower() for c in contrasena), "Una de las contraseñas no contiene una letra minúscula.")
            self.assertTrue(any(c.isdigit() for c in contrasena), "Una de las contraseñas no contiene un dígito.")
            self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in contrasena), "Una de las contraseñas no contiene un símbolo.")

    def test_generar_lista_contrasenas_valor_invalido(self):
        # Prueba que se lance un ValueError si se intenta generar una lista con cantidad menor a 1.
        with self.assertRaises(ValueError):
            generar_lista_contrasenas(0)

    def test_generar_contrasena_randomness(self):
        # Prueba que dos contraseñas generadas consecutivamente no sean iguales (para verificar la aleatoriedad).
        contrasena1 = generar_contrasena(12)
        contrasena2 = generar_contrasena(12)
        self.assertNotEqual(contrasena1, contrasena2, "Dos contraseñas consecutivas son iguales, lo cual es improbable.")

if __name__ == "__main__":
    unittest.main()




