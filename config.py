from decouple import config

URL = 'mongodb+srv://santiMongDB:{}@cluster0.nuc2alk.mongodb.net/?retryWrites=true&w=majority'.format(
    config('MONGODB_PASSWORD', default = 'password')
)

# se utiliza el paquete python-decouple para trabajar con variables de entorno. pip install python-decouple