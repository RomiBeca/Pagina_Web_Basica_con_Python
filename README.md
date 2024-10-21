# README 
## Requisitos.
* python 3.12.6
* Flask (instalable via pip)

### Instalar Flask en el entorno local
Para instalar Flask, ejecuta el siguiente comando:
 ```sh
 pip install flask
 ```

## Estructura del Proyecto
* **app.py** : Archivo principal donde se define la lógica de la aplicación Flask, las rutas y el procesamiento del formulario.
* **templates/** : Carpeta donde se encuentran los archivos HTML que utilizan los templates de Flask.
* **static/** : Carpeta donde se encuentran los archivos estáticos como CSS y otros recursos.

## Estructura del directorio
Asegúrate de que la estructura del proyecto se vea de la siguiente manera:
```
desarrollo_web/
├── app.py
├── static/
│   └── css/
│       └── styles.css
└── templates/
    ├── home.html
    ├── user.html
    └── contact.html
```
## Ejecución de la aplicación
Para ejecutar la aplicación y acceder a la ruta principal, abre tu navegador y navega a la siguiente dirección:
```
http://127.0.0.1:5000/
```
## Descripción de los archivos HTML

* **Inicio** : Página principal del proyecto. Ruta: /
* **Perfil de Usuario** : Ruta dinámica que muestra el perfil de un usuario específico. Ejemplo: /user/Nombre
* **Contacto** : Página de contacto con un formulario. Ruta: /contact

### Detalles de las Rutas
* **/**: Página de inicio (home.html).
* **/user/<name>**: Ruta dinámica que muestra un saludo personalizado con el nombre del usuario. Utiliza el template user.html.
* **/contact**: Página de contacto con un formulario.
* **/send_message**: Ruta que procesa el formulario de contacto   utilizando el método POST.

### Descripción de los archivos HTML
* **Home (home.html)**: Página de bienvenida básica con HTML.
* **User Profile (user.html)**: Página que muestra un saludo dinámico basado en el nombre proporcionado en la URL.
* **Contact (contact.html)**: Página con un formulario de contacto donde los usuarios pueden enviar un mensaje.

# Creación de Rutas en Flask.
## Opción 1: Ruta básica con texto plano.
En este ejemplo, veremos cómo crear una ruta simple que devuelve un mensaje de texto al acceder a la página de inicio.

 ```py
 from flask import Flask #importamos flask de flask
app= Flask(__name__) #creamos una instancia

 #definimos una ruta que sera la pagina de inicio y devolvera un mensaje cuandos e visite la pagina Principal
@app.route('/') 
def home():
    return "hola mundo desde flask!, esta es mi primera pagina web con python :)"

#para agregar mas rutas es de la siguiente manera
# ejemplo: http://127.0.0.1:5000/about
@app.route('/about') 
def about():
    return "esta es la pagina About(probando ruta numero 1)"

if __name__=='__main__':
    app.run(debug=True) #se ejecuta la aplicacion con el modo debug para que se ejecuten los cambios de manera instantanea cuando se modifique el codigo
 ```

## Opción 2: Uso de templates con Flask.
En el código principal de este proyecto __*(app.py)*__, utilizamos templates para crear páginas más completas que incluyen HTML, CSS, y manejo de formularios. La lógica detrás de las rutas es más flexible y te permite renderizar archivos HTML en lugar de solo devolver texto plano.