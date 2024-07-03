from flask import Flask, render_template

app = Flask(__name__)

#home > root
@app.route("/")
def hello_world():
    title = "Home"
    saludo = "Hola Mundo desde Flask!"
    # return saludo
    return render_template("home.html", saludo=saludo, title=title)


@app.route("/contacto")
def cargarContacto():
    title ="Contacto"

    users = ["Marcelo","Manuel","Stephanie","Miguel","Marisa","Julian"]

    return render_template("contacto.html", title=title, users=users)

@app.route("/tienda")
def cargarTienda():
    title ="Tienda"
    return render_template("tienda.html", title=title)