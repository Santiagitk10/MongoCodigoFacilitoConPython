from functions import create_user
from functions import get_user
from functions import delete_user
from functions import update_user
from functions import default

from config import URL
from pymongo import MongoClient

# El programa no corre al ejecutar main desde la consola porque sale el siguiente error
# can't create new thread at interpreter shutdown

# Conexión a la base de datos

if __name__ == '__main__':
    client = MongoClient(URL)
    database = client['cursoUbitsMongoDB']
    collection = database['users']


options = {
    'a': create_user,
    'b': get_user,
    'c': delete_user,
    'd': update_user
}


while True: 
    for Key, function in options.items():
        print(function.__doc__)

    option = input('Opcion: ').lower()

    if option == 'q' or option == 'quit':
        break


    function_selected = options.get(option, default)
    function_selected(collection)