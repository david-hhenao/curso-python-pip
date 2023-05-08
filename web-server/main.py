import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # SE CREA UNA INSTANCIA DE ESTA APLICACIÓN
 
@app.get('/') # ES UN DECORADOR QUE SIRVE INIDICAR QUE CON ESA DIRECCIÓN SE PUEDE ACCEDER AHI
def get_list():
    return [1,2,3,4,5]

@app.get('/contacto',response_class=HTMLResponse) # ES UN DECORADOR QUE SIRVE 
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()

'''

import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app2 = FastAPI() # SE CREA UNA INSTANCIA DE ESTA APLICACIÓN
 
@app2.get('/') # ES UN DECORADOR QUE SIRVE INIDICAR QUE CON ESA DIRECCIÓN SE PUEDE ACCEDER AHI
def get_list():
    return [1,2,3,4,5]

@app2.get('/contact') # ES UN DECORADOR QUE SIRVE 
def get_list():
    return {'name':'Platzi'}

@app2.get('/contact2') # ES UN DECORADOR QUE SIRVE 
def get_list():
    return {'name 2':'Que raro'}

@app2.get('/prueba',response_class=HTMLResponse) # ES UN DECORADOR QUE SIRVE 
async def get_list():
    return """
        <h1>Hola soy una página<\h1>
        <b>Hola soy un parrafo</b>
    """

@app2.get('/azul') # ES UN DECORADOR QUE SIRVE 
def get_list():
    return 'Azul'

def run():
    print("Iniciando aplicación")
    store.get_categories()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

'''