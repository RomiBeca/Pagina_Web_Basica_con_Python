from flask import Flask, render_template ,request
app= Flask(__name__)

@app.route('/') 
def home():
    return render_template ('index.html')
# Ruta dinamica
@app.route('/user/<name>')  # Ruta dinámica /user/nombre
def user(name):
    return render_template('user.html', name=name)  # Pasa la variable 'name' al template
@app.route('/contact')
def contact():
    return render_template('contact.html')

# se importa el metodo request
@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return f"Mensaje enviado por {name}. Gracias por contactarnos."  # Aquí puedes procesar el mensaje, guardarlo en una base de datos, o enviar un correo, etc.
if __name__=='__main__':
    app.run(debug=True) 

