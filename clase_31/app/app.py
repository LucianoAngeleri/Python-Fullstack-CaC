from flask import Flask, render_template
from data import personas

app = Flask(__name__)

#home > root
@app.route("/")
def hello_world():
    title = "Home"
    # return saludo
    return render_template("home.html", title=title)


@app.route("/contacto")
def cargarContacto():
    title ="Contacto"
    users = ["Marcelo","Emanuel","Stephanie","Miguel","Marisa","Julian"]
    return render_template("contacto.html", title=title, users=users)

@app.route("/staff")
def cargarStaff():
    title ="Staff"
    return render_template("staff.html", title=title, personas=personas)
@app.route("/staff/<int:id>")
def cargarPersona(id):
    title ="Persona"
    return render_template("persona.html", title=title, persona=personas[id])

@app.route("/tienda")
def cargarTienda():
    title ="Tienda"
    return render_template("tienda.html", title=title)
