from flask import Flask, render_template
from data import personas
from datetime import date, datetime

app = Flask(__name__)

#Obtener datos de tiempo actual
def basicInfo(getTitle):
    #Día actual
    hoy = date.today()
    #Fecha y hora actual
    now = datetime.now()
    #Sección
    title = getTitle
    return [title, hoy.strftime("%Y"), now]

#home > root
@app.route("/")
def hello_world():
    title = "Home"
    # return saludo
    return render_template("home.html", title=basicInfo(title))


@app.route("/contacto")
def cargarContacto():
    title ="Contacto"
    users = ["Marcelo","Emanuel","Stephanie","Miguel","Marisa","Julian"]
    return render_template("contacto.html", title=basicInfo(title), users=users)

@app.route("/staff")
def cargarStaff():
    title ="Staff"
    return render_template("staff.html", title=basicInfo(title), personas=personas)
@app.route("/staff/<int:id>")
def cargarPersona(id):
    title ="Persona"
    return render_template("persona.html", title=basicInfo(title), persona=personas[id])

@app.route("/tienda")
def cargarTienda():
    title ="Tienda"
    return render_template("tienda.html", title=basicInfo(title))
