import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # SE CREA UNA INSTANCIA DE ESTA APLICACIÓN
 
@app.get('/') # ES UN DECORADOR QUE SIRVE INIDICAR QUE CON ESA DIRECCIÓN SE PUEDE ACCEDER AHI
def get_list():
    return [1,2,3,4]

@app.get('/contact/2',response_class=HTMLResponse) # ES UN DECORADOR QUE SIRVE 
async def get_list():
    return """
        <html>
        <h1>Hola soy una página<\h1>
        <b>Hola soy un parrafo</b>
        </html>
    """

@app.get('/prueba',response_class=HTMLResponse) # ES UN DECORADOR QUE SIRVE 
async def get_list():
    return """
        <html>
        <h1>Hola soy una página<\h1>
        <b>Hola soy un parrafo</b>
        </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()