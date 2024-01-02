import os
import pprint


# Decorador para ejecutar la función wrap que es para limpiar la consola antes de la función
# que tienen la anotación del decorador, luego pide cualquier input para continual y vuelve a limpiar la consola
def clear_system(function):
    # Se le pone el nombre de wrap porque es una función que envuelve a otra, es decir añade funcionalidad
    # Se pasa *args, **kwargs para que wrap pueda funcionar con otras funciones como get_user(), etc que podrian 
    # usar otros argumentos diferentes a collection como lo hace create_user(collection)
    def wrap(*args, **kwargs):
        os.system('clear') #para limpiar la pantalla en la consola con el comando clear
        result = function(*args, **kwargs)
        input('')
        os.system('clear')
            
    # Cuando se selecciona la opción crear usuario se debe mostrar la documentación de la función,
    # pero como tiene un decorador se llama la documentación del decorador, por eso a la del decorador se le 
    # asigna la de la función para que muestre "A) Crear un usuario"
    wrap.__doc__ = function.__doc__
    return wrap


def show_user(user):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(user)


@clear_system
def create_user(collection):
    """A) Crear un usuario"""
    
    username = input('Username: ')
    edad = input('Edad: ')
    email = input('Email ')

    # Python no tiene objetos JSON por lo que se utilizan diccionarios
    user = dict(username=username,edad=edad,email=email)

    direccion = input('¿Desea ingresar su dirección? (S/N)').lower()

    if direccion == 's':
        user['direccion'] = get_address()

    collection.insert_one(user)

    show_user(user)

    return user


def get_address():
    calle = input('Calle: ')
    ciudad = input('Ciudad: ')
    estado = input('Estado: ')
    codigo_postal = input('Código Postal: ')

    direccion = dict(calle=calle,
                     ciudad=ciudad,
                     estado=estado,
                     codigo_postal=codigo_postal)

    
    return direccion



@clear_system
def get_user(collection):
    """B) Consultar un usuario"""
    
    username = input('Username: ')

    user = collection.find_one(
        {'username': username},
        {'_id': false}
    )

    if user:
        show_user(user)
        return user
    else:
        print('No fue posible obtener el documento')

    

@clear_system
def delete_user(collection):
    """C) Eliminar un usuario"""

   username = input('Username': )

   return collecion.delete_one(
    {'username': username}
   )

def update_user():
    """D) Actualizar un usuario"""
    print('Actualizar un usuario')

def default(*args, **kwargs):
    print('Opción no válida')