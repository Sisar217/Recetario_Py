from pathlib import Path
from os import system

#Funciones para el recetario
def solicitar_categoria():
    categoria = input("Ingresa el nombre de la categoría que deseas explorar: ")
    return categoria

def mostrar_categorias():
    for categoria in guia.iterdir():
        if categoria.is_dir():
            print(categoria.name)

def buscar_categoria(categoria):
    ruta = Path(Path.home() / "Recetario" / categoria)
    return ruta

def mostrar_recetas(categoria):
    ruta = Path(Path.home() / "Recetario" / categoria)
    for receta in ruta.glob("*.txt"):
        print(receta.stem)

def solicitar_receta():
    receta = input("Ingresa la receta que deseas buscar: ")
    return receta

def buscar_recetas():

    return

nombre_usuario: str = input("Ingresa tu nombre: ")
print(f"Hola, {nombre_usuario}. Bienvenido al Recetario.")
base = Path("Recetario")
guia = Path(Path.home() / "Recetario")
cantidad = sum(1 for _ in Path(guia).glob("**/*.txt"))
print(f"Puedes encontrar los archivos del recetario en {base}.\nHay un total de {cantidad} recetas.")
#El código anterior sirve únicamente como presentación o parte inicial del programa.

editando = True
while editando:

   system("clear")
   menu = int(input("Selecciona una opción del siguiente menú:\n1. Leer recetas\n2. Crear receta\n"
                 "3. Crear nueva categoría\n4. Eliminar receta\n5. Eliminar categoría\n6. Salir del programa"))
   if menu == 1:
       #función que muestra las recetas.
       categoria_elegida = solicitar_categoria()
       receta_elegida = solicitar_receta()
       mostrar_categorias()
       solicitar_categoria()
       buscar_categoria(categoria_elegida)
       mostrar_recetas(categoria_elegida)
       buscar_recetas()
       continuar = input("Desea realizar alguna otra acción?\n1. Si / 2. No")
       if continuar == 1:
           print("Muy bien. Reiniciaremos el programa. Espere un momentito.")
       elif continuar != 1:
           print("De acuerdo. Hasta la próxima!")
           editando = False
       else:
           print("Por favor seleccione solo 1 o 2. Cualquier otro valor será rechazado.")

   elif menu == 2:
       #función que crea una nueva receta.
      pass

   elif menu == 3:
      #función que crea una nueva categoría.
      pass

   elif menu == 4:
      #función que elimina una receta.
      pass

   elif menu == 5:
      #funcion que elimina una categoría.
      pass

   elif menu == 6:
      print('Hasta la próxima.')
      editando = False

   else:
       print('Por favor ingresa una opción válida.')
       system('clear')
