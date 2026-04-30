from pathlib import Path
from os import system

#Funciones para el recetario
def mostrar_categorias():
    categorias = guia.relative_to(Path("Recetario"))
    print(categorias)

def buscar_categoria(nombre_categoria):
    pass

nombre_usuario: str = input("Ingresa tu nombre: ")
print(f"Hola, {nombre_usuario}. Bienvenido al Recetario.")
base = Path("Recetario")
guia = Path(Path.home() / "Recetario")
cantidad = 0
for cantidad in Path(guia).glob("**/*.txt"):
    cantidad += 1
print(f"Puedes encontrar los archivos del recetario en {base}.\nHay un total de {cantidad} recetas.")
#El código anterior sirve únicamente como presentación o parte inicial del programa.

editando = True
while editando:
   menu = int(input("Selecciona una opción del siguiente menú:\n1. Leer recetas\n2. Crear receta\n"
                 "3. Crear nueva categoría\n4. Eliminar receta\n5. Eliminar categoría\n6. Salir del programa"))
   if menu == 1:
       #función que muestra las recetas.
       nombre_categoria = input("Ingresa el nombre de la categoría en la que quieres ver recetas: ")

   elif menu == 2:
       #función que crea una nueva receta.

   elif menu == 3:
       #función que crea una nueva categoría.

   elif menu == 4:
      #función que elimina una receta.

   elif menu == 5:
      #funcion que elimina una categoría.

   elif menu == 6:
      print('Hasta la próxima.')
      editando = False

   else:
       print('Por favor ingresa una opción válida.')
       system('clear')
