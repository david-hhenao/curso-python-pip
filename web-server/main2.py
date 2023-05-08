import store
from fastapi import FastAPI

app = FastAPI() # SE CREA UNA INSTANCIA DE ESTA APLICACIÓN
 
@app.get('/') # ES UN DECORADOR QUE SIRVE INIDICAR QUE CON ESA DIRECCIÓN SE PUEDE ACCEDER AHI
def get_list():
    return [1,2,3,4,5]

@app.get('/azul') # ES UN DECORADOR QUE SIRVE 
def get_list():
    return 'Azul'

@app.get('/contact') # ES UN DECORADOR QUE SIRVE 
def get_list():
    return {'name':'Platzi'}

@app.get('/contact2') # ES UN DECORADOR QUE SIRVE 
def get_list():
    return {'name 2':'Que raro'}

def run():
    store.get_categories()

if __name__ == '__main__':
    run()