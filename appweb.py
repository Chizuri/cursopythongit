#Para hacer aplicaciones web / es para reciclar codigo
#pip install flask
from flask import Flask #importa los archivos donde convierte python en html
app = Flask(__name__) #crea una variable donde utiliza un integrador

@app.route('/')  #una ruta de la app 
def hello_word():
    return 'Hola amigos de Geeky Theory!'

#funcion  para que la aplicacion  es la aplicacion maestra
if __name__ == '__main__':
    app.run(host='0.0.0.0') #esta es la direccion que va a usar